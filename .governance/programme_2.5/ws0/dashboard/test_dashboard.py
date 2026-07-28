
from pathlib import Path
import json
from datetime import datetime

class TestDashboard:
    def __init__(self, dashboard_file: Path):
        self.dashboard_file = dashboard_file
        self.data = {
            "last_run": None,
            "regression": {"pass_rate": 0.0, "total": 0, "passed": 0},
            "determinism": {"pass_rate": 0.0, "total": 0, "passed": 0},
            "fresh_clone": {"pass_rate": 0.0, "total": 0, "passed": 0},
            "corruption": {"pass_rate": 0.0, "total": 0, "passed": 0},
            "stress": {"pass_rate": 0.0, "total": 0, "passed": 0},
            "fuzz": {"pass_rate": 0.0, "total": 0, "passed": 0},
            "performance": {},
            "evidence": [],
            "failure_history": [],
        }

    def update_regression(self, results: list):
        total = len(results)
        passed = sum(1 for r in results if r.get("passed", False))
        self.data["regression"] = {
            "pass_rate": passed / total if total > 0 else 0.0,
            "total": total,
            "passed": passed,
        }

    def update_determinism(self, results: list):
        total = len(results)
        passed = sum(1 for r in results if r.get("passed", False))
        self.data["determinism"] = {
            "pass_rate": passed / total if total > 0 else 0.0,
            "total": total,
            "passed": passed,
        }

    def update_fresh_clone(self, results: list):
        total = len(results)
        passed = sum(1 for r in results if r.get("passed", False))
        self.data["fresh_clone"] = {
            "pass_rate": passed / total if total > 0 else 0.0,
            "total": total,
            "passed": passed,
        }

    def update_corruption(self, results: list):
        total = len(results)
        passed = sum(1 for r in results if r.get("passed", False))
        self.data["corruption"] = {
            "pass_rate": passed / total if total > 0 else 0.0,
            "total": total,
            "passed": passed,
        }

    def update_stress(self, results: list):
        total = len(results)
        passed = sum(1 for r in results if r.get("passed", False))
        self.data["stress"] = {
            "pass_rate": passed / total if total > 0 else 0.0,
            "total": total,
            "passed": passed,
        }

    def update_fuzz(self, results: list):
        total = len(results)
        passed = sum(1 for r in results if r.get("passed", False))
        self.data["fuzz"] = {
            "pass_rate": passed / total if total > 0 else 0.0,
            "total": total,
            "passed": passed,
        }

    def add_evidence(self, evidence: dict):
        self.data["evidence"].append(evidence)

    def add_failure(self, failure: dict):
        self.data["failure_history"].append(failure)

    def save(self):
        self.data["last_run"] = datetime.utcnow().isoformat()
        with open(self.dashboard_file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2)
