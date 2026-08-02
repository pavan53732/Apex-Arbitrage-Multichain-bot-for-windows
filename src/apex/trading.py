"""Trade lifecycle state machine.

Implements `docs/apex-app-docs/execution/trading/trading-lifecycle.md`.

The specification states allowed transitions and forbidden transitions as two
separate lists. Both are encoded here, and the forbidden list is checked
explicitly rather than left implicit in the allowed list. That is deliberate:
a transition absent from the allowed set is rejected as unrecognised, but one
named in the forbidden set is rejected as *prohibited*, and the distinction
matters when diagnosing why a trade stalled.

Phase 1 reaches `SIMULATING` and stops. `EXECUTING` is unreachable because live
execution is blocked, so the lifecycle here terminates at the simulation state
rather than advancing into a stage the phase forbids.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class TradeState(str, Enum):
    """States from the canonical trade state machine."""

    IDLE = "idle"
    SCANNING = "scanning"
    OPPORTUNITY_DETECTED = "opportunity_detected"
    RISK_CHECK = "risk_check"
    SIMULATING = "simulating"
    EXECUTING = "executing"
    VERIFYING = "verifying"
    SETTLED = "settled"
    FAILED = "failed"
    RETRY = "retry"


# Transcribed from the specification's "Allowed transitions" list.
_ALLOWED: dict[TradeState, frozenset[TradeState]] = {
    TradeState.IDLE: frozenset({TradeState.SCANNING}),
    TradeState.SCANNING: frozenset({TradeState.OPPORTUNITY_DETECTED}),
    TradeState.OPPORTUNITY_DETECTED: frozenset({TradeState.RISK_CHECK}),
    TradeState.RISK_CHECK: frozenset({TradeState.SIMULATING}),
    TradeState.SIMULATING: frozenset({TradeState.EXECUTING}),
    TradeState.EXECUTING: frozenset({TradeState.VERIFYING}),
    TradeState.VERIFYING: frozenset({TradeState.SETTLED, TradeState.FAILED}),
    TradeState.FAILED: frozenset({TradeState.RETRY}),
    TradeState.RETRY: frozenset({TradeState.SCANNING}),
    TradeState.SETTLED: frozenset({TradeState.IDLE}),
}

# Transcribed from the specification's "Forbidden transitions" list. Every entry
# is already absent from `_ALLOWED`; naming them separately lets the engine
# report a prohibited move differently from an unrecognised one.
_FORBIDDEN: frozenset[tuple[TradeState, TradeState]] = frozenset(
    {
        (TradeState.EXECUTING, TradeState.SETTLED),
        (TradeState.IDLE, TradeState.EXECUTING),
        (TradeState.SETTLED, TradeState.SCANNING),
        (TradeState.SCANNING, TradeState.SETTLED),
    }
)

# States a Phase 1 build may enter. Live execution is blocked, so the trade
# cannot legitimately advance past simulation.
_PHASE_1_REACHABLE: frozenset[TradeState] = frozenset(
    {
        TradeState.IDLE,
        TradeState.SCANNING,
        TradeState.OPPORTUNITY_DETECTED,
        TradeState.RISK_CHECK,
        TradeState.SIMULATING,
        TradeState.FAILED,
        TradeState.RETRY,
    }
)


class InvalidTransition(Exception):
    """Raised when a transition is not in the allowed set."""


class ForbiddenTradeTransition(InvalidTransition):
    """Raised when a transition is explicitly prohibited by the specification."""


class PhaseBoundaryViolation(InvalidTransition):
    """Raised when a transition would enter a state this phase forbids.

    Distinct from a forbidden transition: the move is legal in the state
    machine but unreachable while live execution is blocked.
    """


@dataclass(frozen=True)
class TradeTransition:
    """One recorded step in a trade's history."""

    source: TradeState
    target: TradeState
    at_ms: int
    reason: str


@dataclass
class Trade:
    """A trade progressing through the canonical lifecycle.

    History is retained because the lifecycle contract requires a trade's path
    be reconstructable — a settled trade and a retried one that eventually
    settled are different outcomes, and only the history distinguishes them.
    """

    identity: str
    state: TradeState = TradeState.IDLE
    history: list[TradeTransition] = field(default_factory=list)
    retry_count: int = 0

    def can_advance_to(self, target: TradeState) -> bool:
        return target in _ALLOWED.get(self.state, frozenset())

    def advance(
        self,
        target: TradeState,
        *,
        at_ms: int,
        reason: str = "",
        allow_execution: bool = False,
    ) -> "Trade":
        """Advance to `target`, or raise explaining why the move is refused.

        `allow_execution` exists so the execution states remain testable while
        staying unreachable by default. It does not enable execution — nothing
        in this build signs or broadcasts — it only permits the state machine
        to model the stage.
        """
        if (self.state, target) in _FORBIDDEN:
            raise ForbiddenTradeTransition(
                f"{self.identity}: {self.state.value} -> {target.value} is explicitly forbidden"
            )
        if not self.can_advance_to(target):
            raise InvalidTransition(
                f"{self.identity}: {self.state.value} -> {target.value} is not an allowed transition"
            )
        if target not in _PHASE_1_REACHABLE and not allow_execution:
            raise PhaseBoundaryViolation(
                f"{self.identity}: {target.value} is unreachable while live execution is blocked"
            )

        self.history.append(
            TradeTransition(source=self.state, target=target, at_ms=at_ms, reason=reason)
        )
        if target is TradeState.RETRY:
            self.retry_count += 1
        self.state = target
        return self

    @property
    def path(self) -> tuple[TradeState, ...]:
        """Every state visited, starting from the initial state."""
        if not self.history:
            return (self.state,)
        return (self.history[0].source,) + tuple(t.target for t in self.history)

    @property
    def is_terminal(self) -> bool:
        """Whether the trade has reached a resting state.

        `SETTLED` returns to `IDLE`, so neither is genuinely terminal in the
        machine; a trade is at rest when it is idle with history behind it.
        """
        return self.state is TradeState.IDLE and bool(self.history)
