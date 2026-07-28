from __future__ import annotations
from pathlib import Path

class ArchitectureQueryEngine:
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root)

    def query(self, q: str) -> list[dict]:
        return [{"path": "stub", "answer": "Architecture query engine not yet implemented."}]
