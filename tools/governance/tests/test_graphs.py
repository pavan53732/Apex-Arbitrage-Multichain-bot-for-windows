from governance.graphs.graph_builder import GraphBuilder
from governance.metadata.models import DocumentMetadata

def test_graph_builder_smoke():
    gb = GraphBuilder()
    meta = DocumentMetadata(path="docs/TEST.md", type="SPECIFICATION", owner="docs/TEST.md", status="DRAFT", version="0.0.1")
    gb.add_document(meta)
    assert "docs/TEST.md" in gb.doc_graph.nodes


def test_document_graph_populates_edges_from_cross_references():
    """Regression test for a real defect found during WS4 verification:
    document_graph previously had nodes only (0 edges, confirmed via
    apex-gov run: 277 nodes / 0 edges even after WS4's initial 14-graph
    implementation pass), because add_document() only ever called
    add_node() for it. Fixed by adding cross_references-derived edges,
    since cross_references is populated for 220/277 real documents and
    is the correct source for document-to-document relationships
    (distinct from dependency_graph's narrower depends_on/required_by
    semantic)."""
    gb = GraphBuilder()
    meta = DocumentMetadata(path="docs/A.md", type="REFERENCE", cross_references=["docs/B.md", "docs/C.md"])
    gb.add_document(meta)
    assert gb.doc_graph.number_of_edges() == 2
    assert ("docs/A.md", "docs/B.md") in gb.doc_graph.edges()
    assert ("docs/A.md", "docs/C.md") in gb.doc_graph.edges()


def test_add_event_matrix_edges_populates_event_graph():
    """WS4: closing the event_graph data-completeness gap via
    governance.references.event_matrix_parser -- edges are added via a
    separate method (not add_document()) since this data comes from a
    single external table, not per-document metadata."""
    gb = GraphBuilder()
    edges = [
        {"source_document": "docs/TRADING-ENGINE.md", "event_name": "trade.opened", "relation": "produces"},
        {"source_document": "docs/RISK-ENGINE.md", "event_name": "trade.opened", "relation": "consumes"},
    ]
    gb.add_event_matrix_edges(edges)
    assert gb.event_graph.number_of_nodes() == 3
    assert gb.event_graph.number_of_edges() == 2
    assert ("docs/TRADING-ENGINE.md", "trade.opened") in gb.event_graph.edges()
    assert ("trade.opened", "docs/RISK-ENGINE.md") in gb.event_graph.edges()


def test_add_schema_references_populates_schema_graph_with_resolved_only():
    """WS4: closing the schema_graph data-completeness gap via
    governance.references.schema_reference_scanner -- only RESOLVED
    references become edges; unresolved mentions must never appear in
    the graph."""
    from governance.references.schema_reference_scanner import SchemaReference

    gb = GraphBuilder()
    scan_results = {
        "docs/PLUGIN-LIFECYCLE.md": [
            SchemaReference("docs/PLUGIN-LIFECYCLE.md", 114, "schemas/plugin.schema.json", "plugin.schema.json", True),
        ],
        "docs/TESTING.md": [
            SchemaReference("docs/TESTING.md", 100, "config.schema.json", "config.schema.json", False),
        ],
    }
    gb.add_schema_references(scan_results)
    assert gb.schema_graph.number_of_edges() == 1
    assert ("docs/PLUGIN-LIFECYCLE.md", "plugin.schema.json") in gb.schema_graph.edges()
    assert "config.schema.json" not in gb.schema_graph.nodes()
