"""STATE-001: a document that declares state machine content (`##
State machine` / `state_machines` field) must also declare recovery
behaviour (`## Recovery` / `recovery` field) OR failure behaviour
(`## Failure modes` / `failure_behaviour` field). A state machine
without any documented recovery or failure path is a genuine
specification gap: every real state machine has failure states."""
from __future__ import annotations

import networkx as nx

from ...metadata.models import DocumentMetadata
from ..base import CategoryFinding

VALIDATOR_ID = "STATE-001"
CATEGORY = "state_machine"


def run(docs: list[DocumentMetadata], graph: nx.DiGraph) -> list[CategoryFinding]:
    findings: list[CategoryFinding] = []
    for d in docs:
        if d.state_machines and not (d.recovery or d.failure_behaviour):
            findings.append(CategoryFinding(
                validator_id=VALIDATOR_ID,
                path=d.path,
                severity="MEDIUM",
                message="Declares state machine content but no recovery or failure-behaviour section",
                rule="STATE_MACHINE_HAS_RECOVERY_PATH",
            ))
    return findings
