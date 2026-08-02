"""Opportunity detection, lifecycle, and ranking.

Implements the Phase 1 subset of:

* `docs/apex-app-docs/market/opportunities/opportunity-detection.md`
* `docs/apex-app-docs/market/opportunities/opportunity-lifecycle.md`
* `docs/apex-app-docs/market/opportunities/opportunity-ranking.md`

Three rules from those documents shape this module:

* Detection is deterministic for the same input snapshot. The same snapshot must
  always produce the same candidates in the same order.
* A rejected candidate carries a reason code. The detection contract requires
  rejections be queryable by gate for tuning, so a rejection is a recorded
  outcome rather than a silent omission.
* Policy gates are evaluated in a fixed order and the first failing gate
  produces the reason. This makes the rejection explanation stable rather than
  dependent on evaluation accident.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from .dex import BPS_DENOMINATOR, Pool


class OpportunityState(str, Enum):
    """Lifecycle states from `opportunity-lifecycle.md`.

    Phase 1 reaches `SIMULATED` and stops: `APPROVED` requires risk and
    operator policy gating, and `EXECUTED` is unreachable while live execution
    is blocked.
    """

    DETECTED = "detected"
    VALIDATED = "validated"
    SCORED = "scored"
    SIMULATED = "simulated"
    APPROVED = "approved"
    EXECUTED = "executed"
    CLOSED = "closed"
    ARCHIVED = "archived"


# Allowed forward transitions, transcribed from the lifecycle state machine.
# Encoded as data so a forbidden transition is rejected by the same rule the
# document states, rather than by scattered conditionals.
_ALLOWED_TRANSITIONS: dict[OpportunityState, frozenset[OpportunityState]] = {
    OpportunityState.DETECTED: frozenset({OpportunityState.VALIDATED, OpportunityState.ARCHIVED}),
    OpportunityState.VALIDATED: frozenset({OpportunityState.SCORED, OpportunityState.DETECTED, OpportunityState.ARCHIVED}),
    OpportunityState.SCORED: frozenset({OpportunityState.SIMULATED, OpportunityState.ARCHIVED}),
    OpportunityState.SIMULATED: frozenset({OpportunityState.APPROVED, OpportunityState.ARCHIVED}),
    OpportunityState.APPROVED: frozenset({OpportunityState.EXECUTED, OpportunityState.ARCHIVED}),
    OpportunityState.EXECUTED: frozenset({OpportunityState.CLOSED, OpportunityState.SIMULATED}),
    OpportunityState.CLOSED: frozenset({OpportunityState.ARCHIVED}),
    OpportunityState.ARCHIVED: frozenset(),
}


class RejectionCode(str, Enum):
    """Reason codes for rejected candidates.

    The detection contract requires that rejection reasons be queryable by
    strategy and gate, which requires a closed vocabulary rather than free text.
    """

    STALE_SNAPSHOT = "STALE_SNAPSHOT"
    INSUFFICIENT_LIQUIDITY = "INSUFFICIENT_LIQUIDITY"
    BELOW_MIN_EDGE = "BELOW_MIN_EDGE"
    NO_TRADABLE_PAIR = "NO_TRADABLE_PAIR"
    QUOTE_UNAVAILABLE = "QUOTE_UNAVAILABLE"


class ForbiddenTransition(Exception):
    """Raised when a lifecycle transition is not permitted."""


@dataclass(frozen=True)
class Candidate:
    """A detected arbitrage candidate.

    Carries the inputs and timestamp it was detected from, because the
    detection contract requires every candidate be traceable to the snapshot
    that produced it.
    """

    pair: tuple[str, str]
    buy_pool: Pool
    sell_pool: Pool
    gross_edge_bps: int
    detected_at_ms: int
    state: OpportunityState = OpportunityState.DETECTED

    @property
    def identity(self) -> str:
        """A stable identifier for this candidate.

        Derived from the pair and the venues involved, so the same opportunity
        detected from an equivalent snapshot carries the same identity. The
        detection contract requires a candidate reused across strategies be
        detected once and shared by reference.
        """
        return f"{self.pair[0]}/{self.pair[1]}@{self.buy_pool.dex_id}->{self.sell_pool.dex_id}"

    def transition_to(self, target: OpportunityState) -> "Candidate":
        """Return a copy in `target` state, or raise if the move is forbidden.

        Transitions return a new value rather than mutating, so a candidate's
        recorded history cannot be rewritten in place.
        """
        if target not in _ALLOWED_TRANSITIONS[self.state]:
            raise ForbiddenTransition(
                f"{self.identity}: {self.state.value} -> {target.value} is not an allowed transition"
            )
        return Candidate(
            pair=self.pair,
            buy_pool=self.buy_pool,
            sell_pool=self.sell_pool,
            gross_edge_bps=self.gross_edge_bps,
            detected_at_ms=self.detected_at_ms,
            state=target,
        )


@dataclass(frozen=True)
class Rejection:
    """A candidate that failed a detection gate."""

    pair: tuple[str, str]
    code: RejectionCode
    detail: str


@dataclass(frozen=True)
class DetectionResult:
    """The full outcome of one detection pass.

    Rejections are returned alongside candidates rather than discarded, so the
    rejection rate is observable and tunable as the contract requires.
    """

    candidates: tuple[Candidate, ...] = ()
    rejections: tuple[Rejection, ...] = ()

    @property
    def rejection_codes(self) -> tuple[RejectionCode, ...]:
        return tuple(r.code for r in self.rejections)


def spot_price_bps(pool: Pool) -> int:
    """Marginal price of `token_out` per `token_in`, in basis points.

    Integer arithmetic only: this value feeds edge calculation, and the coding
    standard forbids floating point on a path that influences a financial
    decision.
    """
    return (pool.reserve_out * BPS_DENOMINATOR) // pool.reserve_in


def detect(
    pools: list[Pool],
    *,
    now_ms: int,
    freshness_budget_ms: int,
    min_edge_bps: int,
    min_reserve_in: int = 0,
) -> DetectionResult:
    """Detect two-venue arbitrage candidates from a pool snapshot.

    Gates are applied in a fixed order — freshness, then liquidity, then
    tradability, then edge — and the first failing gate produces the reason.
    Ordering is part of the contract, not an implementation detail: it makes
    the explanation for a rejection stable.

    Determinism is guaranteed by sorting the output on a total key, so the same
    snapshot always yields the same candidates in the same order regardless of
    input ordering or dictionary iteration.
    """
    fresh: list[Pool] = []
    rejections: list[Rejection] = []

    # Gate 1 — freshness. A stale snapshot cannot produce a candidate at all.
    for pool in pools:
        age = now_ms - pool.observed_at_ms
        if age < 0 or age > freshness_budget_ms:
            rejections.append(
                Rejection(
                    pair=(pool.token_in, pool.token_out),
                    code=RejectionCode.STALE_SNAPSHOT,
                    detail=f"{pool.dex_id}: observation age {age}ms exceeds {freshness_budget_ms}ms",
                )
            )
            continue
        # Gate 2 — liquidity floor.
        if pool.reserve_in < min_reserve_in:
            rejections.append(
                Rejection(
                    pair=(pool.token_in, pool.token_out),
                    code=RejectionCode.INSUFFICIENT_LIQUIDITY,
                    detail=f"{pool.dex_id}: reserve_in {pool.reserve_in} below floor {min_reserve_in}",
                )
            )
            continue
        fresh.append(pool)

    # Group by directed pair so only comparable venues are paired.
    by_pair: dict[tuple[str, str], list[Pool]] = {}
    for pool in fresh:
        by_pair.setdefault((pool.token_in, pool.token_out), []).append(pool)

    candidates: list[Candidate] = []
    for pair, venues in by_pair.items():
        # Gate 3 — tradability. Arbitrage needs at least two venues.
        if len(venues) < 2:
            rejections.append(
                Rejection(
                    pair=pair,
                    code=RejectionCode.NO_TRADABLE_PAIR,
                    detail=f"only {len(venues)} venue(s) quote {pair[0]}/{pair[1]}",
                )
            )
            continue

        # Buy where the output token is cheapest, sell where it is dearest.
        ordered = sorted(venues, key=lambda p: (spot_price_bps(p), p.dex_id))
        buy, sell = ordered[-1], ordered[0]
        buy_price, sell_price = spot_price_bps(buy), spot_price_bps(sell)

        if sell_price <= 0:
            rejections.append(
                Rejection(pair=pair, code=RejectionCode.QUOTE_UNAVAILABLE,
                          detail=f"{sell.dex_id}: non-positive spot price"),
            )
            continue

        edge_bps = ((buy_price - sell_price) * BPS_DENOMINATOR) // sell_price

        # Gate 4 — minimum edge. Withheld with a reason, not dropped silently.
        if edge_bps < min_edge_bps:
            rejections.append(
                Rejection(
                    pair=pair,
                    code=RejectionCode.BELOW_MIN_EDGE,
                    detail=f"edge {edge_bps}bps below minimum {min_edge_bps}bps",
                )
            )
            continue

        candidates.append(
            Candidate(
                pair=pair,
                buy_pool=buy,
                sell_pool=sell,
                gross_edge_bps=edge_bps,
                detected_at_ms=now_ms,
            )
        )

    # Deterministic order: strongest edge first, identity as an explicit
    # tie-break so equal-edge candidates never reorder between runs.
    candidates.sort(key=lambda c: (-c.gross_edge_bps, c.identity))
    rejections.sort(key=lambda r: (r.pair, r.code.value, r.detail))

    return DetectionResult(candidates=tuple(candidates), rejections=tuple(rejections))
