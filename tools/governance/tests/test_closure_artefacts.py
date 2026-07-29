"""Tests for per-behavioural-root closure artefacts (WS2 readiness
checklist: closure hashing, closure versioning, and the 5 per-root
artefacts -- manifest, dependency graph, audit, work queue, maturity
report)."""
import json

import networkx as nx

from governance.closure.closure_artefacts import (
    build_closure_audit,
    build_closure_dependency_graph,
    build_closure_manifest,
    build_closure_maturity_report,
    build_closure_work_queue,
    compute_closure_hash,
    next_version,
    root_dir_name,
    write_all_root_artefacts,
)
from governance.metadata.models import DocumentMetadata


def _graph():
    g = nx.DiGraph()
    g.add_edge("A.md", "B.md")
    g.add_edge("B.md", "C.md")
    g.add_edge("X.md", "Y.md")  # outside the A/B/C closure
    return g


def test_closure_hash_is_deterministic():
    g = _graph()
    h1 = compute_closure_hash({"A.md", "B.md", "C.md"}, g)
    h2 = compute_closure_hash({"A.md", "B.md", "C.md"}, g)
    assert h1 == h2
    assert len(h1) == 64  # sha256 hex digest


def test_closure_hash_changes_with_different_membership():
    g = _graph()
    h1 = compute_closure_hash({"A.md", "B.md"}, g)
    h2 = compute_closure_hash({"A.md", "B.md", "C.md"}, g)
    assert h1 != h2


def test_closure_hash_excludes_edges_outside_closure():
    g = _graph()
    h_without_outside_edge = compute_closure_hash({"A.md", "B.md", "C.md"}, g)
    g2 = _graph()
    g2.add_edge("A.md", "Z.md")  # Z.md not in closure -- must not affect hash
    h_with_extra_external_edge = compute_closure_hash({"A.md", "B.md", "C.md"}, g2)
    assert h_without_outside_edge == h_with_extra_external_edge


def test_root_dir_name_derives_from_filename_stem():
    assert root_dir_name("docs/APEX-KERNEL.md") == "APEX-KERNEL"


def test_next_version_starts_at_1_for_new_root(tmp_path):
    assert next_version(tmp_path / "does_not_exist.json", "somehash") == 1


def test_next_version_increments_on_hash_change(tmp_path):
    manifest_path = tmp_path / "manifest.json"
    manifest_path.write_text(json.dumps({"closure_hash": "old_hash", "version": 3}))
    assert next_version(manifest_path, "new_hash") == 4


def test_next_version_stays_same_when_hash_unchanged(tmp_path):
    manifest_path = tmp_path / "manifest.json"
    manifest_path.write_text(json.dumps({"closure_hash": "same_hash", "version": 3}))
    assert next_version(manifest_path, "same_hash") == 3


def test_build_closure_manifest_fields(tmp_path):
    g = _graph()
    manifest = build_closure_manifest(
        "A.md", g, {"A.md", "B.md", "C.md"}, {"A.md"},
        tmp_path, "2026-07-29T00:00:00Z", "abc123",
    )
    assert manifest.root_path == "A.md"
    assert manifest.closure_size == 3
    assert manifest.reverse_closure_size == 1
    assert manifest.version == 1
    assert manifest.closure_documents == ["A.md", "B.md", "C.md"]


def test_build_closure_dependency_graph_is_induced_subgraph():
    g = _graph()
    sub = build_closure_dependency_graph("A.md", g, {"A.md", "B.md", "C.md"})
    assert set(sub.nodes()) == {"A.md", "B.md", "C.md"}
    assert ("X.md", "Y.md") not in sub.edges()
    assert ("A.md", "B.md") in sub.edges()


def test_build_closure_audit_aggregates_per_document():
    docs_by_path = {
        "A.md": DocumentMetadata(path="A.md", type="CONTRACT"),
        "B.md": DocumentMetadata(path="B.md", type="REFERENCE"),
    }
    findings_by_path = {"A.md": [{"rule": "X"}]}
    completeness_by_path = {"A.md": 0.5, "B.md": 1.0}
    audit = build_closure_audit("A.md", docs_by_path, {"A.md", "B.md"}, findings_by_path, completeness_by_path)
    assert audit["closure_size"] == 2
    assert audit["total_findings_in_closure"] == 1
    assert audit["avg_completeness_in_closure"] == 0.75


def test_build_closure_work_queue_filters_and_sorts_by_completeness():
    docs_by_path = {"A.md": DocumentMetadata(path="A.md", owner="Team")}
    completeness_by_path = {"A.md": 0.2, "B.md": 0.9, "C.md": 0.1}
    wq = build_closure_work_queue("A.md", docs_by_path, {"A.md", "B.md", "C.md"}, completeness_by_path, completeness_threshold=0.85)
    assert wq["queue_length"] == 2
    assert [i["path"] for i in wq["items"]] == ["C.md", "A.md"]  # ascending completeness


def test_build_closure_maturity_report_empty_closure():
    report = build_closure_maturity_report("A.md", set(), {}, {})
    assert report["maturity_score"] == 0.0
    assert report["closure_size"] == 0


def test_build_closure_maturity_report_penalizes_findings():
    closure = {"A.md", "B.md"}
    completeness = {"A.md": 1.0, "B.md": 1.0}
    no_findings = build_closure_maturity_report("A.md", closure, completeness, {})
    with_findings = build_closure_maturity_report("A.md", closure, completeness, {"A.md": [{"rule": "x"}] * 10})
    assert with_findings["maturity_score"] < no_findings["maturity_score"]


