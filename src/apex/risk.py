"""Risk check pipeline.

Implements the Phase 1 subset of
`docs/apex-app-docs/execution/risk-policy/risk-engine.md`.

The specification defines seven checks that run sequentially, and states that
all must pass for a trade to proceed. Three properties follow from that and are
enforced here:

* **Fixed order.** The pipeline runs Phase Gate, Max Loss, Liquidity, Slippage,
  Spread Integrity, Timing Budget, Exposure — in that order. The first failure
  produces the rejection code, so the reason a trade was stopped is stable
  rather than dependent on evaluation accident.
* **Phase Gate is first and unconditional.** In Phase 1 the gate rejects with
  `PHASE_1_EXECUTION_BLOCK` before any other check runs. A trade cannot be
  approved by passing the remaining six.
* **Fail closed.** A check that cannot be evaluated rejects rather than passes.
  An unavailable input is not an absent objection.

Arithmetic is integer-only. Monetary values are carried in cents and
percentages in basis points, because the coding standard forbids floating point
where a value influences a financial decision.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

BPS_DENOMINATOR = 10_000


class RiskCode(str, Enum):
    """Rejection codes, transcribed from the specification's check definitions."""

    PHASE_1_EXECUTION_BLOCK = "PHASE_1_EXECUTION_BLOCK"
    LOSS_LIMIT_EXCEEDED = "LOSS_LIMIT_EXCEEDED"
    LIQUIDITY_INSUFFICIENT = "LIQUIDITY_INSUFFICIENT"
    SLIPPAGE_EXCEEDED = "SLIPPAGE_EXCEEDED"
    PRICE_INTEGRITY_FAIL = "PRICE_INTEGRITY_FAIL"
    TIMING_BUDGET_EXCEEDED = "TIMING_BUDGET_EXCEEDED"
    EXPOSURE_LIMIT_EXCEEDED = "EXPOSURE_LIMIT_EXCEEDED"
    INPUT_UNAVAILABLE = "INPUT_UNAVAILABLE"


@dataclass(frozen=True)
class RiskLimits:
    """Configured risk thresholds.

    Defaults are the specification's stated defaults where it gives one. Limits
    the specification marks "N/A (execution blocked)" for Phase 1 still carry a
    value, because the checks run in Phase 1 for observability even though no
    trade can be approved.
    """

    max_loss_per_trade_cents: int = 2_500
    max_liquidity_usage_bps: int = 500          # 5%
    max_slippage_bps: int = 100                 # 1%
    max_price_deviation_bps: int = 200          # 2%
    timing_buffer_bps: int = 8_000              # 80% of window
    max_total_exposure_cents: int = 50_000

    def __post_init__(self) -> None:
        for name in (
            "max_loss_per_trade_cents",
            "max_liquidity_usage_bps",
            "max_slippage_bps",
            "max_price_deviation_bps",
            "timing_buffer_bps",
            "max_total_exposure_cents",
        ):
            if getattr(self, name) < 0:
                raise ValueError(f"{name} must not be negative")


@dataclass(frozen=True)
class TradeAssessment:
    """The inputs one risk evaluation needs.

    Every field is required. The specification's fail-closed rule means a
    missing input must reject rather than be defaulted, so optionality is
    represented explicitly by `None` and handled as `INPUT_UNAVAILABLE`.
    """

    position_size_cents: int
    max_adverse_movement_bps: int
    pool_liquidity_cents: int
    expected_output: int
    minimum_output: int
    dex_price_bps: int
    oracle_price_bps: int | None
    estimated_execution_ms: int
    window_remaining_ms: int
    open_exposure_cents: int


@dataclass(frozen=True)
class CheckOutcome:
    """The result of a single named check."""

    name: str
    passed: bool
    code: RiskCode | None = None
    detail: str = ""


@dataclass(frozen=True)
class RiskVerdict:
    """The outcome of a full pipeline run.

    Carries every check that ran, not only the failing one. The specification
    requires risk decisions be auditable, which means the passing checks are
    part of the record.
    """

    approved: bool
    code: RiskCode | None
    outcomes: tuple[CheckOutcome, ...]

    @property
    def failed_check(self) -> CheckOutcome | None:
        for outcome in self.outcomes:
            if not outcome.passed:
                return outcome
        return None

    @property
    def summary(self) -> str:
        if self.approved:
            return f"APPROVED ({len(self.outcomes)} checks passed)"
        failed = self.failed_check
        return f"REJECTED: {self.code.value if self.code else 'UNKNOWN'} — {failed.detail if failed else ''}"


def _phase_gate(simulation_only: bool) -> CheckOutcome:
    """Phase Gate — Phase 1 rejects unconditionally.

    Runs first so that no combination of passing checks can produce an approved
    trade while the product is simulation-only.
    """
    if simulation_only:
        return CheckOutcome(
            "phase_gate",
            False,
            RiskCode.PHASE_1_EXECUTION_BLOCK,
            "execution_mode is SIMULATION_ONLY; live execution is always rejected",
        )
    return CheckOutcome("phase_gate", True)


def _max_loss(a: TradeAssessment, limits: RiskLimits) -> CheckOutcome:
    """estimated_loss = position_size × max_adverse_movement."""
    estimated_loss_cents = (a.position_size_cents * a.max_adverse_movement_bps) // BPS_DENOMINATOR
    if estimated_loss_cents > limits.max_loss_per_trade_cents:
        return CheckOutcome(
            "max_loss",
            False,
            RiskCode.LOSS_LIMIT_EXCEEDED,
            f"estimated loss {estimated_loss_cents}c exceeds limit "
            f"{limits.max_loss_per_trade_cents}c",
        )
    return CheckOutcome("max_loss", True)


