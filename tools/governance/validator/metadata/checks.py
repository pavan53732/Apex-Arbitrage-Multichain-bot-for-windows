"""METADATA-001 (category required by readiness_checklist.json
CHECK-WS3). Checks that every document has all 4 required front-matter
fields (type, owner, status, version) populated -- delegates the
required-field list to `MetadataParser.REQUIRED_FIELDS` (the single
source of truth for which fields are required) rather than
hard-coding a second copy of that list here.
"""
from __future__ import annotations

import networkx as nx

from ...metadata.metadata_parser import MetadataParser
from ...metadata.models import DocumentMetadata
from ..base import CategoryFinding

VALIDATOR_ID = "METADATA-001"
CATEGORY = "metadata"


def run(docs: list[DocumentMetadata], graph: nx.DiGraph) -> list[CategoryFinding]:
    findings: list[CategoryFinding] = []
    for d in docs:
        for field in MetadataParser.REQUIRED_FIELDS:
            if getattr(d, field, None) in (None, ""):
                findings.append(CategoryFinding(
                    validator_id=VALIDATOR_ID,
                    path=d.path,
                    severity="HIGH",
                    message=f"Missing required metadata field: {field}",
                    rule="REQUIRED_METADATA_FIELD_PRESENT",
                ))
    return findings
