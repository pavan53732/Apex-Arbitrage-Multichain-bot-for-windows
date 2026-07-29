"""Tests for the 6-tier + 4-category Behavioural Root Taxonomy
(Programme 2.5 Phase-0 root_taxonomy.json implementation, WS1).

Prior to this module, BehaviouralRootDetector had zero tier concept
(confirmed by the Programme 2.5 Final Certification Audit) -- this file
tests `governance.closure.root_taxonomy`, which assigns every document
exactly one of the 10 frozen taxonomy categories.
"""
from governance.closure.root_taxonomy import (
    ALL_TIERS,
    ADR,
    GUIDE,
    REFERENCE,
    REGISTRY,
    TIER_A_PLATFORM_ROOT,
    TIER_B_KERNEL_ROOT,
    TIER_C_RUNTIME_ROOT,
    TIER_D_SUBSYSTEM_ROOT,
    TIER_E_INTEGRATION_ROOT,
    TIER_F_UI_ROOT,
    assign_tier,
    build_tier_report,
)
from governance.metadata.models import DocumentMetadata


def test_all_ten_taxonomy_categories_match_frozen_spec():
    """The module's taxonomy must exactly match
    phase_0/root_taxonomy.json's frozen list of 10 categories, in order."""
    assert ALL_TIERS == [
        "Tier A: Platform Root",
        "Tier B: Kernel Root",
        "Tier C: Runtime Root",
        "Tier D: Subsystem Root",
        "Tier E: Integration Root",
        "Tier F: UI Root",
        "Registry",
        "Reference",
        "Guide",
        "ADR",
    ]


def test_apex_kernel_is_tier_a_platform_root():
    doc = DocumentMetadata(path="docs/APEX-KERNEL.md", type="CONTRACT")
    assert assign_tier(doc, is_behavioural_root=True) == TIER_A_PLATFORM_ROOT


def test_orchestrator_is_tier_b_kernel_root():
    doc = DocumentMetadata(path="docs/ORCHESTRATOR.md", type="CONTRACT")
    assert assign_tier(doc, is_behavioural_root=True) == TIER_B_KERNEL_ROOT


def test_cache_manager_is_tier_c_runtime_root():
    doc = DocumentMetadata(path="docs/CACHE-MANAGER.md", type="CONTRACT")
    assert assign_tier(doc, is_behavioural_root=True) == TIER_C_RUNTIME_ROOT


def test_trading_engine_is_tier_d_subsystem_root():
    doc = DocumentMetadata(path="docs/TRADING-ENGINE.md", type="CONTRACT")
    assert assign_tier(doc, is_behavioural_root=True) == TIER_D_SUBSYSTEM_ROOT


def test_chain_integration_is_tier_e_integration_root():
    doc = DocumentMetadata(path="docs/CHAIN-INTEGRATION.md", type="CONTRACT")
    assert assign_tier(doc, is_behavioural_root=True) == TIER_E_INTEGRATION_ROOT


def test_dashboard_runtime_is_tier_f_ui_root():
    doc = DocumentMetadata(path="docs/DASHBOARD-RUNTIME.md", type="CONTRACT")
    assert assign_tier(doc, is_behavioural_root=True) == TIER_F_UI_ROOT


def test_service_registry_is_tier_d_not_registry_category():
    """SERVICE-REGISTRY.md is a genuine active-lifecycle subsystem
    (registration/discovery/lifecycle), not a static catalogue -- it must
    be tiered as a Subsystem Root, not miscategorised as the generic
    Registry bucket meant for static reference catalogues."""
    doc = DocumentMetadata(path="docs/SERVICE-REGISTRY.md", type="CONTRACT")
    assert assign_tier(doc, is_behavioural_root=True) == TIER_D_SUBSYSTEM_ROOT


def test_static_catalogue_registries_are_registry_category():
    for fn in ["CHAIN-REGISTRY.md", "TOKEN-REGISTRY.md", "CONTRACT-REGISTRY.md", "DEX-REGISTRY.md"]:
        doc = DocumentMetadata(path=f"docs/{fn}", type="CONTRACT")
        assert assign_tier(doc, is_behavioural_root=False) == REGISTRY, fn


def test_adr_documents_are_adr_category():
    doc = DocumentMetadata(path="docs/adr/0001-provider-abstraction.md", type="ADR")
    assert assign_tier(doc, is_behavioural_root=False) == ADR


def test_non_root_reference_document_defaults_to_reference():
    doc = DocumentMetadata(path="docs/SOME-CATALOG.md", type="REFERENCE")
    assert assign_tier(doc, is_behavioural_root=False) == REFERENCE


def test_guide_type_document_maps_to_guide_category():
    doc = DocumentMetadata(path="docs/SOME-GUIDE.md", type="GUIDE")
    assert assign_tier(doc, is_behavioural_root=False) == GUIDE


def test_build_tier_report_covers_every_document_and_every_root():
    docs = [
        DocumentMetadata(path="docs/APEX-KERNEL.md", type="CONTRACT"),
        DocumentMetadata(path="docs/CHAIN-REGISTRY.md", type="CONTRACT"),
        DocumentMetadata(path="docs/SOME-REFERENCE.md", type="REFERENCE"),
        DocumentMetadata(path="docs/adr/0001-x.md", type="ADR"),
    ]
    roots = {"docs/APEX-KERNEL.md"}
    report = build_tier_report(docs, roots)
    assert report["total_documents"] == 4
    assert report["total_roots"] == 1
    assert report["untiered_roots"] == []
    assert report["root_tiers"]["docs/APEX-KERNEL.md"] == TIER_A_PLATFORM_ROOT
    assert "docs/CHAIN-REGISTRY.md" in report["by_tier"][REGISTRY]
    assert "docs/SOME-REFERENCE.md" in report["by_tier"][REFERENCE]
    assert "docs/adr/0001-x.md" in report["by_tier"][ADR]
    assert sum(report["counts"].values()) == 4
