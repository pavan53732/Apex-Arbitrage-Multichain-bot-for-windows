"""Tests for route construction, scoring, ranking, and lifecycle.

The idempotency and hard-reject tests are the important ones: both are
explicit guarantees in `routing-engine.md`.
"""

from __future__ import annotations

import pytest

from apex.dex import Pool
from apex.opportunity import Candidate, detect
from apex.routing import (
    ForbiddenRouteTransition,
    Route,
    RouteRejected,
    RouteState,
    build_route,
    rank_routes,
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


def make_candidate(edge_bps: int = 1_000, **pool_overrides: object) -> Candidate:
    return Candidate(
        pair=("USDC", "WETH"),
        buy_pool=make_pool("venue-b", 1_000_000_000, 550_000_000, **pool_overrides),
        sell_pool=make_pool("venue-a", 1_000_000_000, 500_000_000, **pool_overrides),
        gross_edge_bps=edge_bps,
        detected_at_ms=NOW,
    )


ROUTE_ARGS = dict(
    now_ms=NOW,
    freshness_budget_ms=5_000,
    max_slippage_bps=500,
    gas_cost_units=1_000,
)


def test_builds_route_with_score_breakdown() -> None:
    route = build_route(make_candidate(), 1_000_000, **ROUTE_ARGS)  # type: ignore[arg-type]

    assert route.hop_count == 2
    assert route.breakdown.edge_bps == 1_000
    assert route.breakdown.gas_penalty_bps > 0
    assert route.net_edge_bps == route.breakdown.total_bps


def test_score_breakdown_is_exposed_not_collapsed() -> None:
    """A withheld candidate must be able to show why."""
    route = build_route(make_candidate(), 1_000_000, **ROUTE_ARGS)  # type: ignore[arg-type]
    b = route.breakdown
    assert b.total_bps == (
        b.edge_bps - b.gas_penalty_bps - b.slippage_penalty_bps + b.liquidity_bonus_bps
    )


def test_fingerprint_is_stable_across_recomputation() -> None:
    """Re-evaluating under unchanged inputs must preserve the fingerprint."""
    first = build_route(make_candidate(), 1_000_000, **ROUTE_ARGS)  # type: ignore[arg-type]
    second = build_route(make_candidate(), 1_000_000, **ROUTE_ARGS)  # type: ignore[arg-type]
    assert first.fingerprint == second.fingerprint


def test_fingerprint_survives_lifecycle_advance() -> None:
    """Fingerprint identifies economic content, not lifecycle position."""
    route = build_route(make_candidate(), 1_000_000, **ROUTE_ARGS)  # type: ignore[arg-type]
    advanced = route.transition_to(RouteState.SCORED).transition_to(RouteState.VALIDATED)
    assert advanced.fingerprint == route.fingerprint


def test_fingerprint_changes_when_economics_change() -> None:
    small = build_route(make_candidate(), 1_000_000, **ROUTE_ARGS)  # type: ignore[arg-type]
    large = build_route(make_candidate(), 2_000_000, **ROUTE_ARGS)  # type: ignore[arg-type]
    assert small.fingerprint != large.fingerprint


def test_stale_leg_rejects_whole_route() -> None:
    """A two-venue arbitrage with one unusable leg is not an opportunity."""
    candidate = Candidate(
        pair=("USDC", "WETH"),
        buy_pool=make_pool("venue-b", 1_000_000_000, 550_000_000, observed_at_ms=NOW - 60_000),
        sell_pool=make_pool("venue-a", 1_000_000_000, 500_000_000),
        gross_edge_bps=1_000,
        detected_at_ms=NOW,
    )
    with pytest.raises(RouteRejected):
        build_route(candidate, 1_000_000, **ROUTE_ARGS)  # type: ignore[arg-type]


def test_ranking_is_idempotent() -> None:
    """The same input snapshot must yield the same ranking."""
    pools = [
        make_pool("venue-a", 1_000_000_000, 500_000_000),
        make_pool("venue-b", 1_000_000_000, 550_000_000),
    ]
    detection = detect(pools, now_ms=NOW, freshness_budget_ms=5_000, min_edge_bps=0)

    runs = [
        rank_routes(list(detection.candidates), 1_000_000, **ROUTE_ARGS)  # type: ignore[arg-type]
        for _ in range(3)
    ]
    fingerprints = [tuple(r.fingerprint for r in run.routes) for run in runs]
    assert len(set(fingerprints)) == 1


def test_ranking_orders_by_net_edge_descending() -> None:
    weak = make_candidate(edge_bps=100)
    strong = make_candidate(edge_bps=900)
    # Give them distinct identities so both survive ranking.
    strong = Candidate(
        pair=("DAI", "WETH"),
        buy_pool=make_pool("venue-d", 1_000_000_000, 550_000_000),
        sell_pool=make_pool("venue-c", 1_000_000_000, 500_000_000),
        gross_edge_bps=900,
        detected_at_ms=NOW,
    )

    result = rank_routes([weak, strong], 1_000_000, **ROUTE_ARGS)  # type: ignore[arg-type]

    assert len(result.routes) == 2
    assert result.routes[0].net_edge_bps >= result.routes[1].net_edge_bps


def test_ranking_is_order_independent() -> None:
    a = make_candidate(edge_bps=100)
    b = Candidate(
        pair=("DAI", "WETH"),
        buy_pool=make_pool("venue-d", 1_000_000_000, 550_000_000),
        sell_pool=make_pool("venue-c", 1_000_000_000, 500_000_000),
        gross_edge_bps=900,
        detected_at_ms=NOW,
    )
    forward = rank_routes([a, b], 1_000_000, **ROUTE_ARGS)  # type: ignore[arg-type]
    reverse = rank_routes([b, a], 1_000_000, **ROUTE_ARGS)  # type: ignore[arg-type]

    assert [r.fingerprint for r in forward.routes] == [r.fingerprint for r in reverse.routes]


def test_below_minimum_net_edge_is_rejected_with_reason() -> None:
    result = rank_routes(
        [make_candidate(edge_bps=10)],
        1_000_000,
        now_ms=NOW,
        freshness_budget_ms=5_000,
        max_slippage_bps=500,
        gas_cost_units=1_000,
        min_net_edge_bps=5_000,
    )
    assert result.routes == ()
    assert any("below minimum" in r.reason for r in result.rejections)


def test_hard_reject_when_no_safe_route_exists() -> None:
    """No degraded unsafe path is returned; the caller gets a hard reject."""
    result = rank_routes([], 1_000_000, **ROUTE_ARGS)  # type: ignore[arg-type]
    with pytest.raises(RouteRejected, match="no safe route"):
        _ = result.best


def test_gas_penalty_scales_against_notional() -> None:
    """Gas hurts a small trade more than a large one."""
    small = build_route(
        make_candidate(), 100_000,
        now_ms=NOW, freshness_budget_ms=5_000, max_slippage_bps=5_000, gas_cost_units=1_000,
    )
    large = build_route(
        make_candidate(), 10_000_000,
        now_ms=NOW, freshness_budget_ms=5_000, max_slippage_bps=5_000, gas_cost_units=1_000,
    )
    assert small.breakdown.gas_penalty_bps > large.breakdown.gas_penalty_bps


def test_liquidity_bonus_is_capped() -> None:
    """Depth must not rescue an unprofitable route."""
    route = build_route(
        Candidate(
            pair=("USDC", "WETH"),
            buy_pool=make_pool("b", 10**15, 10**15),
            sell_pool=make_pool("a", 10**15, 10**15),
            gross_edge_bps=0,
            detected_at_ms=NOW,
        ),
        1_000,
        **ROUTE_ARGS,  # type: ignore[arg-type]
    )
    assert route.breakdown.liquidity_bonus_bps <= 25


def test_scores_are_integers() -> None:
    route = build_route(make_candidate(), 1_000_000, **ROUTE_ARGS)  # type: ignore[arg-type]
    for value in (
        route.net_edge_bps,
        route.breakdown.edge_bps,
        route.breakdown.gas_penalty_bps,
        route.breakdown.slippage_penalty_bps,
        route.breakdown.liquidity_bonus_bps,
    ):
        assert isinstance(value, int)


# --- lifecycle -------------------------------------------------------------


def test_route_lifecycle_follows_declared_path() -> None:
    route = build_route(make_candidate(), 1_000_000, **ROUTE_ARGS)  # type: ignore[arg-type]
    advanced = route.transition_to(RouteState.SCORED).transition_to(RouteState.VALIDATED)
    assert advanced.state is RouteState.VALIDATED


def test_route_cannot_skip_validation_to_approved() -> None:
    route = build_route(make_candidate(), 1_000_000, **ROUTE_ARGS)  # type: ignore[arg-type]
    with pytest.raises(ForbiddenRouteTransition):
        route.transition_to(RouteState.SCORED).transition_to(RouteState.APPROVED)


def test_replaced_only_reachable_via_invalidated() -> None:
    route = build_route(make_candidate(), 1_000_000, **ROUTE_ARGS)  # type: ignore[arg-type]
    with pytest.raises(ForbiddenRouteTransition):
        route.transition_to(RouteState.REPLACED)

    invalidated = route.transition_to(RouteState.INVALIDATED)
    assert invalidated.transition_to(RouteState.REPLACED).state is RouteState.REPLACED


def test_ranked_routes_are_in_scored_state() -> None:
    result = rank_routes([make_candidate()], 1_000_000, **ROUTE_ARGS)  # type: ignore[arg-type]
    assert result.routes[0].state is RouteState.SCORED
