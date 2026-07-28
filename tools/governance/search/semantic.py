from __future__ import annotations
from pathlib import Path

class SemanticSearch:
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root)

    def search(self, query: str) -> list[dict]:
        return [{"path": "stub", "score": 0.0, "snippet": "Semantic search not yet implemented."}]
