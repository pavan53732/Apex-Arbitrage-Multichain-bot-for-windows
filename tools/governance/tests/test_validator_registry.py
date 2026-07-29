"""Tests for the Validator Registry (Repository Canonicality Repair, Work Item 7)."""
from pathlib import Path

from governance.validator.registry import list_validators, run_all_validators


def _repo_root() -> Path:
    return Path(__file__).parent.parent.parent.parent


def test_registry_lists_both_validator_layers():
    validators = list_validators()
    layers = {v.layer for v in validators}
    assert "in-engine" in layers
    assert "architecture-test" in layers


def test_registry_every_entry_has_required_fields():
    for v in list_validators():
        assert v.id
        assert v.owner
        assert v.inputs
        assert v.outputs
        assert v.severity
        assert v.evidence
        assert v.documentation
        assert v.tests
        assert v.invoke


def test_run_all_validators_returns_pass_for_current_repository():
    results = run_all_validators(_repo_root())
    failed = [r for r in results if r["status"] != "PASS"]
    assert not failed, f"unexpected validator failures: {failed}"
