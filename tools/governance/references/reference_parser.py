
from __future__ import annotations
import re
from pathlib import Path
from typing import Iterable


def _dedupe_preserve_order(items: list[str]) -> list[str]:
    """Deduplicate a list while preserving first-seen order.

    `list(set(items))` is non-deterministic across process restarts because
    Python's string hashing (and therefore `set` iteration order) is
    randomized per-process by default (`PYTHONHASHSEED`). Regex extraction
    order from a fixed input text is itself deterministic, so preserving
    that order while dropping duplicates gives a fully deterministic,
    reproducible result across any process, shell, or `PYTHONHASHSEED`.
    """
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


class ReferenceParser:
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root)

    def extract_links(self, text: str) -> list[tuple[str, str]]:
        """Extract all markdown links [text](target)."""
        return re.findall(r'\[([^\]]+)\]\(([^)]+)\)', text)

    def extract_doc_links(self, text: str, source_path: str) -> list[dict]:
        """Extract all markdown links that point to .md files."""
        edges = []
        source = Path(source_path)
        links = self.extract_links(text)

        for label, target in links:
            if not target.endswith(".md"):
                continue

            # Resolve relative path
            if target.startswith("/"):
                target_path = target[1:]
            else:
                target_path = str((source.parent / target).as_posix())

            # Normalize path
            if target_path.startswith("docs/"):
                target_path = target_path[5:]  # Remove docs/ prefix for consistency

            edges.append({
                "source": str(source.as_posix()),
                "target": target_path,
                "label": label,
                "relation": "references",
            })

        return edges

    def extract_cross_references(self, text: str, source_path: str) -> list[str]:
        """Extract document references from Cross References section."""
        refs = []
        # Match Cross References section
        match = re.search(r"## Cross.*?References?\n+(.+?)(?=\n##|\n---|$)", text, re.IGNORECASE | re.DOTALL)
        if not match:
            return refs

        content = match.group(1)
        # Extract markdown links and bare .md references
        for pattern in [r'\[([^\]]+)\]\(([^)]+)\)', r'`([A-Z][A-Z0-9_.-]+\.md)`', r'([A-Z][A-Z0-9_.-]+\.md)']:
            for m in re.finditer(pattern, content):
                if m.lastindex >= 1:
                    ref = m.group(m.lastindex)
                    if ref.endswith(".md"):
                        # Normalize path
                        if ref.startswith("docs/"):
                            ref = ref[5:]
                        refs.append(ref)

        return _dedupe_preserve_order(refs)

    def extract_depends_on(self, text: str, source_path: str) -> list[str]:
        """Extract dependencies from Depends On section."""
        deps = []
        match = re.search(r"## Depends On\n+(.+?)(?=\n##|\n---|$)", text, re.IGNORECASE | re.DOTALL)
        if not match:
            # Try Dependencies section
            match = re.search(r"## Dependencies\n+(.+?)(?=\n##|\n---|$)", text, re.IGNORECASE | re.DOTALL)
        if not match:
            return deps

        content = match.group(1)
        for pattern in [r'\[([^\]]+)\]\(([^)]+)\)', r'`([A-Z][A-Z0-9_.-]+\.md)`', r'([A-Z][A-Z0-9_.-]+\.md)']:
            for m in re.finditer(pattern, content):
                if m.lastindex >= 1:
                    ref = m.group(m.lastindex)
                    if ref.endswith(".md"):
                        if ref.startswith("docs/"):
                            ref = ref[5:]
                        deps.append(ref)

        return _dedupe_preserve_order(deps)
