from __future__ import annotations
from pathlib import Path
from markdown_it_py import MarkdownIt

md = MarkdownIt()

class MarkdownParser:
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root)

    def parse_file(self, rel_path: str) -> dict:
        full = self.repo_root / rel_path
        text = full.read_text(encoding="utf-8")
        tokens = md.parse(text)
        return {"path": rel_path, "raw_text": text, "tokens": tokens}
