"""End-to-end tests for the detect -> route -> simulate path.

These exercise the widened Phase 1 pipeline as a whole, including that the
execution block still holds once the path produces a real, ranked route.
"""

from __future__ import annotations

import pytest

from apex.config import load_config
from apex.dex import Pool
from apex.opportunity import OpportunityState, RejectionCode
from apex.pipeline import (
    PHASE_1_BLOCK_CODE,
    ExecutionBlocked,
    SimulationPipeline,
)
from apex.routing import RouteRejected
from apex.rpc import ChainMismatchError, RpcError, RpcPool, static_transport

NOW = 1_000_000

RAW_CONFIG = {
    "phase": "simulation_only",
    "chain_id": 137,
    "rpc_endpoints": ["https://rpc-a.example", "https://rpc-b.example"],
    "max_slippage_bps": 500,
    "quote_freshness_ms": 5_000,
    "min_edge_bps": 10,
}


def build_pipeline(transport=None, **config_overrides: object) -> SimulationPipeline:
    config = load_config({**RAW_CONFIG, **config_overrides})
    pool = RpcPool(config.rpc, transport or static_transport({"eth_chainId": "0x89"}))
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


def test_discovers_ranked_route_end_to_end() -> None:
    pipeline = build_pipeline()
    result = pipeline.discover(spread_pools(), 1_000_000, now_ms=NOW, gas_cost_units=1_000)

    assert result.chain_id == 137
    assert result.has_route
    assert result.best_route.net_edge_bps > 0
    assert len(result.best_route.fingerprint) == 16


def test_winning_candidate_advances_to_simulated() -> None:
    """SIMULATED is the furthest state reachable while execution is blocked."""
    pipeline = build_pipeline()
    result = pipeline.discover(spread_pools(), 1_000_000, now_ms=NOW, gas_cost_units=1_000)

    assert result.best_candidate is not None
    assert result.best_candidate.state is OpportunityState.SIMULATED


def test_execution_still_blocked_after_discovery() -> None:
    """The Phase 1 invariant survives the wider pipeline."""
    pipeline = build_pipeline()
    result = pipeline.discover(spread_pools(), 1_000_000, now_ms=NOW, gas_cost_units=1_000)

    assert result.executed is False
    assert result.rejection_code == PHASE_1_BLOCK_CODE
    with pytest.raises(ExecutionBlocked) as excinfo:
        pipeline.execute(result)
    assert excinfo.value.code == PHASE_1_BLOCK_CODE


def test_discovery_is_reproducible() -> None:
    """Simulation paths must produce reproducible results."""
    fingerprints = []
    for _ in range(3):
        pipeline = build_pipeline()
        result = pipeline.discover(spread_pools(), 1_000_000, now_ms=NOW, gas_cost_units=1_000)
        fingerprints.append(result.best_route.fingerprint)
    assert len(set(fingerprints)) == 1


def test_no_spread_yields_no_route_but_reports_reasons() -> None:
    flat = [
        make_pool("venue-a", 1_000_000_000, 500_000_000),
        make_pool("venue-b", 2_000_000_000, 1_000_000_000),
    ]
    pipeline = build_pipeline()
    result = pipeline.discover(flat, 1_000_000, now_ms=NOW, gas_cost_units=1_000)

    assert result.has_route is False
    assert RejectionCode.BELOW_MIN_EDGE in result.detection.rejection_codes
    with pytest.raises(RouteRejected):
        _ = result.best_route


def test_detection_and_routing_rejections_stay_distinct() -> None:
    """Collapsing them would hide which gate stopped the trade."""
    pipeline = build_pipeline()
    pools = spread_pools() + [make_pool("stale", 1_000_000, 900_000, observed_at_ms=NOW - 60_000)]
    result = pipeline.discover(pools, 1_000_000, now_ms=NOW, gas_cost_units=1_000)

    assert RejectionCode.STALE_SNAPSHOT in result.detection.rejection_codes
    assert isinstance(result.routing.rejections, tuple)


def test_gas_cost_reduces_net_edge() -> None:
    """Gas is charged against the trade, not ignored."""
    pipeline = build_pipeline()
    cheap_gas = pipeline.discover(spread_pools(), 1_000_000, now_ms=NOW, gas_cost_units=1_000)
    dear_gas = pipeline.discover(spread_pools(), 1_000_000, now_ms=NOW, gas_cost_units=50_000)

    assert cheap_gas.has_route
    assert dear_gas.has_route
    assert cheap_gas.best_route.net_edge_bps > dear_gas.best_route.net_edge_bps


def test_prohibitive_gas_eliminates_the_route() -> None:
    """A trade that cannot cover its own gas is not offered."""
    pipeline = build_pipeline()
    result = pipeline.discover(
        spread_pools(), 1_000_000, now_ms=NOW, gas_cost_units=10_000_000
    )
    assert result.has_route is False
    assert any("below minimum" in r.reason for r in result.routing.rejections)


def test_chain_mismatch_prevents_discovery() -> None:
    pipeline = build_pipeline(static_transport({"eth_chainId": "0x1"}))
    with pytest.raises(ChainMismatchError):
        pipeline.discover(spread_pools(), 1_000_000, now_ms=NOW, gas_cost_units=1_000)


def test_dead_rpc_prevents_discovery() -> None:
    """An absent input is never treated as an unchanged one."""

    def dead(endpoint: str, method: str) -> object:
        raise RpcError("unreachable")

    pipeline = build_pipeline(dead)
    with pytest.raises(RpcError):
        pipeline.discover(spread_pools(), 1_000_000, now_ms=NOW, gas_cost_units=1_000)


def test_redundancy_warning_surfaced_during_discovery() -> None:
    pipeline = build_pipeline(rpc_endpoints=["https://only.example"])
    result = pipeline.discover(spread_pools(), 1_000_000, now_ms=NOW, gas_cost_units=1_000)

    assert result.has_route
    assert any("autonomous execution requires at least 2" in w for w in pipeline.warnings)


def test_all_stale_pools_yield_no_candidates() -> None:
    stale = [
        make_pool("venue-a", 1_000_000_000, 500_000_000, observed_at_ms=NOW - 60_000),
        make_pool("venue-b", 1_000_000_000, 550_000_000, observed_at_ms=NOW - 60_000),
    ]
    pipeline = build_pipeline()
    result = pipeline.discover(stale, 1_000_000, now_ms=NOW, gas_cost_units=1_000)

    assert result.detection.candidates == ()
    assert result.has_route is False


def test_summary_reports_execution_block() -> None:
    pipeline = build_pipeline()
    result = pipeline.discover(spread_pools(), 1_000_000, now_ms=NOW, gas_cost_units=1_000)
    assert PHASE_1_BLOCK_CODE in result.summary


def test_summary_reports_absence_of_route() -> None:
    pipeline = build_pipeline()
    result = pipeline.discover([], 1_000_000, now_ms=NOW, gas_cost_units=1_000)
    assert "no safe route" in result.summary
