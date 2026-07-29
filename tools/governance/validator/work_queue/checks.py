"""Work queue integrity checks (Programme 2.5 Phase-0, WS9 Integrity
Engine: "Work queue integrity checks pass").

Prior to this module, `.governance/work_queue/*.json` (e.g.
AI-ORCHESTRATION_full_queue.json, 800 tasks) was entirely unvalidated
by IntegrityEngine's 13 checks (confirmed by the Programme 2.5 Final
Certification Audit). This module validates the structural correctness
of every work-queue file found under `.governance/work_queue/`:

- Every task has the required fields (task_id, root_path, dimension,
  document_path, status, priority).
- task_id is unique within each file.
- document_path resolves to a real file on disk.
- status is one of the known values (PENDING, IN_PROGRESS, COMPLETED,
  BLOCKED, CANCELLED).
- priority is one of the known values (CRITICAL, HIGH, MEDIUM, LOW).

This does not attempt to reconcile work-queue tasks against the
canonical document corpus indexed by `apex-gov run` (a separate,
already-disclosed gap: `docs/ai-orchestration/*.md`, the 80 files these
tasks reference, are not matched by `docs_globs` and are therefore
never indexed as canonical documents at all -- changing `docs_globs`
to fix that is a distinct, larger decision affecting every other
workstream's document/root/graph counts, not silently bundled into
this integrity check).
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

VALID_STATUSES = {"PENDING", "IN_PROGRESS", "COMPLETED", "BLOCKED", "CANCELLED"}
VALID_PRIORITIES = {"CRITICAL", "HIGH", "MEDIUM", "LOW"}
REQUIRED_TASK_FIELDS = ["task_id", "root_path", "dimension", "document_path", "status", "priority"]


def check_work_queue_file(queue_path: Path, repo_root: Path) -> dict[str, Any]:
    """Validate a single work-queue JSON file. Returns a result dict
    with status PASS/FAIL and a list of specific, actionable problems."""
    problems: list[str] = []
    try:
        data = queue_path.read_text(encoding="utf-8")
        import json
        tasks = json.loads(data)
    except Exception as exc:
        return {"file": str(queue_path), "status": "FAIL", "problems": [f"could not parse as JSON: {exc}"], "task_count": 0}

    if not isinstance(tasks, list):
        return {"file": str(queue_path), "status": "FAIL", "problems": ["top-level JSON must be a list of tasks"], "task_count": 0}

    seen_task_ids: set[str] = set()
    for i, task in enumerate(tasks):
        if not isinstance(task, dict):
            problems.append(f"task[{i}] is not an object")
            continue
        missing_fields = [f for f in REQUIRED_TASK_FIELDS if f not in task]
        if missing_fields:
            problems.append(f"task[{i}] (task_id={task.get('task_id', '?')}) missing required field(s): {missing_fields}")
            continue

        task_id = task["task_id"]
        if task_id in seen_task_ids:
            problems.append(f"duplicate task_id: {task_id}")
        seen_task_ids.add(task_id)

        doc_path = task["document_path"]
        if not (repo_root / doc_path).exists():
            problems.append(f"task {task_id}: document_path does not exist on disk: {doc_path}")

        status = task["status"]
        if status not in VALID_STATUSES:
            problems.append(f"task {task_id}: invalid status {status!r} (expected one of {sorted(VALID_STATUSES)})")

        priority = task["priority"]
        if priority not in VALID_PRIORITIES:
            problems.append(f"task {task_id}: invalid priority {priority!r} (expected one of {sorted(VALID_PRIORITIES)})")

    return {
        "file": str(queue_path.relative_to(repo_root)) if queue_path.is_absolute() else str(queue_path),
        "status": "FAIL" if problems else "PASS",
        "problems": problems,
        "task_count": len(tasks),
    }


def check_all_work_queues(work_queue_dir: Path, repo_root: Path) -> dict[str, Any]:
    """Validate every *.json file under `work_queue_dir`. Returns an
    aggregate result: overall PASS iff every file individually passes.
    If the directory does not exist or contains no files, this is
    treated as PASS (vacuously -- there is no work queue to be
    invalid), consistent with this codebase's convention for optional,
    not-yet-populated subsystems (e.g. schema_coverage's 1.0-on-empty
    convention in metrics_specification_engine.py)."""
    if not work_queue_dir.exists():
        return {"status": "PASS", "detail": "no work_queue directory found (nothing to validate)", "files": []}

    queue_files = sorted(work_queue_dir.glob("*.json"))
    if not queue_files:
        return {"status": "PASS", "detail": "work_queue directory exists but contains no files", "files": []}

    results = [check_work_queue_file(p, repo_root) for p in queue_files]
    overall_status = "PASS" if all(r["status"] == "PASS" for r in results) else "FAIL"
    total_tasks = sum(r["task_count"] for r in results)
    total_problems = sum(len(r["problems"]) for r in results)
    return {
        "status": overall_status,
        "detail": f"{len(queue_files)} work-queue file(s), {total_tasks} total tasks, {total_problems} problem(s)",
        "files": results,
    }
