"""Tests for graph-vs-source-document validation (WS4: "Every graph is
validated against source documents" -- previously not implemented as a
distinct check beyond IntegrityEngine.check_graphs()'s structural
sanity)."""
import networkx as nx

from governance.graphs.graph_builder import GraphBuilder
from governance.graphs.graph_source_validator import (
    validate_all_graphs,
    validate_dependency_graph,
    validate_document_graph,
    validate_event_graph,
    validate_field_derived_graph,
    validate_ownership_graph,
    validate_schema_graph,
)
from governance.metadata.models import DocumentMetadata


def test_validate_field_derived_graph_passes_for_real_documents():
    docs = [DocumentMetadata(path="docs/A.md", configuration=["timeout"])]
    g = nx.DiGraph()
    g.add_edge("docs/A.md", "timeout")
    result = validate_field_derived_graph("config_graph", g, docs, "configuration")
    assert result.valid is True
    assert result.phantom_nodes == []


def test_validate_field_derived_graph_flags_document_no_longer_indexed():
    """A graph node representing a document that is no longer in the
    current `docs` list (e.g. renamed/removed) must be flagged as
    phantom."""
    docs: list[DocumentMetadata] = []  # docs/STALE.md no longer exists
    g = nx.DiGraph()
    g.add_edge("docs/STALE.md", "timeout")
    result = validate_field_derived_graph("config_graph", g, docs, "configuration")
    assert result.valid is False
    assert "docs/STALE.md" in result.phantom_nodes


def test_validate_field_derived_graph_flags_field_now_empty():
    """A graph edge exists but the document's CURRENT metadata no
    longer has that field populated -- e.g. content was edited to
    remove the configuration section without regenerating the graph."""
    docs = [DocumentMetadata(path="docs/A.md", configuration=[])]  # now empty
    g = nx.DiGraph()
    g.add_edge("docs/A.md", "timeout")  # stale edge from a prior run
    result = validate_field_derived_graph("config_graph", g, docs, "configuration")
    assert result.valid is False
    assert "docs/A.md" in result.phantom_nodes


def test_validate_field_derived_graph_ignores_value_nodes():
    """A 'value' node (e.g. the configuration key name itself) has no
    outgoing edges and must never be flagged, even though it is not a
    document path."""
    docs = [DocumentMetadata(path="docs/A.md", configuration=["timeout"])]
    g = nx.DiGraph()
    g.add_edge("docs/A.md", "timeout")
    result = validate_field_derived_graph("config_graph", g, docs, "configuration")
    assert "timeout" not in result.phantom_nodes


def test_validate_document_graph_uses_cross_references_field():
    docs = [DocumentMetadata(path="docs/A.md", cross_references=["docs/B.md"])]
    gb = GraphBuilder()
    gb.add_document(docs[0])
    result = validate_document_graph(gb.doc_graph, docs)
    assert result.valid is True


def test_validate_event_graph_passes_for_matrix_resolved_edges():
    docs = [DocumentMetadata(path="docs/TRADING-ENGINE.md")]
    gb = GraphBuilder()
    gb.add_event_matrix_edges([
        {"source_document": "docs/TRADING-ENGINE.md", "event_name": "trade.opened", "relation": "produces"},
    ])
    result = validate_event_graph(gb.event_graph, docs)
    assert result.valid is True


def test_validate_event_graph_flags_phantom_document():
    docs: list[DocumentMetadata] = []  # TRADING-ENGINE.md not indexed
    gb = GraphBuilder()
    gb.add_event_matrix_edges([
        {"source_document": "docs/TRADING-ENGINE.md", "event_name": "trade.opened", "relation": "produces"},
    ])
    result = validate_event_graph(gb.event_graph, docs)
    assert result.valid is False


def test_validate_schema_graph_passes_for_resolved_references():
    from governance.references.schema_reference_scanner import SchemaReference
    docs = [DocumentMetadata(path="docs/PLUGIN-LIFECYCLE.md")]
    gb = GraphBuilder()
    gb.add_schema_references({
        "docs/PLUGIN-LIFECYCLE.md": [SchemaReference("docs/PLUGIN-LIFECYCLE.md", 1, "x", "plugin.schema.json", True)],
    })
    result = validate_schema_graph(gb.schema_graph, docs)
    assert result.valid is True


def test_validate_ownership_graph_passes_for_matching_owner():
    docs = [DocumentMetadata(path="docs/A.md", owner="Team X")]
    gb = GraphBuilder()
    gb.add_document(docs[0])
    result = validate_ownership_graph(gb.ownership_graph, docs)
    assert result.valid is True


