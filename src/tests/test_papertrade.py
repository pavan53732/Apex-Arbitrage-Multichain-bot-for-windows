"""End-to-end tests for the full Phase 1 loop.

Covers detect -> route -> risk-check -> paper-trade -> record, and confirms the
execution boundary still holds at the end of the widened path.
"""

from __future__ import annotations

import pytest

from apex.config import load_config
from apex.dex import Pool
from apex.pipeline import ExecutionBlocked, PHASE_1_BLOCK_CODE, SimulationPipeline
from apex.risk import RiskCode, RiskLimits, TradeAssessment
from apex.routing import RouteRejected
from apex.rpc import RpcPool, static_transport
from apex.simulation import FailureCode

NOW = 1_000_000

RAW_CONFIG = {
    "phase": "simulation_only",
    "chain_id": 137,
    "rpc_endpoints": ["https://rpc-a.example", "https://rpc-b.example"],
    "max_slippage_bps": 500,
    "quote_freshness_ms": 5_000,
    "min_edge_bps": 10,
}


def build_pipeline(**overrides: object) -> SimulationPipeline:
    config = load_config({**RAW_CONFIG, **overrides})
    pool = RpcPool(config.rpc, static_transport({"eth_chainId": "0x89"}))
    return SimulationPipeline(config=config, rpc=pool)


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


def spread_pools() -> list[Pool]:
    return [
        make_pool("venue-a", 1_000_000_000, 500_000_000),
        make_pool("venue-b", 1_000_000_000, 550_000_000),
    ]


def assessment(**overrides: object) -> TradeAssessment:
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


def test_full_loop_detect_route_risk_simulate() -> None:
    pipeline = build_pipeline()
    discovery = pipeline.discover(spread_pools(), 1_000_000, now_ms=NOW, gas_cost_units=1_000)

    result = pipeline.paper_trade(
        discovery, 1_000_000, now_ms=NOW, assessment=assessment(), gas_cost_cents=10
    )

    assert result.route_fingerprint == discovery.best_route.fingerprint
    assert result.gross_proceeds_cents > 0
    assert result.snapshot_hash


def test_phase_1_risk_gate_marks_every_trade_rejected() -> None:
    """The pipeline always runs risk in simulation-only mode."""
    pipeline = build_pipeline()
    discovery = pipeline.discover(spread_pools(), 1_000_000, now_ms=NOW, gas_cost_units=1_000)
    result = pipeline.paper_trade(
        discovery, 1_000_000, now_ms=NOW, assessment=assessment(), gas_cost_cents=10
    )

    verdict = pipeline.last_risk_verdict
    assert verdict is not None
    assert verdict.approved is False
    assert verdict.code is RiskCode.PHASE_1_EXECUTION_BLOCK
    assert result.failure_code is FailureCode.RISK_REJECTED


def test_execution_still_blocked_after_paper_trade() -> None:
    """The furthest the pipeline goes is a recorded paper trade."""
    pipeline = build_pipeline()
    discovery = pipeline.discover(spread_pools(), 1_000_000, now_ms=NOW, gas_cost_units=1_000)
    result = pipeline.paper_trade(
        discovery, 1_000_000, now_ms=NOW, assessment=assessment(), gas_cost_cents=10
    )

    assert result.executed is False
    assert result.rejection_code == PHASE_1_BLOCK_CODE
    with pytest.raises(ExecutionBlocked):
        pipeline.execute(result)


def test_trade_is_still_simulated_despite_risk_rejection() -> None:
    """Phase 1 gathers performance data on rejected trades too."""
    pipeline = build_pipeline()
    discovery = pipeline.discover(spread_pools(), 1_000_000, now_ms=NOW, gas_cost_units=1_000)
    result = pipeline.paper_trade(
        discovery, 1_000_000, now_ms=NOW, assessment=assessment(), gas_cost_cents=10
    )
    assert result.gross_proceeds_cents > 0
    assert result.slippage_cost_cents >= 0


def test_ledger_accumulates_across_trades() -> None:
    pipeline = build_pipeline()
    for _ in range(3):
        discovery = pipeline.discover(
            spread_pools(), 1_000_000, now_ms=NOW, gas_cost_units=1_000
        )
        pipeline.paper_trade(
            discovery, 1_000_000, now_ms=NOW, assessment=assessment(), gas_cost_cents=10
        )
    assert len(pipeline.ledger.results) == 3
    assert "3 simulated" in pipeline.ledger.summary


def test_paper_trade_without_route_raises() -> None:
    """A hard reject propagates rather than producing an empty simulation."""
    pipeline = build_pipeline()
    discovery = pipeline.discover([], 1_000_000, now_ms=NOW, gas_cost_units=1_000)
    with pytest.raises(RouteRejected):
        pipeline.paper_trade(
            discovery, 1_000_000, now_ms=NOW, assessment=assessment(), gas_cost_cents=10
        )


def test_full_loop_is_reproducible() -> None:
    """Same inputs must produce the same PNL and snapshot across runs."""
    outcomes = []
    for _ in range(3):
        pipeline = build_pipeline()
        discovery = pipeline.discover(
            spread_pools(), 1_000_000, now_ms=NOW, gas_cost_units=1_000
        )
        result = pipeline.paper_trade(
            discovery, 1_000_000, now_ms=NOW, assessment=assessment(),
            gas_cost_cents=10, seed=99,
        )
        outcomes.append((result.simulated_pnl_cents, result.snapshot_hash, result.confidence_bps))
    assert len(set(outcomes)) == 1


def test_risk_limits_are_honoured() -> None:
    """A custom limit set changes the verdict, proving limits are wired."""
    pipeline = build_pipeline()
    discovery = pipeline.discover(spread_pools(), 1_000_000, now_ms=NOW, gas_cost_units=1_000)
    pipeline.paper_trade(
        discovery, 1_000_000, now_ms=NOW,
        assessment=assessment(open_exposure_cents=999_999),
        gas_cost_cents=10,
        limits=RiskLimits(max_total_exposure_cents=1_000),
    )
    verdict = pipeline.last_risk_verdict
    assert verdict is not None
    exposure = next(o for o in verdict.outcomes if o.name == "exposure")
    assert exposure.passed is False


def test_stale_route_fails_at_simulation() -> None:
    pipeline = build_pipeline()
    discovery = pipeline.discover(spread_pools(), 1_000_000, now_ms=NOW, gas_cost_units=1_000)
    result = pipeline.paper_trade(
        discovery, 1_000_000, now_ms=NOW + 60_000,
        assessment=assessment(), gas_cost_cents=10,
    )
    assert result.failure_code is FailureCode.STALE_MARKET_DATA


def test_no_execution_capability_after_widening() -> None:
    """Structural guard still holds across every new module."""
    import pathlib

    import apex

    forbidden = ("send_raw_transaction", "sign_transaction", "private_key", "eth_sendRaw")
    package_dir = pathlib.Path(apex.__file__).parent
    for source in package_dir.glob("*.py"):
        text = source.read_text(encoding="utf-8").lower()
        for token in forbidden:
            assert token.lower() not in text, f"{source.name} exposes {token!r}"
