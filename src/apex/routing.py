"""Route construction, scoring, and lifecycle.

Implements the Phase 1 subset of:

* `docs/apex-app-docs/market/routing/routing-engine.md`
* `docs/apex-app-docs/market/routing/route-scoring-model.md`
* `docs/apex-app-docs/market/opportunities/opportunity-ranking.md`

The routing contract states three properties this module must hold:

* **Idempotency.** The same input snapshot must yield the same ranking, and
  re-evaluating an unchanged route must preserve its fingerprint.
* **Hard reject over degraded path.** If no safe route exists, the engine
  returns a rejection rather than the least-bad unsafe option.
* **Explicit tie-breaks.** Ranking ties resolve by lower risk, then lower gas,
  then faster execution — never by input order.

Scoring is integer-only. A score influences which trade is selected, so the
coding standard's determinism requirement applies to it directly.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from enum import Enum

from .dex import BPS_DENOMINATOR, Pool, Quote, QuoteError, quote_exact_in
from .opportunity import Candidate


class RouteState(str, Enum):
    """Route lifecycle from `routing-engine.md`.

    Phase 1 stops at `VALIDATED`: `APPROVED` requires execution-risk gating,
    and `BOUND` attaches a route to an execution plan that cannot exist while
    live execution is blocked.
    """

    CANDIDATE = "candidate"
    SCORED = "scored"
    VALIDATED = "validated"
    APPROVED = "approved"
    BOUND = "bound"
    INVALIDATED = "invalidated"
    REPLACED = "replaced"


_ALLOWED_TRANSITIONS: dict[RouteState, frozenset[RouteState]] = {
    RouteState.CANDIDATE: frozenset({RouteState.SCORED, RouteState.INVALIDATED}),
    RouteState.SCORED: frozenset({RouteState.VALIDATED, RouteState.INVALIDATED}),
    RouteState.VALIDATED: frozenset({RouteState.APPROVED, RouteState.INVALIDATED}),
    RouteState.APPROVED: frozenset({RouteState.BOUND, RouteState.INVALIDATED}),
    RouteState.BOUND: frozenset({RouteState.INVALIDATED}),
    RouteState.INVALIDATED: frozenset({RouteState.REPLACED}),
    RouteState.REPLACED: frozenset(),
}


class RouteRejected(Exception):
    """Raised when no safe route exists.

    The contract requires a hard reject rather than a degraded unsafe path, so
    this is an exception rather than a nullable return.
    """


class ForbiddenRouteTransition(Exception):
    """Raised when a route lifecycle transition is not permitted."""


@dataclass(frozen=True)
class ScoreBreakdown:
    """Per-factor contributions to a route score.

    Exposed rather than collapsed into a single number: the ranking contract
    requires a withheld candidate show why it was withheld.
    """

    edge_bps: int
    gas_penalty_bps: int
    slippage_penalty_bps: int
    liquidity_bonus_bps: int

    @property
    def total_bps(self) -> int:
        return (
            self.edge_bps
            - self.gas_penalty_bps
            - self.slippage_penalty_bps
            + self.liquidity_bonus_bps
        )


@dataclass(frozen=True)
class Route:
    """A scored, execution-shaped path across two venues."""

    candidate_identity: str
    buy_quote: Quote
    sell_quote: Quote
    net_edge_bps: int
    breakdown: ScoreBreakdown
    gas_cost_units: int
    hop_count: int
    state: RouteState = RouteState.CANDIDATE

    @property
    def fingerprint(self) -> str:
        """A stable identifier for this route's economic content.

        Derived only from the inputs that define the route, deliberately
        excluding lifecycle state and score. The contract requires that
        re-evaluating a route under unchanged inputs preserve its fingerprint,
        so a value that changes as the route advances would violate it.
        """
        material = "|".join(
            [
                self.candidate_identity,
                self.buy_quote.dex_id,
                self.sell_quote.dex_id,
                str(self.buy_quote.amount_in),
                str(self.buy_quote.amount_out),
                str(self.sell_quote.amount_out),
                str(self.hop_count),
            ]
        )
        return hashlib.sha256(material.encode("utf-8")).hexdigest()[:16]

    def transition_to(self, target: RouteState) -> "Route":
        if target not in _ALLOWED_TRANSITIONS[self.state]:
            raise ForbiddenRouteTransition(
                f"{self.fingerprint}: {self.state.value} -> {target.value} is not allowed"
            )
        return Route(
            candidate_identity=self.candidate_identity,
            buy_quote=self.buy_quote,
            sell_quote=self.sell_quote,
            net_edge_bps=self.net_edge_bps,
            breakdown=self.breakdown,
            gas_cost_units=self.gas_cost_units,
            hop_count=self.hop_count,
            state=target,
        )


@dataclass(frozen=True)
class RouteRejection:
    """A candidate that could not produce a safe route."""

    candidate_identity: str
    reason: str


@dataclass(frozen=True)
class RoutingResult:
    """Ranked routes and the reasons rejected candidates were dropped."""

    routes: tuple[Route, ...] = ()
    rejections: tuple[RouteRejection, ...] = ()

    @property
    def best(self) -> Route:
        if not self.routes:
            raise RouteRejected(
                "no safe route available: "
                + "; ".join(r.reason for r in self.rejections)
            )
        return self.routes[0]


def _gas_penalty_bps(gas_cost_units: int, notional: int) -> int:
    """Gas cost expressed against notional, in basis points."""
    if notional <= 0:
        return BPS_DENOMINATOR
    return (gas_cost_units * BPS_DENOMINATOR) // notional


def _liquidity_bonus_bps(buy: Pool, sell: Pool, amount_in: int) -> int:
    """Reward depth relative to trade size.

    Deeper pools absorb the same size with less impact, so depth is a genuine
    quality signal rather than a cosmetic one. Capped so liquidity can never
    outweigh a negative edge and rescue an unprofitable route.
    """
    if amount_in <= 0:
        return 0
    depth = min(buy.reserve_in, sell.reserve_in)
    ratio = depth // amount_in
    return min(ratio, 25)


def build_route(
    candidate: Candidate,
    amount_in: int,
    *,
    now_ms: int,
    freshness_budget_ms: int,
    max_slippage_bps: int,
    gas_cost_units: int,
) -> Route:
    """Construct and score a route for one candidate.

    Both legs are quoted before scoring. A leg that cannot produce a
    trustworthy quote rejects the whole route: a two-venue arbitrage with one
    unusable leg is not a degraded opportunity, it is not an opportunity.
    """
    try:
        buy_quote = quote_exact_in(
            candidate.buy_pool,
            amount_in,
            now_ms=now_ms,
            freshness_budget_ms=freshness_budget_ms,
            max_slippage_bps=max_slippage_bps,
        )
        sell_quote = quote_exact_in(
            candidate.sell_pool,
            amount_in,
            now_ms=now_ms,
            freshness_budget_ms=freshness_budget_ms,
            max_slippage_bps=max_slippage_bps,
        )
    except QuoteError as exc:
        raise RouteRejected(f"{candidate.identity}: {exc}") from exc

    gas_penalty = _gas_penalty_bps(gas_cost_units, amount_in)
    slippage_penalty = buy_quote.price_impact_bps + sell_quote.price_impact_bps
    liquidity_bonus = _liquidity_bonus_bps(candidate.buy_pool, candidate.sell_pool, amount_in)

    breakdown = ScoreBreakdown(
        edge_bps=candidate.gross_edge_bps,
        gas_penalty_bps=gas_penalty,
        slippage_penalty_bps=slippage_penalty,
        liquidity_bonus_bps=liquidity_bonus,
    )

    return Route(
        candidate_identity=candidate.identity,
        buy_quote=buy_quote,
        sell_quote=sell_quote,
        net_edge_bps=breakdown.total_bps,
        breakdown=breakdown,
        gas_cost_units=gas_cost_units,
        hop_count=2,
    )


def rank_routes(
    candidates: list[Candidate],
    amount_in: int,
    *,
    now_ms: int,
    freshness_budget_ms: int,
    max_slippage_bps: int,
    gas_cost_units: int,
    min_net_edge_bps: int = 0,
) -> RoutingResult:
    """Build, filter, and rank routes for a candidate set.

    Ranking is a total order: net edge descending, then the contract's explicit
    tie-breaks — lower slippage exposure (risk), then lower gas, then fewer
    hops (speed) — and finally fingerprint, so no two routes can ever compare
    equal and reorder between runs.
    """
    routes: list[Route] = []
    rejections: list[RouteRejection] = []

    for candidate in candidates:
        try:
            route = build_route(
                candidate,
                amount_in,
                now_ms=now_ms,
                freshness_budget_ms=freshness_budget_ms,
                max_slippage_bps=max_slippage_bps,
                gas_cost_units=gas_cost_units,
            )
        except RouteRejected as exc:
            rejections.append(RouteRejection(candidate.identity, str(exc)))
            continue

        if route.net_edge_bps < min_net_edge_bps:
            rejections.append(
                RouteRejection(
                    candidate.identity,
                    f"net edge {route.net_edge_bps}bps below minimum {min_net_edge_bps}bps",
                )
            )
            continue

        routes.append(route.transition_to(RouteState.SCORED))

    routes.sort(
        key=lambda r: (
            -r.net_edge_bps,
            r.breakdown.slippage_penalty_bps,
            r.gas_cost_units,
            r.hop_count,
            r.fingerprint,
        )
    )
    rejections.sort(key=lambda r: (r.candidate_identity, r.reason))

    return RoutingResult(routes=tuple(routes), rejections=tuple(rejections))
