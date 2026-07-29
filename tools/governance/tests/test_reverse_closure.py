"""Tests for reverse closure (Repository Canonicality Repair, Remediation
Item 5: "Complete reverse-closure support if it remains part of
Programme 2.5's acceptance criteria.").

Prior to this fix, `ClosureEngine` had no reverse-closure method at all
(confirmed by direct `hasattr` check during the Evidence-First
Verification audit).
"""
import networkx as nx

from governance.closure.closure_engine import ClosureEngine


def test_reverse_closure_finds_dependents():
    """A -> B -> C (A depends on B, B depends on C).
    Forward closure of A: {A, B, C} (everything A depends on).
    Reverse closure of C: {C, B, A} (everything that depends on C)."""
    g = nx.DiGraph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    engine = ClosureEngine(g)

    forward_a = engine.compute_closure("A")
    assert forward_a == {"A", "B", "C"}

    reverse_c = engine.compute_reverse_closure("C")
    assert reverse_c == {"A", "B", "C"}


def test_reverse_closure_of_a_leaf_dependency_finds_all_transitive_dependents():
    g = nx.DiGraph()
    g.add_edge("ROOT1", "SHARED")
    g.add_edge("ROOT2", "SHARED")
    g.add_edge("ROOT3", "OTHER")
    engine = ClosureEngine(g)

    reverse = engine.compute_reverse_closure("SHARED")
    assert reverse == {"SHARED", "ROOT1", "ROOT2"}
    assert "ROOT3" not in reverse


def test_reverse_closure_of_isolated_node_is_just_itself():
    g = nx.DiGraph()
    g.add_node("ISOLATED")
    engine = ClosureEngine(g)
    assert engine.compute_reverse_closure("ISOLATED") == {"ISOLATED"}


def test_reverse_closure_of_unknown_node_returns_just_itself():
    g = nx.DiGraph()
    g.add_edge("A", "B")
    engine = ClosureEngine(g)
    # NetworkXError (node not in graph) is caught and treated as an empty
    # reverse closure, then the root itself is still added.
    assert engine.compute_reverse_closure("NOT-IN-GRAPH") == {"NOT-IN-GRAPH"}


def test_validate_closure_includes_both_forward_and_reverse():
    g = nx.DiGraph()
    g.add_edge("A", "B")
    engine = ClosureEngine(g)
    result = engine.validate_closure("A", {"A", "B"})
    assert "closure_size" in result
    assert "reverse_closure_size" in result
    assert "closure_docs" in result
    assert "reverse_closure_docs" in result


def test_reverse_closure_is_deterministic_and_reproducible():
    import yaml
    from pathlib import Path
    from governance.indexer.repo_indexer import RepoIndexer
    from governance.parser.markdown_parser import MarkdownParser
    from governance.metadata.metadata_parser import MetadataParser
    from governance.graphs.graph_builder import GraphBuilder
    from governance.closure.closure_engine import BehaviouralRootDetector

    repo_root = Path(__file__).parent.parent.parent.parent
    cfg = yaml.safe_load((repo_root / "tools/governance/config/governance.yaml").read_text())
    indexer = RepoIndexer(str(repo_root), cfg["docs_globs"])
    inventory = indexer.build_inventory()
    known_paths = [item["path"] for item in inventory]
    md_parser = MarkdownParser(str(repo_root))
    meta_parser = MetadataParser(known_paths=known_paths)
    graph_builder = GraphBuilder()
    docs = []
    for item in inventory:
        parsed = md_parser.parse_file(item["path"])
        meta = meta_parser.parse_document(parsed["raw_text"], item["path"])
        docs.append(meta)
        graph_builder.add_document(meta)

    detector = BehaviouralRootDetector(cfg["behavioural_root_signals"])
    roots = detector.detect_roots(docs)
    engine = ClosureEngine(graph_builder.dependency_graph)

    run1 = {r.path: sorted(engine.compute_reverse_closure(r.path)) for r in roots}
    run2 = {r.path: sorted(engine.compute_reverse_closure(r.path)) for r in roots}
    assert run1 == run2
