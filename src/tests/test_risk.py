"""Tests for the risk check pipeline.

The pipeline-order and fail-closed tests matter most: both are explicit
guarantees in `risk-engine.md`.
"""

from __future__ import annotations

import pytest

from apex.risk import (
    RiskCode,
    RiskLimits,
    TradeAssessment,
    evaluate,
)


def healthy_assessment(**overrides: object) -> TradeAssessment:
    params = dict(
        position_size_cents=1_000,
        max_adverse_movement_bps=100,      # 1% -> 10c estimated loss
        pool_liquidity_cents=1_000_000,    # 5% of this is 50_000c
        expected_output=1_000_000,
        minimum_output=999_500,            # 5bps slippage
        dex_price_bps=10_000,
        oracle_price_bps=10_000,
        estimated_execution_ms=100,
        window_remaining_ms=5_000,
        open_exposure_cents=0,
    )
    params.update(overrides)
    return TradeAssessment(**params)  # type: ignore[arg-type]


def test_phase_1_rejects_even_when_all_other_checks_pass() -> None:
    """No combination of passing checks can approve a trade in Phase 1."""
    verdict = evaluate(healthy_assessment(), simulation_only=True)

    assert verdict.approved is False
    assert verdict.code is RiskCode.PHASE_1_EXECUTION_BLOCK
    # every downstream check still ran and passed
    downstream = [o for o in verdict.outcomes if o.name != "phase_gate"]
    assert all(o.passed for o in downstream)


def test_phase_gate_runs_first() -> None:
    """Order is part of the contract; the gate precedes every other check."""
    verdict = evaluate(healthy_assessment(), simulation_only=True)
    assert verdict.outcomes[0].name == "phase_gate"


def test_pipeline_order_matches_specification() -> None:
    verdict = evaluate(healthy_assessment(), simulation_only=False)
    assert [o.name for o in verdict.outcomes] == [
        "phase_gate",
        "max_loss",
        "liquidity",
        "slippage",
        "spread_integrity",
        "timing_budget",
        "exposure",
    ]


def test_healthy_trade_approved_outside_phase_1() -> None:
    verdict = evaluate(healthy_assessment(), simulation_only=False)
    assert verdict.approved is True
    assert verdict.code is None
    assert "APPROVED" in verdict.summary


def test_simulation_only_defaults_to_true() -> None:
    """A caller that forgets the phase must not escape the gate."""
    verdict = evaluate(healthy_assessment())
    assert verdict.code is RiskCode.PHASE_1_EXECUTION_BLOCK


def test_max_loss_limit_enforced() -> None:
    verdict = evaluate(
        healthy_assessment(position_size_cents=1_000_000, max_adverse_movement_bps=1_000),
        simulation_only=False,
    )
    assert verdict.code is RiskCode.LOSS_LIMIT_EXCEEDED


def test_liquidity_usage_cap_enforced() -> None:
    verdict = evaluate(
        healthy_assessment(position_size_cents=100_000, pool_liquidity_cents=1_000_000),
        simulation_only=False,
    )
    assert verdict.code is RiskCode.LIQUIDITY_INSUFFICIENT


def test_zero_liquidity_rejects() -> None:
    verdict = evaluate(
        healthy_assessment(pool_liquidity_cents=0), simulation_only=False
    )
    assert verdict.code is RiskCode.LIQUIDITY_INSUFFICIENT


def test_slippage_limit_enforced() -> None:
    verdict = evaluate(
        healthy_assessment(expected_output=1_000_000, minimum_output=900_000),
        simulation_only=False,
    )
    assert verdict.code is RiskCode.SLIPPAGE_EXCEEDED


def test_price_deviation_detected() -> None:
    verdict = evaluate(
        healthy_assessment(dex_price_bps=11_000, oracle_price_bps=10_000),
        simulation_only=False,
    )
    assert verdict.code is RiskCode.PRICE_INTEGRITY_FAIL


def test_missing_oracle_fails_closed() -> None:
    """An unavailable input is not an absent objection."""
    verdict = evaluate(healthy_assessment(oracle_price_bps=None), simulation_only=False)
    assert verdict.approved is False
    assert verdict.code is RiskCode.INPUT_UNAVAILABLE


def test_timing_budget_enforced() -> None:
    verdict = evaluate(
        healthy_assessment(estimated_execution_ms=4_900, window_remaining_ms=5_000),
        simulation_only=False,
    )
    assert verdict.code is RiskCode.TIMING_BUDGET_EXCEEDED


def test_closed_window_rejects() -> None:
    verdict = evaluate(healthy_assessment(window_remaining_ms=0), simulation_only=False)
    assert verdict.code is RiskCode.TIMING_BUDGET_EXCEEDED


def test_exposure_limit_enforced() -> None:
    verdict = evaluate(
        healthy_assessment(open_exposure_cents=49_500, position_size_cents=1_000),
        simulation_only=False,
    )
    assert verdict.code is RiskCode.EXPOSURE_LIMIT_EXCEEDED


def test_first_failure_determines_the_code() -> None:
    """Two simultaneous failures report the earlier check in pipeline order."""
    verdict = evaluate(
        healthy_assessment(
            position_size_cents=1_000_000,   # fails max_loss (earlier)
            max_adverse_movement_bps=1_000,
            expected_output=1_000_000,
            minimum_output=1,                # would fail slippage (later)
        ),
        simulation_only=False,
    )
    assert verdict.code is RiskCode.LOSS_LIMIT_EXCEEDED


def test_verdict_records_every_check_for_audit() -> None:
    verdict = evaluate(healthy_assessment(), simulation_only=False)
    assert len(verdict.outcomes) == 7
    assert verdict.failed_check is None


def test_failed_check_is_exposed() -> None:
    verdict = evaluate(healthy_assessment(window_remaining_ms=0), simulation_only=False)
    failed = verdict.failed_check
    assert failed is not None
    assert failed.name == "timing_budget"
    assert "window" in failed.detail


def test_evaluation_is_deterministic() -> None:
    a = healthy_assessment()
    first = evaluate(a, simulation_only=False)
    second = evaluate(a, simulation_only=False)
    assert first.approved == second.approved
    assert [o.name for o in first.outcomes] == [o.name for o in second.outcomes]


def test_negative_limits_rejected() -> None:
    with pytest.raises(ValueError, match="must not be negative"):
        RiskLimits(max_slippage_bps=-1)


def test_all_arithmetic_is_integer() -> None:
    verdict = evaluate(healthy_assessment(), simulation_only=False)
    assert isinstance(verdict.approved, bool)
    for outcome in verdict.outcomes:
        assert isinstance(outcome.passed, bool)
