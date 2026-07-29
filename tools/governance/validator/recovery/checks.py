"""RECOVERY-001: a behavioural root (a document whose type is CONTRACT
and which the closure/root-detection layer would classify as a
behavioural root) should declare recovery or failure-behaviour content
-- a subsystem important enough to be a behavioural root but with zero
documented recovery/failure story is a genuine specification gap.

This validator receives the set of root paths explicitly (rather than
recomputing root detection itself) to preserve the single-canonical-
computation invariant: root detection happens exactly once, in
`BehaviouralRootDetector`, and every consumer (including this
validator) is handed the result rather than re-deriving it.
"""
from __future__ import annotations

import networkx as nx

from ...metadata.models import DocumentMetadata
from ..base import CategoryFinding

VALIDATOR_ID = "RECOVERY-001"
CATEGORY = "recovery"


def run(
    docs: list[DocumentMetadata],
    graph: nx.DiGraph,
    root_paths: set[str] | None = None,
) -> list[CategoryFinding]:
    findings: list[CategoryFinding] = []
    root_paths = root_paths or set()
    for d in docs:
        if d.path in root_paths and not (d.recovery or d.failure_behaviour):
            findings.append(CategoryFinding(
                validator_id=VALIDATOR_ID,
                path=d.path,
                severity="MEDIUM",
                message="Behavioural root has no recovery or failure-behaviour content",
                rule="ROOT_HAS_RECOVERY_STORY",
            ))
    return findings
