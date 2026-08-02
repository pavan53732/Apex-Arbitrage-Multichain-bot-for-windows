"""Decision engine — the gatekeeper between recommendation and execution.

Implements the Phase 1 subset of
`docs/apex-app-docs/execution/risk-policy/decision-engine.md`, with the quorum
and veto rules from `docs/apex-app-docs/ai/orchestration/ai-consensus.md`.

The governing rule is stated in the specification's own words: the engine fails
closed, and *no failure path may produce an APPROVED outcome*. Every branch
below therefore ends in REJECTED or DEFER unless every gate has affirmatively
passed.

The distinction between REJECTED and DEFER is load-bearing and comes straight
from the failure table:

* An unavailable **risk** verdict is REJECTED — treated as a veto, not as an
  absent objection. A missing objection is not consent.
* An unavailable **simulation** result is DEFER — execution is withheld pending
  a usable result, because absence of evidence here is not evidence of danger.

Phase 1 never reaches APPROVED regardless: the risk engine's phase gate rejects
first. The full path is implemented so the gate is exercised and testable, not
because it can currently succeed.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .ledger import DecisionOutcome
from .risk import RiskCode, RiskVerdict
from .simulation import FailureCode, SimulationResult


class DecisionState(str, Enum):
    """States from the Decision Engine state machine."""

    RECOMMEND_RECEIVED = "recommend_received"
    VALIDATE_INPUTS = "validate_inputs"
    CHECK_CONSENSUS = "check_consensus"
    RISK_GATE = "risk_gate"
    SIMULATION_GATE = "simulation_gate"
    APPROVED = "approved"
    REJECTED = "rejected"
    DEFER = "defer"


class DecisionCode(str, Enum):
    """Reason codes for a non-approved decision."""

    INPUTS_INVALID = "INPUTS_INVALID"
    CONSENSUS_UNAVAILABLE = "CONSENSUS_UNAVAILABLE"
    CONSENSUS_FAILED = "CONSENSUS_FAILED"
    RISK_VETO = "RISK_VETO"
    RISK_UNAVAILABLE = "RISK_UNAVAILABLE"
    SIMULATION_UNAVAILABLE = "SIMULATION_UNAVAILABLE"
    SIMULATION_FAILED = "SIMULATION_FAILED"
    DECISION_EXPIRED = "DECISION_EXPIRED"
    POLICY_READ_FAILED = "POLICY_READ_FAILED"


# Default decision lifetime. The specification names DECISION_TTL_SECONDS
# without fixing a value, so it is configurable with an explicit default rather
# than hard-coded.
DEFAULT_DECISION_TTL_MS = 30_000

# Consensus quorum. The veto hierarchy states the planner may override only
# with 2/3 consensus, which fixes the required majority.
QUORUM_NUMERATOR = 2
QUORUM_DENOMINATOR = 3


@dataclass(frozen=True)
class AgentVote:
    """One agent's contribution to consensus.

    `confidence_bps` is retained even for abstentions because the consensus
    contract requires output remain traceable to individual agent inputs.
    """

    agent: str
    approve: bool
    confidence_bps: int
    is_veto: bool = False


@dataclass(frozen=True)
class ConsensusResult:
    """Outcome of a consensus round."""

    reached: bool
    approved: bool
    votes: tuple[AgentVote, ...]
    vetoed_by: str | None = None

    @property
    def approvals(self) -> int:
        return sum(1 for v in self.votes if v.approve)

    @property
    def detail(self) -> str:
        if self.vetoed_by:
            return f"vetoed by {self.vetoed_by}"
        return f"{self.approvals}/{len(self.votes)} approvals"


def evaluate_consensus(votes: tuple[AgentVote, ...] | list[AgentVote]) -> ConsensusResult:
    """Apply quorum and veto rules to a set of agent votes.

    A veto is absolute and is checked before counting: the hierarchy places the
    Risk Agent's veto above the planner's majority, so a 3/3 approval alongside
    a veto is still a rejection.

    An empty vote set has not reached quorum. That is distinct from a set that
    voted and failed, and the caller treats the two differently.
    """
    votes = tuple(votes)
    if not votes:
        return ConsensusResult(reached=False, approved=False, votes=())

    veto = next((v for v in votes if v.is_veto), None)
    if veto is not None:
        return ConsensusResult(
            reached=True, approved=False, votes=votes, vetoed_by=veto.agent
        )

    approvals = sum(1 for v in votes if v.approve)
    required = (len(votes) * QUORUM_NUMERATOR + QUORUM_DENOMINATOR - 1) // QUORUM_DENOMINATOR
    return ConsensusResult(reached=True, approved=approvals >= required, votes=votes)


@dataclass(frozen=True)
class Recommendation:
    """A candidate action submitted to the decision engine."""

    identity: str
    route_fingerprint: str
    created_at_ms: int
    notional_cents: int

    def is_valid(self) -> bool:
        """Whether the recommendation is structurally complete.

        Validation is deliberately strict: a malformed recommendation is
        rejected rather than repaired, because repairing it would substitute
        the engine's guess for the caller's intent.
        """
        return bool(
            self.identity.strip()
            and self.route_fingerprint.strip()
            and self.created_at_ms >= 0
            and self.notional_cents > 0
        )


@dataclass(frozen=True)
class Decision:
    """The engine's verdict, with the path it took to reach it."""

    outcome: DecisionOutcome
    state: DecisionState
    code: DecisionCode | None
    detail: str
    path: tuple[DecisionState, ...]
    human_override: bool = False

    @property
    def approved(self) -> bool:
        return self.outcome is DecisionOutcome.APPROVED

    @property
    def summary(self) -> str:
        base = f"{self.outcome.value.upper()} at {self.state.value}"
        if self.code:
            base += f" [{self.code.value}]"
        if self.human_override:
            base += " (human override)"
        return f"{base}: {self.detail}"


