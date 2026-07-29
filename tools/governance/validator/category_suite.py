"""Orchestrates all 14 category validators (WS3 Validator Framework)
against the single canonical pipeline's already-computed inputs.

This module is the ONLY place that assembles the shared inputs (docs,
graph, root_paths, closures_by_root, schemas_dir, freeze_records) and
dispatches them to each category validator's `run()` -- preserving the
single-canonical-computation invariant (ADR-0011): no category
validator recomputes indexing, parsing, root detection, or closures
itself.

Produces evidence: `run_category_validators()`'s return value is
written to `.governance/exports/category_validator_findings.json` by
the CLI, satisfying "Every validator produces evidence" for all 14
categories (distinct from GovernanceValidator's findings, and distinct
from architecture-tests' stdout-only evidence).
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import networkx as nx

from ..metadata.models import DocumentMetadata
from .base import CategoryFinding
from .ownership.checks import run as run_ownership
from .dependency.checks import run as run_dependency
from .event.checks import run as run_event
from .schema.checks import run as run_schema
from .interface.checks import run as run_interface
from .state_machine.checks import run as run_state_machine
from .recovery.checks import run as run_recovery
from .security.checks import run as run_security
from .configuration.checks import run as run_configuration
from .graph.checks import run as run_graph
from .freeze.checks import run as run_freeze
from .algorithm.checks import run as run_algorithm
from .metadata.checks import run as run_metadata
from .closure.checks import run as run_closure

CATEGORY_ORDER = [
    "ownership", "dependency", "event", "schema", "interface",
    "state_machine", "recovery", "security", "configuration", "graph",
    "freeze", "algorithm", "metadata", "closure",
]

# 14 validator IDs from validator_catalogue.json, mapped to the category
# directory that implements them, for cross-reference/reporting.
CATALOGUE_ID_TO_CATEGORY = {
    "OWNERSHIP-001": "ownership",
    "DEPENDENCY-001": "dependency",
    "DEPENDENCY-002": "dependency",
    "EVENT-001": "event",
    "EVENT-002": "event",
    "SCHEMA-001": "schema",
    "SCHEMA-002": "schema",
    "INTERFACE-001": "interface",
    "STATE-001": "state_machine",
    "RECOVERY-001": "recovery",
    "SECURITY-001": "security",
    "CONFIG-001": "configuration",
    "GRAPH-001": "graph",
    "FREEZE-001": "freeze",
}


def run_category_validators(
    docs: list[DocumentMetadata],
    graph: nx.DiGraph,
    root_paths: set[str],
    closures_by_root: dict[str, set[str]],
    schemas_dir: Path | None,
    freeze_records: list[dict],
    repo_root: Path,
) -> dict[str, Any]:
    findings_by_category: dict[str, list[CategoryFinding]] = {}

    findings_by_category["ownership"] = run_ownership(docs, graph)
    findings_by_category["dependency"] = run_dependency(docs, graph)
    findings_by_category["event"] = run_event(docs, graph)
    findings_by_category["schema"] = run_schema(docs, graph, schemas_dir=schemas_dir)
    findings_by_category["interface"] = run_interface(docs, graph)
    findings_by_category["state_machine"] = run_state_machine(docs, graph)
    findings_by_category["recovery"] = run_recovery(docs, graph, root_paths=root_paths)
    findings_by_category["security"] = run_security(docs, graph, root_paths=root_paths)
    findings_by_category["configuration"] = run_configuration(docs, graph)
    findings_by_category["graph"] = run_graph(docs, graph, root_paths=root_paths)
    findings_by_category["freeze"] = run_freeze(docs, graph, freeze_records=freeze_records, repo_root=repo_root)
    findings_by_category["algorithm"] = run_algorithm(docs, graph)
    findings_by_category["metadata"] = run_metadata(docs, graph)
    findings_by_category["closure"] = run_closure(docs, graph, closures_by_root=closures_by_root)

    total_findings = sum(len(v) for v in findings_by_category.values())
    return {
        "categories_executed": CATEGORY_ORDER,
        "total_categories": len(CATEGORY_ORDER),
        "total_findings": total_findings,
        "findings_by_category": {
            cat: [f.to_dict() for f in findings]
            for cat, findings in findings_by_category.items()
        },
        "finding_counts_by_category": {cat: len(v) for cat, v in findings_by_category.items()},
        "catalogue_id_to_category": CATALOGUE_ID_TO_CATEGORY,
    }


def save_category_validator_report(report: dict[str, Any], path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path
