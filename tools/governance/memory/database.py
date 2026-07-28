from __future__ import annotations
from pathlib import Path

class AIMemoryDatabase:
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root)

    def store(self, key: str, value: dict) -> None:
        pass

    def load(self, key: str) -> dict | None:
        return None
