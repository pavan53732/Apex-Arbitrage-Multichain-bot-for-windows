"""Tests for the category-validator orchestrator (WS3)."""
import networkx as nx

from governance.metadata.models import DocumentMetadata
from governance.validator.category_suite import (
    CATALOGUE_ID_TO_CATEGORY,
    CATEGORY_ORDER,
    run_category_validators,
)


def test_all_14_categories_are_executed(tmp_path):
    docs = [DocumentMetadata(path="A.md", type="CONTRACT", owner="Team", status="Canonical", version="1.0.0")]
    report = run_category_validators(
        docs=docs,
        graph=nx.DiGraph(),
        root_paths=set(),
        closures_by_root={},
        schemas_dir=tmp_path,
        freeze_records=[],
        repo_root=tmp_path,
    )
    assert report["total_categories"] == 14
    assert set(report["categories_executed"]) == set(CATEGORY_ORDER)
    assert set(report["finding_counts_by_category"].keys()) == set(CATEGORY_ORDER)


def test_catalogue_id_mapping_covers_all_14_frozen_ids():
    frozen_ids = {
        "OWNERSHIP-001", "DEPENDENCY-001", "DEPENDENCY-002", "EVENT-001",
        "EVENT-002", "SCHEMA-001", "SCHEMA-002", "INTERFACE-001",
        "STATE-001", "RECOVERY-001", "SECURITY-001", "CONFIG-001",
        "GRAPH-001", "FREEZE-001",
    }
    assert set(CATALOGUE_ID_TO_CATEGORY.keys()) == frozen_ids


def test_report_reflects_real_findings():
    docs = [DocumentMetadata(path="A.md", owner=None)]  # missing owner
    report = run_category_validators(
        docs=docs, graph=nx.DiGraph(), root_paths=set(), closures_by_root={},
        schemas_dir=None, freeze_records=[], repo_root=None,
    )
    assert report["finding_counts_by_category"]["ownership"] == 1
    assert report["total_findings"] >= 1


def test_registry_and_category_suite_catalogue_mappings_never_drift():
    """registry.py deliberately duplicates category_suite.py's
    CATALOGUE_ID_TO_CATEGORY mapping (to avoid an import cycle) -- this
    test ensures the two copies are always identical."""
    from governance.validator.registry import CATALOGUE_ID_TO_CATEGORY_FALLBACK
    assert CATALOGUE_ID_TO_CATEGORY_FALLBACK == CATALOGUE_ID_TO_CATEGORY