def test_build_closure_dependency_graph_is_deterministic_across_processes():
    """Regression test for a real non-determinism defect found via a
    live 'apex-gov freeze' re-run producing different work_queue.json/
    manifest bytes at the identical commit: build_closure_dependency_graph
    used to call graph.subgraph(closure_docs) directly, which -- like
    graphs/derived_graphs.py's identical prior defect -- does not
    preserve node/edge order regardless of input order, because
    networkx internally re-wraps the node collection in a `set` whose
    iteration is subject to per-process PYTHONHASHSEED randomisation.
    """
    import subprocess
    import sys

    script = """
import sys
sys.path.insert(0, "tools/governance")
import networkx as nx
from governance.closure.closure_artefacts import build_closure_dependency_graph

g = nx.DiGraph()
for i in range(30):
    g.add_edge(f"doc-{i}.md", f"doc-{(i + 1) % 30}.md")
closure = {f"doc-{i}.md" for i in range(0, 30, 2)}
result = build_closure_dependency_graph("root.md", g, closure)
import io
buf = io.BytesIO()
nx.write_graphml(result, buf)
print(buf.getvalue().hex())
"""
    hashes = set()
    for _ in range(5):
        proc = subprocess.run([sys.executable, "-c", script], capture_output=True, text=True)
        assert proc.returncode == 0, proc.stderr
        hashes.add(proc.stdout.strip())
    assert len(hashes) == 1, f"build_closure_dependency_graph is non-deterministic across processes: {len(hashes)} distinct outputs"


def test_build_closure_work_queue_breaks_ties_deterministically_across_processes():
    """Regression test for the exact defect found in a live
    'apex-gov freeze' re-run: work_queue.json's item ORDER changed
    between two runs at the identical commit, because
    build_closure_work_queue iterated a `set[str]` before scoring, and
    the subsequent items.sort() is a stable sort -- so tied-completeness
    documents (common in this corpus, e.g. many 0.0-completeness docs)
    leaked the set's randomised insertion order through the sort."""
    import subprocess
    import sys

    script = """
import sys
sys.path.insert(0, "tools/governance")
from governance.closure.closure_artefacts import build_closure_work_queue
from governance.metadata.models import DocumentMetadata

closure = {f"doc-{i}.md" for i in range(20)}
docs_by_path = {p: DocumentMetadata(path=p, owner="Team") for p in closure}
completeness = {p: 0.0 for p in closure}  # all tied at 0.0 -- forces tie-break to matter
wq = build_closure_work_queue("root.md", docs_by_path, closure, completeness, completeness_threshold=0.85)
print(",".join(item["path"] for item in wq["items"]))
"""
    outputs = set()
    for _ in range(5):
        proc = subprocess.run([sys.executable, "-c", script], capture_output=True, text=True)
        assert proc.returncode == 0, proc.stderr
        outputs.add(proc.stdout.strip())
    assert len(outputs) == 1, f"build_closure_work_queue tie-breaking is non-deterministic across processes: {len(outputs)} distinct orderings"


def test_write_all_root_artefacts_creates_all_5_files(tmp_path):
    g = _graph()
    docs_by_path = {
        "A.md": DocumentMetadata(path="A.md", type="CONTRACT", owner="Team"),
        "B.md": DocumentMetadata(path="B.md", type="REFERENCE"),
        "C.md": DocumentMetadata(path="C.md", type="REFERENCE"),
    }
    result = write_all_root_artefacts(
        root_path="A.md",
        graph=g,
        closure_docs={"A.md", "B.md", "C.md"},
        reverse_closure_docs={"A.md"},
        docs_by_path=docs_by_path,
        findings_by_path={},
        completeness_by_path={"A.md": 0.5, "B.md": 0.9, "C.md": 0.95},
        completeness_threshold=0.85,
        closures_dir=tmp_path,
        generated_at="2026-07-29T00:00:00Z",
        generated_at_commit="abc123",
    )
    root_dir = tmp_path / "A"
    assert (root_dir / "manifest.json").exists()
    assert (root_dir / "dependency_graph.graphml").exists()
    assert (root_dir / "audit.json").exists()
    assert (root_dir / "work_queue.json").exists()
    assert (root_dir / "maturity_report.json").exists()
    assert result["version"] == 1

    # Re-run with identical inputs: version must not increment (hash unchanged).
    result2 = write_all_root_artefacts(
        root_path="A.md", graph=g, closure_docs={"A.md", "B.md", "C.md"},
        reverse_closure_docs={"A.md"}, docs_by_path=docs_by_path,
        findings_by_path={}, completeness_by_path={"A.md": 0.5, "B.md": 0.9, "C.md": 0.95},
        completeness_threshold=0.85, closures_dir=tmp_path,
        generated_at="2026-07-29T01:00:00Z", generated_at_commit="def456",
    )
    assert result2["version"] == 1
    assert result2["closure_hash"] == result["closure_hash"]

    # Change closure membership: version must increment.
    result3 = write_all_root_artefacts(
        root_path="A.md", graph=g, closure_docs={"A.md", "B.md"},
        reverse_closure_docs={"A.md"}, docs_by_path=docs_by_path,
        findings_by_path={}, completeness_by_path={"A.md": 0.5, "B.md": 0.9},
        completeness_threshold=0.85, closures_dir=tmp_path,
        generated_at="2026-07-29T02:00:00Z", generated_at_commit="ghi789",
    )
    assert result3["version"] == 2
    assert result3["closure_hash"] != result["closure_hash"]
