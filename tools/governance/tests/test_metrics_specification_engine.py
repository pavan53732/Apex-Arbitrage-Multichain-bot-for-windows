"""Tests for the 10-metric specification engine (WS8 Metrics Engine)."""
import json

import networkx as nx

from governance.metadata.models import DocumentMetadata
from governance.metrics.metrics_specification_engine import (
    closure_completeness,
    compute_all_metrics,
    event_coverage,
    graph_integrity,
    interface_coverage,
    ownership_integrity,
    reference_integrity,
    repository_completeness,
    schema_coverage,
    security_coverage,
    validator_coverage,
)


def test_repository_completeness_ratio():
    docs = [DocumentMetadata(path="A.md"), DocumentMetadata(path="B.md")]
    findings_by_path = {"A.md": [{"rule": "X"}]}
    assert repository_completeness(docs, findings_by_path) == 0.5


def test_repository_completeness_vacuous_when_no_docs():
    assert repository_completeness([], {}) == 1.0


def test_closure_completeness_ratio():
    roots = {"A.md", "B.md"}
    closures = {"A.md": {"A.md", "C.md"}, "B.md": set()}  # B's closure is empty -> invalid
    assert closure_completeness(roots, closures) == 0.5


def test_validator_coverage_ratio():
    catalogued = ["ID1", "ID2", "ID3"]
    executed = {"ID1", "ID2"}
    assert abs(validator_coverage(catalogued, executed) - (2 / 3)) < 1e-5


def test_reference_integrity_ratio():
    docs = [DocumentMetadata(path="A.md", depends_on=["B.md", "MISSING.md"])]
    known = {"A.md", "B.md"}
    assert reference_integrity(docs, known) == 0.5


def test_ownership_integrity_ratio():
    docs = [DocumentMetadata(path="A.md", owner="Team"), DocumentMetadata(path="B.md", owner=None)]
    assert ownership_integrity(docs) == 0.5


def test_graph_integrity_ratio():
    g = nx.DiGraph()
    g.add_edge("A.md", "B.md")
    g.add_edge("A.md", "MISSING.md")
    known = {"A.md", "B.md"}
    assert graph_integrity(g, known) == 0.5


def test_security_coverage_ratio():
    docs = [
        DocumentMetadata(path="A.md", purpose="Handles credential storage.", security=["dpapi"]),
        DocumentMetadata(path="B.md", purpose="Handles secret rotation."),  # no security section
    ]
    roots = {"A.md", "B.md"}
    assert security_coverage(docs, roots) == 0.5


def test_security_coverage_vacuous_when_no_security_sensitive_roots():
    docs = [DocumentMetadata(path="A.md", purpose="Renders UI widgets.")]
    assert security_coverage(docs, {"A.md"}) == 1.0


def test_schema_coverage_ratio(tmp_path):
    (tmp_path / "good.schema.json").write_text(json.dumps({"$schema": "x", "type": "object"}))
    (tmp_path / "bad.schema.json").write_text("{not json")
    assert schema_coverage(tmp_path) == 0.5


def test_schema_coverage_vacuous_when_no_schemas_dir():
    assert schema_coverage(None) == 1.0


def test_interface_coverage_ratio():
    docs = [
        DocumentMetadata(path="A.md", interfaces=["Unique1"]),
        DocumentMetadata(path="B.md", interfaces=["Duplicate"]),
        DocumentMetadata(path="C.md", interfaces=["Duplicate"]),
    ]
    # 2 distinct interfaces (Unique1, Duplicate); Duplicate is invalid (2 owners)
    assert interface_coverage(docs) == 0.5


def test_event_coverage_ratio():
    docs = [
        DocumentMetadata(path="A.md", events_produced=["e1"]),
        DocumentMetadata(path="B.md", events_consumed=["e1", "e2"]),  # e2 has no producer
    ]
    # distinct events: e1, e2; e1 has producer, e2 does not
    assert event_coverage(docs) == 0.5


def test_compute_all_metrics_returns_exactly_the_10_frozen_names():
    docs = [DocumentMetadata(path="A.md", owner="Team")]
    result = compute_all_metrics(
        docs=docs, graph=nx.DiGraph(), root_paths=set(), closures_by_root={},
        findings_by_path={}, catalogued_validator_ids=["ID1"], executed_validator_ids={"ID1"},
        schemas_dir=None,
    )
    expected_names = {
        "Repository Completeness", "Closure Completeness", "Validator Coverage",
        "Reference Integrity", "Ownership Integrity", "Graph Integrity",
        "Security Coverage", "Schema Coverage", "Interface Coverage", "Event Coverage",
    }
    assert set(result.keys()) == expected_names
    assert len(result) == 10
    assert all(isinstance(v, float) for v in result.values())
