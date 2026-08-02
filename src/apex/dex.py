"""Constant-product DEX adapter and quote simulation.

Implements the Phase 1 subset of `docs/apex-app-docs/market/dex/dex-integration.md`.

The specification's governing rule is that a venue which cannot produce a
trustworthy quote is excluded from routing, because a stale or unverifiable
quote is more dangerous than a missing one: routing would treat it as a real
opportunity. Every failure path here therefore excludes rather than degrades.

Arithmetic is integer-only. The coding standard requires deterministic,
auditable financial calculations with fixed-point expectations, so no floating
point is used anywhere a value influences a quote.
"""

from __future__ import annotations

from dataclasses import dataclass

BPS_DENOMINATOR = 10_000


class QuoteError(Exception):
    """Raised when a venue cannot produce a trustworthy quote."""


class StaleQuoteError(QuoteError):
    """Raised when reserves are older than the configured freshness budget."""


class InsufficientLiquidityError(QuoteError):
    """Raised when a pool cannot support the requested size."""


@dataclass(frozen=True)
class Pool:
    """A constant-product pool snapshot.

    `observed_at_ms` is carried with the reserves rather than alongside them so
    that a quote can never be computed from reserves whose age is unknown.
    """

    dex_id: str
    token_in: str
    token_out: str
    reserve_in: int
    reserve_out: int
    fee_bps: int
    observed_at_ms: int

    def __post_init__(self) -> None:
        if self.reserve_in <= 0 or self.reserve_out <= 0:
            raise InsufficientLiquidityError(
                f"{self.dex_id}: pool {self.token_in}/{self.token_out} has non-positive reserves"
            )
        if not 0 <= self.fee_bps < BPS_DENOMINATOR:
            raise QuoteError(f"{self.dex_id}: fee_bps {self.fee_bps} outside 0..9999")


@dataclass(frozen=True)
class Quote:
    """A simulated swap result.

    A quote is a statement about a specific pool observation, so it carries the
    identifiers needed to audit it later: the venue, the pool age, and the
    price impact the sizing implied.
    """

    dex_id: str
    token_in: str
    token_out: str
    amount_in: int
    amount_out: int
    fee_bps: int
    price_impact_bps: int
    observed_at_ms: int


def quote_exact_in(
    pool: Pool,
    amount_in: int,
    *,
    now_ms: int,
    freshness_budget_ms: int,
    max_slippage_bps: int,
) -> Quote:
    """Simulate an exact-input swap against a constant-product pool.

    Applies the venue fee, then the constant-product invariant
    `x * y = k`, using integer arithmetic throughout.

    The quote is rejected rather than returned when the reserves are stale or
    the price impact exceeds tolerance. Both are exclusion conditions in the
    specification: a quote computed from an observation the caller cannot trust
    is worse than no quote at all.
    """
    if amount_in <= 0:
        raise QuoteError(f"{pool.dex_id}: amount_in must be positive, got {amount_in}")

    age_ms = now_ms - pool.observed_at_ms
    if age_ms < 0:
        raise StaleQuoteError(
            f"{pool.dex_id}: pool observation is {-age_ms}ms in the future; clock is unusable"
        )
    if age_ms > freshness_budget_ms:
        raise StaleQuoteError(
            f"{pool.dex_id}: reserves are {age_ms}ms old, exceeding the "
            f"{freshness_budget_ms}ms freshness budget"
        )

    amount_in_after_fee = (amount_in * (BPS_DENOMINATOR - pool.fee_bps)) // BPS_DENOMINATOR
    if amount_in_after_fee <= 0:
        raise QuoteError(f"{pool.dex_id}: amount_in {amount_in} rounds to zero after fee")

    # Constant product: out = (y * dx) / (x + dx), floor-divided so the quote
    # never overstates the amount received.
    numerator = pool.reserve_out * amount_in_after_fee
    denominator = pool.reserve_in + amount_in_after_fee
    amount_out = numerator // denominator

    if amount_out <= 0:
        raise InsufficientLiquidityError(
            f"{pool.dex_id}: pool too shallow to return any output for {amount_in}"
        )
    if amount_out >= pool.reserve_out:
        raise InsufficientLiquidityError(
            f"{pool.dex_id}: swap would drain the pool ({amount_out} of {pool.reserve_out})"
        )

    price_impact_bps = _price_impact_bps(pool, amount_in_after_fee, amount_out)
    if price_impact_bps > max_slippage_bps:
        raise QuoteError(
            f"{pool.dex_id}: price impact {price_impact_bps}bps exceeds "
            f"tolerance {max_slippage_bps}bps"
        )

    return Quote(
        dex_id=pool.dex_id,
        token_in=pool.token_in,
        token_out=pool.token_out,
        amount_in=amount_in,
        amount_out=amount_out,
        fee_bps=pool.fee_bps,
        price_impact_bps=price_impact_bps,
        observed_at_ms=pool.observed_at_ms,
    )


def _price_impact_bps(pool: Pool, amount_in_after_fee: int, amount_out: int) -> int:
    """Price impact in basis points, as integer arithmetic.

    Compares the marginal (spot) rate against the realised rate. Both are
    expressed as scaled integers so no floating point enters a financial path.
    """
    spot_out = (pool.reserve_out * amount_in_after_fee) // pool.reserve_in
    if spot_out <= 0:
        return 0
    shortfall = spot_out - amount_out
    if shortfall <= 0:
        return 0
    return (shortfall * BPS_DENOMINATOR) // spot_out


def best_quote(
    pools: list[Pool],
    amount_in: int,
    *,
    now_ms: int,
    freshness_budget_ms: int,
    max_slippage_bps: int,
) -> tuple[Quote, list[str]]:
    """Select the best quote across venues, excluding those that cannot answer.

    Returns the winning quote and the reasons each excluded venue was dropped.
    Exclusions are returned rather than discarded so a persistently broken
    adapter is distinguishable from a temporarily illiquid market, which the
    specification requires be observable.

    Raises `QuoteError` when every venue is excluded.
    """
    best: Quote | None = None
    exclusions: list[str] = []

    for pool in pools:
        try:
            quote = quote_exact_in(
                pool,
                amount_in,
                now_ms=now_ms,
                freshness_budget_ms=freshness_budget_ms,
                max_slippage_bps=max_slippage_bps,
            )
        except QuoteError as exc:
            exclusions.append(str(exc))
            continue

        # Ties resolve to the venue seen first, keeping selection deterministic.
        if best is None or quote.amount_out > best.amount_out:
            best = quote

    if best is None:
        raise QuoteError(
            "every venue was excluded; no trustworthy quote available: " + "; ".join(exclusions)
        )
    return best, exclusions
