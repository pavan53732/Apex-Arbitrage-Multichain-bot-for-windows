"""Paper-trading simulation engine.

Implements the Phase 1 subset of
`docs/apex-app-docs/execution/simulation/simulation-engine.md`.

The specification is unusually direct about this module's role: in Phase 1 the
simulation engine is the *primary* execution mode, and its execution boundaries
are stated explicitly — detect, score, rank, simulate, record PNL are permitted;
sign, broadcast, and move funds are not.

Two contract rules shape the implementation:

* **Reproducibility is mandatory in all phases.** Same inputs and same seed must
  produce the same outcome, and the recorded result must be sufficient to replay
  the trade. Every simulation therefore records the snapshot it ran against, the
  seed, and the code version.
* **Simulated PNL is realistic, not optimistic.** The flow requires slippage and
  gas be applied before net PNL is computed, so a simulation cannot report a
  profit the real trade would not have made.

Arithmetic is integer-only, in cents, per the coding standard.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from enum import Enum

from . import __version__
from .risk import BPS_DENOMINATOR, RiskCode, RiskVerdict
from .routing import Route


class SimulationMode(str, Enum):
    """Modes from the specification's §1.

    Only `PAPER_TRADING` is implemented. The others are named so a caller
    requesting them is refused explicitly rather than silently given paper
    trading.
    """

    PAPER_TRADING = "paper_trading"
    HISTORICAL_REPLAY = "historical_replay"
    STRESS_TEST = "stress_test"


class FailureCode(str, Enum):
    """Simulation failure modes recorded on an unsuccessful run."""

    STALE_MARKET_DATA = "STALE_MARKET_DATA"
    RISK_REJECTED = "RISK_REJECTED"
    NEGATIVE_PNL = "NEGATIVE_PNL"
    MODE_NOT_IMPLEMENTED = "MODE_NOT_IMPLEMENTED"


class SimulationError(Exception):
    """Raised when a simulation cannot be run at all."""


# The specification requires market data be fresher than 5 seconds for paper
# trading. Stated as a constant so the number is traceable to the document.
MARKET_DATA_MAX_AGE_MS = 5_000


@dataclass(frozen=True)
class SimulationResult:
    """The recorded outcome of one paper trade.

    Field names follow the specification's declared outputs: simulated PNL,
    latency, failure code, and a confidence score.
    """

    route_fingerprint: str
    mode: SimulationMode
    simulated_pnl_cents: int
    gross_proceeds_cents: int
    gas_cost_cents: int
    slippage_cost_cents: int
    latency_ms: int
    confidence_bps: int
    failure_code: FailureCode | None
    snapshot_hash: str
    seed: int
    code_version: str
    executed: bool = False
    rejection_code: str = RiskCode.PHASE_1_EXECUTION_BLOCK.value

    @property
    def profitable(self) -> bool:
        return self.failure_code is None and self.simulated_pnl_cents > 0

    @property
    def summary(self) -> str:
        status = "profitable" if self.profitable else (
            self.failure_code.value if self.failure_code else "unprofitable"
        )
        return (
            f"{self.route_fingerprint}: PNL {self.simulated_pnl_cents}c "
            f"({status}, confidence {self.confidence_bps}bps, "
            f"latency {self.latency_ms}ms, execution {self.rejection_code})"
        )


def snapshot_hash(route: Route, amount_in: int, now_ms: int) -> str:
    """Hash the inputs a simulation ran against.

    The reproducibility rule requires recording the market snapshot so any
    simulated trade can be replayed. Hashing the inputs gives a compact,
    comparable record of exactly what was simulated.
    """
    material = "|".join(
        [
            route.fingerprint,
            str(route.buy_quote.amount_in),
            str(route.buy_quote.amount_out),
            str(route.sell_quote.amount_out),
            str(route.buy_quote.observed_at_ms),
            str(route.sell_quote.observed_at_ms),
            str(amount_in),
            str(now_ms),
        ]
    )
    return hashlib.sha256(material.encode("utf-8")).hexdigest()[:16]


def _confidence_bps(route: Route, verdict: RiskVerdict) -> int:
    """Confidence in the simulated outcome, in basis points.

    Derived from evidence rather than asserted: a route with a wide net edge
    and low slippage exposure is more likely to survive contact with the real
    market than a marginal one. A risk rejection caps confidence low, because a
    trade the risk engine refused is not one to be confident about.

    Deterministic by construction — the same route and verdict always produce
    the same score, as the reproducibility rule requires.
    """
    if not verdict.approved:
        base = 2_500
    else:
        base = 7_500

    # Reward edge, penalise slippage exposure. Both are already in bps.
    adjustment = route.net_edge_bps - route.breakdown.slippage_penalty_bps
    score = base + max(-base, min(adjustment, BPS_DENOMINATOR - base))
    return max(0, min(score, BPS_DENOMINATOR))


def simulate(
    route: Route,
    amount_in: int,
    *,
    now_ms: int,
    gas_cost_cents: int,
    risk_verdict: RiskVerdict,
    price_cents_per_unit_bps: int = BPS_DENOMINATOR,
    latency_ms: int = 0,
    seed: int = 0,
    mode: SimulationMode = SimulationMode.PAPER_TRADING,
) -> SimulationResult:
    """Simulate one trade in paper-trading mode.

    Follows the specification's execution flow: validate market-data freshness,
    apply slippage, subtract gas, compute net PNL, record the result.

    A risk rejection does not prevent simulation. Phase 1 exists to gather
    hypothetical performance data, and only simulating trades the risk engine
    would have approved would bias that record toward success. The rejection is
    recorded on the result instead.
    """
    if mode is not SimulationMode.PAPER_TRADING:
        raise SimulationError(
            f"mode {mode.value!r} is not implemented; Phase 1 supports paper trading only"
        )
    if amount_in <= 0:
        raise SimulationError(f"amount_in must be positive, got {amount_in}")

    # Step 2 — market data freshness. Applied to the older of the two legs,
    # because a route is only as fresh as its stalest input.
    oldest_observation = min(
        route.buy_quote.observed_at_ms, route.sell_quote.observed_at_ms
    )
    age_ms = now_ms - oldest_observation
    fingerprint = route.fingerprint
    digest = snapshot_hash(route, amount_in, now_ms)

    if age_ms < 0 or age_ms > MARKET_DATA_MAX_AGE_MS:
        return SimulationResult(
            route_fingerprint=fingerprint,
            mode=mode,
            simulated_pnl_cents=0,
            gross_proceeds_cents=0,
            gas_cost_cents=gas_cost_cents,
            slippage_cost_cents=0,
            latency_ms=latency_ms,
            confidence_bps=0,
            failure_code=FailureCode.STALE_MARKET_DATA,
            snapshot_hash=digest,
            seed=seed,
            code_version=__version__,
        )

    # Step 3 — simulate the route. Gross proceeds are the edge captured on the
    # notional; slippage is already measured by the quotes, and is charged
    # explicitly so the cost is visible in the record rather than absorbed.
    gross_proceeds_cents = (
        amount_in * route.breakdown.edge_bps * price_cents_per_unit_bps
    ) // (BPS_DENOMINATOR * BPS_DENOMINATOR)

    slippage_cost_cents = (
        amount_in * route.breakdown.slippage_penalty_bps * price_cents_per_unit_bps
    ) // (BPS_DENOMINATOR * BPS_DENOMINATOR)

    simulated_pnl_cents = gross_proceeds_cents - slippage_cost_cents - gas_cost_cents

    failure_code: FailureCode | None = None
    if not risk_verdict.approved:
        failure_code = FailureCode.RISK_REJECTED
    elif simulated_pnl_cents <= 0:
        failure_code = FailureCode.NEGATIVE_PNL

    return SimulationResult(
        route_fingerprint=fingerprint,
        mode=mode,
        simulated_pnl_cents=simulated_pnl_cents,
        gross_proceeds_cents=gross_proceeds_cents,
        gas_cost_cents=gas_cost_cents,
        slippage_cost_cents=slippage_cost_cents,
        latency_ms=latency_ms,
        confidence_bps=_confidence_bps(route, risk_verdict),
        failure_code=failure_code,
        snapshot_hash=digest,
        seed=seed,
        code_version=__version__,
    )


@dataclass
class PerformanceLedger:
    """Cumulative record of simulated outcomes.

    The specification requires Phase 1 generate performance reports for Phase 2
    eligibility, which requires the outcomes be accumulated rather than
    discarded after each run.
    """

    results: list[SimulationResult]

    def __init__(self) -> None:
        self.results = []

    def record(self, result: SimulationResult) -> None:
        self.results.append(result)

    @staticmethod
    def _is_traded(result: SimulationResult) -> bool:
        """Whether a result represents a trading decision that was evaluated.

        `NEGATIVE_PNL` marks a simulated trade that lost money — a real
        outcome that belongs in the performance record. `RISK_REJECTED` and
        `STALE_MARKET_DATA` mark trades that were never taken, and counting
        those as losses would misreport the strategy's accuracy.
        """
        return result.failure_code in (None, FailureCode.NEGATIVE_PNL)

    @property
    def total_pnl_cents(self) -> int:
        return sum(r.simulated_pnl_cents for r in self.results if self._is_traded(r))

    @property
    def wins(self) -> int:
        return sum(1 for r in self.results if r.profitable)

    @property
    def losses(self) -> int:
        return sum(
            1 for r in self.results
            if self._is_traded(r) and r.simulated_pnl_cents <= 0
        )

    @property
    def rejected(self) -> int:
        return sum(1 for r in self.results if not self._is_traded(r))

    @property
    def win_rate_bps(self) -> int:
        """Win rate over evaluated trades, in basis points.

        Rejected simulations are excluded from the denominator: a trade the risk
        engine refused was never a trading decision, and counting it as a loss
        would understate the strategy's actual accuracy.
        """
        evaluated = self.wins + self.losses
        if evaluated == 0:
            return 0
        return (self.wins * BPS_DENOMINATOR) // evaluated

    @property
    def summary(self) -> str:
        return (
            f"{len(self.results)} simulated, {self.wins} win / {self.losses} loss / "
            f"{self.rejected} rejected, net {self.total_pnl_cents}c, "
            f"win rate {self.win_rate_bps}bps"
        )
