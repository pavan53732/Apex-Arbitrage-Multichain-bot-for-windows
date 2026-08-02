"""Tests for the trade lifecycle state machine.

The specification lists allowed and forbidden transitions separately, so both
lists are tested — a forbidden move must be refused as prohibited, not merely
as unrecognised.
"""

from __future__ import annotations

import pytest

from apex.trading import (
    ForbiddenTradeTransition,
    InvalidTransition,
    PhaseBoundaryViolation,
    Trade,
    TradeState,
)

NOW = 1_000_000


def new_trade() -> Trade:
    return Trade(identity="USDC/WETH@b->a")


def advance_to_simulating(trade: Trade) -> Trade:
    for target in (
        TradeState.SCANNING,
        TradeState.OPPORTUNITY_DETECTED,
        TradeState.RISK_CHECK,
        TradeState.SIMULATING,
    ):
        trade.advance(target, at_ms=NOW)
    return trade


def test_trade_starts_idle() -> None:
    assert new_trade().state is TradeState.IDLE


def test_declared_happy_path_is_walkable() -> None:
    trade = advance_to_simulating(new_trade())
    assert trade.state is TradeState.SIMULATING
    assert trade.path == (
        TradeState.IDLE,
        TradeState.SCANNING,
        TradeState.OPPORTUNITY_DETECTED,
        TradeState.RISK_CHECK,
        TradeState.SIMULATING,
    )


@pytest.mark.parametrize(
    "source,target",
    [
        (TradeState.EXECUTING, TradeState.SETTLED),
        (TradeState.IDLE, TradeState.EXECUTING),
        (TradeState.SETTLED, TradeState.SCANNING),
        (TradeState.SCANNING, TradeState.SETTLED),
    ],
)
def test_forbidden_transitions_are_refused_as_prohibited(
    source: TradeState, target: TradeState
) -> None:
    """Each pair the specification names as forbidden."""
    trade = Trade(identity="t", state=source)
    with pytest.raises(ForbiddenTradeTransition, match="explicitly forbidden"):
        trade.advance(target, at_ms=NOW, allow_execution=True)


def test_unrecognised_transition_is_refused_as_invalid() -> None:
    """Distinct from forbidden: not in the allowed set, not named prohibited."""
    trade = new_trade()
    with pytest.raises(InvalidTransition, match="not an allowed transition"):
        trade.advance(TradeState.RISK_CHECK, at_ms=NOW)


def test_execution_state_unreachable_in_phase_1() -> None:
    """SIMULATING -> EXECUTING is allowed by the machine but blocked by phase."""
    trade = advance_to_simulating(new_trade())
    with pytest.raises(PhaseBoundaryViolation, match="unreachable while live execution"):
        trade.advance(TradeState.EXECUTING, at_ms=NOW)


def test_execution_state_modellable_when_explicitly_permitted() -> None:
    """The stage stays testable without being reachable by default."""
    trade = advance_to_simulating(new_trade())
    trade.advance(TradeState.EXECUTING, at_ms=NOW, allow_execution=True)
    assert trade.state is TradeState.EXECUTING


def test_failure_path_routes_through_retry() -> None:
    trade = Trade(identity="t", state=TradeState.VERIFYING)
    trade.advance(TradeState.FAILED, at_ms=NOW, reason="confirmation failed")
    trade.advance(TradeState.RETRY, at_ms=NOW + 1)
    trade.advance(TradeState.SCANNING, at_ms=NOW + 2)
    assert trade.state is TradeState.SCANNING
    assert trade.retry_count == 1


def test_retry_count_accumulates() -> None:
    trade = Trade(identity="t", state=TradeState.VERIFYING)
    for i in range(3):
        trade.advance(TradeState.FAILED, at_ms=NOW + i)
        trade.advance(TradeState.RETRY, at_ms=NOW + i)
        trade.advance(TradeState.SCANNING, at_ms=NOW + i)
        trade.advance(TradeState.OPPORTUNITY_DETECTED, at_ms=NOW + i)
        trade.advance(TradeState.RISK_CHECK, at_ms=NOW + i)
        trade.advance(TradeState.SIMULATING, at_ms=NOW + i)
        trade.advance(TradeState.EXECUTING, at_ms=NOW + i, allow_execution=True)
        trade.advance(TradeState.VERIFYING, at_ms=NOW + i, allow_execution=True)
    assert trade.retry_count == 3


def test_settled_returns_to_idle() -> None:
    trade = Trade(identity="t", state=TradeState.VERIFYING)
    trade.advance(TradeState.SETTLED, at_ms=NOW, allow_execution=True)
    trade.advance(TradeState.IDLE, at_ms=NOW + 1)
    assert trade.is_terminal is True


def test_fresh_idle_trade_is_not_terminal() -> None:
    """Terminal means at rest after work, not merely idle."""
    assert new_trade().is_terminal is False


def test_history_records_reason_and_time() -> None:
    trade = new_trade()
    trade.advance(TradeState.SCANNING, at_ms=NOW, reason="scan cycle started")
    step = trade.history[0]
    assert step.source is TradeState.IDLE
    assert step.target is TradeState.SCANNING
    assert step.at_ms == NOW
    assert step.reason == "scan cycle started"


def test_history_distinguishes_direct_settle_from_retried_settle() -> None:
    """Only the history separates a clean trade from a recovered one."""
    clean = Trade(identity="clean", state=TradeState.VERIFYING)
    clean.advance(TradeState.SETTLED, at_ms=NOW, allow_execution=True)

    retried = Trade(identity="retried", state=TradeState.VERIFYING)
    retried.advance(TradeState.FAILED, at_ms=NOW)
    retried.advance(TradeState.RETRY, at_ms=NOW)

    assert clean.retry_count == 0
    assert retried.retry_count == 1
    assert TradeState.FAILED not in clean.path
    assert TradeState.FAILED in retried.path


def test_can_advance_reports_without_raising() -> None:
    trade = new_trade()
    assert trade.can_advance_to(TradeState.SCANNING) is True
    assert trade.can_advance_to(TradeState.EXECUTING) is False


def test_refused_transition_does_not_mutate_state() -> None:
    trade = new_trade()
    with pytest.raises(InvalidTransition):
        trade.advance(TradeState.SETTLED, at_ms=NOW)
    assert trade.state is TradeState.IDLE
    assert trade.history == []
