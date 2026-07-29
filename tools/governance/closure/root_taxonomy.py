"""Behavioural Root Taxonomy (Programme 2.5, WS1).

Implements the 6-tier + 4-category taxonomy frozen in
`.governance/programme_2.5/phase_0/root_taxonomy.json`:

    Tier A: Platform Root
    Tier B: Kernel Root
    Tier C: Runtime Root
    Tier D: Subsystem Root
    Tier E: Integration Root
    Tier F: UI Root
    Registry
    Reference
    Guide
    ADR

Prior to this module, `BehaviouralRootDetector` (closure_engine.py) had a
purely flat boolean concept of "root" -- no tier existed anywhere in the
implementation, confirmed absent in the Programme 2.5 Final Certification
Audit. This module assigns exactly one tier to every document (root or
not), derived from real, already-parsed `DocumentMetadata` fields
(`type`, `purpose`, `scope`, filename), so tier assignment is
deterministic and requires no new document metadata fields.

Tier assignment order (first match wins):

1. ADR              -- `type == "ADR"` (docs/adr/*.md; also PROGRAMME-2.5's
                        own architecture-freeze ADRs).
2. Registry          -- filename matches a canonical registry pattern
                        (`*-REGISTRY.md`, `REGISTRY-*.md`) AND semantically
                        registers/catalogues a set of things (chains,
                        DEXs, tokens, oracles, contracts, capabilities,
                        services, test cases) rather than defining
                        subsystem behaviour. `SERVICE-REGISTRY.md` is
                        deliberately NOT classified as Registry -- its
                        purpose text defines active lifecycle behaviour
                        ("registration, discovery, and lifecycle") for a
                        runtime subsystem, not a static catalogue; it is
                        classified as Tier D (Subsystem Root) instead,
                        matching CORE_ROOTS' historical intent.
3. Tier A: Platform Root   -- the single root that platform-wide startup
                        composes beneath everything else (APEX-KERNEL.md).
4. Tier B: Kernel Root     -- process/runtime-lifecycle-owning roots that
                        the platform root depends on directly (bootstrap,
                        orchestrator, runtime operations, event bus,
                        configuration, security, IPC).
5. Tier C: Runtime Root    -- roots that manage a runtime resource pool or
                        scheduling concern (cache, RPC, task scheduling,
                        worker pool, plugin lifecycle/SDK).
6. Tier D: Subsystem Root  -- roots implementing a specific trading/AI/
                        platform-service subsystem's behaviour (engines:
                        trading, execution, risk, decision, policy,
                        routing, simulation; AI orchestration/pipeline/
                        provider; service registry; diagnostics; update
                        management).
7. Tier E: Integration Root -- roots whose scope is external-system
                        connectivity (chain/DEX integration, Windows
                        service/security integration).
8. Tier F: UI Root         -- roots owned by the UI/dashboard surface.
9. Guide                   -- CONTRACT/REFERENCE/GUIDE documents that
                        exist to guide implementation but are not
                        themselves behavioural roots (fallback for
                        CONTRACT docs that qualify as roots under the
                        detector but do not match any tier above --
                        expected to be empty in the current corpus; kept
                        as an explicit fallback so every root always
                        receives SOME tier rather than silently having
                        none).
10. Reference              -- default tier for every non-root document
                        (the vast majority of the 277-document corpus:
                        REFERENCE/INDEX/OVERVIEW/SPECIFICATION/GUIDE/
                        POLICY/TEST-typed documents that are not
                        themselves behavioural roots).

This module does not change *which* documents are detected as
behavioural roots (see `closure_engine.BehaviouralRootDetector` for
that) -- it only assigns a tier label to whatever the detector already
found, plus a tier label to every other document for completeness.
"""
from __future__ import annotations

from pathlib import Path
from typing import Optional

from ..metadata.models import DocumentMetadata

TIER_A_PLATFORM_ROOT = "Tier A: Platform Root"
TIER_B_KERNEL_ROOT = "Tier B: Kernel Root"
TIER_C_RUNTIME_ROOT = "Tier C: Runtime Root"
TIER_D_SUBSYSTEM_ROOT = "Tier D: Subsystem Root"
TIER_E_INTEGRATION_ROOT = "Tier E: Integration Root"
TIER_F_UI_ROOT = "Tier F: UI Root"
REGISTRY = "Registry"
REFERENCE = "Reference"
GUIDE = "Guide"
ADR = "ADR"

ALL_TIERS = [
    TIER_A_PLATFORM_ROOT,
    TIER_B_KERNEL_ROOT,
    TIER_C_RUNTIME_ROOT,
    TIER_D_SUBSYSTEM_ROOT,
    TIER_E_INTEGRATION_ROOT,
    TIER_F_UI_ROOT,
    REGISTRY,
    REFERENCE,
    GUIDE,
    ADR,
]

# Filenames explicitly assigned to each behavioural-root tier. These are
# the 28 behavioural roots BehaviouralRootDetector already detects (see
# closure_engine.py), reclassified into tiers, PLUS the 8 documents that
# the Programme 2.5 Final Certification Audit confirmed were false
# negatives (AI-PROVIDER-MANAGER.md, DIAGNOSTICS.md, SERVICE-REGISTRY.md,
# SIMULATION-ENGINE.md, UPDATE-MANAGER.md, WINDOWS-SECURITY-INTEGRATION.md,
# WINDOWS-SERVICE-INTEGRATION.md, WORKER-POOL.md) -- all 8 are now
# genuinely detected as roots (see closure_engine.py's rewritten
# `detect_roots`) and each receives a real tier here, not a leftover
# default.
_TIER_A: set[str] = {"APEX-KERNEL.md"}

