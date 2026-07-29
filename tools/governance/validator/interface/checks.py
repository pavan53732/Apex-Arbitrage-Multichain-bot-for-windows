"""INTERFACE-001: every declared interface name must be unique across
the corpus (two different documents both claiming to define the exact
same interface name is a genuine authority conflict, distinct from
architecture-tests/validate_ownership.py's document-level ownership
check -- this operates on the finer-grained `interfaces` metadata
field)."""
from __future__ import annotations

import networkx as nx

from ...metadata.models import DocumentMetadata
from ..base import CategoryFinding

VALIDATOR_ID = "INTERFACE-001"
CATEGORY = "interface"


def run(docs: list[DocumentMetadata], graph: nx.DiGraph) -> list[CategoryFinding]:
    findings: list[CategoryFinding] = []
    owners_by_interface: dict[str, list[str]] = {}
    for d in docs:
        for iface in d.interfaces:
            owners_by_interface.setdefault(iface, []).append(d.path)

    for iface, paths in owners_by_interface.items():
        if len(paths) > 1:
            for p in paths:
                findings.append(CategoryFinding(
                    validator_id=VALIDATOR_ID,
                    path=p,
                    severity="MEDIUM",
                    message=f"Interface '{iface}' is declared by {len(paths)} documents: {sorted(paths)}",
                    rule="INTERFACE_SINGLE_OWNER",
                ))
    return findings
