from __future__ import annotations

import sqlite3
import json
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime, timezone


@dataclass
class Task:
    task_id: str
    closure_id: str
    dimension: str
    document_path: str
    section: str
    priority: str
    estimated_effort: str
    validators: List[str]
    acceptance_criteria: List[str]
    status: str = "PENDING"
    assigned_worker: Optional[str] = None
    dependencies: List[str] = None
    blocked_by: List[str] = None
    retry_count: int = 0
    max_retries: int = 3
    created_at: Optional[str] = None
    started_at: Optional[str] = None
    completed_at: Optional[str] = None
    error_message: Optional[str] = None

    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = []
        if self.blocked_by is None:
            self.blocked_by = []


class GovernanceTaskScheduler:
    """Programme 3 Governance Task Scheduler.

    Responsible for:
    - Pending Tasks
    - Dependency Resolution
    - Ready Queue
    - Blocked Queue
    - Worker Assignment
    - Retry Queue
    - Completed Queue
    """

    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

    def _get_conn(self):
        return sqlite3.connect(self.db_path)

    def get_pending_tasks(self, closure_id: str, dimension: str) -> List[Task]:
        """Get all pending tasks for a closure and dimension."""
        conn = self._get_conn()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM tasks 
        WHERE closure_id = ? AND dimension_name = ? AND status = 'PENDING'
        ORDER BY priority DESC, created_at ASC
        """, (closure_id, dimension))
        rows = cursor.fetchall()
        conn.close()
        return [self._row_to_task(r) for r in rows]

    def _row_to_task(self, row: sqlite3.Row) -> Task:
        return Task(
            task_id=row["task_id"],
            closure_id=row["closure_id"],
            dimension=row["dimension_name"],
            document_path=row["document_path"],
            section=row["section_name"],
            priority=row["priority"],
            estimated_effort=row["estimated_effort"],
            validators=json.loads(row["validators"]),
            acceptance_criteria=json.loads(row["acceptance_criteria"]),
            status=row["status"],
            assigned_worker=row.get("assigned_worker"),
            dependencies=json.loads(row.get("dependencies", "[]")),
            blocked_by=json.loads(row.get("blocked_by", "[]")),
            retry_count=row.get("retry_count", 0),
            max_retries=row.get("max_retries", 3),
            created_at=row.get("created_at"),
            started_at=row.get("started_at"),
            completed_at=row.get("completed_at"),
            error_message=row.get("error_message"),
        )

    def get_ready_tasks(self, closure_id: str, dimension: str) -> List[Task]:
        """Get tasks that are ready to execute (no blocking dependencies)."""
        pending = self.get_pending_tasks(closure_id, dimension)
        ready = []
        for task in pending:
            if not task.blocked_by:
                ready.append(task)
        return ready

    def get_blocked_tasks(self, closure_id: str, dimension: str) -> List[Task]:
        """Get tasks that are blocked by dependencies."""
        pending = self.get_pending_tasks(closure_id, dimension)
        blocked = []
        for task in pending:
            if task.blocked_by:
                blocked.append(task)
        return blocked

    def assign_task(self, task_id: str, worker_id: str) -> bool:
        """Assign a task to a worker."""
        conn = self._get_conn()
        cursor = conn.cursor()
        now = datetime.now(timezone.utc).isoformat()
        cursor.execute("""
        UPDATE tasks 
        SET assigned_worker = ?, status = 'IN_PROGRESS', started_at = ?, updated_at = ?
        WHERE task_id = ?
        """, (worker_id, now, now, task_id))
        conn.commit()
        conn.close()
        return cursor.rowcount > 0

    def complete_task(self, task_id: str, success: bool, error_message: Optional[str] = None) -> bool:
        """Mark a task as complete."""
        conn = self._get_conn()
        cursor = conn.cursor()
        now = datetime.now(timezone.utc).isoformat()
        if success:
            cursor.execute("""
            UPDATE tasks 
            SET status = 'COMPLETED', completed_at = ?, updated_at = ?
            WHERE task_id = ?
            """, (now, now, task_id))
        else:
            # Increment retry count
            cursor.execute("""
            UPDATE tasks 
            SET status = 'FAILED', error_message = ?, retry_count = retry_count + 1, updated_at = ?
            WHERE task_id = ?
            """, (error_message, now, task_id))
        conn.commit()
        conn.close()
        return cursor.rowcount > 0

    def get_retry_tasks(self, closure_id: str, dimension: str) -> List[Task]:
        """Get tasks that failed and can be retried."""
        conn = self._get_conn()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM tasks 
        WHERE closure_id = ? AND dimension_name = ? AND status = 'FAILED' AND retry_count < max_retries
        ORDER BY priority DESC, created_at ASC
        """, (closure_id, dimension))
        rows = cursor.fetchall()
        conn.close()
        return [self._row_to_task(r) for r in rows]

    def get_completed_tasks(self, closure_id: str, dimension: str) -> List[Task]:
        """Get all completed tasks for a closure and dimension."""
        conn = self._get_conn()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM tasks 
        WHERE closure_id = ? AND dimension_name = ? AND status = 'COMPLETED'
        ORDER BY completed_at DESC
        """, (closure_id, dimension))
        rows = cursor.fetchall()
        conn.close()
        return [self._row_to_task(r) for r in rows]

    def close(self):
        self.conn.close()