def decide(
    recommendation: Recommendation,
    *,
    now_ms: int,
    consensus: ConsensusResult | None,
    risk_verdict: RiskVerdict | None,
    simulation: SimulationResult | None,
    policy_available: bool = True,
    ttl_ms: int = DEFAULT_DECISION_TTL_MS,
    human_override: bool | None = None,
) -> Decision:
    """Run the decision state machine.

    Gates run in the order the state machine declares: validate inputs, check
    consensus, risk gate, simulation gate. The first gate that fails determines
    the outcome, so the reason a recommendation was stopped is stable.

    `human_override` implements the hierarchy's top rule — a human decision via
    the dashboard always wins. It is honoured in both directions: an explicit
    False rejects a recommendation every automated gate approved. It is applied
    only after the automated path has run, so the record still shows what the
    engine would have decided on its own.
    """
    path: list[DecisionState] = [DecisionState.RECOMMEND_RECEIVED]

    def finish(
        state: DecisionState,
        outcome: DecisionOutcome,
        code: DecisionCode | None,
        detail: str,
    ) -> Decision:
        path.append(state)
        # A human decision overrides the automated outcome, but never silently:
        # the path retains every state the engine actually visited.
        if human_override is not None:
            forced = DecisionOutcome.APPROVED if human_override else DecisionOutcome.REJECTED
            return Decision(
                outcome=forced,
                state=DecisionState.APPROVED if human_override else DecisionState.REJECTED,
                code=None if human_override else code,
                detail=f"human override applied; automated outcome was {outcome.value}",
                path=tuple(path),
                human_override=True,
            )
        return Decision(outcome=outcome, state=state, code=code, detail=detail, path=tuple(path))

    # TTL is checked first. A stale decision is void regardless of how well it
    # would otherwise have scored, because the market it described has moved.
    age_ms = now_ms - recommendation.created_at_ms
    if age_ms < 0 or age_ms > ttl_ms:
        return finish(
            DecisionState.REJECTED,
            DecisionOutcome.REJECTED,
            DecisionCode.DECISION_EXPIRED,
            f"recommendation age {age_ms}ms exceeds TTL {ttl_ms}ms",
        )

    # Policy availability gates everything: a threshold that cannot be read is
    # never defaulted.
    if not policy_available:
        return finish(
            DecisionState.REJECTED,
            DecisionOutcome.REJECTED,
            DecisionCode.POLICY_READ_FAILED,
            "policy engine could not supply a required threshold",
        )

    path.append(DecisionState.VALIDATE_INPUTS)
    if not recommendation.is_valid():
        return finish(
            DecisionState.REJECTED,
            DecisionOutcome.REJECTED,
            DecisionCode.INPUTS_INVALID,
            "recommendation is malformed or incomplete",
        )

    path.append(DecisionState.CHECK_CONSENSUS)
    if consensus is None or not consensus.reached:
        # Quorum not reached is a DEFER: the agents have not spoken, which is
        # not the same as having spoken against.
        return finish(
            DecisionState.DEFER,
            DecisionOutcome.DEFERRED,
            DecisionCode.CONSENSUS_UNAVAILABLE,
            "agent quorum not reached; recommendation re-enters the queue until TTL",
        )
    if not consensus.approved:
        return finish(
            DecisionState.REJECTED,
            DecisionOutcome.REJECTED,
            DecisionCode.CONSENSUS_FAILED,
            f"consensus rejected: {consensus.detail}",
        )

    path.append(DecisionState.RISK_GATE)
    if risk_verdict is None:
        # An unavailable risk verdict is a veto, not an absent objection.
        return finish(
            DecisionState.REJECTED,
            DecisionOutcome.REJECTED,
            DecisionCode.RISK_UNAVAILABLE,
            "risk verdict unavailable; treated as a veto",
        )
    if not risk_verdict.approved:
        return finish(
            DecisionState.REJECTED,
            DecisionOutcome.REJECTED,
            DecisionCode.RISK_VETO,
            f"risk engine rejected: {risk_verdict.code.value if risk_verdict.code else 'unknown'}",
        )

    path.append(DecisionState.SIMULATION_GATE)
    if simulation is None:
        # Unavailable simulation defers rather than rejects: execution is
        # withheld pending a usable result.
        return finish(
            DecisionState.DEFER,
            DecisionOutcome.DEFERRED,
            DecisionCode.SIMULATION_UNAVAILABLE,
            "simulation result unavailable; execution withheld pending a usable result",
        )
    if simulation.failure_code is not None:
        return finish(
            DecisionState.REJECTED,
            DecisionOutcome.REJECTED,
            DecisionCode.SIMULATION_FAILED,
            f"simulation reported {simulation.failure_code.value}",
        )
    if simulation.simulated_pnl_cents <= 0:
        return finish(
            DecisionState.REJECTED,
            DecisionOutcome.REJECTED,
            DecisionCode.SIMULATION_FAILED,
            f"simulated PNL {simulation.simulated_pnl_cents}c is not positive",
        )

    return finish(
        DecisionState.APPROVED,
        DecisionOutcome.APPROVED,
        None,
        "all gates passed",
    )
