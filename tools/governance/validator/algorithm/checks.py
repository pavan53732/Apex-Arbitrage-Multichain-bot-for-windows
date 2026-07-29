"""ALGORITHM-001 (category required by readiness_checklist.json
CHECK-WS3; not itself one of validator_catalogue.json's 14 frozen IDs,
which allocates algorithm-adjacent concerns under GRAPH-001/STATE-001
instead -- this category directory is still required standalone by the
checklist, so it is implemented here with its own genuinely useful
check rather than left as an empty stub directory).

Checks that a document whose purpose/scope text claims to define an
"algorithm" (explicit scoring formulas, decision trees, routing/ranking
logic -- the corpus's TRADING-ENGINE.md, ROUTING-ENGINE.md, RISK-ENGINE.md
being the clearest examples) declares non-empty `## Validation` content:
an algorithm with no documented validation/acceptance criteria cannot be
tested for correctness.
"""
from __future__ import annotations

import networkx as nx

from ...metadata.models import DocumentMetadata
from ..base import CategoryFinding

VALIDATOR_ID = "ALGORITHM-001"
CATEGORY = "algorithm"

ALGORITHM_KEYWORDS = [
    "algorithm", "scoring", "formula", "decision tree", "ranking", "routing logic",
]


def _claims_algorithm_content(doc: DocumentMetadata) -> bool:
    blob = " ".join([doc.purpose or "", doc.scope or ""]).lower()
    return any(kw in blob for kw in ALGORITHM_KEYWORDS)


def run(docs: list[DocumentMetadata], graph: nx.DiGraph) -> list[CategoryFinding]:
    findings: list[CategoryFinding] = []
    for d in docs:
        if _claims_algorithm_content(d) and not d.validation:
            findings.append(CategoryFinding(
                validator_id=VALIDATOR_ID,
                path=d.path,
                severity="MEDIUM",
                message="Purpose/scope claims algorithmic content (scoring/formula/routing logic) but declares no Validation section",
                rule="ALGORITHM_HAS_VALIDATION_CRITERIA",
            ))
    return findings
