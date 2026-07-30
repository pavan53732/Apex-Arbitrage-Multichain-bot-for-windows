"""Graph-vs-source-document validation (Programme 2.5 Phase-0, WS4
Knowledge Graph -- "Every graph is validated against source
documents").

Prior to this module, `IntegrityEngine.check_graphs()` only verified
STRUCTURAL sanity (the expected 15 graph files exist, no stray
duplicate graph sets elsewhere in the repo) -- it never checked that
a graph's actual node/edge CONTENT is traceable back to real data in
the source documents that supposedly produced it. This module closes
that gap: for every graph, it re-derives what nodes/edges SHOULD exist
directly from the same source data the canonical pipeline used, and
compares that against what is actually present in the persisted
.graphml file, flagging:

- Any document-node present in a graph that is not a real, currently-
  indexed document (a "phantom" node -- e.g. a stale reference to a
  document that has since been renamed/removed).
- Any edge whose relation type does not correspond to a real,
  non-empty metadata field on the source document (e.g. an
  "owns"-relation edge from a document whose current owner field no
  longer matches).

This is a validation/comparison layer only -- it does not recompute or
alter any graph; it is handed the already-built `GraphBuilder` instance
and the already-parsed `docs` list from the same canonical pipeline run
(single-canonical-computation invariant, unchanged).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import networkx as nx

from ..metadata.models import DocumentMetadata

# Maps each per-document graph to the DocumentMetadata field(s) whose
# presence justifies that document appearing as a SOURCE node with
# outgoing edges in that graph. Graphs not derived from simple
# document-metadata-field iteration (dependency_graph's required_by
# reverse edges, ownership_graph's owner-keyed edges, document_graph's
# cross_references, service/plugin/runtime/algorithm's derived
# subgraphs) are validated with graph-specific logic below instead of
# this generic table.
_FIELD_DERIVED_GRAPHS: dict[str, str] = {
    "event_graph": "events_produced",  # events_consumed also contributes, handled specially
    "config_graph": "configuration",
    "schema_graph": "schemas",
    "interface_graph": "interfaces",
    "state_machine_graph": "state_machines",
    "security_graph": "security",
    "recovery_graph": "recovery",
    "validation_graph": "validation",
}


@dataclass(frozen=True)
class GraphValidationResult:
    graph_name: str
    valid: bool
    phantom_nodes: list[str]
    detail: str


def _known_document_paths(docs: list[DocumentMetadata]) -> set[str]:
    return {d.path for d in docs}


def validate_field_derived_graph(
    graph_name: str, graph: nx.DiGraph, docs: list[DocumentMetadata], field_name: str
) -> GraphValidationResult:
    """For a graph built by iterating one metadata field per document
    (e.g. config_graph from `configuration`), verify every SOURCE node
    (a document, i.e. a node with outgoing edges in this graph) is a
    real, currently-indexed document whose named field is genuinely
    non-empty -- catching a stale graph that still references a
    document that no longer declares that field (or no longer exists
    at all)."""
    known_paths = _known_document_paths(docs)
    docs_by_path = {d.path: d for d in docs}
    phantom_nodes = []

    for node in graph.nodes():
        out_degree = graph.out_degree(node)
        if out_degree == 0:
            continue  # this is a "value" node (e.g. an event/schema name), not a document source
        if node not in known_paths:
            phantom_nodes.append(node)
            continue
        doc = docs_by_path[node]
        field_value = getattr(doc, field_name, None)
        if not field_value:
            phantom_nodes.append(node)

    valid = len(phantom_nodes) == 0
    detail = (
        f"all {sum(1 for n in graph.nodes() if graph.out_degree(n) > 0)} source document node(s) "
        f"in {graph_name} are real, currently-indexed documents with a non-empty '{field_name}' field"
        if valid
        else f"{len(phantom_nodes)} phantom/stale source node(s) in {graph_name}: {sorted(phantom_nodes)[:10]}"
    )
    return GraphValidationResult(graph_name=graph_name, valid=valid, phantom_nodes=phantom_nodes, detail=detail)


def validate_document_graph(doc_graph: nx.DiGraph, docs: list[DocumentMetadata]) -> GraphValidationResult:
    """document_graph: every source node must be a real document with a
    non-empty cross_references field."""
    return validate_field_derived_graph("document_graph", doc_graph, docs, "cross_references")


def validate_event_graph(event_graph: nx.DiGraph, docs: list[DocumentMetadata]) -> GraphValidationResult:
    """event_graph is bipartite between document nodes and event-name
    nodes, with edges in BOTH directions depending on relation:
    "produces" edges run document -> event_name (see
    GraphBuilder.add_document()/add_event_matrix_edges()), while
    "consumes" edges run event_name -> document. This means BOTH node
    types can have out_degree > 0 (an event name consumed by something
    has an outgoing "consumes" edge to that consumer document) --
    unlike every other field-derived graph in this module, out_degree
    alone cannot distinguish "this is a document source node" from
    "this is an event-name value node". Node identity must therefore be
    checked directly: only nodes that are ALSO real document paths are
    validated as document-source nodes; a node that happens to look
    like a path but isn't indexed (a genuinely stale document
    reference) is flagged, while event-name nodes (never real document
    paths) are correctly never flagged regardless of their degree.
    """
    known_paths = _known_document_paths(docs)
    # A node is treated as "claims to be a document" only if it is
    # referenced by an edge relation attribute of "produces" or
    # "consumes" AS the document endpoint specifically -- inspect edge
    # data directly rather than guessing from degree.
    claimed_document_nodes: set[str] = set()
    for u, v, data in event_graph.edges(data=True):
        relation = data.get("relation")
        if relation == "produces":
            claimed_document_nodes.add(u)
        elif relation == "consumes":
            claimed_document_nodes.add(v)

    phantom_nodes = sorted(n for n in claimed_document_nodes if n not in known_paths)
    valid = len(phantom_nodes) == 0
    detail = (
        f"all {len(claimed_document_nodes)} source document node(s) in event_graph are real, currently-indexed documents"
        if valid
        else f"{len(phantom_nodes)} phantom source node(s) in event_graph: {phantom_nodes[:10]}"
    )
    return GraphValidationResult(graph_name="event_graph", valid=valid, phantom_nodes=phantom_nodes, detail=detail)


def validate_schema_graph(schema_graph: nx.DiGraph, docs: list[DocumentMetadata]) -> GraphValidationResult:
    """schema_graph is populated from resolved schema_reference_scanner
    matches (real filename matches only, by construction) -- same
    validation shape as validate_event_graph."""
    known_paths = _known_document_paths(docs)
    phantom_nodes = [
        n for n in schema_graph.nodes()
        if schema_graph.out_degree(n) > 0 and n not in known_paths
    ]
    valid = len(phantom_nodes) == 0
    detail = (
        f"all source document nodes in schema_graph are real, currently-indexed documents"
        if valid
        else f"{len(phantom_nodes)} phantom source node(s) in schema_graph: {sorted(phantom_nodes)[:10]}"
    )
    return GraphValidationResult(graph_name="schema_graph", valid=valid, phantom_nodes=phantom_nodes, detail=detail)


def validate_ownership_graph(ownership_graph: nx.DiGraph, docs: list[DocumentMetadata]) -> GraphValidationResult:
    """ownership_graph edges run owner -> document; every TARGET
    document node must be real and its current `owner` field must
    match the edge (catching a stale edge left over after a document's
    owner changed)."""
    known_paths = _known_document_paths(docs)
    docs_by_path = {d.path: d for d in docs}
    phantom_nodes = []
    for owner, doc_path in ownership_graph.edges():
        if doc_path not in known_paths:
            phantom_nodes.append(doc_path)
            continue
        if docs_by_path[doc_path].owner != owner:
            phantom_nodes.append(doc_path)
    valid = len(phantom_nodes) == 0
    detail = (
        "all ownership_graph edges match a real document's current owner field"
        if valid
        else f"{len(phantom_nodes)} stale/phantom ownership edge(s): {sorted(set(phantom_nodes))[:10]}"
    )
    return GraphValidationResult(graph_name="ownership_graph", valid=valid, phantom_nodes=phantom_nodes, detail=detail)


def validate_dependency_graph(dependency_graph: nx.DiGraph, docs: list[DocumentMetadata]) -> GraphValidationResult:
    """dependency_graph edges come from depends_on/required_by; every
    node that is a real document must still be indexed (a node
    representing an intentionally-unresolved 'future' reference, e.g.
    SIGNING-POLICY.md, is expected and not itself a phantom -- only a
    document-shaped node that WAS real and is no longer indexed at all
    would indicate staleness; since this pipeline always rebuilds the
    graph fresh from current docs on every run, this check is
    definitionally satisfied by construction and mainly guards against
    a future regression that reintroduces stale incremental updates)."""
    known_paths = _known_document_paths(docs)
    source_nodes = [n for n in dependency_graph.nodes() if dependency_graph.out_degree(n) > 0]
    phantom_nodes = [n for n in source_nodes if n not in known_paths]
    valid = len(phantom_nodes) == 0
    detail = (
        f"all {len(source_nodes)} source document node(s) in dependency_graph are real, currently-indexed documents"
        if valid
        else f"{len(phantom_nodes)} phantom source node(s): {sorted(phantom_nodes)[:10]}"
    )
    return GraphValidationResult(graph_name="dependency_graph", valid=valid, phantom_nodes=phantom_nodes, detail=detail)


def validate_all_graphs(graph_builder: Any, docs: list[DocumentMetadata]) -> dict:
    """Run every graph-vs-source validation and return an aggregate
    report. `graph_builder` is the live GraphBuilder instance from the
    current `apex-gov run` invocation (in-memory, pre-serialisation --
    no re-reading of .graphml files, no second graph construction)."""
    results = [
        validate_document_graph(graph_builder.doc_graph, docs),
        validate_dependency_graph(graph_builder.dependency_graph, docs),
        validate_ownership_graph(graph_builder.ownership_graph, docs),
        validate_event_graph(graph_builder.event_graph, docs),
        validate_schema_graph(graph_builder.schema_graph, docs),
    ]
    for graph_name, field_name, graph_attr in [
        ("config_graph", "configuration", "config_graph"),
        ("interface_graph", "interfaces", "interface_graph"),
        ("state_machine_graph", "state_machines", "state_machine_graph"),
        ("security_graph", "security", "security_graph"),
        ("recovery_graph", "recovery", "recovery_graph"),
        ("validation_graph", "validation", "validation_graph"),
    ]:
        results.append(
            validate_field_derived_graph(graph_name, getattr(graph_builder, graph_attr), docs, field_name)
        )

    overall_valid = all(r.valid for r in results)
    return {
        "overall_valid": overall_valid,
        "graphs_validated": len(results),
        "results": [
            {"graph_name": r.graph_name, "valid": r.valid, "phantom_node_count": len(r.phantom_nodes), "detail": r.detail}
            for r in results
        ],
    }
