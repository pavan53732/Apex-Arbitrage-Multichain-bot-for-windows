"""DEPENDENCY-001, DEPENDENCY-002: dependency-graph structural validators.

DEPENDENCY-001: every `depends_on` reference must resolve to a document
that exists in the indexed corpus (broken-reference check restricted to
the `depends_on` field specifically -- distinct from
GovernanceValidator's BROKEN_REFERENCE rule, which also covers
`cross_references`).

DEPENDENCY-002: no document may list itself in its own `depends_on`
(self-dependency), which would make its own closure trivially include
itself as a "dependency" rather than only as the closure root.
"""
from __future__ import annotations

import networkx as nx

from ...metadata.models import DocumentMetadata
from ..base import CategoryFinding

CATEGORY = "dependency"


def run(docs: list[DocumentMetadata], graph: nx.DiGraph) -> list[CategoryFinding]:
    findings: list[CategoryFinding] = []
    known_paths = {d.path for d in docs}

    for d in docs:
        # DEPENDENCY-001: depends_on target must exist.
        for dep in d.depends_on:
            if dep not in known_paths:
                findings.append(CategoryFinding(
                    validator_id="DEPENDENCY-001",
                    path=d.path,
                    severity="MEDIUM",
                    message=f"depends_on references non-existent document: {dep}",
                    rule="DEPENDENCY_TARGET_EXISTS",
                ))
        # DEPENDENCY-002: no self-dependency.
        if d.path in d.depends_on:
            findings.append(CategoryFinding(
                validator_id="DEPENDENCY-002",
                path=d.path,
                severity="MEDIUM",
                message="Document lists itself in its own depends_on",
                rule="NO_SELF_DEPENDENCY",
            ))
    return findings
