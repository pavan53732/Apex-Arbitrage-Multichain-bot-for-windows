"""Tests for MetricsDashboard (WS8: previously an unimplemented stub
returning {"status": "stub"} unconditionally)."""
from governance.dashboard.metrics_dashboard import MetricsDashboard
from governance.storage.sqlite_store import SqliteStore


def test_render_reports_no_data_when_db_missing(tmp_path):
    dashboard = MetricsDashboard(str(tmp_path), db_path=str(tmp_path / "nonexistent.db"))
    result = dashboard.render()
    assert result["status"] == "no_data"


def test_render_reports_no_metrics_when_table_empty(tmp_path):
    db_path = tmp_path / "empty.db"
    SqliteStore(str(db_path))  # creates schema, no metrics rows
    dashboard = MetricsDashboard(str(tmp_path), db_path=str(db_path))
    result = dashboard.render()
    assert result["status"] == "no_metrics"


def test_render_reports_metrics_and_history_summary(tmp_path):
    db_path = tmp_path / "populated.db"
    store = SqliteStore(str(db_path))
    store.upsert_metrics({"Repository Completeness": 0.8, "Ownership Integrity": 1.0}, computed_at="t1", commit_hash="c1")
    store.upsert_metrics({"Repository Completeness": 0.9}, computed_at="t2", commit_hash="c2")

    dashboard = MetricsDashboard(str(tmp_path), db_path=str(db_path))
    result = dashboard.render()
    assert result["status"] == "ok"
    assert result["metric_count"] == 2
    assert result["metrics"]["Repository Completeness"]["value"] == 0.9  # latest overwrite
    assert result["history_summary"]["Repository Completeness"]["history_entries"] == 2
    assert result["history_summary"]["Ownership Integrity"]["history_entries"] == 1


def test_history_for_metric_returns_all_entries_in_order(tmp_path):
    db_path = tmp_path / "hist.db"
    store = SqliteStore(str(db_path))
    store.upsert_metrics({"M": 0.1}, computed_at="t1", commit_hash="c1")
    store.upsert_metrics({"M": 0.2}, computed_at="t2", commit_hash="c2")
    store.upsert_metrics({"M": 0.3}, computed_at="t3", commit_hash="c3")

    dashboard = MetricsDashboard(str(db_path.parent), db_path=str(db_path))
    history = dashboard.history_for_metric("M")
    assert [h["value"] for h in history] == [0.1, 0.2, 0.3]
    assert [h["commit_hash"] for h in history] == ["c1", "c2", "c3"]


def test_history_for_metric_empty_when_db_missing(tmp_path):
    dashboard = MetricsDashboard(str(tmp_path), db_path=str(tmp_path / "nope.db"))
    assert dashboard.history_for_metric("anything") == []
