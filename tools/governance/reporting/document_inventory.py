"""Canonical Document Inventory — Repository Canonicality Repair, Work Item 9.

Produces exactly ONE inventory view, composed entirely from canonical
runtime outputs (indexer, metadata parser, root detector, closure engine,
validator registry) — it does not re-derive or duplicate any of their
logic, and it does not introduce a second competing document export.
`export_documents_json()` (tools/governance/storage/json_export.py)
remains the canonical raw per-document metadata export; this module adds
the specific derived fields the Repository Canonicality Repair directive
requested (Document ID, Category, Behavioural Root flag, Closure size,
Validator coverage, Graph node/edge degree, Dependencies, Consumers) as a
read-only, regenerable *view* on top of it.

Competing-inventory check: prior to this repair, four other "inventory"
files existed (`complete_repository_inventory.json`, `file_inventory.json`,
`behavioural_root_registry.json`, `programme3_execution_plan.json`), all
produced by tooling that no longer exists, all disagreeing with the
canonical runtime's live counts. They have been archived — see
`.governance/archive/pre-consolidation-2026-07-29/ARCHIVE-MANIFEST.md`.
This module's output (`.governance/exports/document_inventory.json`) is
now the only enriched inventory view, alongside the one raw export
(`.governance/exports/documents.json`).
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml


def build_document_inventory(repo_root: Path, config_path: str = "tools/governance/config/governance.yaml") -> list[dict[str, Any]]:
    from ..indexer.repo_indexer import RepoIndexer
    from ..parser.markdown_parser import MarkdownParser
    from ..metadata.metadata_parser import MetadataParser
    from ..graphs.graph_builder import GraphBuilder
    from ..closure.closure_engine import BehaviouralRootDetector, ClosureEngine

    cfg = yaml.safe_load((repo_root / config_path).read_text(encoding="utf-8"))

    indexer = RepoIndexer(str(repo_root), cfg["docs_globs"])
    md_parser = MarkdownParser(str(repo_root))
    meta_parser = MetadataParser()
    graph_builder = GraphBuilder()

    docs = []
    for item in indexer.build_inventory():
        parsed = md_parser.parse_file(item["path"])
        meta = meta_parser.parse_document(parsed["raw_text"], item["path"])
        docs.append(meta)
        graph_builder.add_document(meta)

    root_detector = BehaviouralRootDetector(cfg["behavioural_root_signals"])
    roots = root_detector.detect_roots(docs)
    root_paths = {r.path for r in roots}

    closure_engine = ClosureEngine(graph_builder.dependency_graph)
    closures = {r.path: closure_engine.compute_closure(r.path) for r in roots}

    # Consumers: documents that depend_on / required_by this one, i.e.
    # reverse edges in the dependency graph. Sorted for determinism.
    reverse_deps: dict[str, list[str]] = {}
    for d in docs:
        for dep in d.depends_on:
            reverse_deps.setdefault(dep, []).append(d.path)

    doc_graph = graph_builder.doc_graph
    dep_graph = graph_builder.dependency_graph

    try:
        from ..validator.registry import list_validators
        validator_ids = sorted(v.id for v in list_validators())
    except ImportError:
        validator_ids = []

    inventory = []
    for idx, d in enumerate(sorted(docs, key=lambda x: x.path), start=1):
        is_root = d.path in root_paths
        closure = closures.get(d.path)
        inventory.append({
            "document_id": f"DOC-{idx:04d}",
            "path": d.path,
            "type": d.type,
            "owner": d.owner,
            "status": d.status,
            "version": d.version,
            "category": _categorize(d.path),
            "behavioural_root": is_root,
            "closure_size": len(closure) if closure is not None else None,
            # NOTE on validator_coverage / evidence: every validator in the
            # Validator Registry (Work Item 7) operates over the whole
            # document corpus at once (e.g. cycle detection, cross-reference
            # checking) rather than being independently scoped to a single
            # document. There is currently no per-document validator result
            # granularity in the canonical runtime. Rather than fabricate a
            # false per-document PASS/FAIL, this field honestly lists which
            # corpus-wide validators *apply to* this document (all of them,
            # for every document, today) and points at the evidence record
            # that covers the run in which this inventory was generated.
            "validator_coverage": validator_ids,
            "evidence_reference": ".governance/evidence/evidence_latest.json",
            "graph_node_present": doc_graph.has_node(d.path),
            "graph_out_edges": dep_graph.out_degree(d.path) if dep_graph.has_node(d.path) else 0,
            "graph_in_edges": dep_graph.in_degree(d.path) if dep_graph.has_node(d.path) else 0,
            "dependencies": sorted(d.depends_on),
            "consumers": sorted(reverse_deps.get(d.path, [])),
        })

    return inventory


def _categorize(path: str) -> str:
    """Coarse category derived purely from path structure (no new
    classification logic beyond directory/naming conventions already used
    elsewhere in the repository, e.g. docs/adr/, docs/ai-orchestration/)."""
    if path.startswith("docs/adr/"):
        return "ADR"
    if path.startswith("docs/ai-orchestration/"):
        return "AI-ORCHESTRATION-CONTRACT"
    if path.startswith("docs/"):
        return "DOCS"
    if "/" not in path:
        return "ROOT-GATE"
    return "OTHER"


def save_document_inventory(repo_root: Path, output_path: Path, config_path: str = "tools/governance/config/governance.yaml") -> int:
    inventory = build_document_inventory(repo_root, config_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(inventory, indent=2), encoding="utf-8")
    return len(inventory)
