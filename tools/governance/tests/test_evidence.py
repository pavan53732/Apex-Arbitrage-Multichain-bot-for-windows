"""Tests for the Evidence Engine (Repository Canonicality Repair, Work Item 5)."""
from pathlib import Path

from governance.evidence.evidence_engine import EvidenceEngine


def _repo_root() -> Path:
    return Path(__file__).parent.parent.parent.parent


def test_evidence_engine_collects_required_fields():
    engine = EvidenceEngine(_repo_root())
    record = engine.collect()

    assert record.engine
    assert record.command == "apex-gov run"
    assert isinstance(record.inputs, dict)
    assert isinstance(record.outputs, dict)
    assert len(record.hashes) > 0
    assert record.execution_time_ms > 0
    assert len(record.validator_ids) > 0
    assert len(record.commit) == 40  # full git SHA
    assert len(record.repository_hash) == 40
    assert record.producer
    assert len(record.consumer) > 0
    assert record.timestamp


def test_evidence_engine_record_hash_is_reproducible():
    """The Repository Canonicality Repair required evidence to be
    reproducible. record_hash() excludes timestamp/execution_time_ms
    (which are expected to vary between runs) and must be identical
    across two consecutive collections against an unchanged repository."""
    engine = EvidenceEngine(_repo_root())
    record1 = engine.collect()
    record2 = engine.collect()
    assert record1.record_hash() == record2.record_hash(), (
        "Evidence record content (outputs, hashes, validator_results) "
        "must be identical across consecutive collections against an "
        "unchanged repository."
    )
