"""Tests for the 14 category validators (WS3 Validator Framework,
validator/<category>/checks.py). Each category validator is tested
independently, with no dependency on a full apex-gov run pipeline
execution -- directly exercising "every validator independently
executable" and "every validator has test coverage" for all 14
categories required by readiness_checklist.json CHECK-WS3.
"""
import json
from pathlib import Path

import networkx as nx

from governance.metadata.models import DocumentMetadata
from governance.validator.ownership.checks import run as run_ownership
from governance.validator.dependency.checks import run as run_dependency
from governance.validator.event.checks import run as run_event
from governance.validator.schema.checks import run as run_schema
from governance.validator.interface.checks import run as run_interface
from governance.validator.state_machine.checks import run as run_state_machine
from governance.validator.recovery.checks import run as run_recovery
from governance.validator.security.checks import run as run_security
from governance.validator.configuration.checks import run as run_configuration
from governance.validator.graph.checks import run as run_graph
from governance.validator.freeze.checks import run as run_freeze
from governance.validator.algorithm.checks import run as run_algorithm
from governance.validator.metadata.checks import run as run_metadata
from governance.validator.closure.checks import run as run_closure


def test_ownership_flags_missing_owner():
    docs = [DocumentMetadata(path="A.md", owner=None), DocumentMetadata(path="B.md", owner="Team")]
    findings = run_ownership(docs, nx.DiGraph())
    assert len(findings) == 1
    assert findings[0].path == "A.md"
    assert findings[0].validator_id == "OWNERSHIP-001"


def test_dependency_flags_broken_target_and_self_dependency():
    docs = [
        DocumentMetadata(path="A.md", depends_on=["MISSING.md", "A.md"]),
        DocumentMetadata(path="B.md", depends_on=["A.md"]),
    ]
    findings = run_dependency(docs, nx.DiGraph())
    rules = {(f.path, f.rule) for f in findings}
    assert ("A.md", "DEPENDENCY_TARGET_EXISTS") in rules
    assert ("A.md", "NO_SELF_DEPENDENCY") in rules
    assert not any(f.path == "B.md" for f in findings)


def test_event_flags_consumer_without_producer_and_self_produce_consume():
    docs = [
        DocumentMetadata(path="A.md", events_consumed=["trade.opened"]),
        DocumentMetadata(path="B.md", events_produced=["trade.closed"], events_consumed=["trade.closed"]),
    ]
    findings = run_event(docs, nx.DiGraph())
    rules = {(f.path, f.rule) for f in findings}
    assert ("A.md", "EVENT_HAS_PRODUCER") in rules
    assert ("B.md", "EVENT_NOT_SELF_PRODUCED_AND_CONSUMED") in rules


def test_schema_flags_invalid_json_and_missing_reference(tmp_path):
    (tmp_path / "good.schema.json").write_text(json.dumps({"$schema": "x", "type": "object"}))
    (tmp_path / "bad.schema.json").write_text("{not valid json")
    (tmp_path / "no_schema_key.schema.json").write_text(json.dumps({"foo": "bar"}))
    docs = [DocumentMetadata(path="A.md", schemas=["nonexistent"])]
    findings = run_schema(docs, nx.DiGraph(), schemas_dir=tmp_path)
    rules = {(f.path, f.rule) for f in findings}
    assert any(r == "SCHEMA_VALID_JSON" for _, r in rules)
    assert any(r == "SCHEMA_WELL_FORMED" for _, r in rules)
    assert ("A.md", "SCHEMA_REFERENCE_RESOLVES") in rules


def test_schema_accepts_resolvable_reference(tmp_path):
    (tmp_path / "event.schema.json").write_text(json.dumps({"$schema": "x", "type": "object"}))
    docs = [DocumentMetadata(path="A.md", schemas=["event"])]
    findings = run_schema(docs, nx.DiGraph(), schemas_dir=tmp_path)
    assert not any(f.rule == "SCHEMA_REFERENCE_RESOLVES" for f in findings)


def test_interface_flags_duplicate_declaration():
    docs = [
        DocumentMetadata(path="A.md", interfaces=["ChainAdapter"]),
        DocumentMetadata(path="B.md", interfaces=["ChainAdapter"]),
    ]
    findings = run_interface(docs, nx.DiGraph())
    assert len(findings) == 2
    assert {f.path for f in findings} == {"A.md", "B.md"}


