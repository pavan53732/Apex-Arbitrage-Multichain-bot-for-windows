"""End-to-end tests for the complete Phase 1 pipeline.

detect -> route -> risk -> paper-trade -> adjudicate -> record, and the
execution boundary at the end of it.
"""

from __future__ import annotations

import pytest

from apex.config import load_config
from apex.decision import AgentVote, DecisionCode, evaluate_consensus
from apex.dex import Pool
from apex.ledger import DecisionOutcome, TamperDetected
from apex.pipeline import ExecutionBlocked, PHASE_1_BLOCK_CODE, SimulationPipeline
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
        dex_id=dex_id,
        token_in="USDC",
        token_out="WETH",
        reserve_in=reserve_in,
        reserve_out=reserve_out,
        fee_bps=30,
        observed_at_ms=NOW,
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
        [
            AgentVote("market", True, 9_000),
            AgentVote("risk", True, 8_500),
            AgentVote("planner", True, 8_000),
        ]
    )


def run_full_loop(pipeline: SimulationPipeline, **adjudicate_kwargs: object):
    discovery = pipeline.discover(spread_pools(), 1_000_000, now_ms=NOW, gas_cost_units=1_000)
    paper = pipeline.paper_trade(
        discovery, 1_000_000, now_ms=NOW, assessment=assessment(), gas_cost_cents=10
    )
    kwargs = dict(consensus=unanimous(), notional_cents=1_000)
    kwargs.update(adjudicate_kwargs)
    decision = pipeline.adjudicate(discovery, paper, now_ms=NOW, **kwargs)  # type: ignore[arg-type]
    return discovery, paper, decision


def test_full_loop_reaches_a_recorded_decision() -> None:
    pipeline = build_pipeline()
    _, _, decision = run_full_loop(pipeline)

    assert decision.outcome in (DecisionOutcome.REJECTED, DecisionOutcome.DEFERRED)
    assert len(pipeline.decisions) == 1


def test_phase_1_decision_is_rejected_by_the_risk_gate() -> None:
    """The phase block propagates all the way to the decision outcome."""
    pipeline = build_pipeline()
    _, _, decision = run_full_loop(pipeline)

    assert decision.outcome is DecisionOutcome.REJECTED
    assert decision.code is DecisionCode.RISK_VETO
    assert RiskCode.PHASE_1_EXECUTION_BLOCK.value in decision.detail


def test_rejected_decisions_are_recorded_too() -> None:
    """A ledger holding only approvals records successes, not decisions."""
    pipeline = build_pipeline()
    run_full_loop(pipeline)

    record = pipeline.decisions.records[0]
    assert record.final_decision is DecisionOutcome.REJECTED
    assert record.risk_verdict.startswith("REJECTED")


def test_ledger_chain_verifies_across_multiple_decisions() -> None:
    pipeline = build_pipeline()
    for _ in range(3):
        run_full_loop(pipeline)

    assert len(pipeline.decisions) == 3
    pipeline.decisions.verify()
    assert len(pipeline.decisions.replay()) == 3


def test_recorded_lineage_is_complete() -> None:
    pipeline = build_pipeline()
    _, paper, _ = run_full_loop(pipeline)

    record = pipeline.decisions.records[0]
    assert record.market_snapshot == paper.snapshot_hash
    assert record.trigger_event == "discovery:137"
    assert "net_edge_bps" in record.deterministic_calculations
    assert "simulated_pnl_cents" in record.deterministic_calculations


def test_execution_absence_is_recorded_explicitly() -> None:
    """Phase 1 forbids execution; recording that is the required lineage."""
    pipeline = build_pipeline()
    run_full_loop(pipeline)

    record = pipeline.decisions.records[0]
    assert record.execution_result is None
    assert record.post_execution_outcome is None


def test_tampering_with_recorded_history_is_detected() -> None:
    import dataclasses

    pipeline = build_pipeline()
    run_full_loop(pipeline)
    run_full_loop(pipeline)

    pipeline.decisions._records[0] = dataclasses.replace(
        pipeline.decisions._records[0], recommendation="ALTERED"
    )
    with pytest.raises(TamperDetected):
        pipeline.decisions.verify()


def test_execution_still_blocked_after_adjudication() -> None:
    """Adjudication is the last stage; it never unlocks execution."""
    pipeline = build_pipeline()
    _, paper, _ = run_full_loop(pipeline)

    with pytest.raises(ExecutionBlocked) as excinfo:
        pipeline.execute(paper)
    assert excinfo.value.code == PHASE_1_BLOCK_CODE


def test_human_override_cannot_bypass_the_execution_block() -> None:
    """Even a human approval leaves execution structurally impossible."""
    pipeline = build_pipeline()
    _, paper, decision = run_full_loop(pipeline, human_override=True)

    assert decision.approved is True
    assert decision.human_override is True
    with pytest.raises(ExecutionBlocked):
        pipeline.execute(paper)


def test_missing_consensus_defers_and_is_recorded() -> None:
    pipeline = build_pipeline()
    _, _, decision = run_full_loop(pipeline, consensus=None)

    assert decision.outcome is DecisionOutcome.DEFERRED
    assert pipeline.decisions.records[0].final_decision is DecisionOutcome.DEFERRED


def test_full_loop_is_reproducible() -> None:
    digests = []
    for _ in range(3):
        pipeline = build_pipeline()
        run_full_loop(pipeline)
        digests.append(pipeline.decisions.records[0].digest)
    assert len(set(digests)) == 1


def test_no_execution_capability_across_all_modules() -> None:
    """Structural guard, re-run over the widened package."""
    import pathlib

    import apex

    forbidden = ("send_raw_transaction", "sign_transaction", "private_key", "eth_sendRaw")
    package_dir = pathlib.Path(apex.__file__).parent
    modules = list(package_dir.glob("*.py"))
    assert len(modules) >= 9
    for source in modules:
        text = source.read_text(encoding="utf-8").lower()
        for token in forbidden:
            assert token.lower() not in text, f"{source.name} exposes {token!r}"
