"""Tests for opportunity detection, lifecycle, and rejection reporting."""

from __future__ import annotations

import pytest

from apex.dex import Pool
from apex.opportunity import (
    Candidate,
    ForbiddenTransition,
    OpportunityState,
    RejectionCode,
    detect,
    spot_price_bps,
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


def test_detects_spread_between_two_venues() -> None:
    cheap = make_pool("venue-a", 1_000_000, 500_000)
    dear = make_pool("venue-b", 1_000_000, 550_000)

    result = detect([cheap, dear], now_ms=NOW, freshness_budget_ms=5_000, min_edge_bps=0)

    assert len(result.candidates) == 1
    candidate = result.candidates[0]
    assert candidate.state is OpportunityState.DETECTED
    # 550_000 vs 500_000 => 1000 bps spread
    assert candidate.gross_edge_bps == 1_000


def test_no_candidate_when_prices_match() -> None:
    a = make_pool("venue-a", 1_000_000, 500_000)
    b = make_pool("venue-b", 2_000_000, 1_000_000)

    result = detect([a, b], now_ms=NOW, freshness_budget_ms=5_000, min_edge_bps=1)

    assert result.candidates == ()
    assert RejectionCode.BELOW_MIN_EDGE in result.rejection_codes


def multi_pair_pools() -> list[Pool]:
    """Three distinct pairs, so detection yields three candidates.

    Ordering can only be tested when more than one candidate exists; a
    single-candidate snapshot would pass regardless of sort behaviour.
    """
    return [
        make_pool("a1", 1_000_000, 500_000, token_in="USDC", token_out="WETH"),
        make_pool("a2", 1_000_000, 550_000, token_in="USDC", token_out="WETH"),
        make_pool("b1", 1_000_000, 500_000, token_in="DAI", token_out="WETH"),
        make_pool("b2", 1_000_000, 600_000, token_in="DAI", token_out="WETH"),
        make_pool("c1", 1_000_000, 500_000, token_in="USDT", token_out="WBTC"),
        make_pool("c2", 1_000_000, 520_000, token_in="USDT", token_out="WBTC"),
    ]


def test_detection_yields_one_candidate_per_tradable_pair() -> None:
    result = detect(multi_pair_pools(), now_ms=NOW, freshness_budget_ms=5_000, min_edge_bps=0)
    assert len(result.candidates) == 3


def test_detection_is_deterministic_regardless_of_input_order() -> None:
    """Same snapshot must yield the same candidates in the same order."""
    pools = multi_pair_pools()
    forward = detect(pools, now_ms=NOW, freshness_budget_ms=5_000, min_edge_bps=0)
    reverse = detect(list(reversed(pools)), now_ms=NOW, freshness_budget_ms=5_000, min_edge_bps=0)
    shuffled = detect(
        [pools[3], pools[0], pools[5], pools[2], pools[4], pools[1]],
        now_ms=NOW,
        freshness_budget_ms=5_000,
        min_edge_bps=0,
    )

    expected = [c.identity for c in forward.candidates]
    assert len(expected) == 3
    assert [c.identity for c in reverse.candidates] == expected
    assert [c.identity for c in shuffled.candidates] == expected


def test_candidates_are_ordered_by_edge_descending() -> None:
    """Ranking order is part of the contract, not incidental."""
    result = detect(multi_pair_pools(), now_ms=NOW, freshness_budget_ms=5_000, min_edge_bps=0)
    edges = [c.gross_edge_bps for c in result.candidates]
    assert edges == sorted(edges, reverse=True)
    # DAI pair has the widest spread (500_000 -> 600_000 = 2000bps).
    assert result.candidates[0].pair == ("DAI", "WETH")


def test_stale_pool_rejected_with_reason_code() -> None:
    fresh = make_pool("fresh", 1_000_000, 550_000)
    stale = make_pool("stale", 1_000_000, 500_000, observed_at_ms=NOW - 60_000)

    result = detect([fresh, stale], now_ms=NOW, freshness_budget_ms=5_000, min_edge_bps=0)

    assert RejectionCode.STALE_SNAPSHOT in result.rejection_codes
    assert any("stale" in r.detail for r in result.rejections)


def test_freshness_gate_precedes_liquidity_gate() -> None:
    """Gates run in fixed order; the first failure produces the reason."""
    both_bad = make_pool("bad", 10, 5, observed_at_ms=NOW - 60_000)

    result = detect(
        [both_bad], now_ms=NOW, freshness_budget_ms=5_000, min_edge_bps=0, min_reserve_in=1_000
    )

    codes = result.rejection_codes
    assert RejectionCode.STALE_SNAPSHOT in codes
    assert RejectionCode.INSUFFICIENT_LIQUIDITY not in codes


def test_thin_pool_rejected_on_liquidity_floor() -> None:
    thin = make_pool("thin", 100, 50)
    deep = make_pool("deep", 1_000_000, 550_000)

    result = detect(
        [thin, deep], now_ms=NOW, freshness_budget_ms=5_000, min_edge_bps=0, min_reserve_in=1_000
    )

    assert RejectionCode.INSUFFICIENT_LIQUIDITY in result.rejection_codes


def test_single_venue_pair_is_not_tradable() -> None:
    lonely = make_pool("only", 1_000_000, 500_000)

    result = detect([lonely], now_ms=NOW, freshness_budget_ms=5_000, min_edge_bps=0)

    assert result.candidates == ()
    assert RejectionCode.NO_TRADABLE_PAIR in result.rejection_codes


def test_below_min_edge_is_withheld_not_discarded() -> None:
    """A withheld candidate must show why it was withheld."""
    a = make_pool("venue-a", 1_000_000, 500_000)
    b = make_pool("venue-b", 1_000_000, 505_000)

    result = detect([a, b], now_ms=NOW, freshness_budget_ms=5_000, min_edge_bps=500)

    assert result.candidates == ()
    rejection = next(r for r in result.rejections if r.code is RejectionCode.BELOW_MIN_EDGE)
    assert "below minimum 500bps" in rejection.detail


def test_candidate_identity_is_stable() -> None:
    cheap = make_pool("venue-a", 1_000_000, 500_000)
    dear = make_pool("venue-b", 1_000_000, 550_000)

    first = detect([cheap, dear], now_ms=NOW, freshness_budget_ms=5_000, min_edge_bps=0)
    second = detect([cheap, dear], now_ms=NOW, freshness_budget_ms=5_000, min_edge_bps=0)

    assert first.candidates[0].identity == second.candidates[0].identity


def test_spot_price_is_integer_arithmetic() -> None:
    pool = make_pool("v", 1_000_000, 500_000)
    price = spot_price_bps(pool)
    assert isinstance(price, int)
    assert price == 5_000


# --- lifecycle -------------------------------------------------------------


def base_candidate() -> Candidate:
    return Candidate(
        pair=("USDC", "WETH"),
        buy_pool=make_pool("venue-b", 1_000_000, 550_000),
        sell_pool=make_pool("venue-a", 1_000_000, 500_000),
        gross_edge_bps=1_000,
        detected_at_ms=NOW,
    )


def test_lifecycle_follows_declared_path() -> None:
    candidate = base_candidate()
    for target in (
        OpportunityState.VALIDATED,
        OpportunityState.SCORED,
        OpportunityState.SIMULATED,
    ):
        candidate = candidate.transition_to(target)
    assert candidate.state is OpportunityState.SIMULATED


def test_skipping_validation_is_forbidden() -> None:
    """The lifecycle forbids skipping validation."""
    with pytest.raises(ForbiddenTransition, match="not an allowed transition"):
        base_candidate().transition_to(OpportunityState.SCORED)


def test_execution_without_approval_is_forbidden() -> None:
    candidate = (
        base_candidate()
        .transition_to(OpportunityState.VALIDATED)
        .transition_to(OpportunityState.SCORED)
        .transition_to(OpportunityState.SIMULATED)
    )
    with pytest.raises(ForbiddenTransition):
        candidate.transition_to(OpportunityState.EXECUTED)


def test_archived_opportunity_cannot_be_resurrected() -> None:
    archived = base_candidate().transition_to(OpportunityState.ARCHIVED)
    for target in OpportunityState:
        with pytest.raises(ForbiddenTransition):
            archived.transition_to(target)


def test_transition_does_not_mutate_original() -> None:
    original = base_candidate()
    original.transition_to(OpportunityState.VALIDATED)
    assert original.state is OpportunityState.DETECTED
