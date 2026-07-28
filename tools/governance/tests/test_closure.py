import networkx as nx
from governance.closure.closure_engine import ClosureEngine, BehaviouralRootDetector
from governance.metadata.models import DocumentMetadata, BehaviouralRoot

def test_closure_engine():
    g = nx.DiGraph()
    g.add_edge("A.md", "B.md")
    g.add_edge("B.md", "C.md")
    engine = ClosureEngine(g)
    closure = engine.compute_closure("A.md")
    assert closure == {"A.md", "B.md", "C.md"}

def test_root_detector():
    detector = BehaviouralRootDetector(["Engine", "Pipeline"])
    docs = [DocumentMetadata(path="docs/ENGINE.md", type="CONTRACT", purpose="Engine for X")]
    roots = detector.detect_roots(docs)
    assert len(roots) == 1
    assert "Engine" in roots[0].signals
