"""Tests for the Integrity Engine (Repository Canonicality Repair, Work Item 6)."""
from pathlib import Path

from governance.integrity.integrity_engine import IntegrityEngine


def _repo_root() -> Path:
    return Path(__file__).parent.parent.parent.parent


def test_integrity_engine_runs_all_checks_and_returns_overall_verdict():
    repo_root = _repo_root()
    engine = IntegrityEngine(repo_root)
    report = engine.run_all()

    assert report["overall"] in ("PASS", "FAIL")
    expected_checks = {
        "configuration", "database", "graphs", "runtime", "roots",
        "closures", "validators", "ownership", "cross_references",
        "freeze", "evidence", "metrics", "repository",
    }
    actual_checks = {c["check"] for c in report["checks"]}
    assert expected_checks.issubset(actual_checks), (
        f"missing checks: {expected_checks - actual_checks}"
    )


def test_integrity_engine_database_check_detects_canonical_db():
    repo_root = _repo_root()
    engine = IntegrityEngine(repo_root)
    engine.check_database()
    assert len(engine.results) == 1
    result = engine.results[0]
    assert result.check == "database"
    # After Work Item 2 (Database Consolidation), exactly one canonical
    # database must exist with no stray copies outside .governance/archive/.
    assert result.status == "PASS", result.detail


def test_integrity_engine_graphs_check_detects_no_duplicates():
    repo_root = _repo_root()
    engine = IntegrityEngine(repo_root)
    engine.check_graphs()
    result = engine.results[0]
    assert result.check == "graphs"
    # After Work Item 3 (Graph Consolidation), exactly 8 canonical graphs
    # must exist with no stray copies outside .governance/archive/.
    assert result.status == "PASS", result.detail
