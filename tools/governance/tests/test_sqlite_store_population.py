"""Tests for the WS5 SqliteStore population methods (behavioural_roots,
closures, closure_documents, validators, graphs, metrics, commits) and
the standalone migration CLI."""
import sqlite3
import subprocess
import sys

from governance.storage.sqlite_store import SqliteStore
from governance.closure.root_registry import RootRegistryEntry


def test_schema_version_accessible_via_store(tmp_path):
    store = SqliteStore(str(tmp_path / "t.db"))
    assert store.schema_version() == 1


def test_upsert_behavioural_roots(tmp_path):
    store = SqliteStore(str(tmp_path / "t.db"))
    entries = [RootRegistryEntry(path="docs/A.md", tier="Tier A: Platform Root", signals=["CONTRACT"], reason="x", lifecycle_state="ACTIVE", owner="Team")]
    store.upsert_behavioural_roots(entries)
    cur = store.conn.cursor()
    cur.execute("SELECT path, tier, owner FROM behavioural_roots")
    assert cur.fetchall() == [("docs/A.md", "Tier A: Platform Root", "Team")]


def test_upsert_closures_and_closure_documents(tmp_path):
    store = SqliteStore(str(tmp_path / "t.db"))
    store.upsert_closures([{
        "root_path": "docs/A.md", "closure_hash": "abc", "version": 1,
        "closure_size": 2, "reverse_closure_size": 1,
        "generated_at": "2026-01-01T00:00:00Z", "generated_at_commit": "deadbeef",
    }])
    store.upsert_closure_documents("docs/A.md", ["docs/A.md", "docs/B.md"])
    cur = store.conn.cursor()
    cur.execute("SELECT root_path, closure_hash, version FROM closures")
    assert cur.fetchall() == [("docs/A.md", "abc", 1)]
    cur.execute("SELECT document_path FROM closure_documents WHERE root_path = 'docs/A.md' ORDER BY document_path")
    assert cur.fetchall() == [("docs/A.md",), ("docs/B.md",)]


def test_upsert_graphs(tmp_path):
    store = SqliteStore(str(tmp_path / "t.db"))
    store.upsert_graphs([{"graph_name": "document_graph", "node_count": 10, "edge_count": 5, "file_hash": "h1", "generated_at": "t"}])
    cur = store.conn.cursor()
    cur.execute("SELECT graph_name, node_count, edge_count FROM graphs")
    assert cur.fetchall() == [("document_graph", 10, 5)]


def test_upsert_metrics_populates_both_current_and_history(tmp_path):
    store = SqliteStore(str(tmp_path / "t.db"))
    store.upsert_metrics({"avg_completeness": 0.5}, computed_at="t1", commit_hash="c1")
    store.upsert_metrics({"avg_completeness": 0.6}, computed_at="t2", commit_hash="c2")
    cur = store.conn.cursor()
    cur.execute("SELECT value FROM metrics WHERE metric_name = 'avg_completeness'")
    assert cur.fetchone() == (0.6,)  # current value overwritten
    cur.execute("SELECT value FROM metric_history WHERE metric_name = 'avg_completeness' ORDER BY id")
    assert cur.fetchall() == [(0.5,), (0.6,)]  # history preserves both


def test_insert_commit(tmp_path):
    store = SqliteStore(str(tmp_path / "t.db"))
    store.insert_commit("deadbeef", "2026-01-01T00:00:00Z", 277, 35)
    cur = store.conn.cursor()
    cur.execute("SELECT commit_hash, documents_indexed, behavioural_roots FROM commits")
    assert cur.fetchall() == [("deadbeef", 277, 35)]


def test_insert_freeze_record_and_evidence(tmp_path):
    store = SqliteStore(str(tmp_path / "t.db"))
    store.insert_freeze_record("f1", "WS0", "deadbeef", "treehash", "2026-01-01T00:00:00Z")
    store.insert_evidence("evhash", "apex-gov run", "deadbeef", "2026-01-01T00:00:00Z")
    cur = store.conn.cursor()
    cur.execute("SELECT freeze_id FROM freeze_records")
    assert cur.fetchall() == [("f1",)]
    cur.execute("SELECT freeze_id FROM freeze_history")
    assert cur.fetchall() == [("f1",)]
    cur.execute("SELECT record_hash FROM evidence")
    assert cur.fetchall() == [("evhash",)]


def test_migrate_cli_check_mode_on_fresh_db(tmp_path):
    db_path = tmp_path / "check.db"
    proc = subprocess.run(
        [sys.executable, "-m", "governance.storage.migrate_cli", "--db-path", str(db_path), "--check"],
        capture_output=True, text=True,
    )
    # A non-existent DB reports version 0, which needs migration -> exit 1.
    assert proc.returncode == 1
    assert "needs migration" in proc.stdout


def test_migrate_cli_applies_migrations_and_reports_success(tmp_path):
    db_path = tmp_path / "migrated.db"
    proc = subprocess.run(
        [sys.executable, "-m", "governance.storage.migrate_cli", "--db-path", str(db_path)],
        capture_output=True, text=True,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "Migration successful" in proc.stdout
    assert db_path.exists()

    conn = sqlite3.connect(str(db_path))
    cur = conn.cursor()
    cur.execute("PRAGMA user_version")
    assert cur.fetchone()[0] == 1
    conn.close()

    # Re-running in --check mode now reports up to date.
    proc2 = subprocess.run(
        [sys.executable, "-m", "governance.storage.migrate_cli", "--db-path", str(db_path), "--check"],
        capture_output=True, text=True,
    )
    assert proc2.returncode == 0
    assert "up to date" in proc2.stdout
