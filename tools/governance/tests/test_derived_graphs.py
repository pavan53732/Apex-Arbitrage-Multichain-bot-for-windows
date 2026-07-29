"""Tests for the 4 derived knowledge graphs (WS4: service, plugin,
runtime, algorithm) that complete the 14-graph Phase-0 specification."""
import networkx as nx

from governance.graphs.derived_graphs import (
    build_algorithm_graph,
    build_plugin_graph,
    build_runtime_graph,
    build_service_graph,
)
from governance.metadata.models import DocumentMetadata


def _dep_graph():
    g = nx.DiGraph()
    g.add_edge("docs/TRADING-ENGINE.md", "docs/RISK-ENGINE.md")
    g.add_edge("docs/APEX-KERNEL.md", "docs/ORCHESTRATOR.md")
    g.add_edge("docs/PLUGIN-SDK.md", "docs/PLUGIN-LIFECYCLE.md")
    g.add_edge("docs/UNRELATED.md", "docs/OTHER.md")
    return g


def test_service_graph_includes_only_subsystem_and_integration_tiers():
    g = _dep_graph()
    tiers = {
        "docs/TRADING-ENGINE.md": "Tier D: Subsystem Root",
        "docs/RISK-ENGINE.md": "Tier D: Subsystem Root",
        "docs/APEX-KERNEL.md": "Tier A: Platform Root",
    }
    result = build_service_graph(g, tiers)
    assert set(result.nodes()) == {"docs/TRADING-ENGINE.md", "docs/RISK-ENGINE.md"}


def test_runtime_graph_includes_only_platform_kernel_runtime_tiers():
    g = _dep_graph()
    tiers = {
        "docs/APEX-KERNEL.md": "Tier A: Platform Root",
        "docs/ORCHESTRATOR.md": "Tier B: Kernel Root",
        "docs/TRADING-ENGINE.md": "Tier D: Subsystem Root",
    }
    result = build_runtime_graph(g, tiers)
    assert set(result.nodes()) == {"docs/APEX-KERNEL.md", "docs/ORCHESTRATOR.md"}


def test_plugin_graph_includes_plugin_documents_and_neighbours():
    g = _dep_graph()
    docs = [
        DocumentMetadata(path="docs/PLUGIN-SDK.md", purpose="Defines the plugin SDK."),
        DocumentMetadata(path="docs/PLUGIN-LIFECYCLE.md", purpose="Plugin lifecycle."),
        DocumentMetadata(path="docs/TRADING-ENGINE.md", purpose="Trading."),
    ]
    result = build_plugin_graph(g, docs)
    assert "docs/PLUGIN-SDK.md" in result.nodes()
    assert "docs/PLUGIN-LIFECYCLE.md" in result.nodes()
    assert "docs/TRADING-ENGINE.md" not in result.nodes()


def test_algorithm_graph_includes_algorithm_documents_and_neighbours():
    g = _dep_graph()
    docs = [
        DocumentMetadata(path="docs/TRADING-ENGINE.md", purpose="Implements the routing scoring algorithm."),
        DocumentMetadata(path="docs/RISK-ENGINE.md", purpose="Risk checks."),
    ]
    result = build_algorithm_graph(g, docs)
    assert "docs/TRADING-ENGINE.md" in result.nodes()
    assert "docs/RISK-ENGINE.md" in result.nodes()  # neighbour of TRADING-ENGINE.md


def test_service_and_runtime_graphs_empty_when_no_matching_tiers():
    g = _dep_graph()
    assert build_service_graph(g, {}).number_of_nodes() == 0
    assert build_runtime_graph(g, {}).number_of_nodes() == 0


def test_derived_graphs_are_deterministic_across_fresh_processes():
    """Regression test for a real non-determinism defect found during
    WS4 implementation: nx.DiGraph.subgraph(nodes) does NOT preserve
    node/edge order even when passed a pre-sorted list, because it
    internally re-wraps the node collection in a `set` (see
    networkx.classes.filters.show_nodes), whose iteration order is
    subject to Python's per-process string hash randomisation
    (PYTHONHASHSEED). This was confirmed to produce 3 different
    GraphML byte sequences across 3 fresh subprocess runs on the exact
    same logical graph before the fix (building a fresh nx.DiGraph via
    explicit sorted() iteration in _deterministic_induced_subgraph,
    rather than relying on subgraph()'s node view).

    This test spawns fresh subprocesses (not just fresh function calls
    in the same interpreter) because PYTHONHASHSEED is fixed for the
    lifetime of one interpreter process -- an in-process-only test would
    not have caught the original bug.
    """
    import subprocess
    import sys

    script = """
import networkx as nx
import sys
sys.path.insert(0, "tools/governance")
from governance.graphs.derived_graphs import build_service_graph

g = nx.DiGraph()
for i in range(30):
    g.add_edge(f"docs/DOC-{i}.md", f"docs/DOC-{(i + 1) % 30}.md")
tiers = {f"docs/DOC-{i}.md": "Tier D: Subsystem Root" for i in range(0, 30, 2)}
result = build_service_graph(g, tiers)
import io
buf = io.BytesIO()
nx.write_graphml(result, buf)
print(buf.getvalue().hex())
"""
    # This test doesn't need the real repository docs -- it builds a
    # synthetic graph purely in-process via governance.graphs.derived_graphs,
    # which is importable once the `governance` package is installed
    # (pip install -e tools/governance), independent of cwd.
    hashes = set()
    for _ in range(5):
        proc = subprocess.run([sys.executable, "-c", script.replace('sys.path.insert(0, "tools/governance")\n', "")], capture_output=True, text=True)
        assert proc.returncode == 0, proc.stderr
        hashes.add(proc.stdout.strip())
    assert len(hashes) == 1, f"Derived graph serialization is non-deterministic across processes: {len(hashes)} distinct outputs"
