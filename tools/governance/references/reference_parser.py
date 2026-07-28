from __future__ import annotations
import re
from pathlib import Path
from typing import Iterable

LINK_PATTERN = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

class ReferenceParser:
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root)

    def extract_links(self, text: str) -> list[tuple[str, str]]:
        return LINK_PATTERN.findall(text)

    def resolve_doc_links(self, links: list[tuple[str, str]], source_path: str) -> list[dict]:
        edges = []
        source = Path(source_path)
        for label, target in links:
            if not target.endswith(".md"):
                continue
            if target.startswith("/"):
                target_path = target[1:]
            else:
                target_path = str((source.parent / target).as_posix())
            edges.append({"source": str(source.as_posix()), "target": target_path, "label": label, "relation": "references"})
        return edges
