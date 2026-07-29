"""Shared base for the 14 category validators (Programme 2.5 Phase-0,
WS3 Validator Framework).

`validator_catalogue.json` freezes 14 validator IDs organised by
category (`OWNERSHIP-001`, `DEPENDENCY-001/002`, `EVENT-001/002`,
`SCHEMA-001/002`, `INTERFACE-001`, `STATE-001`, `RECOVERY-001`,
`SECURITY-001`, `CONFIG-001`, `GRAPH-001`, `FREEZE-001`) and
`readiness_checklist.json` CHECK-WS3 requires 14 corresponding
`validator/<category>/` subdirectories, each independently executable,
tested, and evidence-producing.

Every category validator in `validator/<category>/checks.py` implements
this `CategoryValidator` protocol: a `run(docs, graph)` method that
returns a list of `CategoryFinding`, operating ONLY on data the
canonical pipeline already parses (`DocumentMetadata`, the dependency
graph) -- no category validator performs its own document indexing or
parsing, preserving the single-canonical-runtime invariant (ADR-0011).

Each category validator is independently importable and callable
without depending on any other category validator or on
`GovernanceValidator` -- this is what makes "every validator
independently executable" true in a literal, testable sense (each has
its own `test_<category>.py` that constructs minimal `DocumentMetadata`
fixtures and calls `run()` directly, with no dependency on a full
`apex-gov run` pipeline execution).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

import networkx as nx

from ..metadata.models import DocumentMetadata


@dataclass(frozen=True)
class CategoryFinding:
    validator_id: str
    path: str
    severity: str  # CRITICAL | HIGH | MEDIUM | LOW | INFO
    message: str
    rule: str

    def to_dict(self) -> dict:
        return {
            "validator_id": self.validator_id,
            "path": self.path,
            "severity": self.severity,
            "message": self.message,
            "rule": self.rule,
        }


class CategoryValidator(Protocol):
    validator_id: str
    category: str

    def run(self, docs: list[DocumentMetadata], graph: nx.DiGraph) -> list[CategoryFinding]:
        ...
