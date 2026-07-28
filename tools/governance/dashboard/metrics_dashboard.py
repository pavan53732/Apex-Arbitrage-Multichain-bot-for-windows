from __future__ import annotations
from pathlib import Path

class MetricsDashboard:
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root)

    def render(self) -> dict:
        return {"status": "stub", "message": "Metrics dashboard not yet implemented."}
