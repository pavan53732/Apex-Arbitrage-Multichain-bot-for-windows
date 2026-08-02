"""Tests for the constant-product DEX adapter.

Financial calculations are covered with fixed inputs and fixed expected
outputs, per the deterministic-testing requirement in
`docs/apex-repository-docs/standards/coding-standards.md`.
"""

from __future__ import annotations

import pytest

from apex.dex import (
    InsufficientLiquidityError,
    Pool,
    QuoteError,
    StaleQuoteError,
    best_quote,
    quote_exact_in,
)

NOW = 1_000_000


def make_pool(**overrides: object) -> Pool:
    params = dict(
        dex_id="uniswap-v2",
        token_in="USDC",
        token_out="WETH",
        reserve_in=1_000_000_000,
        reserve_out=500_000_000,
        fee_bps=30,
        observed_at_ms=NOW,
    )
    params.update(overrides)
    return Pool(**params)  # type: ignore[arg-type]


def test_quote_matches_fixed_expected_value() -> None:
    """Exact expected output, derived from the constant-product invariant.

    amount_in       = 1_000_000
    after 30bps fee = 1_000_000 * 9970 // 10_000 = 997_000
    numerator       = 500_000_000 * 997_000     = 498_500_000_000_000
    denominator     = 1_000_000_000 + 997_000   = 1_000_997_000
    amount_out      = 498_500_000_000_000 // 1_000_997_000 = 498_003
    """
    quote = quote_exact_in(
        make_pool(),
        1_000_000,
        now_ms=NOW,
        freshness_budget_ms=5_000,
        max_slippage_bps=100,
    )
    assert quote.amount_out == 498_003
    assert quote.fee_bps == 30
    assert quote.dex_id == "uniswap-v2"


def test_quote_is_deterministic() -> None:
    args = dict(now_ms=NOW, freshness_budget_ms=5_000, max_slippage_bps=100)
    first = quote_exact_in(make_pool(), 1_000_000, **args)  # type: ignore[arg-type]
    second = quote_exact_in(make_pool(), 1_000_000, **args)  # type: ignore[arg-type]
    assert first == second


def test_larger_size_has_greater_price_impact() -> None:
    args = dict(now_ms=NOW, freshness_budget_ms=5_000, max_slippage_bps=10_000)
    small = quote_exact_in(make_pool(), 1_000_000, **args)  # type: ignore[arg-type]
    large = quote_exact_in(make_pool(), 100_000_000, **args)  # type: ignore[arg-type]
    assert large.price_impact_bps > small.price_impact_bps


def test_stale_reserves_rejected() -> None:
    """A stale quote is more dangerous than a missing one."""
    pool = make_pool(observed_at_ms=NOW - 6_000)
    with pytest.raises(StaleQuoteError, match="freshness budget"):
        quote_exact_in(pool, 1_000, now_ms=NOW, freshness_budget_ms=5_000, max_slippage_bps=100)


def test_future_dated_observation_rejected() -> None:
    """An unusable clock must not silently pass as fresh."""
    pool = make_pool(observed_at_ms=NOW + 1_000)
    with pytest.raises(StaleQuoteError, match="in the future"):
        quote_exact_in(pool, 1_000, now_ms=NOW, freshness_budget_ms=5_000, max_slippage_bps=100)


def test_excessive_price_impact_rejected() -> None:
    with pytest.raises(QuoteError, match="exceeds tolerance"):
        quote_exact_in(
            make_pool(),
            500_000_000,
            now_ms=NOW,
            freshness_budget_ms=5_000,
            max_slippage_bps=50,
        )


def test_empty_pool_rejected_at_construction() -> None:
    with pytest.raises(InsufficientLiquidityError):
        make_pool(reserve_in=0)


def test_non_positive_amount_rejected() -> None:
    with pytest.raises(QuoteError, match="amount_in must be positive"):
        quote_exact_in(make_pool(), 0, now_ms=NOW, freshness_budget_ms=5_000, max_slippage_bps=100)


def test_invalid_fee_rejected() -> None:
    with pytest.raises(QuoteError, match="fee_bps"):
        make_pool(fee_bps=10_000)


def test_best_quote_selects_highest_output() -> None:
    shallow = make_pool(dex_id="shallow", reserve_in=1_000_000, reserve_out=500_000)
    deep = make_pool(dex_id="deep")
    best, exclusions = best_quote(
        [shallow, deep], 1_000_000, now_ms=NOW, freshness_budget_ms=5_000, max_slippage_bps=10_000
    )
    assert best.dex_id == "deep"
    assert exclusions == []


def test_best_quote_excludes_untrustworthy_venues_and_reports_why() -> None:
    """Exclusions are surfaced so a broken adapter is distinguishable."""
    stale = make_pool(dex_id="stale-venue", observed_at_ms=NOW - 60_000)
    healthy = make_pool(dex_id="healthy-venue")
    best, exclusions = best_quote(
        [stale, healthy], 1_000_000, now_ms=NOW, freshness_budget_ms=5_000, max_slippage_bps=100
    )
    assert best.dex_id == "healthy-venue"
    assert len(exclusions) == 1
    assert "stale-venue" in exclusions[0]


def test_best_quote_raises_when_every_venue_excluded() -> None:
    stale = make_pool(dex_id="a", observed_at_ms=NOW - 60_000)
    also_stale = make_pool(dex_id="b", observed_at_ms=NOW - 60_000)
    with pytest.raises(QuoteError, match="every venue was excluded"):
        best_quote(
            [stale, also_stale],
            1_000,
            now_ms=NOW,
            freshness_budget_ms=5_000,
            max_slippage_bps=100,
        )


def test_output_never_overstated_by_rounding() -> None:
    """Floor division must not round in the trader's favour."""
    pool = make_pool(reserve_in=3, reserve_out=7, fee_bps=0)
    quote = quote_exact_in(pool, 1, now_ms=NOW, freshness_budget_ms=5_000, max_slippage_bps=10_000)
    assert quote.amount_out == (7 * 1) // (3 + 1)
    assert quote.amount_out < pool.reserve_out
