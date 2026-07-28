from governance.graphs.graph_builder import GraphBuilder
from governance.metadata.models import DocumentMetadata

def test_graph_builder_smoke():
    gb = GraphBuilder()
    meta = DocumentMetadata(path="docs/TEST.md", type="SPECIFICATION", owner="docs/TEST.md", status="DRAFT", version="0.0.1")
    gb.add_document(meta)
    assert "docs/TEST.md" in gb.doc_graph.nodes
