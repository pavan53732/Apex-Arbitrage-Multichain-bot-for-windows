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
