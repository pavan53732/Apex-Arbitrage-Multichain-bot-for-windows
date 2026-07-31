"""
Path normalization and repository root detection utilities.
"""

from __future__ import annotations
from pathlib import Path


def find_repo_root(start_path: Path | None = None) -> Path:
    """Find repository root by looking for .git directory."""
    if start_path is None:
        start_path = Path.cwd()

    current = start_path.resolve()
    while current != current.parent:
        if (current / ".git").exists():
            return current
        current = current.parent

    # Fallback to current directory
    return Path.cwd().resolve()


def normalize_path(path: Path, repo_root: Path) -> str:
    """Normalize path to relative from repo root with forward slashes."""
    try:
        rel = path.relative_to(repo_root)
        return str(rel).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def ensure_within_repo(path: Path, repo_root: Path) -> bool:
    """Check if path is within repository root."""
    try:
        path.resolve().relative_to(repo_root.resolve())
        return True
    except ValueError:
        return False