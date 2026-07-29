"""Tests for the Freeze Engine (Repository Canonicality Repair, Remediation
Item 4: "Implement a real Freeze Framework producer that generates freeze
records through the canonical runtime rather than relying on manually
generated JSON.").

Prior to this module, NO code in the repository produced
`.governance/freeze/freeze_WS0.json` -- confirmed by a full repository
grep for write-sites, and by ruling out both candidate classes that could
plausibly have been the producer (`FreezeManager`, which has zero call
sites and an unrelated SQL schema; `ClosureOrchestrator`, whose
same-named `freeze_dimension`/`freeze_closure` methods are empty no-op
stubs). Every historical regeneration of that file was performed via ad
hoc interactive Python, never committed as reusable code.
"""
from pathlib import Path

from governance.freeze.freeze_engine import FreezeEngine


def _repo_root() -> Path:
    return Path(__file__).parent.parent.parent.parent


def test_freeze_engine_produces_all_required_fields():
    engine = FreezeEngine(_repo_root())
    record = engine.freeze().to_dict()

    # version
    assert "workstream_version" in record["identity"]
    assert "schema_version" in record["identity"]
    # commit
    assert "commit_hash" in record["repository"]
    assert len(record["repository"]["commit_hash"]) == 40
    # repository hash
    assert "repository_tree_hash" in record["repository"]
    # validator versions/results
    assert "validator_results" in record["validation"]
    assert len(record["validation"]["validator_results"]) > 0
    # evidence hashes
    assert "artefact_hashes" in record["evidence"]
    assert len(record["evidence"]["artefact_hashes"]) > 0
    assert "evidence_record_hash" in record["evidence"]
    # metrics (canonical_output)
    assert "documents_indexed" in record["canonical_output"]
    # graphs -- 15 total after WS4 (Programme 2.5 Phase-0 graph
    # specification) added the 6 remaining frozen graphs (security,
    # recovery, validation, service, plugin, runtime) plus algorithm_graph,
    # to the original 8 (document/dependency/ownership/interface/event/
    # config/schema/state_machine).
    assert "graph_hashes" in record["graphs"]
    assert record["graphs"]["graph_count"] == 15
    # database hash
    assert record["database"]["database_hash"] is not None
    # timestamp
    assert "freeze_timestamp" in record["freeze"]
    assert "timestamp" in record["execution"]
    # integrity checksum
    assert "integrity_checksum" in record["integrity"]


def test_freeze_engine_producer_is_identified():
    """The freeze record must explicitly name its own producer, so
    future audits never again have to reverse-engineer whether a freeze
    record has a real producer or not."""
    engine = FreezeEngine(_repo_root())
    record = engine.freeze().to_dict()
    assert record["identity"]["producer"] == "tools.governance.freeze.freeze_engine.FreezeEngine"


def test_freeze_engine_commit_hash_matches_actual_git_head():
    import subprocess
    repo_root = _repo_root()
    actual_head = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=repo_root, capture_output=True, text=True
    ).stdout.strip()
    engine = FreezeEngine(repo_root)
    record = engine.freeze().to_dict()
    assert record["repository"]["commit_hash"] == actual_head


def test_freeze_and_save_writes_a_file(tmp_path):
    # signing_key_path is deliberately isolated to tmp_path, NOT the
    # real repository's shared production signing keypair under
    # <repo_root>/.governance/freeze/ -- signing against the real repo's
    # keys from a test would either (a) silently create/reuse the real
    # production private key as a side effect of running the test suite
    # (a real problem in itself: tests should never touch production
    # secrets), or (b), after the fresh-clone-corruption fix, correctly
    # raise RuntimeError in any checkout that has a committed public key
    # but no private key (e.g. a fresh clone running the test suite,
    # confirmed as a real failure via this session's own fresh-clone
    # re-verification). Using an isolated tmp_path keypair avoids both.
    engine = FreezeEngine(_repo_root(), signing_key_path=tmp_path / "isolated_signing_key" / ".signing_key")
    output_path = tmp_path / "freeze_TEST.json"
    engine.freeze_and_save(output_path)
    assert output_path.exists()
    import json
    data = json.loads(output_path.read_text())
    assert data["identity"]["workstream_id"] == "WS0"
    assert data["tamper_evidence"]["algorithm"] == "Ed25519"
