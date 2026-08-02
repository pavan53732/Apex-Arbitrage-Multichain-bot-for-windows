"""Decision explanation traces.

Implements `docs/apex-app-docs/ai/explainability/explainability.md`.

The specification defines a mandatory trace format with eight required fields
and one hard rule: *an explanation without a rationale is non-compliant and is
rejected for storage.* That rule is enforced at construction, so a
non-compliant explanation cannot exist long enough to be stored by mistake.

The ledger already holds decision lineage. This module is the human-readable
counterpart: the ledger answers "what was decided", an explanation answers
"why", including for the decisions that were skipped or delayed. Arbitrage
explanations must state why an opportunity was taken *or skipped*, so a
rejection produces an explanation exactly as an approval does.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from .decision import Decision, DecisionState
from .ledger import DecisionOutcome


class ExplanationState(str, Enum):
    """States from the explainability state machine."""

    CAPTURED = "captured"
    EXPLAINED = "explained"
    STORED = "stored"
    REPLAYABLE = "replayable"


_ALLOWED: dict[ExplanationState, frozenset[ExplanationState]] = {
    ExplanationState.CAPTURED: frozenset({ExplanationState.EXPLAINED}),
    ExplanationState.EXPLAINED: frozenset({ExplanationState.STORED}),
    ExplanationState.STORED: frozenset({ExplanationState.REPLAYABLE}),
    ExplanationState.REPLAYABLE: frozenset(),
}


class NonCompliantExplanation(Exception):
    """Raised when a trace is missing a field the specification requires."""


class InvalidExplanationTransition(Exception):
    """Raised when an explanation lifecycle transition is not permitted."""


@dataclass(frozen=True)
class Explanation:
    """A compliant explanation trace.

    Field names follow the specification's required-fields list. Validation
    happens in `__post_init__` so an incomplete trace raises at construction
    rather than at storage — by storage time the context needed to complete it
    is usually gone.
    """

    decision_id: str
    rationale: str
    confidence_bps: int
    alternatives_considered: tuple[str, ...]
    inputs_used: tuple[str, ...]
    gates_passed: tuple[str, ...]
    veto_source: str | None
    timestamp_ms: int
    outcome: DecisionOutcome
    state: ExplanationState = ExplanationState.CAPTURED

    def __post_init__(self) -> None:
        if not self.decision_id.strip():
            raise NonCompliantExplanation("explanation is missing a decision ID")
        if not self.rationale.strip():
            # The specification's explicit rule, enforced as an error.
            raise NonCompliantExplanation(
                f"explanation for {self.decision_id} has no rationale; "
                f"a rationale-free explanation is rejected for storage"
            )
        if not 0 <= self.confidence_bps <= 10_000:
            raise NonCompliantExplanation(
                f"confidence {self.confidence_bps}bps outside 0..10000"
            )
        if not self.inputs_used:
            raise NonCompliantExplanation(
                f"explanation for {self.decision_id} records no inputs; "
                f"decision context is required for auditability"
            )
        if self.timestamp_ms < 0:
            raise NonCompliantExplanation("timestamp must not be negative")

    def transition_to(self, target: ExplanationState) -> "Explanation":
        if target not in _ALLOWED[self.state]:
            raise InvalidExplanationTransition(
                f"{self.decision_id}: {self.state.value} -> {target.value} is not allowed"
            )
        return Explanation(
            decision_id=self.decision_id,
            rationale=self.rationale,
            confidence_bps=self.confidence_bps,
            alternatives_considered=self.alternatives_considered,
            inputs_used=self.inputs_used,
            gates_passed=self.gates_passed,
            veto_source=self.veto_source,
            timestamp_ms=self.timestamp_ms,
            outcome=self.outcome,
            state=target,
        )

    @property
    def is_replayable(self) -> bool:
        return self.state is ExplanationState.REPLAYABLE

    def render(self) -> str:
        """A human-readable trace.

        The audience is an operator asking why a trade did or did not happen,
        so the outcome and its reason lead, and the supporting detail follows.
        """
        lines = [
            f"Decision {self.decision_id} — {self.outcome.value.upper()}",
            f"  Rationale: {self.rationale}",
            f"  Confidence: {self.confidence_bps}bps",
            f"  Gates passed: {', '.join(self.gates_passed) if self.gates_passed else 'none'}",
        ]
        if self.veto_source:
            lines.append(f"  Veto source: {self.veto_source}")
        if self.alternatives_considered:
            lines.append(f"  Alternatives: {', '.join(self.alternatives_considered)}")
        lines.append(f"  Inputs: {', '.join(self.inputs_used)}")
        lines.append(f"  At: {self.timestamp_ms}ms")
        return "\n".join(lines)


def _rationale_for(decision: Decision) -> str:
    """Derive a rationale from the decision's own outcome and path.

    Built from what the engine recorded rather than restated by the caller, so
    the explanation cannot drift from the decision it explains.
    """
    if decision.human_override:
        verdict = "approved" if decision.approved else "rejected"
        return f"Human override {verdict} the recommendation; {decision.detail}"
    if decision.approved:
        return f"All gates passed through {decision.state.value}; {decision.detail}"
    if decision.outcome is DecisionOutcome.DEFERRED:
        return f"Deferred at {decision.state.value}: {decision.detail}"
    return f"Rejected at {decision.state.value}: {decision.detail}"


def _gates_passed(decision: Decision) -> tuple[str, ...]:
    """Gates the decision cleared before reaching its outcome.

    The path records every state visited; the terminal state is the outcome
    rather than a gate, so it is excluded.
    """
    terminal = {DecisionState.APPROVED, DecisionState.REJECTED, DecisionState.DEFER}
    return tuple(
        state.value
        for state in decision.path
        if state not in terminal and state is not DecisionState.RECOMMEND_RECEIVED
    )


def explain(
    decision: Decision,
    *,
    decision_id: str,
    timestamp_ms: int,
    confidence_bps: int,
    inputs_used: tuple[str, ...] | list[str],
    alternatives_considered: tuple[str, ...] | list[str] = (),
    veto_source: str | None = None,
) -> Explanation:
    """Build a compliant explanation from a decision.

    Produced for every decision, not only approvals: the contract requires an
    arbitrage explanation state why an opportunity was skipped, including the
    rejection reason.
    """
    return Explanation(
        decision_id=decision_id,
        rationale=_rationale_for(decision),
        confidence_bps=confidence_bps,
        alternatives_considered=tuple(alternatives_considered),
        inputs_used=tuple(inputs_used),
        gates_passed=_gates_passed(decision),
        veto_source=veto_source or (decision.code.value if decision.code else None),
        timestamp_ms=timestamp_ms,
        outcome=decision.outcome,
    )


@dataclass
class ExplanationStore:
    """Explanations advanced to a replayable state.

    Storage advances the lifecycle explicitly rather than accepting an
    arbitrary state, so a trace only becomes replayable by passing through
    CAPTURED -> EXPLAINED -> STORED as the state machine requires.
    """

    _explanations: list[Explanation] = field(default_factory=list, init=False)

    def __len__(self) -> int:
        return len(self._explanations)

    def store(self, explanation: Explanation) -> Explanation:
        advanced = (
            explanation
            .transition_to(ExplanationState.EXPLAINED)
            .transition_to(ExplanationState.STORED)
            .transition_to(ExplanationState.REPLAYABLE)
        )
        self._explanations.append(advanced)
        return advanced

    @property
    def explanations(self) -> tuple[Explanation, ...]:
        return tuple(self._explanations)

    def for_decision(self, decision_id: str) -> Explanation:
        for explanation in self._explanations:
            if explanation.decision_id == decision_id:
                return explanation
        raise KeyError(f"no explanation stored for {decision_id!r}")
