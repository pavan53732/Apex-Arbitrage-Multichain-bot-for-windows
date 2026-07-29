"""OWNERSHIP-001: every document must have a non-empty `owner` field.

This is the category-validator implementation of validator_catalogue.json's
OWNERSHIP-001 ID. It duplicates neither logic nor computation from
`GovernanceValidator._check_missing_owners` by accident -- both exist
because the two validator layers are frozen as distinct in Phase-0
(`registry.py`'s docstring already documents this as intentional, not a
defect); this module is the category-organised, independently
importable/testable form the readiness checklist explicitly requires
(`validator/ownership/ implemented`), operating on the same
already-parsed `DocumentMetadata` list without re-parsing anything.
"""
from __future__ import annotations

import networkx as nx

from ...metadata.models import DocumentMetadata
from ..base import CategoryFinding

VALIDATOR_ID = "OWNERSHIP-001"
CATEGORY = "ownership"


def run(docs: list[DocumentMetadata], graph: nx.DiGraph) -> list[CategoryFinding]:
    findings = []
    for d in docs:
        if not d.owner:
            findings.append(CategoryFinding(
                validator_id=VALIDATOR_ID,
                path=d.path,
                severity="HIGH",
                message="Document has no owner assigned",
                rule="OWNERSHIP_REQUIRED",
            ))
    return findings
