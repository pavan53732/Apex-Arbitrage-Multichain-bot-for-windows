"""Tests for the Behavioural Root Registry (WS1 readiness checklist:
"Behavioural Root Registry exists and is valid", "Root lifecycle is
defined")."""
import json

from governance.closure.root_registry import (
    LIFECYCLE_ACTIVE,
    LIFECYCLE_DEPRECATED,
    RootRegistryEntry,
    build_registry,
    is_valid,
    load_lifecycle_overrides,
    load_registry,
    save_registry,
)
from governance.metadata.models import BehaviouralRoot, DocumentMetadata


def test_build_registry_assigns_tier_and_default_active_lifecycle():
    docs = [DocumentMetadata(path="docs/APEX-KERNEL.md", type="CONTRACT", owner="Runtime Team")]
    roots = [BehaviouralRoot(path="docs/APEX-KERNEL.md", signals=["CONTRACT", "Kernel"], reason="Behavioural root: CONTRACT, Kernel")]
    entries = build_registry(docs, roots)
    assert len(entries) == 1
    e = entries[0]
    assert e.path == "docs/APEX-KERNEL.md"
    assert e.tier == "Tier A: Platform Root"
    assert e.lifecycle_state == LIFECYCLE_ACTIVE
    assert e.owner == "Runtime Team"


def test_build_registry_applies_lifecycle_overrides():
    docs = [DocumentMetadata(path="docs/APEX-KERNEL.md", type="CONTRACT")]
    roots = [BehaviouralRoot(path="docs/APEX-KERNEL.md", signals=[], reason="x")]
    entries = build_registry(docs, roots, lifecycle_overrides={"docs/APEX-KERNEL.md": LIFECYCLE_DEPRECATED})
    assert entries[0].lifecycle_state == LIFECYCLE_DEPRECATED


def test_registry_is_valid_for_well_formed_entries():
    entries = [
        RootRegistryEntry(path="docs/A.md", tier="Tier A: Platform Root", signals=[], reason="x", lifecycle_state=LIFECYCLE_ACTIVE),
        RootRegistryEntry(path="docs/B.md", tier="Tier B: Kernel Root", signals=[], reason="x", lifecycle_state=LIFECYCLE_ACTIVE),
    ]
    valid, errors = is_valid(entries)
    assert valid is True
    assert errors == []


def test_registry_invalid_on_duplicate_path():
    entries = [
        RootRegistryEntry(path="docs/A.md", tier="Tier A: Platform Root", signals=[], reason="x", lifecycle_state=LIFECYCLE_ACTIVE),
        RootRegistryEntry(path="docs/A.md", tier="Tier A: Platform Root", signals=[], reason="x", lifecycle_state=LIFECYCLE_ACTIVE),
    ]
    valid, errors = is_valid(entries)
    assert valid is False
    assert any("duplicate" in e for e in errors)


def test_registry_invalid_on_unknown_tier():
    entries = [RootRegistryEntry(path="docs/A.md", tier="UNKNOWN", signals=[], reason="x", lifecycle_state=LIFECYCLE_ACTIVE)]
    valid, errors = is_valid(entries)
    assert valid is False
    assert any("tier" in e for e in errors)


def test_registry_invalid_on_bad_lifecycle_state():
    entries = [RootRegistryEntry(path="docs/A.md", tier="Tier A: Platform Root", signals=[], reason="x", lifecycle_state="BOGUS")]
    valid, errors = is_valid(entries)
    assert valid is False
    assert any("lifecycle_state" in e for e in errors)


def test_save_and_load_registry_roundtrip(tmp_path):
    entries = [RootRegistryEntry(path="docs/A.md", tier="Tier A: Platform Root", signals=["CONTRACT"], reason="x", lifecycle_state=LIFECYCLE_ACTIVE, owner="Team")]
    out_path = tmp_path / "registry.json"
    save_registry(entries, out_path)
    loaded = load_registry(out_path)
    assert loaded["valid"] is True
    assert loaded["total_roots"] == 1
    assert loaded["roots"][0]["path"] == "docs/A.md"
    assert loaded["schema_version"] == "1.0.0"


def test_load_lifecycle_overrides_missing_file_returns_empty(tmp_path):
    result = load_lifecycle_overrides(tmp_path / "does_not_exist.json")
    assert result == {}


def test_load_lifecycle_overrides_rejects_invalid_state(tmp_path):
    p = tmp_path / "overrides.json"
    p.write_text(json.dumps({"docs/A.md": "NOT_A_REAL_STATE"}))
    try:
        load_lifecycle_overrides(p)
        assert False, "should have raised"
    except ValueError:
        pass
