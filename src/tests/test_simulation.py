"""Tests for the paper-trading simulation engine.

Reproducibility is a mandatory contract rule in all phases, so it is tested
directly rather than assumed.
"""

from __future__ import annotations

import pytest

from apex.dex import Pool
from apex.opportunity import Candidate
from apex.risk import RiskCode, TradeAssessment, evaluate
from apex.routing import build_route
from apex.simulation import (
    MARKET_DATA_MAX_AGE_MS,
    FailureCode,
    PerformanceLedger,
    SimulationError,
    SimulationMode,
    simulate,
    snapshot_hash,
)

NOW = 1_000_000


def make_pool(dex_id: str, reserve_in: int, reserve_out: int, **overrides: object) -> Pool:
    params = dict(
        dex_id=dex_id,
        token_in="USDC",
        token_out="WETH",
        reserve_in=reserve_in,
        reserve_out=reserve_out,
        fee_bps=30,
        observed_at_ms=NOW,
    )
    params.update(overrides)
    return Pool(**params)  # type: ignore[arg-type]


def make_route(edge_bps: int = 1_000, **pool_overrides: object):
    candidate = Candidate(
        pair=("USDC", "WETH"),
        buy_pool=make_pool("venue-b", 1_000_000_000, 550_000_000, **pool_overrides),
        sell_pool=make_pool("venue-a", 1_000_000_000, 500_000_000, **pool_overrides),
        gross_edge_bps=edge_bps,
        detected_at_ms=NOW,
    )
    return build_route(
        candidate,
        1_000_000,
        now_ms=NOW,
        freshness_budget_ms=5_000,
        max_slippage_bps=500,
        gas_cost_units=1_000,
    )


def healthy_assessment(**overrides: object) -> TradeAssessment:
    params = dict(
        position_size_cents=1_000,
        max_adverse_movement_bps=100,
        pool_liquidity_cents=1_000_000,
        expected_output=1_000_000,
        minimum_output=999_500,
        dex_price_bps=10_000,
        oracle_price_bps=10_000,
        estimated_execution_ms=100,
        window_remaining_ms=5_000,
        open_exposure_cents=0,
    )
    params.update(overrides)
    return TradeAssessment(**params)  # type: ignore[arg-type]


APPROVED = None  # set in setup below


def approved_verdict():
    return evaluate(healthy_assessment(), simulation_only=False)


def blocked_verdict():
    return evaluate(healthy_assessment(), simulation_only=True)


def test_paper_trade_records_pnl_components() -> None:
    result = simulate(
        make_route(), 1_000_000, now_ms=NOW, gas_cost_cents=10,
        risk_verdict=approved_verdict(),
    )
    assert result.gross_proceeds_cents > 0
    assert result.gas_cost_cents == 10
    assert result.simulated_pnl_cents == (
        result.gross_proceeds_cents - result.slippage_cost_cents - result.gas_cost_cents
    )


def test_slippage_and_gas_are_subtracted_before_pnl() -> None:
    """A simulation must not report a profit the real trade would not make."""
    cheap = simulate(
        make_route(), 1_000_000, now_ms=NOW, gas_cost_cents=0,
        risk_verdict=approved_verdict(),
    )
    dear = simulate(
        make_route(), 1_000_000, now_ms=NOW, gas_cost_cents=500,
        risk_verdict=approved_verdict(),
    )
    assert dear.simulated_pnl_cents == cheap.simulated_pnl_cents - 500


def test_simulation_is_reproducible() -> None:
    """Same inputs and seed must produce the same outcome."""
    runs = [
        simulate(
            make_route(), 1_000_000, now_ms=NOW, gas_cost_cents=10,
            risk_verdict=approved_verdict(), seed=42,
        )
        for _ in range(3)
    ]
    assert len({r.simulated_pnl_cents for r in runs}) == 1
    assert len({r.snapshot_hash for r in runs}) == 1
    assert len({r.confidence_bps for r in runs}) == 1


def test_result_records_replay_material() -> None:
    """The record must be sufficient to replay the trade."""
    result = simulate(
        make_route(), 1_000_000, now_ms=NOW, gas_cost_cents=10,
        risk_verdict=approved_verdict(), seed=7,
    )
    assert result.seed == 7
    assert result.code_version
    assert len(result.snapshot_hash) == 16
    assert result.mode is SimulationMode.PAPER_TRADING


def test_snapshot_hash_changes_with_inputs() -> None:
    route = make_route()
    a = snapshot_hash(route, 1_000_000, NOW)
    b = snapshot_hash(route, 2_000_000, NOW)
    assert a != b


def test_stale_market_data_fails_the_simulation() -> None:
    """A route built from fresh data can still go stale before simulation.

    Routing rejects a stale quote at build time, so staleness reaches the
    simulator only when time passes between construction and execution — which
    is exactly the case the freshness gate exists to catch.
    """
    route = make_route()  # built against fresh reserves at NOW
    later = NOW + MARKET_DATA_MAX_AGE_MS + 1

    result = simulate(
        route, 1_000_000, now_ms=later,
        gas_cost_cents=10, risk_verdict=approved_verdict(),
    )
    assert result.failure_code is FailureCode.STALE_MARKET_DATA
    assert result.simulated_pnl_cents == 0
    assert result.confidence_bps == 0