def test_state_machine_flags_missing_recovery():
    docs = [
        DocumentMetadata(path="A.md", state_machines=["S1"]),
        DocumentMetadata(path="B.md", state_machines=["S1"], recovery=["retry"]),
    ]
    findings = run_state_machine(docs, nx.DiGraph())
    assert len(findings) == 1
    assert findings[0].path == "A.md"


def test_recovery_flags_root_without_recovery_content():
    docs = [
        DocumentMetadata(path="A.md"),
        DocumentMetadata(path="B.md", recovery=["retry"]),
    ]
    findings = run_recovery(docs, nx.DiGraph(), root_paths={"A.md", "B.md"})
    assert len(findings) == 1
    assert findings[0].path == "A.md"


def test_security_flags_sensitive_root_without_security_section():
    docs = [DocumentMetadata(path="A.md", purpose="Handles credential storage and secret rotation.")]
    findings = run_security(docs, nx.DiGraph(), root_paths={"A.md"})
    assert len(findings) == 1


def test_security_ignores_non_sensitive_root():
    docs = [DocumentMetadata(path="A.md", purpose="Renders a dashboard widget.")]
    findings = run_security(docs, nx.DiGraph(), root_paths={"A.md"})
    assert findings == []


def test_configuration_flags_spelling_variants():
    docs = [
        DocumentMetadata(path="A.md", configuration=["RPC_TIMEOUT"]),
        DocumentMetadata(path="B.md", configuration=["rpc-timeout"]),
    ]
    findings = run_configuration(docs, nx.DiGraph())
    assert len(findings) == 2


def test_graph_flags_isolated_root():
    g = nx.DiGraph()
    g.add_node("A.md")
    g.add_edge("B.md", "C.md")
    findings = run_graph([], g, root_paths={"A.md", "B.md"})
    assert len(findings) == 1
    assert findings[0].path == "A.md"


def test_graph_flags_root_missing_from_graph_entirely():
    g = nx.DiGraph()
    findings = run_graph([], g, root_paths={"MISSING.md"})
    assert len(findings) == 1
    assert findings[0].rule == "ROOT_HAS_GRAPH_CONNECTIVITY"


def test_freeze_flags_unresolvable_commit(tmp_path):
    import subprocess
    subprocess.run(["git", "init", "-q"], cwd=tmp_path)
    records = [{"repository": {"commit_hash": "0" * 40}, "_source_path": "freeze_X.json"}]
    findings = run_freeze([], nx.DiGraph(), freeze_records=records, repo_root=tmp_path)
    assert len(findings) == 1
    assert findings[0].validator_id == "FREEZE-001"


def test_freeze_accepts_resolvable_commit(tmp_path):
    import subprocess
    subprocess.run(["git", "init", "-q"], cwd=tmp_path)
    subprocess.run(["git", "config", "user.email", "t@t.com"], cwd=tmp_path)
    subprocess.run(["git", "config", "user.name", "t"], cwd=tmp_path)
    (tmp_path / "f.txt").write_text("x")
    subprocess.run(["git", "add", "-A"], cwd=tmp_path)
    subprocess.run(["git", "commit", "-q", "-m", "init"], cwd=tmp_path)
    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=tmp_path, capture_output=True, text=True).stdout.strip()
    records = [{"repository": {"commit_hash": commit}, "_source_path": "freeze_X.json"}]
    findings = run_freeze([], nx.DiGraph(), freeze_records=records, repo_root=tmp_path)
    assert findings == []


def test_algorithm_flags_missing_validation_section():
    docs = [DocumentMetadata(path="A.md", purpose="Implements the routing logic scoring formula.")]
    findings = run_algorithm(docs, nx.DiGraph())
    assert len(findings) == 1


def test_metadata_flags_missing_required_fields():
    docs = [DocumentMetadata(path="A.md", type=None, owner=None, status=None, version=None)]
    findings = run_metadata(docs, nx.DiGraph())
    assert len(findings) == 4


def test_closure_flags_root_not_in_own_closure_and_empty_closure():
    findings = run_closure([], nx.DiGraph(), closures_by_root={
        "A.md": {"B.md"},  # A.md missing from its own closure
        "C.md": set(),     # empty closure
    })
    rules_by_path = {f.path: f.rule for f in findings if f.rule == "CLOSURE_CONTAINS_ROOT"}
    assert "A.md" in rules_by_path
    empty_paths = {f.path for f in findings if f.rule == "CLOSURE_NON_EMPTY"}
    assert "C.md" in empty_paths