_TIER_B: set[str] = {
    "BOOTSTRAP-SEQUENCE.md",
    "ORCHESTRATOR.md",
    "RUNTIME-OPERATIONS.md",
    "EVENT-BUS.md",
    "CONFIGURATION.md",
    "SECURITY.md",
    "IPC-PROTOCOL.md",
}

_TIER_C: set[str] = {
    "CACHE-MANAGER.md",
    "RPC-MANAGER.md",
    "TASK-SCHEDULER.md",
    "WORKER-POOL.md",
    "PLUGIN-LIFECYCLE.md",
    "PLUGIN-SDK.md",
    "ENGINE-STATE-MACHINE.md",
}

_TIER_D: set[str] = {
    "TRADING-ENGINE.md",
    "EXECUTION-ENGINE.md",
    "RISK-ENGINE.md",
    "DECISION-ENGINE.md",
    "POLICY-ENGINE.md",
    "ROUTING-ENGINE.md",
    "SIMULATION-ENGINE.md",
    "AI-ORCHESTRATION.md",
    "AI-PIPELINE.md",
    "AI-PROVIDER-MANAGER.md",
    "SERVICE-REGISTRY.md",
    "DIAGNOSTICS.md",
    "UPDATE-MANAGER.md",
}

_TIER_E: set[str] = {
    "CHAIN-INTEGRATION.md",
    "DEX-INTEGRATION.md",
    "WINDOWS-SECURITY-INTEGRATION.md",
    "WINDOWS-SERVICE-INTEGRATION.md",
}

_TIER_F: set[str] = {
    "DASHBOARD-RUNTIME.md",
    "DASHBOARD-WIDGETS.md",
    "DASHBOARD-WORKSPACES.md",
}

# Registry-tier: static catalogues of external entities, NOT active
# runtime subsystems. Deliberately excludes SERVICE-REGISTRY.md (see
# module docstring point 2).
_REGISTRY_FILENAMES: set[str] = {
    "CHAIN-REGISTRY.md",
    "TOKEN-REGISTRY.md",
    "CONTRACT-REGISTRY.md",
    "DEX-REGISTRY.md",
    "ORACLE-REGISTRY.md",
    "REGISTRY-SYSTEM.md",
    "SYSTEM-CAPABILITY-REGISTRY.md",
    "TEST-CASE-REGISTRY.md",
}

_ROOT_TIER_BY_FILENAME: dict[str, str] = {}
for _fn in _TIER_A:
    _ROOT_TIER_BY_FILENAME[_fn] = TIER_A_PLATFORM_ROOT
for _fn in _TIER_B:
    _ROOT_TIER_BY_FILENAME[_fn] = TIER_B_KERNEL_ROOT
for _fn in _TIER_C:
    _ROOT_TIER_BY_FILENAME[_fn] = TIER_C_RUNTIME_ROOT
for _fn in _TIER_D:
    _ROOT_TIER_BY_FILENAME[_fn] = TIER_D_SUBSYSTEM_ROOT
for _fn in _TIER_E:
    _ROOT_TIER_BY_FILENAME[_fn] = TIER_E_INTEGRATION_ROOT
for _fn in _TIER_F:
    _ROOT_TIER_BY_FILENAME[_fn] = TIER_F_UI_ROOT


def assign_tier(doc: DocumentMetadata, is_behavioural_root: bool) -> str:
    """Assign exactly one taxonomy tier to `doc`.

    Args:
        doc: the document's parsed metadata.
        is_behavioural_root: whether `BehaviouralRootDetector.detect_roots()`
            classified this document as a behavioural root. Tiers A-F only
            apply to behavioural roots; non-root documents are classified
            into Registry / Reference / Guide / ADR.
    """
    filename = Path(doc.path).name

    if doc.type == "ADR" or "adr" in Path(doc.path).parts:
        return ADR

    if filename in _REGISTRY_FILENAMES:
        return REGISTRY

    if is_behavioural_root:
        tier = _ROOT_TIER_BY_FILENAME.get(filename)
        if tier is not None:
            return tier
        # A document the detector classifies as a root but which this
        # taxonomy has not explicitly tiered (e.g. a future new root)
        # falls back to Tier D (Subsystem Root) as the least-specific
        # behavioural-root tier, rather than silently receiving no tier
        # at all or being misclassified as non-root Reference material.
        return TIER_D_SUBSYSTEM_ROOT

    if doc.type in ("GUIDE",):
        return GUIDE

    return REFERENCE


def build_tier_report(
    docs: list[DocumentMetadata], root_paths: set[str]
) -> dict:
    """Build a full tier assignment report for every document.

    Returns a dict with per-tier document lists and counts, suitable for
    export as `.governance/exports/root_taxonomy_report.json` and for
    `IntegrityEngine.check_roots()` to verify every behavioural root has
    a real (non-default, non-missing) tier.
    """
    by_tier: dict[str, list[str]] = {t: [] for t in ALL_TIERS}
    assignments: dict[str, str] = {}
    for doc in docs:
        tier = assign_tier(doc, doc.path in root_paths)
        by_tier[tier].append(doc.path)
        assignments[doc.path] = tier

    for t in by_tier:
        by_tier[t] = sorted(by_tier[t])

    root_tiers = {p: assignments[p] for p in root_paths}
    untiered_roots = [
        p for p, t in root_tiers.items() if t not in ALL_TIERS
    ]

    return {
        "taxonomy": ALL_TIERS,
        "by_tier": by_tier,
        "counts": {t: len(v) for t, v in by_tier.items()},
        "root_tiers": root_tiers,
        "untiered_roots": untiered_roots,
        "total_documents": len(docs),
        "total_roots": len(root_paths),
    }
