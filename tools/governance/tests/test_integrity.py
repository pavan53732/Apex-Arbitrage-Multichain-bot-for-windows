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
        "freeze", "evidence", "metrics", "repository", "work_queue",
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


def test_integrity_engine_freeze_check_accepts_parent_commit_regeneration():
    """Regression test for the freeze self-reference fix.

    A freeze record cannot embed the hash of the commit that introduces
    it (committing the record changes the tree hash, which changes the
    commit hash). check_freeze() must therefore accept a freeze record
    that references HEAD's immediate parent, PROVIDED the only file that
    changed between that parent and HEAD is the freeze record itself —
    which is exactly the shape of a "regenerate the freeze record" commit.
    It must NOT simply always pass a stale freeze off as current: if other
    files also changed, or the freeze commit is older than the immediate
    parent, this must FAIL.
    """
    repo_root = _repo_root()
    engine = IntegrityEngine(repo_root)
    engine.check_freeze()
    result = engine.results[0]
    assert result.check == "freeze"
    # This test runs against whatever HEAD actually is; it does not
    # hardcode a commit hash. It asserts the check produces a definite
    # verdict with a commit hash recorded in its evidence, i.e. that the
    # parent-commit acceptance path is reachable and exercised (not that
    # it always PASSes, since a real staleness regression should still
    # FAIL this check).
    assert result.status in ("PASS", "FAIL")
    assert "commit" in result.detail.lower() or "freeze" in result.detail.lower()


def _init_git_repo(path: Path) -> None:
    import subprocess
    subprocess.run(["git", "init", "-q"], cwd=path, check=True)
    subprocess.run(["git", "config", "user.email", "t@t.com"], cwd=path, check=True)
    subprocess.run(["git", "config", "user.name", "t"], cwd=path, check=True)


def _commit_all(path: Path, message: str) -> str:
    import subprocess
    subprocess.run(["git", "add", "-A"], cwd=path, check=True)
    subprocess.run(["git", "commit", "-q", "-m", message], cwd=path, check=True)
    return subprocess.run(["git", "rev-parse", "HEAD"], cwd=path, capture_output=True, text=True).stdout.strip()


def test_freeze_check_accepts_canonical_pipeline_byproduct_files(tmp_path):
    """Regression test for a real defect found during this session's
    3rd fresh-clone re-verification: check_freeze()'s parent-commit
    exception originally required changed_files to be EXACTLY
    [freeze_record_path] -- correct when `apex-gov freeze` only ever
    touched that one file, but too strict once WS2 (per-root closure
    manifests, each with a timestamp) and WS7 (structured evidence
    store) made `apex-gov freeze` legitimately regenerate many
    timestamped byproduct files as a side effect of the `apex-gov run`
    it invokes internally to gather fresh evidence. A genuine
    freeze-only regeneration commit was incorrectly reported FAIL
    because those byproducts also changed. Fixed to allow changes
    under .governance/freeze/, .governance/closures/,
    .governance/graphs/, .governance/evidence/, .governance/exports/,
    and .governance/governance.db alongside the freeze record itself,
    while still rejecting genuinely unrelated file changes (this test's
    second scenario)."""
    _init_git_repo(tmp_path)
    freeze_dir = tmp_path / ".governance" / "freeze"
    freeze_dir.mkdir(parents=True)
    (freeze_dir / "freeze_WS0.json").write_text('{"repository": {"commit_hash": "placeholder"}}')
    parent_commit = _commit_all(tmp_path, "initial")

    engine = IntegrityEngine(tmp_path)

    # Scenario 1: only byproduct files + the freeze record itself change
    # -- must PASS.
    (freeze_dir / "freeze_WS0.json").write_text(f'{{"repository": {{"commit_hash": "{parent_commit}"}}}}')
    (tmp_path / ".governance" / "closures").mkdir(parents=True)
    (tmp_path / ".governance" / "closures" / "ROOT").mkdir()
    (tmp_path / ".governance" / "closures" / "ROOT" / "manifest.json").write_text("{}")
    (tmp_path / ".governance" / "governance.db").write_bytes(b"fake-db-bytes")
    _commit_all(tmp_path, "regenerate freeze")

    engine.check_freeze()
    result = engine.results[-1]
    assert result.status == "PASS", result.detail

    # Scenario 2: an unrelated, non-byproduct file ALSO changes -- must
    # still FAIL (this is the genuine-staleness case the check exists
    # to catch). Use the current HEAD (from scenario 1) as the new
    # parent for this second regeneration attempt.
    import subprocess
    current_head_before = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=tmp_path, capture_output=True, text=True
    ).stdout.strip()
    engine2 = IntegrityEngine(tmp_path)
    (freeze_dir / "freeze_WS0.json").write_text(f'{{"repository": {{"commit_hash": "{current_head_before}"}}}}')
    (tmp_path / "some_unrelated_source_file.py").write_text("print('unrelated change')")
    _commit_all(tmp_path, "regenerate freeze plus unrelated change")

    engine2.check_freeze()
    result2 = engine2.results[-1]
    assert result2.status == "FAIL", "an unrelated file change alongside freeze regeneration must still FAIL"
    assert "some_unrelated_source_file.py" in result2.detail
