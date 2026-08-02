"""Tests for the hash-chained decision ledger.

Tamper detection and rejection of incomplete records are explicit integrity
rules in `decision-ledger.md`, so both are tested directly.
"""

from __future__ import annotations

import dataclasses

import pytest

from apex.ledger import (
    GENESIS_DIGEST,
    DecisionLedger,
    DecisionOutcome,
    IncompleteRecord,
    LedgerError,
    TamperDetected,
)


def append_one(ledger: DecisionLedger, decision_id: str = "d1", **overrides: object):
    params = dict(
        decision_id=decision_id,
        timestamp_ms=1_000,
        trigger_event="discovery:137",
        market_snapshot="abc123",
        recommendation="USDC/WETH@b->a",
        deterministic_calculations={"net_edge_bps": 900},
        policy_evaluation="available",
        risk_verdict="REJECTED: PHASE_1_EXECUTION_BLOCK",
        simulation_result="pnl 42c",
        final_decision=DecisionOutcome.REJECTED,
    )
    params.update(overrides)
    return ledger.append(**params)  # type: ignore[arg-type]


def test_empty_ledger_head_is_genesis() -> None:
    assert DecisionLedger().head_digest == GENESIS_DIGEST


def test_first_record_chains_to_genesis() -> None:
    ledger = DecisionLedger()
    record = append_one(ledger)
    assert record.previous_digest == GENESIS_DIGEST


def test_records_chain_to_predecessor() -> None:
    ledger = DecisionLedger()
    first = append_one(ledger, "d1")
    second = append_one(ledger, "d2")
    assert second.previous_digest == first.digest
    assert ledger.head_digest == second.digest


def test_chain_verifies_when_intact() -> None:
    ledger = DecisionLedger()
    for i in range(5):
        append_one(ledger, f"d{i}")
    ledger.verify()  # must not raise


def test_tampering_is_detected_on_read() -> None:
    """Altering a stored record breaks every link after it."""
    ledger = DecisionLedger()
    append_one(ledger, "d1")
    append_one(ledger, "d2")
    append_one(ledger, "d3")

    # Frozen records cannot be mutated, so tampering means replacing one.
    tampered = dataclasses.replace(ledger._records[0], recommendation="ALTERED")
    ledger._records[0] = tampered

    with pytest.raises(TamperDetected, match="chain broken at position 1"):
        ledger.verify()


def test_replay_verifies_before_returning() -> None:
    """A replay over a tampered chain would reproduce the tampering."""
    ledger = DecisionLedger()
    append_one(ledger, "d1")
    append_one(ledger, "d2")
    ledger._records[0] = dataclasses.replace(ledger._records[0], market_snapshot="ALTERED")

    with pytest.raises(TamperDetected):
        ledger.replay()


def test_replay_returns_full_chain_when_intact() -> None:
    ledger = DecisionLedger()
    append_one(ledger, "d1")
    append_one(ledger, "d2")
    assert len(ledger.replay()) == 2


def test_record_is_immutable() -> None:
    ledger = DecisionLedger()
    record = append_one(ledger)
    with pytest.raises(dataclasses.FrozenInstanceError):
        record.recommendation = "changed"  # type: ignore[misc]


@pytest.mark.parametrize(
    "field,value",
    [
        ("decision_id", ""),
        ("trigger_event", "   "),
        ("market_snapshot", ""),
        ("recommendation", ""),
        ("policy_evaluation", ""),
        ("risk_verdict", ""),
        ("simulation_result", ""),
        ("deterministic_calculations", {}),
    ],
)
def test_incomplete_record_is_rejected_not_partially_stored(field: str, value: object) -> None:
    ledger = DecisionLedger()
    with pytest.raises(IncompleteRecord, match="missing required"):
        append_one(ledger, **{field: value})  # type: ignore[arg-type]
    assert len(ledger) == 0


def test_duplicate_decision_id_rejected() -> None:
    ledger = DecisionLedger()
    append_one(ledger, "d1")
    with pytest.raises(LedgerError, match="already recorded"):
        append_one(ledger, "d1")


def test_execution_fields_may_be_explicitly_absent() -> None:
    """Phase 1 records decisions that never executed; that is valid lineage."""
    ledger = DecisionLedger()
    record = append_one(ledger)
    assert record.execution_result is None
    assert record.post_execution_outcome is None
    ledger.verify()


def test_digest_is_deterministic() -> None:
    """A replay producing the same content must produce the same digest."""
    a, b = DecisionLedger(), DecisionLedger()
    first = append_one(a)
    second = append_one(b)
    assert first.digest == second.digest


def test_digest_is_order_independent_for_calculations() -> None:
    """Dictionary ordering must not change the digest."""
    a, b = DecisionLedger(), DecisionLedger()
    ra = append_one(a, deterministic_calculations={"x": 1, "y": 2})
    rb = append_one(b, deterministic_calculations={"y": 2, "x": 1})
    assert ra.digest == rb.digest


def test_digest_changes_with_content() -> None:
    a, b = DecisionLedger(), DecisionLedger()
    ra = append_one(a, simulation_result="pnl 42c")
    rb = append_one(b, simulation_result="pnl 43c")
    assert ra.digest != rb.digest


def test_caller_cannot_forge_chain_position() -> None:
    """`previous_digest` is set by the ledger, not supplied by the caller."""
    ledger = DecisionLedger()
    with pytest.raises(TypeError):
        ledger.append(  # type: ignore[call-arg]
            decision_id="d1",
            timestamp_ms=1,
            trigger_event="t",
            market_snapshot="m",
            recommendation="r",
            deterministic_calculations={"a": 1},
            policy_evaluation="p",
            risk_verdict="v",
            simulation_result="s",
            final_decision=DecisionOutcome.REJECTED,
            previous_digest="forged",
        )


def test_find_locates_record() -> None:
    ledger = DecisionLedger()
    append_one(ledger, "d1")
    append_one(ledger, "d2")
    assert ledger.find("d2").decision_id == "d2"
    with pytest.raises(LedgerError, match="no record"):
        ledger.find("missing")


def test_records_property_returns_copy() -> None:
    """A caller must not be able to reach in and alter stored history."""
    ledger = DecisionLedger()
    append_one(ledger, "d1")
    snapshot = ledger.records
    assert isinstance(snapshot, tuple)
    append_one(ledger, "d2")
    assert len(snapshot) == 1
