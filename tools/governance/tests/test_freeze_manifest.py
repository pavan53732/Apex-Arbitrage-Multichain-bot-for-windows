"""Tests for the 5 additional Freeze* classes (WS6 Freeze Framework:
FreezeManifest, FreezeHash, FreezeValidator, FreezeEvidence,
FreezeHistory), completing the 6-class checklist requirement
(FreezeRecord already existed in freeze_engine.py)."""
import json

from governance.freeze.freeze_manifest import (
    FreezeEvidence,
    FreezeHash,
    FreezeHistory,
    FreezeManifest,
    FreezeValidator,
)


def _sample_record_data(commit="abc123", freeze_id="f1"):
    return {
        "identity": {"freeze_id": freeze_id, "workstream_id": "WS0"},
        "repository": {"commit_hash": commit, "repository_tree_hash": "tree1"},
        "execution": {"timestamp": "2026-01-01T00:00:00Z", "execution_time_ms": 123.4},
        "validation": {"all_pass": True},
        "integrity": {"integrity_checksum": "checksum1"},
        "evidence": {"evidence_record_hash": "evhash1", "artefact_hashes": {"a.json": "h1"}},
        "freeze": {"freeze_timestamp": "2026-01-01T00:00:01Z"},
    }


def test_freeze_manifest_extracts_flat_summary():
    data = _sample_record_data()
    manifest = FreezeManifest.from_record_dict(data)
    assert manifest.freeze_id == "f1"
    assert manifest.workstream_id == "WS0"
    assert manifest.commit_hash == "abc123"
    assert manifest.all_validators_pass is True
    d = manifest.to_dict()
    assert d["commit_hash"] == "abc123"


def test_freeze_hash_is_deterministic_and_excludes_volatile_fields():
    data1 = _sample_record_data()
    data2 = _sample_record_data()
    data2["execution"]["timestamp"] = "2026-06-06T00:00:00Z"  # different timestamp
    data2["execution"]["execution_time_ms"] = 999.9
    data2["freeze"]["freeze_timestamp"] = "2026-06-06T00:00:01Z"
    assert FreezeHash.compute(data1) == FreezeHash.compute(data2)


def test_freeze_hash_changes_with_substantive_content_change():
    data1 = _sample_record_data(commit="abc123")
    data2 = _sample_record_data(commit="def456")
    assert FreezeHash.compute(data1) != FreezeHash.compute(data2)


def test_freeze_hash_verify():
    data = _sample_record_data()
    h = FreezeHash.compute(data)
    assert FreezeHash.verify(data, h) is True
    assert FreezeHash.verify(data, "wrong_hash") is False


def test_freeze_validator_sign_and_verify_roundtrip(tmp_path):
    key_path = tmp_path / ".signing_key"
    validator = FreezeValidator(key_path)
    data = _sample_record_data()
    signature = validator.sign(data)
    assert validator.verify(data, signature) is True
    assert key_path.exists()


def test_freeze_validator_detects_tampering(tmp_path):
    key_path = tmp_path / ".signing_key"
    validator = FreezeValidator(key_path)
    data = _sample_record_data()
    signature = validator.sign(data)

    tampered = _sample_record_data()
    tampered["repository"]["commit_hash"] = "malicious-tampered-commit"
    assert validator.verify(tampered, signature) is False, "Tampered record must fail signature verification"


def test_freeze_validator_verify_without_key_file_fails_safe(tmp_path):
    key_path = tmp_path / "missing_key"
    validator = FreezeValidator(key_path)
    data = _sample_record_data()
    assert validator.verify(data, "any_signature") is False


def test_freeze_validator_reuses_same_key_across_instances(tmp_path):
    key_path = tmp_path / ".signing_key"
    v1 = FreezeValidator(key_path)
    data = _sample_record_data()
    sig1 = v1.sign(data)

    v2 = FreezeValidator(key_path)  # new instance, same key file
    assert v2.verify(data, sig1) is True


def test_freeze_evidence_extracts_evidence_fields():
    data = _sample_record_data()
    evidence = FreezeEvidence.from_record_dict(data)
    assert evidence.evidence_record_hash == "evhash1"
    assert evidence.artefact_hashes == {"a.json": "h1"}


def test_freeze_history_append_and_list_all(tmp_path):
    history = FreezeHistory(tmp_path)
    m1 = FreezeManifest.from_record_dict(_sample_record_data(commit="c1", freeze_id="f1"))
    m2 = FreezeManifest.from_record_dict(_sample_record_data(commit="c2", freeze_id="f2"))
    history.append(m1, signature="sig1")
    history.append(m2, signature="sig2")

    all_entries = history.list_all("WS0")
    assert len(all_entries) == 2
    assert all_entries[0]["freeze_id"] == "f1"
    assert all_entries[0]["signature"] == "sig1"
    assert all_entries[1]["freeze_id"] == "f2"


def test_freeze_history_get_by_freeze_id(tmp_path):
    history = FreezeHistory(tmp_path)
    m1 = FreezeManifest.from_record_dict(_sample_record_data(commit="c1", freeze_id="f1"))
    history.append(m1)
    found = history.get_by_freeze_id("WS0", "f1")
    assert found is not None
    assert found["commit_hash"] == "c1"
    assert history.get_by_freeze_id("WS0", "nonexistent") is None


def test_freeze_history_get_by_commit(tmp_path):
    history = FreezeHistory(tmp_path)
    history.append(FreezeManifest.from_record_dict(_sample_record_data(commit="c1", freeze_id="f1")))
    history.append(FreezeManifest.from_record_dict(_sample_record_data(commit="c1", freeze_id="f2")))
    history.append(FreezeManifest.from_record_dict(_sample_record_data(commit="c2", freeze_id="f3")))
    matches = history.get_by_commit("WS0", "c1")
    assert len(matches) == 2
    assert {m["freeze_id"] for m in matches} == {"f1", "f2"}


def test_freeze_history_empty_when_no_file_exists(tmp_path):
    history = FreezeHistory(tmp_path)
    assert history.list_all("NEVER_FROZEN") == []


def test_freeze_hash_excludes_tamper_evidence_key_added_after_signing(tmp_path):
    """Regression-guarding test for the exact sign -> save -> reload ->
    verify sequence freeze_engine.py's freeze_and_save() performs: the
    signature is computed over a record BEFORE the 'tamper_evidence' key
    (which embeds that very signature) is added to the dict that gets
    written to disk. If FreezeHash did not exclude 'tamper_evidence',
    verifying a freshly-reloaded (from-disk) record against its own
    embedded signature would always fail, because the hash computed at
    verify-time (with 'tamper_evidence' present) would differ from the
    hash computed at sign-time (without it)."""
    key_path = tmp_path / ".signing_key"
    validator = FreezeValidator(key_path)
    data = _sample_record_data()

    signature = validator.sign(data)  # signed BEFORE tamper_evidence exists
    data["tamper_evidence"] = {"signature": signature, "algorithm": "HMAC-SHA256"}

    # Simulate save-to-disk-and-reload by round-tripping through JSON.
    reloaded = json.loads(json.dumps(data))
    assert validator.verify(reloaded, reloaded["tamper_evidence"]["signature"]) is True