def test_route_within_freshness_window_simulates() -> None:
    """The boundary case must pass, or the gate is off by one."""
    route = make_route()
    result = simulate(
        route, 1_000_000, now_ms=NOW + MARKET_DATA_MAX_AGE_MS,
        gas_cost_cents=0, risk_verdict=approved_verdict(),
    )
    assert result.failure_code is not FailureCode.STALE_MARKET_DATA


def test_risk_rejection_is_recorded_not_skipped() -> None:
    """Phase 1 gathers data on rejected trades too, to avoid biasing the record."""
    result = simulate(
        make_route(), 1_000_000, now_ms=NOW, gas_cost_cents=10,
        risk_verdict=blocked_verdict(),
    )
    assert result.failure_code is FailureCode.RISK_REJECTED
    assert result.gross_proceeds_cents > 0  # the trade was still simulated


def test_unprofitable_trade_flagged() -> None:
    result = simulate(
        make_route(edge_bps=1), 1_000_000, now_ms=NOW, gas_cost_cents=100_000,
        risk_verdict=approved_verdict(),
    )
    assert result.failure_code is FailureCode.NEGATIVE_PNL
    assert result.profitable is False


def test_confidence_lower_when_risk_rejects() -> None:
    approved = simulate(
        make_route(), 1_000_000, now_ms=NOW, gas_cost_cents=10,
        risk_verdict=approved_verdict(),
    )
    blocked = simulate(
        make_route(), 1_000_000, now_ms=NOW, gas_cost_cents=10,
        risk_verdict=blocked_verdict(),
    )
    assert blocked.confidence_bps < approved.confidence_bps


def test_confidence_is_bounded() -> None:
    result = simulate(
        make_route(edge_bps=100_000), 1_000_000, now_ms=NOW, gas_cost_cents=0,
        risk_verdict=approved_verdict(),
    )
    assert 0 <= result.confidence_bps <= 10_000


def test_execution_flags_never_set() -> None:
    """Simulation records a trade; it never performs one."""
    result = simulate(
        make_route(), 1_000_000, now_ms=NOW, gas_cost_cents=10,
        risk_verdict=approved_verdict(),
    )
    assert result.executed is False
    assert result.rejection_code == RiskCode.PHASE_1_EXECUTION_BLOCK.value


def test_unimplemented_mode_refused() -> None:
    """A mode that is not implemented is refused, not silently downgraded."""
    with pytest.raises(SimulationError, match="not implemented"):
        simulate(
            make_route(), 1_000_000, now_ms=NOW, gas_cost_cents=10,
            risk_verdict=approved_verdict(), mode=SimulationMode.HISTORICAL_REPLAY,
        )


def test_non_positive_amount_refused() -> None:
    with pytest.raises(SimulationError, match="must be positive"):
        simulate(
            make_route(), 0, now_ms=NOW, gas_cost_cents=10,
            risk_verdict=approved_verdict(),
        )


def test_pnl_is_integer_arithmetic() -> None:
    result = simulate(
        make_route(), 1_000_000, now_ms=NOW, gas_cost_cents=10,
        risk_verdict=approved_verdict(),
    )
    for value in (
        result.simulated_pnl_cents,
        result.gross_proceeds_cents,
        result.slippage_cost_cents,
        result.confidence_bps,
    ):
        assert isinstance(value, int)


# --- performance ledger ----------------------------------------------------


def test_ledger_accumulates_outcomes() -> None:
    ledger = PerformanceLedger()
    ledger.record(
        simulate(make_route(), 1_000_000, now_ms=NOW, gas_cost_cents=0,
                 risk_verdict=approved_verdict())
    )
    ledger.record(
        simulate(make_route(edge_bps=1), 1_000_000, now_ms=NOW, gas_cost_cents=100_000,
                 risk_verdict=approved_verdict())
    )
    assert len(ledger.results) == 2
    assert ledger.wins == 1
    assert ledger.losses == 1
    assert ledger.win_rate_bps == 5_000


def test_ledger_excludes_rejected_trades_from_win_rate() -> None:
    """A trade risk refused was never a trading decision."""
    ledger = PerformanceLedger()
    ledger.record(
        simulate(make_route(), 1_000_000, now_ms=NOW, gas_cost_cents=0,
                 risk_verdict=approved_verdict())
    )
    ledger.record(
        simulate(make_route(), 1_000_000, now_ms=NOW, gas_cost_cents=0,
                 risk_verdict=blocked_verdict())
    )
    assert ledger.wins == 1
    assert ledger.rejected == 1
    assert ledger.win_rate_bps == 10_000


def test_empty_ledger_reports_zero_not_error() -> None:
    ledger = PerformanceLedger()
    assert ledger.win_rate_bps == 0
    assert ledger.total_pnl_cents == 0
    assert "0 simulated" in ledger.summary
