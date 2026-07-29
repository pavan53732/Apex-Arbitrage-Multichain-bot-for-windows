"""EVENT-001, EVENT-002: event-contract validators.

EVENT-001: every event a document declares in `events_consumed` should
be produced by at least one document somewhere in the corpus (an event
with no producer is either a documentation gap or a naming
inconsistency).

EVENT-002: no event name may be declared as both produced AND consumed
by the exact same document (a document cannot be its own sole producer/
consumer of the same event with no other participant -- this usually
indicates a copy-paste error in the `## Events Produced` / `## Events
Consumed` sections).

These are genuinely useful checks even though today's corpus has 0
documents with parseable events_produced/events_consumed fields (a
data-completeness gap documented and NOT descoped -- see
_reconciliation/RECONCILIATION-REPORT.md); the checks themselves are
real and become active as soon as any document's metadata populates
these fields, with test fixtures proving correctness now rather than
being aspirational.
"""
from __future__ import annotations

import networkx as nx

from ...metadata.models import DocumentMetadata
from ..base import CategoryFinding

CATEGORY = "event"


def run(docs: list[DocumentMetadata], graph: nx.DiGraph) -> list[CategoryFinding]:
    findings: list[CategoryFinding] = []
    all_produced: set[str] = set()
    for d in docs:
        all_produced.update(d.events_produced)

    for d in docs:
        # EVENT-001: every consumed event must have a producer somewhere.
        for ev in d.events_consumed:
            if ev not in all_produced:
                findings.append(CategoryFinding(
                    validator_id="EVENT-001",
                    path=d.path,
                    severity="MEDIUM",
                    message=f"Consumes event '{ev}' which no document declares producing",
                    rule="EVENT_HAS_PRODUCER",
                ))
        # EVENT-002: a single document cannot both produce and consume
        # the exact same event name.
        both = set(d.events_produced) & set(d.events_consumed)
        for ev in both:
            findings.append(CategoryFinding(
                validator_id="EVENT-002",
                path=d.path,
                severity="LOW",
                message=f"Document both produces and consumes the same event: '{ev}'",
                rule="EVENT_NOT_SELF_PRODUCED_AND_CONSUMED",
            ))
    return findings
