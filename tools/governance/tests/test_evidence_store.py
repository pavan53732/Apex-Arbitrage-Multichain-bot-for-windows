"""Tests for the structured Evidence Store (WS7 Evidence System: 10
subdirectories, queryable/auditable evidence, "no programme complete
without evidence")."""
import json

from governance.evidence.evidence_store import STRUCTURED_SUBDIRS, EvidenceStore


def _sample_record(commit="abc123def456", timestamp="2026-01-01T00:00:00+00:00"):
    return {
        "engine": "tools.governance.cli.main:run",
        "command": "apex-gov run",
        "outputs": {"documents_indexed": 277, "avg_completeness": 0.5},
        "hashes": {".governance/graphs/document_graph.graphml": "h1", ".governance/exports/documents.json": "h2"},
        "validator_ids": ["OWNERSHIP-001"],
        "validator_results": {"OWNERSHIP-001": "PASS"},
        "commit": commit,
        "repository_hash": "treehash1",
        "timestamp": timestamp,
    }


def test_exactly_10_structured_subdirs_defined():
    assert len(STRUCTURED_SUBDIRS) == 10
    assert set(STRUCTURED_SUBDIRS) == {
        "Programme1", "Programme2", "Programme3", "validators", "metrics",
        "graphs", "closures", "hashes", "commits", "reports",
    }


def test_store_creates_all_10_subdirectories(tmp_path):
    store = EvidenceStore(tmp_path)
    store.store(_sample_record(), record_hash="deadbeef" * 8)
    for subdir in STRUCTURED_SUBDIRS:
        assert (tmp_path / subdir).exists(), f"{subdir} was not created"


def test_store_writes_to_default_programme1_and_all_category_dirs(tmp_path):
    store = EvidenceStore(tmp_path)
    written = store.store(_sample_record(), record_hash="deadbeef" * 8)
    assert "Programme1" in written
    assert list((tmp_path / "Programme2").glob("*.json")) == []
    for subdir in ["validators", "metrics", "graphs", "closures", "hashes", "commits", "reports"]:
        files = list((tmp_path / subdir).glob("*.json"))
        assert len(files) == 1, f"{subdir} should have exactly 1 file"


def test_store_respects_explicit_programme_argument(tmp_path):
    store = EvidenceStore(tmp_path)
    store.store(_sample_record(), record_hash="deadbeef" * 8, programme="Programme3")
    assert list((tmp_path / "Programme3").glob("*.json"))
    assert not list((tmp_path / "Programme1").glob("*.json"))


def test_validators_subdir_content_is_scoped_to_validator_fields(tmp_path):
    store = EvidenceStore(tmp_path)
    store.store(_sample_record(), record_hash="deadbeef" * 8)
    files = list((tmp_path / "validators").glob("*.json"))
    data = json.loads(files[0].read_text())
    assert data["validator_results"] == {"OWNERSHIP-001": "PASS"}
    assert "outputs" not in data  # scoped, not the full record


def test_graphs_subdir_only_includes_graphml_hashes(tmp_path):
    store = EvidenceStore(tmp_path)
    store.store(_sample_record(), record_hash="deadbeef" * 8)
    files = list((tmp_path / "graphs").glob("*.json"))
    data = json.loads(files[0].read_text())
    assert ".governance/graphs/document_graph.graphml" in data["graph_hashes"]
    assert ".governance/exports/documents.json" not in data["graph_hashes"]


def test_commits_subdir_filename_includes_commit_prefix(tmp_path):
    store = EvidenceStore(tmp_path)
    store.store(_sample_record(commit="abc123def456"), record_hash="deadbeef" * 8)
    files = list((tmp_path / "commits").glob("*.json"))
    assert len(files) == 1
    assert files[0].name.startswith("abc123def456"[:12])


def test_repeated_store_calls_never_overwrite_prior_evidence(tmp_path):
    """The old flat evidence_latest.json was unconditionally overwritten
    on every run -- this is the specific defect WS7 requires be fixed."""
    store = EvidenceStore(tmp_path)
    store.store(_sample_record(commit="commit1", timestamp="2026-01-01T00:00:00+00:00"), record_hash="hash1" + "0" * 59)
    store.store(_sample_record(commit="commit2", timestamp="2026-01-02T00:00:00+00:00"), record_hash="hash2" + "0" * 59)
    reports = list((tmp_path / "reports").glob("*.json"))
    assert len(reports) == 2, "second store() call must not overwrite the first"


def test_query_by_commit_finds_matching_entries(tmp_path):
    store = EvidenceStore(tmp_path)
    store.store(_sample_record(commit="commit1"), record_hash="hash1" + "0" * 59)
    store.store(_sample_record(commit="commit2"), record_hash="hash2" + "0" * 59)
    results = store.query_by_commit("commit1")
    assert len(results) == 1
    assert results[0]["commit"] == "commit1"


def test_query_by_record_hash(tmp_path):
    store = EvidenceStore(tmp_path)
    record_hash = "abcdef01" * 8
    store.store(_sample_record(), record_hash=record_hash)
    found = store.query_by_record_hash(record_hash)
    assert found is not None
    assert found["commit"] == "abc123def456"
    assert store.query_by_record_hash("nonexistent" * 4) is None


def test_latest_returns_most_recent_by_filename_order(tmp_path):
    store = EvidenceStore(tmp_path)
    store.store(_sample_record(commit="old", timestamp="2026-01-01T00:00:00+00:00"), record_hash="hash1" + "0" * 59)
    store.store(_sample_record(commit="new", timestamp="2026-06-01T00:00:00+00:00"), record_hash="hash2" + "0" * 59)
    latest = store.latest()
    assert latest["commit"] == "new"


def test_counts_reflects_actual_file_counts(tmp_path):
    store = EvidenceStore(tmp_path)
    store.store(_sample_record(), record_hash="deadbeef" * 8)
    counts = store.counts()
    assert counts["reports"] == 1
    assert counts["Programme2"] == 0


def test_has_any_evidence_false_when_empty(tmp_path):
    store = EvidenceStore(tmp_path)
    assert store.has_any_evidence() is False


def test_has_any_evidence_true_after_store(tmp_path):
    store = EvidenceStore(tmp_path)
    store.store(_sample_record(), record_hash="deadbeef" * 8)
    assert store.has_any_evidence() is True
