"""Phase 1 simulation pipeline.

Wires configuration, the RPC pool, and the DEX adapter into the single path
this slice implements: load config, verify connectivity, quote across venues,
and refuse execution.

The refusal is the point. `docs/apex-app-docs/execution/risk-policy/risk-engine.md`
§0 specifies that in Phase 1 any opportunity reaching the execution gate is hard
rejected with `PHASE_1_EXECUTION_BLOCK`, and
`docs/apex-app-docs/execution/risk-policy/decision-engine.md` specifies that the
decision path fails closed. Both are enforced here structurally: there is no
code path that produces an approved execution, so the block cannot be bypassed
by configuration.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .config import Config, ExecutionPhase
from .decision import (
    ConsensusResult,
    Decision,
    Recommendation,
    decide,
)
from .dex import Pool, Quote, QuoteError, best_quote
from .explain import Explanation, ExplanationStore, explain
from .ledger import DecisionLedger, DecisionOutcome
from .opportunity import (
    Candidate,
    DetectionResult,
    OpportunityState,
    Rejection,
    detect,
)
from .risk import RiskLimits, RiskVerdict, TradeAssessment, evaluate as evaluate_risk
from .routing import Route, RouteRejected, RouteState, RoutingResult, rank_routes
from .rpc import RpcError, RpcPool
from .simulation import (
    PerformanceLedger,
    SimulationMode,
    SimulationResult as PaperTradeResult,
    simulate,
)

PHASE_1_BLOCK_CODE = "PHASE_1_EXECUTION_BLOCK"


class ExecutionBlocked(Exception):
    """Raised when execution is attempted under a simulation-only phase.

    Carries the specification's rejection code so a caller can assert the
    reason rather than inferring it from a message.
    """

    def __init__(self, code: str = PHASE_1_BLOCK_CODE) -> None:
        self.code = code
        super().__init__(
            f"{code}: live execution is always rejected in "
            f"{ExecutionPhase.SIMULATION_ONLY.value}"
        )


@dataclass(frozen=True)
class SimulationResult:
    """Outcome of one simulated opportunity evaluation."""

    quote: Quote
    chain_id: int
    excluded_venues: tuple[str, ...] = ()
    executed: bool = False
    rejection_code: str = PHASE_1_BLOCK_CODE

    @property
    def summary(self) -> str:
        return (
            f"{self.quote.dex_id}: {self.quote.amount_in} {self.quote.token_in} -> "
            f"{self.quote.amount_out} {self.quote.token_out} "
            f"(impact {self.quote.price_impact_bps}bps, chain {self.chain_id}, "
            f"execution {self.rejection_code})"
        )


@dataclass(frozen=True)
class DiscoveryResult:
    """Outcome of a full detect-and-route pass.

    Carries the rejections from both stages alongside the winning route.
    Detection and routing rejections are distinct signals — one means no
    opportunity existed, the other that none was safe to take — and collapsing
    them would hide which gate stopped a trade.
    """

    chain_id: int
    detection: DetectionResult
    routing: RoutingResult
    best_candidate: Candidate | None = None
    executed: bool = False
    rejection_code: str = PHASE_1_BLOCK_CODE

    @property
    def has_route(self) -> bool:
        return bool(self.routing.routes)

    @property
    def best_route(self) -> Route:
        """The winning route, or raise if none survived.

        Raising rather than returning None enforces the routing contract's
        hard-reject rule at the call site.
        """
        return self.routing.best

    @property
    def summary(self) -> str:
        if not self.has_route:
            return (
                f"chain {self.chain_id}: no safe route "
                f"({len(self.detection.candidates)} candidate(s), "
                f"{len(self.routing.rejections)} route rejection(s))"
            )
        route = self.routing.routes[0]
        return (
            f"chain {self.chain_id}: {route.candidate_identity} "
            f"net {route.net_edge_bps}bps "
            f"(fingerprint {route.fingerprint}, execution {self.rejection_code})"
        )


@dataclass
class SimulationPipeline:
    """The Phase 1 evaluation path."""

    config: Config
    rpc: RpcPool
    ledger: PerformanceLedger = field(default_factory=PerformanceLedger, init=False)
    decisions: DecisionLedger = field(default_factory=DecisionLedger, init=False)
    explanations: ExplanationStore = field(default_factory=ExplanationStore, init=False)
    _warnings: list[str] = field(default_factory=list, init=False)
    _last_risk_verdict: RiskVerdict | None = field(default=None, init=False)

    @property
    def warnings(self) -> tuple[str, ...]:
        return tuple(self._warnings)

    def evaluate(self, pools: list[Pool], amount_in: int, *, now_ms: int) -> SimulationResult:
        """Evaluate an opportunity and return a simulated, unexecuted result.

        Connectivity is verified before quoting. An unreachable chain yields no
        result rather than a quote computed against unverified state, because
        the specification forbids treating an absent input as an unchanged one.
        """
        self._warnings.clear()

        chain_id = self.rpc.verify_chain_id()

        if not self.rpc.has_redundancy:
            # Reported, not fatal: the redundancy floor gates autonomous
            # execution, which this phase never reaches.
            self._warnings.append(
                f"chain {chain_id} has {len(self.rpc.healthy_endpoints)} healthy endpoint(s); "
                f"autonomous execution requires at least 2"
            )

        quote, exclusions = best_quote(
            pools,
            amount_in,
            now_ms=now_ms,
            freshness_budget_ms=self.config.quote_freshness_ms,
            max_slippage_bps=self.config.max_slippage_bps,
        )

        return SimulationResult(
            quote=quote,
            chain_id=chain_id,
            excluded_venues=tuple(exclusions),
        )

    def discover(
        self,
        pools: list[Pool],
        amount_in: int,
        *,
        now_ms: int,
        gas_cost_units: int,
        min_reserve_in: int = 0,
    ) -> "DiscoveryResult":
        """Run the full Phase 1 discovery path.

        Verifies connectivity, detects candidates, ranks routes, and advances
        the winning opportunity through its lifecycle to `SIMULATED` — the
        furthest state reachable while execution is blocked.

        Connectivity is verified first. A chain that cannot be reached yields no
        discovery at all rather than candidates computed against unverified
        state, because an absent input is never treated as an unchanged one.
        """
        self._warnings.clear()

        chain_id = self.rpc.verify_chain_id()
        if not self.rpc.has_redundancy:
            self._warnings.append(
                f"chain {chain_id} has {len(self.rpc.healthy_endpoints)} healthy endpoint(s); "
                f"autonomous execution requires at least 2"
            )

        detection = detect(
            pools,
            now_ms=now_ms,
            freshness_budget_ms=self.config.quote_freshness_ms,
            min_edge_bps=self.config.min_edge_bps,
            min_reserve_in=min_reserve_in,
        )

        routing = rank_routes(
            list(detection.candidates),
            amount_in,
            now_ms=now_ms,
            freshness_budget_ms=self.config.quote_freshness_ms,
            max_slippage_bps=self.config.max_slippage_bps,
            gas_cost_units=gas_cost_units,
            min_net_edge_bps=self.config.min_edge_bps,
        )

        # Advance the winning candidate through the lifecycle. Each step is a
        # declared transition, so an out-of-order advance raises rather than
        # silently skipping a gate the specification requires.
        best_candidate: Candidate | None = None
        if routing.routes:
            winner = routing.routes[0]
            for candidate in detection.candidates:
                if candidate.identity == winner.candidate_identity:
                    best_candidate = (
                        candidate
                        .transition_to(OpportunityState.VALIDATED)
                        .transition_to(OpportunityState.SCORED)
                        .transition_to(OpportunityState.SIMULATED)
                    )
                    break

        return DiscoveryResult(
            chain_id=chain_id,
            detection=detection,
            routing=routing,
            best_candidate=best_candidate,
        )

    def paper_trade(
        self,
        discovery: "DiscoveryResult",
        amount_in: int,
        *,
        now_ms: int,
        assessment: TradeAssessment,
        gas_cost_cents: int,
        limits: RiskLimits | None = None,
        latency_ms: int = 0,
        seed: int = 0,
    ) -> PaperTradeResult:
        """Risk-check and paper-trade the winning route.

        The risk pipeline runs first and its verdict is carried into the
        simulation rather than gating it. Phase 1 exists to gather hypothetical
        performance data, and simulating only the trades risk would have
        approved would bias that record toward success. The rejection is
        recorded on the result instead.

        Nothing here signs or broadcasts. `paper_trade` is the terminal
        operation available in this build; `execute` remains unconditionally
        blocked.
        """
        route = discovery.best_route  # raises RouteRejected when none survived

        verdict = evaluate_risk(assessment, limits, simulation_only=True)
        self._last_risk_verdict = verdict

        result = simulate(
            route,
            amount_in,
            now_ms=now_ms,
            gas_cost_cents=gas_cost_cents,
            risk_verdict=verdict,
            latency_ms=latency_ms,
            seed=seed,
            mode=SimulationMode.PAPER_TRADING,
        )
        self.ledger.record(result)
        return result

    @property
    def last_risk_verdict(self) -> RiskVerdict | None:
        """The verdict from the most recent paper trade, for auditing."""
        return self._last_risk_verdict

    def adjudicate(
        self,
        discovery: "DiscoveryResult",
        paper_trade: PaperTradeResult,
        *,
        now_ms: int,
        consensus: ConsensusResult | None,
        notional_cents: int,
        created_at_ms: int | None = None,
        human_override: bool | None = None,
        policy_available: bool = True,
    ) -> Decision:
        """Run the decision gate and record the outcome in the ledger.

        The decision is recorded whatever it is. The ledger contract requires
        an immutable trace of decisions, and a ledger holding only approvals
        would be a record of successes rather than of decisions.

        A decision reaching APPROVED here still does not execute: `execute()`
        remains blocked, and in Phase 1 the risk verdict carries the phase gate
        rejection that stops the decision before the simulation gate anyway.
        """
        route = discovery.best_route

        recommendation = Recommendation(
            identity=route.candidate_identity,
            route_fingerprint=route.fingerprint,
            created_at_ms=created_at_ms if created_at_ms is not None else now_ms,
            notional_cents=notional_cents,
        )

        decision = decide(
            recommendation,
            now_ms=now_ms,
            consensus=consensus,
            risk_verdict=self._last_risk_verdict,
            simulation=paper_trade,
            policy_available=policy_available,
            human_override=human_override,
        )

        # The decision ID must be unique per decision, not per route. The same
        # route can legitimately be adjudicated more than once at the same
        # timestamp — re-evaluated after a deferral, or reconsidered under a
        # human override — and each is a distinct decision that the ledger must
        # record separately. The sequence number makes that explicit rather
        # than letting the second decision collide with the first.
        sequence = len(self.decisions)
        decision_id = f"{route.fingerprint}:{now_ms}:{sequence}"

        # Every decision gets an explanation, not only the approvals. The
        # explainability contract requires an arbitrage trace state why an
        # opportunity was skipped, including the rejection reason, so a
        # rejected or deferred decision is explained exactly as an approval is.
        self.explanations.store(
            explain(
                decision,
                decision_id=decision_id,
                timestamp_ms=now_ms,
                confidence_bps=paper_trade.confidence_bps,
                inputs_used=(
                    f"route:{route.fingerprint}",
                    f"snapshot:{paper_trade.snapshot_hash}",
                    f"chain:{discovery.chain_id}",
                    f"notional:{notional_cents}c",
                ),
                alternatives_considered=tuple(
                    r.fingerprint for r in discovery.routing.routes[1:4]
                ),
            )
        )

        self.decisions.append(
            decision_id=decision_id,
            timestamp_ms=now_ms,
            trigger_event=f"discovery:{discovery.chain_id}",
            market_snapshot=paper_trade.snapshot_hash,
            recommendation=recommendation.identity,
            deterministic_calculations={
                "net_edge_bps": route.net_edge_bps,
                "gas_penalty_bps": route.breakdown.gas_penalty_bps,
                "slippage_penalty_bps": route.breakdown.slippage_penalty_bps,
                "simulated_pnl_cents": paper_trade.simulated_pnl_cents,
            },
            policy_evaluation="available" if policy_available else "unavailable",
            risk_verdict=(
                self._last_risk_verdict.summary
                if self._last_risk_verdict
                else "unavailable"
            ),
            simulation_result=paper_trade.summary,
            final_decision=decision.outcome,
            # Explicitly absent rather than omitted: Phase 1 forbids execution,
            # and recording that is itself the required lineage.
            execution_result=None,
            post_execution_outcome=None,
        )
        return decision

    def execute(self, result: "SimulationResult | DiscoveryResult | PaperTradeResult") -> None:
        """Reject execution unconditionally.

        Present so the execution gate exists and is testable. It has no success
        path in this build: the method raises for every input, and there is no
        flag, phase, or configuration that changes that.
        """
        raise ExecutionBlocked()


__all__ = [
    "Decision",
    "Explanation",
    "ExplanationStore",
    "DecisionLedger",
    "DiscoveryResult",
    "PaperTradeResult",
    "PerformanceLedger",
    "ExecutionBlocked",
    "SimulationPipeline",
    "SimulationResult",
    "PHASE_1_BLOCK_CODE",
    "QuoteError",
    "RouteRejected",
    "RpcError",
]
