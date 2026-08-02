"""Tests for the decision engine state machine, consensus, and veto hierarchy.

The fail-closed guarantee is the important one: the specification states that
no failure path may produce an APPROVED outcome.
"""

from __future__ import annotations

import pytest

from apex.decision import (
    DEFAULT_DECISION_TTL_MS,
    AgentVote,
    ConsensusResult,
    DecisionCode,
    DecisionState,
    Recommendation,
    decide,
    evaluate_consensus,
)
from apex.ledger import DecisionOutcome
from apex.risk import TradeAssessment, evaluate
from apex.simulation import FailureCode, SimulationMode, SimulationResult

NOW = 1_000_000


def healthy_assessment(**overrides: object) -> TradeAssessment:
    params = dict(
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
    params.update(overrides)
    return TradeAssessment(**params)  # type: ignore[arg-type]


def approving_risk():
    return evaluate(healthy_assessment(), simulation_only=False)


def blocking_risk():
    return evaluate(healthy_assessment(), simulation_only=True)


def good_simulation(pnl: int = 500, failure: FailureCode | None = None) -> SimulationResult:
    return SimulationResult(
        route_fingerprint="fp0000000000000",
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


def good_recommendation(**overrides: object) -> Recommendation:
    params = dict(
        identity="USDC/WETH@b->a",
        route_fingerprint="fp0000000000000",
        created_at_ms=NOW,
        notional_cents=1_000,
    )
    params.update(overrides)
    return Recommendation(**params)  # type: ignore[arg-type]


def unanimous() -> ConsensusResult:
    return evaluate_consensus(
        [
            AgentVote("market", True, 9_000),
            AgentVote("risk", True, 8_500),
            AgentVote("planner", True, 8_000),
        ]
    )


# --- consensus -------------------------------------------------------------


def test_unanimous_consensus_approves() -> None:
    result = unanimous()
    assert result.reached is True
    assert result.approved is True
    assert result.approvals == 3


def test_two_thirds_majority_reaches_quorum() -> None:
    result = evaluate_consensus(
        [
            AgentVote("market", True, 9_000),
            AgentVote("risk", True, 8_000),
            AgentVote("planner", False, 4_000),
        ]
    )
    assert result.approved is True


def test_one_third_majority_fails_quorum() -> None:
    result = evaluate_consensus(
        [
            AgentVote("market", True, 9_000),
            AgentVote("risk", False, 3_000),
            AgentVote("planner", False, 4_000),
        ]
    )
    assert result.reached is True
    assert result.approved is False


def test_veto_overrides_unanimous_approval() -> None:
    """The hierarchy places a veto above the planner's majority."""
    result = evaluate_consensus(
        [
            AgentVote("market", True, 9_000),
            AgentVote("planner", True, 9_000),
            AgentVote("risk", True, 9_000, is_veto=True),
        ]
    )
    assert result.approved is False
    assert result.vetoed_by == "risk"
    assert "vetoed by risk" in result.detail


def test_empty_vote_set_has_not_reached_quorum() -> None:
    """Not having spoken differs from having spoken against."""
    result = evaluate_consensus([])
    assert result.reached is False
    assert result.approved is False


def test_votes_remain_traceable_to_agents() -> None:
    result = unanimous()
    assert [v.agent for v in result.votes] == ["market", "risk", "planner"]
    assert all(v.confidence_bps > 0 for v in result.votes)


# --- decision state machine ------------------------------------------------


def test_all_gates_passing_approves() -> None:
    decision = decide(
        good_recommendation(),
        now_ms=NOW,
        consensus=unanimous(),
        risk_verdict=approving_risk(),
        simulation=good_simulation(),
    )
    assert decision.approved is True
    assert decision.state is DecisionState.APPROVED
    assert decision.code is None


def test_path_records_every_state_visited() -> None:
    decision = decide(
        good_recommendation(),
        now_ms=NOW,
        consensus=unanimous(),
        risk_verdict=approving_risk(),
        simulation=good_simulation(),
    )
    assert decision.path == (
        DecisionState.RECOMMEND_RECEIVED,
        DecisionState.VALIDATE_INPUTS,
        DecisionState.CHECK_CONSENSUS,
        DecisionState.RISK_GATE,
        DecisionState.SIMULATION_GATE,
        DecisionState.APPROVED,
    )


def test_phase_1_risk_verdict_rejects() -> None:
    """In Phase 1 the risk gate carries the phase block, so nothing approves."""
    decision = decide(
        good_recommendation(),
        now_ms=NOW,
        consensus=unanimous(),
        risk_verdict=blocking_risk(),
        simulation=good_simulation(),
    )
    assert decision.outcome is DecisionOutcome.REJECTED
    assert decision.code is DecisionCode.RISK_VETO
    assert "PHASE_1_EXECUTION_BLOCK" in decision.detail


def test_missing_risk_verdict_is_a_veto_not_an_absent_objection() -> None:
    decision = decide(
        good_recommendation(),
        now_ms=NOW,
        consensus=unanimous(),
        risk_verdict=None,
        simulation=good_simulation(),
    )
    assert decision.outcome is DecisionOutcome.REJECTED
    assert decision.code is DecisionCode.RISK_UNAVAILABLE


def test_missing_simulation_defers_rather_than_rejects() -> None:
    """Absence of evidence here is not evidence of danger."""
    decision = decide(
        good_recommendation(),
        now_ms=NOW,
        consensus=unanimous(),
        risk_verdict=approving_risk(),
        simulation=None,
    )
    assert decision.outcome is DecisionOutcome.DEFERRED
    assert decision.state is DecisionState.DEFER
    assert decision.code is DecisionCode.SIMULATION_UNAVAILABLE


def test_missing_consensus_defers() -> None:
    decision = decide(
        good_recommendation(),
        now_ms=NOW,
        consensus=None,
        risk_verdict=approving_risk(),
        simulation=good_simulation(),
    )
    assert decision.outcome is DecisionOutcome.DEFERRED
    assert decision.code is DecisionCode.CONSENSUS_UNAVAILABLE


def test_failed_consensus_rejects() -> None:
    failed = evaluate_consensus(
        [AgentVote("a", False, 1_000), AgentVote("b", False, 1_000), AgentVote("c", True, 9_000)]
    )
    decision = decide(
        good_recommendation(),
        now_ms=NOW,
        consensus=failed,
        risk_verdict=approving_risk(),
        simulation=good_simulation(),
    )
    assert decision.outcome is DecisionOutcome.REJECTED
    assert decision.code is DecisionCode.CONSENSUS_FAILED


def test_expired_recommendation_is_void() -> None:
    """A stale decision is never executed against current market state."""
    decision = decide(
        good_recommendation(created_at_ms=NOW - DEFAULT_DECISION_TTL_MS - 1),
        now_ms=NOW,
        consensus=unanimous(),
        risk_verdict=approving_risk(),
        simulation=good_simulation(),
    )
    assert decision.code is DecisionCode.DECISION_EXPIRED


def test_ttl_checked_before_any_gate() -> None:
    decision = decide(
        good_recommendation(created_at_ms=NOW - 999_999),
        now_ms=NOW,
        consensus=None,
        risk_verdict=None,
        simulation=None,
    )
    assert decision.code is DecisionCode.DECISION_EXPIRED


def test_policy_unavailable_rejects_without_defaulting() -> None:
    decision = decide(
        good_recommendation(),
        now_ms=NOW,
        consensus=unanimous(),
        risk_verdict=approving_risk(),
        simulation=good_simulation(),
        policy_available=False,
    )
    assert decision.code is DecisionCode.POLICY_READ_FAILED


@pytest.mark.parametrize(
    "override",
    [{"identity": "  "}, {"route_fingerprint": ""}, {"notional_cents": 0}],
)
def test_malformed_recommendation_rejected(override: dict) -> None:
    decision = decide(
        good_recommendation(**override),
        now_ms=NOW,
        consensus=unanimous(),
        risk_verdict=approving_risk(),
        simulation=good_simulation(),
    )
    assert decision.code is DecisionCode.INPUTS_INVALID


def test_failed_simulation_rejects() -> None:
    decision = decide(
        good_recommendation(),
        now_ms=NOW,
        consensus=unanimous(),
        risk_verdict=approving_risk(),
        simulation=good_simulation(failure=FailureCode.STALE_MARKET_DATA),
    )
    assert decision.code is DecisionCode.SIMULATION_FAILED


def test_unprofitable_simulation_rejects() -> None:
    decision = decide(
        good_recommendation(),
        now_ms=NOW,
        consensus=unanimous(),
        risk_verdict=approving_risk(),
        simulation=good_simulation(pnl=0),
    )
    assert decision.code is DecisionCode.SIMULATION_FAILED


def test_no_failure_path_produces_approval() -> None:
    """The specification's central guarantee, asserted exhaustively."""
    failure_cases = [
        dict(consensus=None),
        dict(risk_verdict=None),
        dict(simulation=None),
        dict(risk_verdict=blocking_risk()),
        dict(simulation=good_simulation(failure=FailureCode.RISK_REJECTED)),
        dict(simulation=good_simulation(pnl=-1)),
        dict(policy_available=False),
    ]
    for case in failure_cases:
        kwargs = dict(
            consensus=unanimous(),
            risk_verdict=approving_risk(),
            simulation=good_simulation(),
        )
        kwargs.update(case)
        decision = decide(good_recommendation(), now_ms=NOW, **kwargs)  # type: ignore[arg-type]
        assert decision.approved is False, f"failure case approved: {case}"


# --- human override --------------------------------------------------------


def test_human_override_approves_a_rejected_recommendation() -> None:
    """A human decision via the dashboard always wins."""
    decision = decide(
        good_recommendation(),
        now_ms=NOW,
        consensus=unanimous(),
        risk_verdict=blocking_risk(),
        simulation=good_simulation(),
        human_override=True,
    )
    assert decision.approved is True
    assert decision.human_override is True
    assert "automated outcome was rejected" in decision.detail


def test_human_override_rejects_an_approved_recommendation() -> None:
    decision = decide(
        good_recommendation(),
        now_ms=NOW,
        consensus=unanimous(),
        risk_verdict=approving_risk(),
        simulation=good_simulation(),
        human_override=False,
    )
    assert decision.approved is False
    assert decision.human_override is True


def test_override_preserves_the_automated_path() -> None:
    """The record shows what the engine would have decided on its own."""
    decision = decide(
        good_recommendation(),
        now_ms=NOW,
        consensus=unanimous(),
        risk_verdict=blocking_risk(),
        simulation=good_simulation(),
        human_override=True,
    )
    assert DecisionState.RISK_GATE in decision.path
