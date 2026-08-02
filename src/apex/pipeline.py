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
from .dex import Pool, Quote, QuoteError, best_quote
from .opportunity import (
    Candidate,
    DetectionResult,
    OpportunityState,
    Rejection,
    detect,
)
from .routing import Route, RouteRejected, RouteState, RoutingResult, rank_routes
from .rpc import RpcError, RpcPool

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
    _warnings: list[str] = field(default_factory=list, init=False)

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

    def execute(self, result: "SimulationResult | DiscoveryResult") -> None:
        """Reject execution unconditionally.

        Present so the execution gate exists and is testable. It has no success
        path in this build: the method raises for every input, and there is no
        flag, phase, or configuration that changes that.
        """
        raise ExecutionBlocked()


__all__ = [
    "DiscoveryResult",
    "ExecutionBlocked",
    "SimulationPipeline",
    "SimulationResult",
    "PHASE_1_BLOCK_CODE",
    "QuoteError",
    "RouteRejected",
    "RpcError",
]
