"""GRAPH-001: the dependency graph must contain no isolated behavioural
root -- i.e. every behavioural root must have at least one outgoing or
incoming edge in the dependency graph. A behavioural root with zero
graph connectivity is either a documentation gap (its Cross-references/
Depends On sections are empty) or a mis-detected root.
"""
from __future__ import annotations

import networkx as nx

from ...metadata.models import DocumentMetadata
from ..base import CategoryFinding

VALIDATOR_ID = "GRAPH-001"
CATEGORY = "graph"


def run(
    docs: list[DocumentMetadata],
    graph: nx.DiGraph,
    root_paths: set[str] | None = None,
) -> list[CategoryFinding]:
    findings: list[CategoryFinding] = []
    root_paths = root_paths or set()
    for root in root_paths:
        if root not in graph:
            findings.append(CategoryFinding(
                validator_id=VALIDATOR_ID,
                path=root,
                severity="MEDIUM",
                message="Behavioural root has no node in the dependency graph at all",
                rule="ROOT_HAS_GRAPH_CONNECTIVITY",
            ))
            continue
        degree = graph.in_degree(root) + graph.out_degree(root)
        if degree == 0:
            findings.append(CategoryFinding(
                validator_id=VALIDATOR_ID,
                path=root,
                severity="MEDIUM",
                message="Behavioural root is isolated in the dependency graph (zero in/out edges)",
                rule="ROOT_HAS_GRAPH_CONNECTIVITY",
            ))
    return findings