def _liquidity(a: TradeAssessment, limits: RiskLimits) -> CheckOutcome:
    """trade_size <= pool_liquidity × max_liquidity_usage."""
    if a.pool_liquidity_cents <= 0:
        return CheckOutcome(
            "liquidity",
            False,
            RiskCode.LIQUIDITY_INSUFFICIENT,
            "pool liquidity is zero or unknown",
        )
    permitted = (a.pool_liquidity_cents * limits.max_liquidity_usage_bps) // BPS_DENOMINATOR
    if a.position_size_cents > permitted:
        return CheckOutcome(
            "liquidity",
            False,
            RiskCode.LIQUIDITY_INSUFFICIENT,
            f"trade {a.position_size_cents}c exceeds permitted {permitted}c "
            f"({limits.max_liquidity_usage_bps}bps of pool)",
        )
    return CheckOutcome("liquidity", True)


def _slippage(a: TradeAssessment, limits: RiskLimits) -> CheckOutcome:
    """slippage = (expected_output - minimum_output) / expected_output."""
    if a.expected_output <= 0:
        return CheckOutcome(
            "slippage", False, RiskCode.INPUT_UNAVAILABLE, "expected output is non-positive"
        )
    slippage_bps = ((a.expected_output - a.minimum_output) * BPS_DENOMINATOR) // a.expected_output
    if slippage_bps > limits.max_slippage_bps:
        return CheckOutcome(
            "slippage",
            False,
            RiskCode.SLIPPAGE_EXCEEDED,
            f"slippage {slippage_bps}bps exceeds limit {limits.max_slippage_bps}bps",
        )
    return CheckOutcome("slippage", True)


def _spread_integrity(a: TradeAssessment, limits: RiskLimits) -> CheckOutcome:
    """deviation = |dex_price - oracle_price| / oracle_price.

    An absent oracle reading fails the check. The specification classifies
    oracles as the price-reference authority that validates DEX quotes, so
    proceeding without one would remove the validation this check exists for.
    """
    if a.oracle_price_bps is None or a.oracle_price_bps <= 0:
        return CheckOutcome(
            "spread_integrity",
            False,
            RiskCode.INPUT_UNAVAILABLE,
            "oracle price unavailable; DEX quote cannot be validated",
        )
    deviation_bps = (
        abs(a.dex_price_bps - a.oracle_price_bps) * BPS_DENOMINATOR
    ) // a.oracle_price_bps
    if deviation_bps > limits.max_price_deviation_bps:
        return CheckOutcome(
            "spread_integrity",
            False,
            RiskCode.PRICE_INTEGRITY_FAIL,
            f"price deviation {deviation_bps}bps exceeds limit {limits.max_price_deviation_bps}bps",
        )
    return CheckOutcome("spread_integrity", True)


def _timing_budget(a: TradeAssessment, limits: RiskLimits) -> CheckOutcome:
    """estimated_execution_time < window_remaining × timing_buffer."""
    if a.window_remaining_ms <= 0:
        return CheckOutcome(
            "timing_budget",
            False,
            RiskCode.TIMING_BUDGET_EXCEEDED,
            "arbitrage window has already closed",
        )
    budget_ms = (a.window_remaining_ms * limits.timing_buffer_bps) // BPS_DENOMINATOR
    if a.estimated_execution_ms >= budget_ms:
        return CheckOutcome(
            "timing_budget",
            False,
            RiskCode.TIMING_BUDGET_EXCEEDED,
            f"execution {a.estimated_execution_ms}ms does not fit budget {budget_ms}ms",
        )
    return CheckOutcome("timing_budget", True)


def _exposure(a: TradeAssessment, limits: RiskLimits) -> CheckOutcome:
    """total_exposure + new_position <= max_total_exposure."""
    projected = a.open_exposure_cents + a.position_size_cents
    if projected > limits.max_total_exposure_cents:
        return CheckOutcome(
            "exposure",
            False,
            RiskCode.EXPOSURE_LIMIT_EXCEEDED,
            f"projected exposure {projected}c exceeds limit {limits.max_total_exposure_cents}c",
        )
    return CheckOutcome("exposure", True)


# Pipeline order is part of the contract, not an implementation detail.
_PIPELINE = (
    ("max_loss", _max_loss),
    ("liquidity", _liquidity),
    ("slippage", _slippage),
    ("spread_integrity", _spread_integrity),
    ("timing_budget", _timing_budget),
    ("exposure", _exposure),
)


def evaluate(
    assessment: TradeAssessment,
    limits: RiskLimits | None = None,
    *,
    simulation_only: bool = True,
) -> RiskVerdict:
    """Run the risk pipeline in the specified order.

    Every check runs and its outcome is recorded, so the verdict carries a
    complete audit trail rather than only the first failure. Approval still
    requires that all checks pass: recording a failure does not soften it.

    `simulation_only` defaults to True because Phase 1 is the current phase and
    a caller that forgets to state the phase must not thereby escape the gate.
    """
    limits = limits or RiskLimits()
    outcomes: list[CheckOutcome] = [_phase_gate(simulation_only)]

    for _, check in _PIPELINE:
        outcomes.append(check(assessment, limits))

    first_failure = next((o for o in outcomes if not o.passed), None)
    return RiskVerdict(
        approved=first_failure is None,
        code=first_failure.code if first_failure else None,
        outcomes=tuple(outcomes),
    )
