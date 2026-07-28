from __future__ import annotations
from pathlib import Path

class HistoryTracker:
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root)

    def record(self, event: str, data: dict) -> None:
        pass
