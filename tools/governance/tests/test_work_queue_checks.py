"""Tests for work-queue integrity checks (WS9: "Work queue integrity
checks pass" -- previously entirely unvalidated by IntegrityEngine)."""
import json

from governance.validator.work_queue.checks import check_all_work_queues, check_work_queue_file


def _valid_task(task_id="T1", document_path="doc.md"):
    return {
        "task_id": task_id, "root_path": "docs/ROOT.md", "dimension": "STRUCTURE",
        "document_path": document_path, "status": "PENDING", "priority": "HIGH",
    }


def test_valid_queue_file_passes(tmp_path):
    (tmp_path / "doc.md").write_text("# doc")
    queue_path = tmp_path / "queue.json"
    queue_path.write_text(json.dumps([_valid_task()]))
    result = check_work_queue_file(queue_path, tmp_path)
    assert result["status"] == "PASS"
    assert result["problems"] == []
    assert result["task_count"] == 1


def test_invalid_json_fails():
    import tempfile
    from pathlib import Path
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "bad.json"
        p.write_text("{not valid json")
        result = check_work_queue_file(p, Path(d))
        assert result["status"] == "FAIL"
        assert "could not parse" in result["problems"][0]


def test_non_list_top_level_fails(tmp_path):
    queue_path = tmp_path / "queue.json"
    queue_path.write_text(json.dumps({"not": "a list"}))
    result = check_work_queue_file(queue_path, tmp_path)
    assert result["status"] == "FAIL"
    assert "must be a list" in result["problems"][0]


def test_missing_required_field_fails(tmp_path):
    (tmp_path / "doc.md").write_text("# doc")
    task = _valid_task()
    del task["priority"]
    queue_path = tmp_path / "queue.json"
    queue_path.write_text(json.dumps([task]))
    result = check_work_queue_file(queue_path, tmp_path)
    assert result["status"] == "FAIL"
    assert "missing required field" in result["problems"][0]


def test_duplicate_task_id_fails(tmp_path):
    (tmp_path / "doc.md").write_text("# doc")
    queue_path = tmp_path / "queue.json"
    queue_path.write_text(json.dumps([_valid_task("DUP"), _valid_task("DUP")]))
    result = check_work_queue_file(queue_path, tmp_path)
    assert result["status"] == "FAIL"
    assert any("duplicate task_id" in p for p in result["problems"])


def test_missing_document_path_fails(tmp_path):
    queue_path = tmp_path / "queue.json"
    queue_path.write_text(json.dumps([_valid_task(document_path="nonexistent.md")]))
    result = check_work_queue_file(queue_path, tmp_path)
    assert result["status"] == "FAIL"
    assert any("does not exist on disk" in p for p in result["problems"])


def test_invalid_status_fails(tmp_path):
    (tmp_path / "doc.md").write_text("# doc")
    task = _valid_task()
    task["status"] = "NOT_A_REAL_STATUS"
    queue_path = tmp_path / "queue.json"
    queue_path.write_text(json.dumps([task]))
    result = check_work_queue_file(queue_path, tmp_path)
    assert result["status"] == "FAIL"
    assert any("invalid status" in p for p in result["problems"])


def test_invalid_priority_fails(tmp_path):
    (tmp_path / "doc.md").write_text("# doc")
    task = _valid_task()
    task["priority"] = "URGENT_BUT_NOT_A_VALID_ENUM"
    queue_path = tmp_path / "queue.json"
    queue_path.write_text(json.dumps([task]))
    result = check_work_queue_file(queue_path, tmp_path)
    assert result["status"] == "FAIL"
    assert any("invalid priority" in p for p in result["problems"])


def test_check_all_work_queues_passes_vacuously_when_dir_missing(tmp_path):
    result = check_all_work_queues(tmp_path / "nonexistent", tmp_path)
    assert result["status"] == "PASS"


def test_check_all_work_queues_passes_vacuously_when_dir_empty(tmp_path):
    wq_dir = tmp_path / "work_queue"
    wq_dir.mkdir()
    result = check_all_work_queues(wq_dir, tmp_path)
    assert result["status"] == "PASS"


def test_check_all_work_queues_aggregates_multiple_files(tmp_path):
    (tmp_path / "doc.md").write_text("# doc")
    wq_dir = tmp_path / "work_queue"
    wq_dir.mkdir()
    (wq_dir / "queue_a.json").write_text(json.dumps([_valid_task("A1")]))
    (wq_dir / "queue_b.json").write_text(json.dumps([_valid_task("B1", document_path="missing.md")]))
    result = check_all_work_queues(wq_dir, tmp_path)
    assert result["status"] == "FAIL"  # queue_b has a problem
    assert len(result["files"]) == 2
    assert result["files"][0]["status"] == "PASS"
    assert result["files"][1]["status"] == "FAIL"


def test_real_repository_ai_orchestration_queue_is_structurally_valid():
    """Sanity check against the actual, real work-queue file in this
    repository (.governance/work_queue/AI-ORCHESTRATION_full_queue.json,
    800 tasks) -- confirms the checker handles real-world data, not
    just synthetic fixtures."""
    from pathlib import Path
    repo_root = Path(__file__).resolve().parents[3]
    queue_path = repo_root / ".governance" / "work_queue" / "AI-ORCHESTRATION_full_queue.json"
    if not queue_path.exists():
        import pytest
        pytest.skip("real work_queue file not present in this checkout")
    result = check_work_queue_file(queue_path, repo_root)
    assert result["task_count"] == 800
    assert result["status"] == "PASS", result["problems"][:5]
