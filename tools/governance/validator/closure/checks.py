"""CLOSURE-001 (category required by readiness_checklist.json
CHECK-WS3). Checks that every behavioural root's forward closure
actually contains the root itself (a basic sanity invariant: a root is
always a member of its own closure) and that the closure is non-empty.

This validator receives already-computed closures rather than
recomputing them (single-canonical-computation invariant, same pattern
as recovery/security/graph validators above).
"""
from __future__ import annotations

import networkx as nx

from ...metadata.models import DocumentMetadata
from ..base import CategoryFinding

VALIDATOR_ID = "CLOSURE-001"
CATEGORY = "closure"


def run(
    docs: list[DocumentMetadata],
    graph: nx.DiGraph,
    closures_by_root: dict[str, set[str]] | None = None,
) -> list[CategoryFinding]:
    findings: list[CategoryFinding] = []
    closures_by_root = closures_by_root or {}
    for root, closure in closures_by_root.items():
        if root not in closure:
            findings.append(CategoryFinding(
                validator_id=VALIDATOR_ID,
                path=root,
                severity="CRITICAL",
                message="Root's own forward closure does not contain the root itself",
                rule="CLOSURE_CONTAINS_ROOT",
            ))
        if len(closure) == 0:
            findings.append(CategoryFinding(
                validator_id=VALIDATOR_ID,
                path=root,
                severity="HIGH",
                message="Root's forward closure is empty",
                rule="CLOSURE_NON_EMPTY",
            ))
    return findings
