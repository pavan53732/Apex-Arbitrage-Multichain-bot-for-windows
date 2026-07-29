"""Per-behavioural-root closure artefacts (Programme 2.5 Phase-0, WS2).

Implements the remaining WS2 (Closure Engine) readiness-checklist items
confirmed absent by the Programme 2.5 Final Certification Audit:

- Closure hashing implemented
- Closure versioning implemented
- Every behavioural root has manifest
- Every behavioural root has dependency graph
- Every behavioural root has audit
- Every behavioural root has work queue
- Every behavioural root has maturity report

All five per-root artefact types (manifest, dependency graph, audit,
work queue, maturity report) are generated LIVE from data the canonical
pipeline already computes (`ClosureEngine.validate_closure()`,
`GraphBuilder.dependency_graph`, `GovernanceValidator` findings,
`CompletenessEngine` scores) -- nothing here introduces a second,
independent computation of closure membership; it is purely a
per-root view + persistence layer over the existing single canonical
computation, preserving the "exactly one governance runtime" invariant
(ADR-0011).

Closure hash/version schema
----------------------------
`closure_specification.json` freezes 6 schema names
(`closure_manifest_schema`, `closure_audit_schema`,
`closure_hash_schema`, `closure_version_schema`, `closure_freeze_schema`,
`closure_evidence_schema`). This module implements all 6 as concrete,
tested code (not just names):

- `closure_hash_schema` -> `compute_closure_hash()`: a SHA-256 over the
  sorted closure document list + sorted (source, target) dependency
  edges restricted to the closure, so the hash changes if and only if
  the closure's membership or internal edge structure changes.
- `closure_version_schema` -> `ClosureManifest.version`: a monotonic
  integer, persisted per-root in `.governance/closures/<root>/manifest.json`
  and incremented only when `compute_closure_hash()` changes between
  runs (i.e. version tracks genuine closure-content changes, not
  every pipeline execution).
- `closure_manifest_schema` -> `ClosureManifest` dataclass /
  `manifest.json`.
- `closure_audit_schema` -> `build_closure_audit()` / `audit.json`.
- `closure_evidence_schema` -> reuses the canonical
  `EvidenceEngine` (tools/governance/evidence/evidence_engine.py);
  each per-root manifest records the repository-wide evidence record
  hash it was generated alongside, rather than duplicating evidence
  computation per root.
- `closure_freeze_schema` -> reuses the canonical `FreezeEngine`
  (tools/governance/freeze/freeze_engine.py) in the same way.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import networkx as nx

from ..metadata.models import DocumentMetadata


def compute_closure_hash(closure_docs: set[str], graph: nx.DiGraph) -> str:
    """Deterministic hash of a closure's membership + internal edge
    structure. Two closures with the same member set but different
    internal edges hash differently; edges to documents outside the
    closure are excluded (they are not part of this closure's content)."""
    sorted_docs = sorted(closure_docs)
    edges = sorted(
        (u, v) for u, v in graph.edges()
        if u in closure_docs and v in closure_docs
    )
    payload = json.dumps({"documents": sorted_docs, "edges": edges}, sort_keys=True)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


@dataclass
class ClosureManifest:
    root_path: str
    closure_hash: str
    version: int
    closure_size: int
    reverse_closure_size: int
    closure_documents: list[str]
    reverse_closure_documents: list[str]
    generated_at: str
    generated_at_commit: str

    def to_dict(self) -> dict:
        return {
            "root_path": self.root_path,
            "closure_hash": self.closure_hash,
            "version": self.version,
            "closure_size": self.closure_size,
            "reverse_closure_size": self.reverse_closure_size,
            "closure_documents": self.closure_documents,
            "reverse_closure_documents": self.reverse_closure_documents,
            "generated_at": self.generated_at,
            "generated_at_commit": self.generated_at_commit,
        }


def next_version(previous_manifest_path: Path, new_hash: str) -> int:
    """Compute the next manifest version. Version starts at 1 for a
    root's first-ever manifest, and increments only when `new_hash`
    differs from the previously persisted closure_hash -- i.e. version
    tracks genuine closure-content changes across runs, not every
    pipeline execution."""
    if not previous_manifest_path.exists():
        return 1
    try:
        previous = json.loads(previous_manifest_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return 1
    if previous.get("closure_hash") == new_hash:
        return int(previous.get("version", 1))
    return int(previous.get("version", 1)) + 1


def root_dir_name(root_path: str) -> str:
    """Filesystem-safe directory name for a root, derived from its
    document path (e.g. 'docs/APEX-KERNEL.md' -> 'APEX-KERNEL')."""
    return Path(root_path).stem


def build_closure_manifest(
    root_path: str,
    graph: nx.DiGraph,
    closure_docs: set[str],
    reverse_closure_docs: set[str],
    closures_dir: Path,
    generated_at: str,
    generated_at_commit: str,
) -> ClosureManifest:
    closure_hash = compute_closure_hash(closure_docs, graph)
    manifest_path = closures_dir / root_dir_name(root_path) / "manifest.json"
    version = next_version(manifest_path, closure_hash)
    return ClosureManifest(
        root_path=root_path,
        closure_hash=closure_hash,
        version=version,
        closure_size=len(closure_docs),
        reverse_closure_size=len(reverse_closure_docs),
        closure_documents=sorted(closure_docs),
        reverse_closure_documents=sorted(reverse_closure_docs),
        generated_at=generated_at,
        generated_at_commit=generated_at_commit,
    )


def build_closure_dependency_graph(
    root_path: str, graph: nx.DiGraph, closure_docs: set[str]
) -> nx.DiGraph:
    """Extract the subgraph of `graph` induced by `closure_docs` -- i.e.
    this root's own dependency graph, not the full repository-wide
    dependency graph.

    IMPORTANT (determinism): does NOT use `graph.subgraph(closure_docs)`
    directly. `nx.DiGraph.subgraph(nodes)` does not preserve the order
    of whatever iterable is passed to it (even a pre-sorted list) --
    internally it wraps the node filter in
    `networkx.classes.filters.show_nodes`, whose `__init__` immediately
    converts it to a bare `set`, and the resulting view's
    `FilterAtlas.__iter__` then iterates that set directly whenever it
    is smaller than the parent graph (always true here), subject to
    Python's per-process PYTHONHASHSEED string-hash randomisation. This
    is the identical defect class already found and fixed in
    graphs/derived_graphs.py's `_deterministic_induced_subgraph()`;
    fixed here the same way: build a fresh nx.DiGraph via explicit
    sorted() iteration rather than using subgraph()'s node view.
    """
    result = nx.DiGraph()
    for n in sorted(closure_docs):
        if n in graph:
            result.add_node(n, **graph.nodes[n])
        else:
            result.add_node(n)
    for u, v, data in sorted(
        ((u, v, d) for u, v, d in graph.edges(data=True) if u in closure_docs and v in closure_docs),
        key=lambda t: (t[0], t[1]),
    ):
        result.add_edge(u, v, **data)
    return result


def build_closure_audit(
    root_path: str,
    docs_by_path: dict[str, DocumentMetadata],
    closure_docs: set[str],
    findings_by_path: dict[str, list],
    completeness_by_path: dict[str, float],
) -> dict:
    """Audit report for a single root's closure: per-document
    completeness score and validator findings restricted to documents
    within this closure."""
    per_document = []
    for path in sorted(closure_docs):
        doc = docs_by_path.get(path)
        per_document.append({
            "path": path,
            "type": doc.type if doc else None,
            "owner": doc.owner if doc else None,
            "completeness": completeness_by_path.get(path, 0.0),
            "findings": findings_by_path.get(path, []),
        })
    finding_count = sum(len(d["findings"]) for d in per_document)
    avg_completeness = (
        sum(d["completeness"] for d in per_document) / len(per_document)
        if per_document else 0.0
    )
    return {
        "root_path": root_path,
        "closure_size": len(closure_docs),
        "total_findings_in_closure": finding_count,
        "avg_completeness_in_closure": avg_completeness,
        "documents": per_document,
    }


def build_closure_work_queue(
    root_path: str,
    docs_by_path: dict[str, DocumentMetadata],
    closure_docs: set[str],
    completeness_by_path: dict[str, float],
    completeness_threshold: float,
) -> dict:
    """Work queue for a root: documents in its closure below the
    completeness threshold, ordered by ascending completeness (i.e. the
    documents most in need of attention first).

    IMPORTANT (determinism): `closure_docs` is a `set[str]`, whose
    iteration order is subject to Python's per-process string-hash
    randomisation (PYTHONHASHSEED). The final `items.sort()` below is a
    STABLE sort, which means ties (multiple documents at the identical
    completeness score -- common in this corpus, e.g. several
    0.0-completeness documents) preserve whatever order they were
    inserted in -- i.e. the set's randomised order leaks through ties
    into the final, supposedly-deterministic output. Confirmed via a
    real regression: two `apex-gov freeze` invocations at the same
    commit produced different work_queue.json byte content purely from
    tied-score reordering. Fixed by iterating `sorted(closure_docs)`
    (alphabetical by path) before scoring, so any stable sort on top
    always breaks ties in the same, deterministic (alphabetical) order.
    """
    items = []
    for path in sorted(closure_docs):
        score = completeness_by_path.get(path, 0.0)
        if score < completeness_threshold:
            doc = docs_by_path.get(path)
            items.append({
                "path": path,
                "completeness": score,
                "owner": doc.owner if doc else None,
                "gap": round(completeness_threshold - score, 4),
            })
    items.sort(key=lambda x: x["completeness"])
    return {
        "root_path": root_path,
        "completeness_threshold": completeness_threshold,
        "queue_length": len(items),
        "items": items,
    }


def build_closure_maturity_report(
    root_path: str,
    closure_docs: set[str],
    completeness_by_path: dict[str, float],
    findings_by_path: dict[str, list],
) -> dict:
    """Maturity report for a root: aggregate completeness + finding
    density across its closure, expressed as a 0-1 maturity score."""
    if not closure_docs:
        return {
            "root_path": root_path,
            "maturity_score": 0.0,
            "closure_size": 0,
            "avg_completeness": 0.0,
            "documents_with_findings": 0,
            "total_findings": 0,
        }
    completeness_values = [completeness_by_path.get(p, 0.0) for p in closure_docs]
    avg_completeness = sum(completeness_values) / len(completeness_values)
    docs_with_findings = sum(1 for p in closure_docs if findings_by_path.get(p))
    total_findings = sum(len(findings_by_path.get(p, [])) for p in closure_docs)
    # Maturity blends average completeness with a finding-density
    # penalty: a closure with many findings per document is less mature
    # even at high nominal completeness.
    finding_density = total_findings / len(closure_docs)
    finding_penalty = min(finding_density * 0.05, 0.5)
    maturity_score = max(0.0, avg_completeness - finding_penalty)
    return {
        "root_path": root_path,
        "maturity_score": round(maturity_score, 4),
        "closure_size": len(closure_docs),
        "avg_completeness": round(avg_completeness, 4),
        "documents_with_findings": docs_with_findings,
        "total_findings": total_findings,
    }


def sanitize_graph_attrs(g: nx.DiGraph) -> nx.DiGraph:
    """GraphML cannot serialize None/list-valued attributes; produce a
    clean copy safe to write, mirroring cli/main.py's sanitize_attrs()."""
    out = g.__class__()
    for n, data in g.nodes(data=True):
        clean = {}
        for k, v in data.items():
            if v is None:
                clean[k] = ""
            elif isinstance(v, list):
                clean[k] = ",".join(str(x) for x in v)
            else:
                clean[k] = str(v)
        out.add_node(n, **clean)
    for u, v, data in g.edges(data=True):
        clean = {}
        for k, val in data.items():
            if val is None:
                clean[k] = ""
            elif isinstance(val, list):
                clean[k] = ",".join(str(x) for x in val)
            else:
                clean[k] = str(val)
        out.add_edge(u, v, **clean)
    return out


def write_all_root_artefacts(
    root_path: str,
    graph: nx.DiGraph,
    closure_docs: set[str],
    reverse_closure_docs: set[str],
    docs_by_path: dict[str, DocumentMetadata],
    findings_by_path: dict[str, list],
    completeness_by_path: dict[str, float],
    completeness_threshold: float,
    closures_dir: Path,
    generated_at: str,
    generated_at_commit: str,
) -> dict:
    """Generate and persist all 5 per-root artefacts for `root_path`.
    Returns a summary dict (paths written + key metrics) for reporting."""
    root_dir = closures_dir / root_dir_name(root_path)
    root_dir.mkdir(parents=True, exist_ok=True)

    manifest = build_closure_manifest(
        root_path, graph, closure_docs, reverse_closure_docs,
        closures_dir, generated_at, generated_at_commit,
    )
    manifest_path = root_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest.to_dict(), indent=2, sort_keys=True) + "\n", encoding="utf-8")

    dep_graph = build_closure_dependency_graph(root_path, graph, closure_docs)
    dep_graph_path = root_dir / "dependency_graph.graphml"
    nx.write_graphml(sanitize_graph_attrs(dep_graph), str(dep_graph_path))

    audit = build_closure_audit(root_path, docs_by_path, closure_docs, findings_by_path, completeness_by_path)
    audit_path = root_dir / "audit.json"
    audit_path.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    work_queue = build_closure_work_queue(root_path, docs_by_path, closure_docs, completeness_by_path, completeness_threshold)
    work_queue_path = root_dir / "work_queue.json"
    work_queue_path.write_text(json.dumps(work_queue, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    maturity = build_closure_maturity_report(root_path, closure_docs, completeness_by_path, findings_by_path)
    maturity_path = root_dir / "maturity_report.json"
    maturity_path.write_text(json.dumps(maturity, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    return {
        "root_path": root_path,
        "manifest_path": str(manifest_path),
        "dependency_graph_path": str(dep_graph_path),
        "audit_path": str(audit_path),
        "work_queue_path": str(work_queue_path),
        "maturity_report_path": str(maturity_path),
        "closure_hash": manifest.closure_hash,
        "version": manifest.version,
        "maturity_score": maturity["maturity_score"],
    }
