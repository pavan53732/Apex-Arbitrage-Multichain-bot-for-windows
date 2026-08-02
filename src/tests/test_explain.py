"""Tests for explanation traces.

The rationale rule is the specification's hardest requirement: an explanation
without a rationale is non-compliant and rejected for storage. It is tested
directly, along with the required-field set and the lifecycle.
"""

from __future__ import annotations

import pytest

from apex.decision import (
    AgentVote,
    DecisionCode,
    DecisionState,
    Recommendation,
    decide,
    evaluate_consensus,
)
from apex.explain import (
    Explanation,
    ExplanationState,
    ExplanationStore,
    InvalidExplanationTransition,
    NonCompliantExplanation,
    explain,
)
from apex.ledger import DecisionOutcome
from apex.risk import TradeAssessment, evaluate
from apex.simulation import FailureCode, SimulationMode, SimulationResult

NOW = 1_000_000


def assessment() -> TradeAssessment:
    return TradeAssessment(
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


def simulation(pnl: int = 500, failure: FailureCode | None = None) -> SimulationResult:
    return SimulationResult(
        route_fingerprint="fp00000000000000",
        mode=SimulationMode.PAPER_TRADING,
        simulated_pnl_cents=pnl,
        gross_proceeds_cents=pnl + 100,
        gas_cost_cents=100,
        slippage_cost_cents=0,
        latency_ms=5,
        confidence_bps=8_000,
        failure_code=failure,
        snapshot_hash="snap000000000000",
        seed=0,
        code_version="0.1.0",
    )


def recommendation() -> Recommendation:
    return Recommendation(
        identity="USDC/WETH@b->a",
        route_fingerprint="fp00000000000000",
        created_at_ms=NOW,
        notional_cents=1_000,
    )


def unanimous():
    return evaluate_consensus(
        [AgentVote("market", True, 9_000), AgentVote("risk", True, 8_500), AgentVote("planner", True, 8_000)]
    )


def approved_decision():
    return decide(
        recommendation(), now_ms=NOW, consensus=unanimous(),
        risk_verdict=evaluate(assessment(), simulation_only=False),
        simulation=simulation(),
    )


def rejected_decision():
    return decide(
        recommendation(), now_ms=NOW, consensus=unanimous(),
        risk_verdict=evaluate(assessment(), simulation_only=True),
        simulation=simulation(),
    )


def deferred_decision():
    return decide(
        recommendation(), now_ms=NOW, consensus=None,
        risk_verdict=evaluate(assessment(), simulation_only=False),
        simulation=simulation(),
    )


def build(decision, **overrides):
    params = dict(
        decision_id="d1",
        timestamp_ms=NOW,
        confidence_bps=8_000,
        inputs_used=("route:fp0", "snapshot:s0"),
    )
    params.update(overrides)
    return explain(decision, **params)  # type: ignore[arg-type]


# --- required fields -------------------------------------------------------


def test_rationale_free_explanation_is_rejected() -> None:
    """The specification's explicit rule."""
    with pytest.raises(NonCompliantExplanation, match="no rationale"):
        Explanation(
            decision_id="d1",
            rationale="   ",
            confidence_bps=5_000,
            alternatives_considered=(),
            inputs_used=("x",),
            gates_passed=(),
            veto_source=None,
            timestamp_ms=NOW,
            outcome=DecisionOutcome.REJECTED,
        )


def test_explanation_without_inputs_is_rejected() -> None:
    with pytest.raises(NonCompliantExplanation, match="records no inputs"):
        Explanation(
            decision_id="d1",
            rationale="because",
            confidence_bps=5_000,
            alternatives_considered=(),
            inputs_used=(),
            gates_passed=(),
            veto_source=None,
            timestamp_ms=NOW,
            outcome=DecisionOutcome.REJECTED,
        )


def test_missing_decision_id_is_rejected() -> None:
    with pytest.raises(NonCompliantExplanation, match="missing a decision ID"):
        build(approved_decision(), decision_id="  ")


@pytest.mark.parametrize("confidence", [-1, 10_001])
def test_out_of_range_confidence_rejected(confidence: int) -> None:
    with pytest.raises(NonCompliantExplanation, match="confidence"):
        build(approved_decision(), confidence_bps=confidence)


def test_all_required_fields_present() -> None:
    e = build(approved_decision())
    assert e.decision_id and e.rationale and e.inputs_used
    assert e.confidence_bps >= 0
    assert e.timestamp_ms == NOW
    assert isinstance(e.alternatives_considered, tuple)
    assert isinstance(e.gates_passed, tuple)


# --- derivation from the decision -----------------------------------------


def test_rejection_explains_why_the_opportunity_was_skipped() -> None:
    """Arbitrage traces must state why an opportunity was skipped."""
    e = build(rejected_decision())
    assert e.outcome is DecisionOutcome.REJECTED
    assert "Rejected at" in e.rationale
    assert e.veto_source == DecisionCode.RISK_VETO.value


def test_deferral_is_explained_as_a_delay() -> None:
    e = build(deferred_decision())
    assert e.outcome is DecisionOutcome.DEFERRED
    assert "Deferred at" in e.rationale


def test_approval_is_explained() -> None:
    e = build(approved_decision())
    assert e.outcome is DecisionOutcome.APPROVED
    assert "All gates passed" in e.rationale
    assert e.veto_source is None


def test_human_override_is_named_in_the_rationale() -> None:
    decision = decide(
        recommendation(), now_ms=NOW, consensus=unanimous(),
        risk_verdict=evaluate(assessment(), simulation_only=True),
        simulation=simulation(), human_override=True,
    )
    e = build(decision)
    assert "Human override" in e.rationale


def test_gates_passed_excludes_terminal_states() -> None:
    e = build(approved_decision())
    assert DecisionState.APPROVED.value not in e.gates_passed
    assert DecisionState.RECOMMEND_RECEIVED.value not in e.gates_passed
    assert "risk_gate" in e.gates_passed


def test_rationale_cannot_drift_from_the_decision() -> None:
    """Rationale is derived, not supplied, so it always matches the outcome."""
    for decision in (approved_decision(), rejected_decision(), deferred_decision()):
        e = build(decision)
        assert e.outcome is decision.outcome


# --- lifecycle -------------------------------------------------------------


def test_explanation_starts_captured() -> None:
    assert build(approved_decision()).state is ExplanationState.CAPTURED


def test_lifecycle_follows_declared_path() -> None:
    e = build(approved_decision())
    for target in (
        ExplanationState.EXPLAINED,
        ExplanationState.STORED,
        ExplanationState.REPLAYABLE,
    ):
        e = e.transition_to(target)
    assert e.is_replayable is True


def test_skipping_a_lifecycle_stage_is_refused() -> None:
    e = build(approved_decision())
    with pytest.raises(InvalidExplanationTransition):
        e.transition_to(ExplanationState.STORED)


def test_replayable_is_terminal() -> None:
    e = build(approved_decision())
    e = (
        e.transition_to(ExplanationState.EXPLAINED)
        .transition_to(ExplanationState.STORED)
        .transition_to(ExplanationState.REPLAYABLE)
    )
    with pytest.raises(InvalidExplanationTransition):
        e.transition_to(ExplanationState.CAPTURED)


# --- store -----------------------------------------------------------------


def test_store_advances_through_the_full_lifecycle() -> None:
    store = ExplanationStore()
    stored = store.store(build(approved_decision()))
    assert stored.is_replayable is True
    assert len(store) == 1


def test_store_retrieves_by_decision_id() -> None:
    store = ExplanationStore()
    store.store(build(approved_decision(), decision_id="dX"))
    assert store.for_decision("dX").decision_id == "dX"
    with pytest.raises(KeyError):
        store.for_decision("missing")


def test_render_is_human_readable() -> None:
    text = build(rejected_decision()).render()
    assert "REJECTED" in text
    assert "Rationale:" in text
    assert "Confidence:" in text
    assert "Inputs:" in text
