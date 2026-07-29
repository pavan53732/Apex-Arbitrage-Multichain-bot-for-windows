
from __future__ import annotations
import re
from pathlib import Path
from typing import Iterable, Optional

from .path_resolver import DocumentIdentityResolver


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
    def __init__(self, repo_root: str, resolver: Optional[DocumentIdentityResolver] = None):
        """
        Args:
            repo_root: repository root path.
            resolver: an optional DocumentIdentityResolver built from the
                full set of canonically indexed document paths. When
                provided, every extracted reference is resolved to its
                canonical indexed path (e.g. `DOCUMENTATION-MAP.md` ->
                `docs/DOCUMENTATION-MAP.md`) before being returned.

                When omitted (the default, preserved for backward
                compatibility with any caller that only has access to a
                single document's text and does not yet know the full
                indexed document set), references are returned with
                surrounding whitespace/`./` stripped but WITHOUT blind
                `docs/` prefix removal -- the previous behaviour of
                unconditionally stripping `docs/` was the confirmed root
                cause of the identifier-mismatch defect (see
                path_resolver.py's module docstring): it discarded
                information needed to tell `docs/AGENTS.md` and the
                distinct root-level `AGENTS.md` apart, and it never
                normalized `RepoIndexer`'s own indexed paths to match,
                causing every reference to a `docs/`-owned document to
                appear "broken" and creating phantom graph nodes.
        """
        self.repo_root = Path(repo_root)
        self.resolver = resolver

    def _normalize_raw(self, ref: str) -> str:
        """Strip leading `./` only. Does NOT strip `docs/` -- see
        __init__ docstring for why that was wrong."""
        ref = ref.strip()
        if ref.startswith("./"):
            ref = ref[2:]
        return ref

    def _resolve(self, ref: str, source_path: str) -> str:
        if self.resolver is not None:
            return self.resolver.resolve(ref, source_path)
        return ref

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

            target_path = self._resolve(self._normalize_raw(target_path), source_path)

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
                        ref = self._resolve(self._normalize_raw(ref), source_path)
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
                        ref = self._resolve(self._normalize_raw(ref), source_path)
                        deps.append(ref)

        return _dedupe_preserve_order(deps)

