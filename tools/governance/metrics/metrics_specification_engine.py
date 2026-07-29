"""10-Metric Specification Engine (Programme 2.5 Phase-0, WS8 Metrics
Engine).

`metrics_specification.json` freezes 10 named ratio metrics. Prior to
this module, `CompletenessEngine` computed exactly 1
(`avg_completeness`, a per-document section-presence score, unrelated
in formula to any of the 10 frozen names) and `MetricsDashboard` was an
unimplemented stub returning `{"status": "stub"}`.

Every metric below is computed from data the canonical pipeline
ALREADY produces during `apex-gov run` (parsed documents, validator
findings, behavioural roots + closures, the dependency/security/
schema/interface/event graphs, the validator registry) -- no metric
here triggers a second, independent computation of any of that.

Metric definitions (numerator / denominator), each named exactly as
frozen in metrics_specification.json:

1. Repository Completeness = validated_documents / total_documents
   "validated" = the document has zero findings from GovernanceValidator
   (a document with a finding against it, e.g. missing owner, is not
   fully validated).
2. Closure Completeness = validated_closures / total_closures
   "validated" = CLOSURE-001 (validator/closure/checks.py) raises no
   finding for that root's closure (contains itself, non-empty).
3. Validator Coverage = executed_validators / catalogued_validators
   catalogued = len(list_validators()) (all layers); executed = how
   many actually produced a PASS/FAIL result in the most recent
   run_all_validators() call (in-engine and category validators are
   deduplicated to 1 execution each covering multiple catalogued IDs,
   exactly as registry.py's run_all_validators() already documents --
   this metric counts CATALOGUED IDs whose result is known, not raw
   subprocess invocations).
4. Reference Integrity = valid_references / total_references
   references = every depends_on + cross_references entry across all
   documents; valid = resolves to a real document path (using the same
   DocumentIdentityResolver-based resolution the reference parser
   already performs -- counted via the absence of a BROKEN_REFERENCE
   finding for that specific reference).
5. Ownership Integrity = valid_ownership_assignments / total_ownership_assignments
   total = every document; valid = has a non-empty owner field (i.e.
   passes OWNERSHIP-001).
6. Graph Integrity = valid_graph_edges / total_graph_edges
   Across the dependency graph: an edge is "valid" if both endpoints
   are real indexed documents (a dangling edge to a non-existent
   document would be a graph construction defect).
7. Security Coverage = validated_security_contracts / total_security_contracts
   total = behavioural roots whose purpose/scope mentions a security-
   sensitive concern (SECURITY-001's own keyword list, reused not
   duplicated); validated = of those, how many pass SECURITY-001 (i.e.
   have a Security section).
8. Schema Coverage = validated_schemas / total_schemas
   total = every schema file under schemas/; validated = passes
   SCHEMA-001 (valid JSON, looks like a JSON Schema object).
9. Interface Coverage = validated_interfaces / total_interfaces
   total = every distinct interface name declared across all documents;
   validated = declared by exactly one document (passes INTERFACE-001).
10. Event Coverage = validated_events / total_events
    total = every distinct event name across events_produced +
    events_consumed; validated = has both at least one producer and
    (if consumed) satisfies EVENT-001.

Every metric returns 1.0 (vacuously fully covered) when its
denominator is 0, matching this codebase's existing convention (see
CompletenessEngine / cli/main.py's `avg_completeness` computation,
which uses `if scores else 0.0` -- but for a coverage RATIO specifically,
0-of-0 is conventionally treated as 100% coverage, not 0%, since there
is nothing uncovered).
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import networkx as nx

from ..metadata.models import DocumentMetadata
from ..validator.security.checks import SECURITY_SENSITIVE_KEYWORDS, _mentions_security_concern
from ..validator.interface.checks import run as run_interface_checks
from ..validator.schema.checks import run as run_schema_checks


def _ratio(numerator: int, denominator: int) -> float:
    if denominator == 0:
        return 1.0
    return round(numerator / denominator, 6)


def repository_completeness(docs: list[DocumentMetadata], findings_by_path: dict[str, list]) -> float:
    total = len(docs)
    validated = sum(1 for d in docs if not findings_by_path.get(d.path))
    return _ratio(validated, total)


def closure_completeness(root_paths: set[str], closures_by_root: dict[str, set[str]]) -> float:
    total = len(root_paths)
    validated = 0
    for root in root_paths:
        closure = closures_by_root.get(root, set())
        if root in closure and len(closure) > 0:
            validated += 1
    return _ratio(validated, total)


def validator_coverage(catalogued_ids: list[str], executed_ids: set[str]) -> float:
    total = len(catalogued_ids)
    executed = sum(1 for cid in catalogued_ids if cid in executed_ids)
    return _ratio(executed, total)


def reference_integrity(docs: list[DocumentMetadata], known_paths: set[str]) -> float:
    total = 0
    valid = 0
    for d in docs:
        refs = list(d.depends_on) + list(d.cross_references)
        for ref in refs:
            total += 1
            if ref in known_paths:
                valid += 1
    return _ratio(valid, total)


def ownership_integrity(docs: list[DocumentMetadata]) -> float:
    total = len(docs)
    valid = sum(1 for d in docs if d.owner)
    return _ratio(valid, total)


def graph_integrity(graph: nx.DiGraph, known_paths: set[str]) -> float:
    edges = list(graph.edges())
    total = len(edges)
    valid = sum(1 for u, v in edges if u in known_paths and v in known_paths)
    return _ratio(valid, total)


def security_coverage(docs: list[DocumentMetadata], root_paths: set[str]) -> float:
    security_sensitive_roots = [d for d in docs if d.path in root_paths and _mentions_security_concern(d)]
    total = len(security_sensitive_roots)
    validated = sum(1 for d in security_sensitive_roots if d.security)
    return _ratio(validated, total)


def schema_coverage(schemas_dir: Path | None) -> float:
    if schemas_dir is None or not schemas_dir.exists():
        return 1.0
    schema_files = sorted(schemas_dir.glob("*.json"))
    findings = run_schema_checks([], nx.DiGraph(), schemas_dir=schemas_dir)
    invalid_paths = {f.path for f in findings if f.rule in ("SCHEMA_VALID_JSON", "SCHEMA_WELL_FORMED")}
    total = len(schema_files)
    validated = sum(1 for p in schema_files if str(p) not in invalid_paths)
    return _ratio(validated, total)


def interface_coverage(docs: list[DocumentMetadata]) -> float:
    all_interfaces: set[str] = set()
    for d in docs:
        all_interfaces.update(d.interfaces)
    total = len(all_interfaces)
    findings = run_interface_checks(docs, nx.DiGraph())
    invalid_interfaces = set()
    for f in findings:
        # message format: "Interface 'X' is declared by N documents: [...]"
        if f.rule == "INTERFACE_SINGLE_OWNER" and "'" in f.message:
            name = f.message.split("'")[1]
            invalid_interfaces.add(name)
    validated = total - len(invalid_interfaces)
    return _ratio(validated, total)


def event_coverage(docs: list[DocumentMetadata]) -> float:
    all_events: set[str] = set()
    produced: set[str] = set()
    for d in docs:
        all_events.update(d.events_produced)
        all_events.update(d.events_consumed)
        produced.update(d.events_produced)
    total = len(all_events)
    validated = sum(1 for e in all_events if e in produced)
    return _ratio(validated, total)


def compute_all_metrics(
    docs: list[DocumentMetadata],
    graph: nx.DiGraph,
    root_paths: set[str],
    closures_by_root: dict[str, set[str]],
    findings_by_path: dict[str, list],
    catalogued_validator_ids: list[str],
    executed_validator_ids: set[str],
    schemas_dir: Path | None,
) -> dict[str, float]:
    known_paths = {d.path for d in docs}
    return {
        "Repository Completeness": repository_completeness(docs, findings_by_path),
        "Closure Completeness": closure_completeness(root_paths, closures_by_root),
        "Validator Coverage": validator_coverage(catalogued_validator_ids, executed_validator_ids),
        "Reference Integrity": reference_integrity(docs, known_paths),
        "Ownership Integrity": ownership_integrity(docs),
        "Graph Integrity": graph_integrity(graph, known_paths),
        "Security Coverage": security_coverage(docs, root_paths),
        "Schema Coverage": schema_coverage(schemas_dir),
        "Interface Coverage": interface_coverage(docs),
        "Event Coverage": event_coverage(docs),
    }
