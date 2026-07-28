from __future__ import annotations
import os
from pathlib import Path
from typing import Iterable

class RepoIndexer:
    def __init__(self, repo_root: str, docs_globs: list[str], schemas_glob: str | None = None):
        self.repo_root = Path(repo_root).resolve()
        self.docs_globs = docs_globs
        self.schemas_glob = schemas_glob

    def list_documents(self) -> list[str]:
        paths: list[str] = []
        for pattern in self.docs_globs:
            if os.path.isabs(pattern):
                base = self.repo_root
                rel = os.path.relpath(pattern, self.repo_root)
            else:
                base = self.repo_root
                rel = pattern
            for p in base.glob(rel):
                if p.is_file() and p.suffix == ".md":
                    paths.append(str(p.relative_to(self.repo_root)))
        return sorted(paths)

    def list_schemas(self) -> list[str]:
        if not self.schemas_glob:
            return []
        base = self.repo_root
        rel = self.schemas_glob
        paths = []
        for p in base.glob(rel):
            if p.is_file() and p.suffix == ".json":
                paths.append(str(p.relative_to(self.repo_root)))
        return sorted(paths)

    def build_inventory(self) -> list[dict]:
        docs = self.list_documents()
        inventory = []
        for d in docs:
            inventory.append({"path": d, "type": None, "owner": None, "status": None, "version": None})
        return inventory
