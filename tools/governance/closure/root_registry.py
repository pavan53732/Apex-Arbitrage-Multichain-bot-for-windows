"""Behavioural Root Registry (Programme 2.5 Phase-0, WS1).

Implements the two remaining WS1 readiness-checklist items confirmed
absent by the Programme 2.5 Final Certification Audit:

- "Behavioural Root Registry exists and is valid" -- previously, roots
  were only ever emitted to stdout by `apex-gov roots`; no persisted,
  schema-checkable registry file existed. A stray prior attempt
  (`behavioural_root_registry.json`, introduced by commit `f584abb26`)
  was archived as stale/incorrect during Programme 2.5 remediation
  (it claimed "34 roots" in its own generating commit message but
  contained only 22 entries) and is NOT reused here -- this is a new,
  live-generated registry with a schema (`RootRegistryEntry`) and an
  explicit `is_valid()` check.
- "Root lifecycle is defined" -- previously there was no lifecycle
  concept at all. This module defines three lifecycle states
  (PROPOSED, ACTIVE, DEPRECATED) and assigns one to every registry
  entry, sourced from an explicit override file
  (`root_lifecycle_overrides.json`, defaulting every root not listed
  there to ACTIVE, since every currently-detected root is a live,
  currently-relevant behavioural root -- none are proposed-but-not-yet-
  confirmed or formally deprecated as of this repository state).
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from ..metadata.models import DocumentMetadata, BehaviouralRoot
from .closure_engine import BehaviouralRootDetector
from .root_taxonomy import assign_tier

LIFECYCLE_PROPOSED = "PROPOSED"
LIFECYCLE_ACTIVE = "ACTIVE"
LIFECYCLE_DEPRECATED = "DEPRECATED"
VALID_LIFECYCLE_STATES = {LIFECYCLE_PROPOSED, LIFECYCLE_ACTIVE, LIFECYCLE_DEPRECATED}

REGISTRY_SCHEMA_VERSION = "1.0.0"


@dataclass
class RootRegistryEntry:
    path: str
    tier: str
    signals: list[str]
    reason: str
    lifecycle_state: str
    owner: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "path": self.path,
            "tier": self.tier,
            "signals": self.signals,
            "reason": self.reason,
            "lifecycle_state": self.lifecycle_state,
            "owner": self.owner,
        }


def load_lifecycle_overrides(overrides_path: Optional[Path]) -> dict[str, str]:
    """Load explicit lifecycle-state overrides, keyed by document path.

    Any root not present in this mapping defaults to ACTIVE. The file is
    optional; if absent, every root is ACTIVE.
    """
    if overrides_path is None or not overrides_path.exists():
        return {}
    data = json.loads(overrides_path.read_text(encoding="utf-8"))
    invalid = {p: s for p, s in data.items() if s not in VALID_LIFECYCLE_STATES}
    if invalid:
        raise ValueError(f"Invalid lifecycle state(s) in overrides file: {invalid}")
    return data


def build_registry(
    docs: list[DocumentMetadata],
    roots: list[BehaviouralRoot],
    lifecycle_overrides: Optional[dict[str, str]] = None,
) -> list[RootRegistryEntry]:
    lifecycle_overrides = lifecycle_overrides or {}
    docs_by_path = {d.path: d for d in docs}
    root_paths = {r.path for r in roots}

    entries = []
    for r in roots:
        doc = docs_by_path.get(r.path)
        tier = assign_tier(doc, is_behavioural_root=True) if doc else None
        entries.append(
            RootRegistryEntry(
                path=r.path,
                tier=tier or "UNKNOWN",
                signals=r.signals,
                reason=r.reason,
                lifecycle_state=lifecycle_overrides.get(r.path, LIFECYCLE_ACTIVE),
                owner=doc.owner if doc else None,
            )
        )
    return sorted(entries, key=lambda e: e.path)


def is_valid(entries: list[RootRegistryEntry]) -> tuple[bool, list[str]]:
    """Validate a registry: every entry must have a non-empty path, a
    real taxonomy tier (not UNKNOWN), a valid lifecycle state, and there
    must be zero duplicate paths."""
    errors = []
    seen_paths = set()
    for e in entries:
        if not e.path:
            errors.append("entry with empty path")
            continue
        if e.path in seen_paths:
            errors.append(f"duplicate path: {e.path}")
        seen_paths.add(e.path)
        if e.tier == "UNKNOWN" or not e.tier:
            errors.append(f"{e.path}: missing/unknown tier")
        if e.lifecycle_state not in VALID_LIFECYCLE_STATES:
            errors.append(f"{e.path}: invalid lifecycle_state '{e.lifecycle_state}'")
    return (len(errors) == 0, errors)


def save_registry(entries: list[RootRegistryEntry], path: Path) -> Path:
    valid, errors = is_valid(entries)
    payload = {
        "schema_version": REGISTRY_SCHEMA_VERSION,
        "valid": valid,
        "validation_errors": errors,
        "total_roots": len(entries),
        "roots": [e.to_dict() for e in entries],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def load_registry(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))
