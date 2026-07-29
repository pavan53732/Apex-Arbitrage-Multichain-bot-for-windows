"""Metrics Dashboard (Programme 2.5 Phase-0, WS8 Metrics Engine).

Prior to this module, `MetricsDashboard.render()` was an unimplemented
stub returning `{"status": "stub", "message": "..."}"` unconditionally
(confirmed by the Programme 2.5 Final Certification Audit). This is the
first real implementation: it reads the live `metrics`/`metric_history`
tables (populated by SqliteStore.upsert_metrics(), wired into
`apex-gov run` -- see cli/main.py) and renders a summary view, with no
independent metric computation of its own (single-canonical-computation
invariant).
"""
from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any


class MetricsDashboard:
    def __init__(self, repo_root: str, db_path: str | None = None):
        self.repo_root = Path(repo_root)
        self.db_path = Path(db_path) if db_path else self.repo_root / ".governance" / "governance.db"

    def render(self) -> dict[str, Any]:
        if not self.db_path.exists():
            return {
                "status": "no_data",
                "message": f"Canonical database not found at {self.db_path}. "
                           "Run `apex-gov run` at least once before rendering the dashboard.",
            }
        try:
            conn = sqlite3.connect(str(self.db_path))
            cur = conn.cursor()
            cur.execute("SELECT metric_name, value, computed_at FROM metrics ORDER BY metric_name")
            current = {row[0]: {"value": row[1], "computed_at": row[2]} for row in cur.fetchall()}

            cur.execute(
                "SELECT metric_name, COUNT(*), MIN(computed_at), MAX(computed_at) "
                "FROM metric_history GROUP BY metric_name ORDER BY metric_name"
            )
            history_summary = {
                row[0]: {"history_entries": row[1], "first_computed_at": row[2], "last_computed_at": row[3]}
                for row in cur.fetchall()
            }
            conn.close()
        except sqlite3.Error as exc:
            return {"status": "error", "message": f"Could not query metrics database: {exc}"}

        if not current:
            return {
                "status": "no_metrics",
                "message": "Metrics table exists but is empty. Run `apex-gov run` to populate it.",
            }

        overall_average = round(sum(m["value"] for m in current.values()) / len(current), 6)

        return {
            "status": "ok",
            "metric_count": len(current),
            "overall_average": overall_average,
            "metrics": current,
            "history_summary": history_summary,
        }

    def history_for_metric(self, metric_name: str) -> list[dict[str, Any]]:
        """WS8 checklist item 'Metrics history is queryable'."""
        if not self.db_path.exists():
            return []
        conn = sqlite3.connect(str(self.db_path))
        cur = conn.cursor()
        cur.execute(
            "SELECT value, computed_at, commit_hash FROM metric_history WHERE metric_name = ? ORDER BY id",
            (metric_name,),
        )
        rows = cur.fetchall()
        conn.close()
        return [{"value": r[0], "computed_at": r[1], "commit_hash": r[2]} for r in rows]
