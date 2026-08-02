"""Integration tests: explanations produced by the full pipeline."""

from __future__ import annotations

import pytest

from apex.config import load_config
from apex.decision import AgentVote, DecisionCode, evaluate_consensus
from apex.dex import Pool
from apex.explain import ExplanationState
from apex.ledger import DecisionOutcome
from apex.pipeline import ExecutionBlocked, SimulationPipeline
from apex.risk import RiskCode, TradeAssessment
from apex.rpc import RpcPool, static_transport

NOW = 1_000_000

RAW_CONFIG = {
    "phase": "simulation_only",
    "chain_id": 137,
    "rpc_endpoints": ["https://rpc-a.example", "https://rpc-b.example"],
    "max_slippage_bps": 500,
    "quote_freshness_ms": 5_000,
    "min_edge_bps": 10,
}


def build_pipeline() -> SimulationPipeline:
    config = load_config(RAW_CONFIG)
    return SimulationPipeline(
        config=config,
        rpc=RpcPool(config.rpc, static_transport({"eth_chainId": "0x89"})),
    )


def make_pool(dex_id: str, reserve_in: int, reserve_out: int) -> Pool:
    return Pool(
        dex_id=dex_id, token_in="USDC", token_out="WETH",
        reserve_in=reserve_in, reserve_out=reserve_out,
        fee_bps=30, observed_at_ms=NOW,
    )


def spread_pools() -> list[Pool]:
    return [
        make_pool("venue-a", 1_000_000_000, 500_000_000),
        make_pool("venue-b", 1_000_000_000, 550_000_000),
    ]


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


def unanimous():
    return evaluate_consensus(
        [AgentVote("market", True, 9_000), AgentVote("risk", True, 8_500), AgentVote("planner", True, 8_000)]
    )


def run_loop(pipeline: SimulationPipeline, **kwargs):
    discovery = pipeline.discover(spread_pools(), 1_000_000, now_ms=NOW, gas_cost_units=1_000)
    paper = pipeline.paper_trade(
        discovery, 1_000_000, now_ms=NOW, assessment=assessment(), gas_cost_cents=10
    )
    params = dict(consensus=unanimous(), notional_cents=1_000)
    params.update(kwargs)
    decision = pipeline.adjudicate(discovery, paper, now_ms=NOW, **params)  # type: ignore[arg-type]
    return discovery, paper, decision


def test_every_decision_produces_a_replayable_explanation() -> None:
    pipeline = build_pipeline()
    run_loop(pipeline)

    assert len(pipeline.explanations) == 1
    explanation = pipeline.explanations.explanations[0]
    assert explanation.state is ExplanationState.REPLAYABLE


def test_rejected_decision_is_explained_with_its_reason() -> None:
    """A skipped opportunity must state why it was skipped."""
    pipeline = build_pipeline()
    _, _, decision = run_loop(pipeline)

    assert decision.outcome is DecisionOutcome.REJECTED
    explanation = pipeline.explanations.explanations[0]
    assert explanation.outcome is DecisionOutcome.REJECTED
    assert explanation.veto_source == DecisionCode.RISK_VETO.value
    assert RiskCode.PHASE_1_EXECUTION_BLOCK.value in explanation.rationale


def test_explanation_id_matches_the_ledger_record() -> None:
    """The trace and the record must be joinable."""
    pipeline = build_pipeline()
    run_loop(pipeline)

    record = pipeline.decisions.records[0]
    explanation = pipeline.explanations.for_decision(record.decision_id)
    assert explanation.decision_id == record.decision_id


def test_explanation_records_the_inputs_used() -> None:
    pipeline = build_pipeline()
    _, paper, _ = run_loop(pipeline)

    explanation = pipeline.explanations.explanations[0]
    joined = " ".join(explanation.inputs_used)
    assert paper.snapshot_hash in joined
    assert "chain:137" in joined


def test_gates_passed_recorded_on_the_trace() -> None:
    pipeline = build_pipeline()
    run_loop(pipeline)

    explanation = pipeline.explanations.explanations[0]
    assert "validate_inputs" in explanation.gates_passed
    assert "check_consensus" in explanation.gates_passed


def test_deferred_decision_is_explained_as_delayed() -> None:
    pipeline = build_pipeline()
    _, _, decision = run_loop(pipeline, consensus=None)

    assert decision.outcome is DecisionOutcome.DEFERRED
    explanation = pipeline.explanations.explanations[0]
    assert "Deferred at" in explanation.rationale


def test_human_override_is_traceable() -> None:
    pipeline = build_pipeline()
    _, paper, decision = run_loop(pipeline, human_override=True)

    assert decision.approved is True
    explanation = pipeline.explanations.explanations[0]
    assert "Human override" in explanation.rationale
    # Approval by override still cannot execute.
    with pytest.raises(ExecutionBlocked):
        pipeline.execute(paper)


def test_explanations_accumulate_across_decisions() -> None:
    pipeline = build_pipeline()
    for _ in range(3):
        run_loop(pipeline)
    assert len(pipeline.explanations) == 3
    assert len(pipeline.decisions) == 3


def test_explanation_renders_for_an_operator() -> None:
    pipeline = build_pipeline()
    run_loop(pipeline)

    text = pipeline.explanations.explanations[0].render()
    assert "REJECTED" in text
    assert "Rationale:" in text
    assert "Gates passed:" in text


def test_full_loop_remains_reproducible_with_explanations() -> None:
    renders = []
    for _ in range(3):
        pipeline = build_pipeline()
        run_loop(pipeline)
        renders.append(pipeline.explanations.explanations[0].render())
    assert len(set(renders)) == 1
