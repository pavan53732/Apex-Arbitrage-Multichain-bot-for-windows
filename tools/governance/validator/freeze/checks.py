"""FREEZE-001: every persisted freeze record must reference a real,
resolvable git commit (i.e. `git cat-file -e <commit>` succeeds) --
catching a freeze record whose `commit_hash` was hand-edited, corrupted,
or copied from an unrelated repository/sandbox session (exactly the
defect class the Programme 2.5 Final Certification Audit found in
`ws0_certification_report.json`'s stale foreign-sandbox-path reference,
generalised into a reusable, tested check rather than a one-off manual
finding).
"""
from __future__ import annotations

import subprocess
from pathlib import Path

import networkx as nx

from ...metadata.models import DocumentMetadata
from ..base import CategoryFinding

VALIDATOR_ID = "FREEZE-001"
CATEGORY = "freeze"


def _commit_exists(repo_root: Path, commit_hash: str) -> bool:
    if not commit_hash or not isinstance(commit_hash, str):
        return False
    result = subprocess.run(
        ["git", "cat-file", "-e", f"{commit_hash}^{{commit}}"],
        cwd=repo_root, capture_output=True, text=True,
    )
    return result.returncode == 0


def run(
    docs: list[DocumentMetadata],
    graph: nx.DiGraph,
    freeze_records: list[dict] | None = None,
    repo_root: Path | None = None,
) -> list[CategoryFinding]:
    findings: list[CategoryFinding] = []
    freeze_records = freeze_records or []
    repo_root = repo_root or Path(".")
    for record in freeze_records:
        commit_hash = (
            record.get("repository", {}).get("commit_hash")
            or record.get("repository_hash")
            or record.get("commit_hash")
        )
        source = record.get("_source_path", "<unknown freeze record>")
        if not _commit_exists(repo_root, commit_hash or ""):
            findings.append(CategoryFinding(
                validator_id=VALIDATOR_ID,
                path=str(source),
                severity="CRITICAL",
                message=f"Freeze record references a commit hash that does not resolve in this repository: {commit_hash!r}",
                rule="FREEZE_COMMIT_RESOLVABLE",
            ))
    return findings