def test_validate_ownership_graph_flags_stale_owner_mismatch():
    """The graph has an edge from 'Old Team' -> docs/A.md, but the
    document's CURRENT owner is 'New Team' -- a stale edge."""
    docs = [DocumentMetadata(path="docs/A.md", owner="New Team")]
    g = nx.DiGraph()
    g.add_edge("Old Team", "docs/A.md")
    result = validate_ownership_graph(g, docs)
    assert result.valid is False
    assert "docs/A.md" in result.phantom_nodes


def test_validate_dependency_graph_passes_for_real_documents():
    docs = [DocumentMetadata(path="docs/A.md", depends_on=["docs/B.md"])]
    gb = GraphBuilder()
    gb.add_document(docs[0])
    result = validate_dependency_graph(gb.dependency_graph, docs)
    assert result.valid is True


def test_validate_all_graphs_aggregates_and_passes_for_consistent_state():
    docs = [
        DocumentMetadata(
            path="docs/A.md", owner="Team", configuration=["cfg1"], interfaces=["Iface1"],
            state_machines=["SM1"], security=["sec1"], recovery=["rec1"], validation=["val1"],
        ),
    ]
    gb = GraphBuilder()
    gb.add_document(docs[0])
    report = validate_all_graphs(gb, docs)
    assert report["overall_valid"] is True
    assert report["graphs_validated"] == 11
    assert all(r["valid"] for r in report["results"])


def test_validate_all_graphs_detects_inconsistency():
    docs = [DocumentMetadata(path="docs/A.md", configuration=["cfg1"])]
    gb = GraphBuilder()
    gb.add_document(docs[0])
    # Manually corrupt the graph to simulate staleness: add an edge for
    # a document that isn't in `docs`.
    gb.config_graph.add_edge("docs/GHOST.md", "some_key")
    report = validate_all_graphs(gb, docs)
    assert report["overall_valid"] is False
    config_result = next(r for r in report["results"] if r["graph_name"] == "config_graph")
    assert config_result["valid"] is False
    assert config_result["phantom_node_count"] == 1


def test_real_repository_all_graphs_validate_cleanly():
    """Sanity check: running the actual canonical pipeline against the
    real repository must produce zero phantom nodes across all 11
    validated graphs -- confirming the graphs genuinely trace back to
    real, current source data, not stale leftovers."""
    import subprocess
    import sys
    import json as json_module
    from pathlib import Path

    repo_root = Path(__file__).resolve().parents[3]
    script = """
import sys, json
sys.path.insert(0, "tools/governance")
import yaml
from governance.indexer.repo_indexer import RepoIndexer
from governance.parser.markdown_parser import MarkdownParser
from governance.metadata.metadata_parser import MetadataParser
from governance.graphs.graph_builder import GraphBuilder
from governance.graphs.graph_source_validator import validate_all_graphs
from governance.references.event_matrix_parser import build_event_graph_edges, parse_event_ownership_matrix
from governance.references.schema_reference_scanner import scan_corpus_for_schema_references
from pathlib import Path as P

cfg = yaml.safe_load(open("tools/governance/config/governance.yaml"))
indexer = RepoIndexer(".", cfg["docs_globs"])
inventory = indexer.build_inventory()
known_paths = [item["path"] for item in inventory]
md_parser = MarkdownParser(".")
meta_parser = MetadataParser(known_paths=known_paths)
gb = GraphBuilder()
docs = []
for item in inventory:
    parsed = md_parser.parse_file(item["path"])
    meta = meta_parser.parse_document(parsed["raw_text"], item["path"])
    docs.append(meta)
    gb.add_document(meta)

matrix_path = P("docs/EVENT-OWNERSHIP-MATRIX.md")
if matrix_path.exists():
    rows = parse_event_ownership_matrix(matrix_path.read_text())
    result = build_event_graph_edges(rows, P("docs"))
    gb.add_event_matrix_edges(result["edges"])

schema_results = scan_corpus_for_schema_references(docs, P("schemas"))
gb.add_schema_references(schema_results)

report = validate_all_graphs(gb, docs)
print(json.dumps(report))
"""
    proc = subprocess.run([sys.executable, "-c", script], cwd=repo_root, capture_output=True, text=True)
    assert proc.returncode == 0, proc.stderr
    report = json_module.loads(proc.stdout.strip().splitlines()[-1])
    assert report["overall_valid"] is True, report["results"]
