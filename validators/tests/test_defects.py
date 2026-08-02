"""Each validator must reject the specific defect it exists to catch.

These are the regression tests for the fixes made to this suite. Every case
mutates the healthy baseline in exactly one way and asserts the responsible
validator reports it. A validator that stops detecting its defect — by being
scoped too narrowly, short-circuited, or accidentally disabled — fails here.
"""

from __future__ import annotations

import pytest

from conftest import DocSpec, FixtureRepo, codes, warning_codes


# --- VAL-002 metadata ------------------------------------------------------


def test_missing_frontmatter_is_rejected(repo: FixtureRepo) -> None:
    repo.add_doc(
        "DOC-0001", "docs/apex-app-docs/runtime/orchestrator.md", body="# No frontmatter\n"
    ).write()
    repo.edit(
        "docs/apex-app-docs/runtime/orchestrator.md",
        lambda _: "# Orchestrator\n\nNo frontmatter at all.\n",
    )
    result = repo.run("VAL-002")
    assert result.status == "FAIL"
    assert "MISSING_REQUIRED_FIELD" in codes(result)


def test_malformed_document_id_is_rejected(healthy_repo: FixtureRepo) -> None:
    healthy_repo.edit(
        "docs/apex-app-docs/runtime/orchestrator.md",
        lambda t: t.replace("document_id: DOC-0001", "document_id: NOT-AN-ID"),
    )
    result = healthy_repo.run("VAL-002")
    assert result.status == "FAIL"
    assert "INVALID_ID_FORMAT" in codes(result)


def test_invalid_enum_value_is_rejected(healthy_repo: FixtureRepo) -> None:
    healthy_repo.edit(
        "docs/apex-app-docs/runtime/orchestrator.md",
        lambda t: t.replace("authority: Canonical", "authority: Supreme"),
    )
    result = healthy_repo.run("VAL-002")
    assert result.status == "FAIL"
    assert "INVALID_ENUM_VALUE" in codes(result)


# --- VAL-001 cross-references ----------------------------------------------


def test_unresolvable_doc_reference_is_rejected(healthy_repo: FixtureRepo) -> None:
    healthy_repo.edit(
        "docs/apex-app-docs/runtime/worker-pool.md",
        lambda t: t + "\n\nSee DOC-7777 for details.\n",
    )
    result = healthy_repo.run("VAL-001")
    assert result.status == "FAIL"
    assert "UNRESOLVED_DOC_REF" in codes(result)


def test_broken_markdown_link_is_rejected(healthy_repo: FixtureRepo) -> None:
    healthy_repo.edit(
        "docs/apex-app-docs/runtime/worker-pool.md",
        lambda t: t + "\n\n[missing](./does-not-exist.md)\n",
    )
    result = healthy_repo.run("VAL-001")
    assert result.status == "FAIL"
    assert "UNRESOLVED_MARKDOWN_LINK" in codes(result)


# --- VAL-004 registry consistency ------------------------------------------


def test_registry_pointing_at_missing_file_is_rejected(healthy_repo: FixtureRepo) -> None:
    (healthy_repo.root / "docs/apex-app-docs/runtime/worker-pool.md").unlink()
    result = healthy_repo.run("VAL-004")
    assert result.status == "FAIL"
    assert "REGISTRY_FS_MISMATCH" in codes(result)


def test_document_id_bound_to_the_wrong_file_is_rejected(repo: FixtureRepo) -> None:
    """The collision class that went undetected across 13 documents."""
    repo.add_doc("DOC-0001", "docs/apex-app-docs/runtime/orchestrator.md")
    repo.add_doc(
        "DOC-0002", "docs/apex-app-docs/runtime/worker-pool.md", register=True
    )
    repo.write()
    # A second file now declares an ID the registry maps elsewhere.
    repo.edit(
        "docs/apex-app-docs/runtime/worker-pool.md",
        lambda t: t.replace("document_id: DOC-0002", "document_id: DOC-0001"),
    )
    result = repo.run("VAL-004")
    assert result.status == "FAIL"
    assert "REGISTRY_PATH_MISMATCH" in codes(result)


# --- VAL-003 concept uniqueness --------------------------------------------


def test_duplicate_concept_owner_is_rejected(repo: FixtureRepo) -> None:
    repo.add_doc(
        "DOC-0001", "docs/apex-app-docs/runtime/orchestrator.md", concept_id="CONCEPT-0001"
    )
    repo.add_doc(
        "DOC-0002", "docs/apex-app-docs/runtime/worker-pool.md", concept_id="CONCEPT-0001"
    )
    repo.write()
    result = repo.run("VAL-003")
    assert result.status == "FAIL"
    assert "DUPLICATE_CONCEPT_OWNER" in codes(result)


# --- VAL-006 generated artifacts -------------------------------------------


def test_prohibited_temp_file_is_rejected(healthy_repo: FixtureRepo) -> None:
    (healthy_repo.root / "AUDIT.md").write_text("# Audit\n", encoding="utf-8")
    result = healthy_repo.run("VAL-006")
    assert result.status == "FAIL"
    assert "PROHIBITED_TEMP_FILE" in codes(result)


def test_cicd_workflow_is_rejected(healthy_repo: FixtureRepo) -> None:
    workflows = healthy_repo.root / ".github" / "workflows"
    workflows.mkdir(parents=True, exist_ok=True)
    (workflows / "ci.yml").write_text("name: ci\n", encoding="utf-8")
    result = healthy_repo.run("VAL-006")
    assert result.status == "FAIL"
    assert "PROHIBITED_CICD_FILE" in codes(result)


# --- VAL-007 document class ------------------------------------------------


def test_registry_class_outside_registries_folder_is_rejected(repo: FixtureRepo) -> None:
    repo.add_doc(
        "DOC-0001",
        "docs/apex-app-docs/runtime/orchestrator.md",
        class_="Registry",
        plane="Repository Operating Model",
        domain="Registries",
    ).write()
    result = repo.run("VAL-007")
    assert result.status == "FAIL"
    assert "FOLDER_CLASS_MISMATCH" in codes(result)


def test_plane_domain_mismatch_is_rejected(healthy_repo: FixtureRepo) -> None:
    healthy_repo.edit(
        "docs/apex-app-docs/runtime/orchestrator.md",
        lambda t: t.replace("domain: Runtime", "domain: Governance"),
    )
    result = healthy_repo.run("VAL-007")
    assert result.status == "FAIL"
    assert "PLANE_BOUNDARY_VIOLATION" in codes(result)


# --- VAL-005 orphan detection ----------------------------------------------


def test_unreachable_canonical_document_is_rejected(healthy_repo: FixtureRepo) -> None:
    healthy_repo.edit(
        "docs/apex-repository-docs/documentation-lifecycle/documentation-map.md",
        lambda t: t.replace("- `DOC-0002`\n", ""),
    )
    result = healthy_repo.run("VAL-005")
    assert result.status == "FAIL"
    assert "ORPHANED_CANONICAL_DOCUMENT" in codes(result)


# --- VAL-010 completeness --------------------------------------------------


def test_specification_missing_a_core_section_is_rejected(repo: FixtureRepo) -> None:
    repo.add_doc(
        "DOC-0001",
        "docs/apex-app-docs/runtime/orchestrator.md",
        body="# Orchestrator\n\nNo sections at all.\n",
        omit_fields=("dependencies", "consumers"),
        frontmatter_overrides={"purpose": "purpose:", "scope": "scope:"},
    ).write()
    result = repo.run("VAL-010")
    assert result.status == "FAIL"
    assert "MISSING_REQUIRED_SECTION" in codes(result)


def test_frontmatter_satisfies_a_section_requirement(healthy_repo: FixtureRepo) -> None:
    """Structured metadata counts; the rule must not demand duplicated prose."""
    result = healthy_repo.run("VAL-010")
    assert result.status == "PASS"


# --- VAL-013 state machine coverage ----------------------------------------


def test_stateful_runtime_spec_without_a_state_machine_is_rejected(
    repo: FixtureRepo,
) -> None:
    # Stateful vocabulary without a state-model section or structural table.
    # "state transition" as a literal phrase would itself count as structure,
    # so the prose deliberately avoids it.
    stateful = (
        "# Orchestrator\n\n## Purpose\nRuns things.\n\n## Scope\nRuntime.\n\n"
        "## Failure Handling\nIt fails.\n\n"
        "## Behaviour\n"
        "The worker is running, then idle, then paused, then running again. "
        "A paused worker resumes running. An idle worker becomes running. "
        "Terminal workers stop. Startup precedes shutdown. "
        "Running, idle, paused, terminal, startup, shutdown.\n"
    )
    repo.add_doc(
        "DOC-0001", "docs/apex-app-docs/runtime/orchestrator.md", body=stateful
    ).write()
    result = repo.run("VAL-013")
    assert result.status == "FAIL"
    assert "MISSING_STATE_MACHINE" in codes(result)


def test_stateless_document_is_not_required_to_have_a_state_machine(
    repo: FixtureRepo,
) -> None:
    """Absence of a state machine in a stateless contract is correct."""
    repo.add_doc(
        "DOC-0001",
        "docs/apex-app-docs/runtime/orchestrator.md",
        body="# Orchestrator\n\n## Purpose\nA schema.\n\n## Scope\nFields only.\n\n"
        "## Failure Handling\nNone.\n",
    ).write()
    result = repo.run("VAL-013")
    assert result.status == "PASS"


# --- VAL-011 terminology ---------------------------------------------------


def test_glossary_loads_and_terminology_runs(healthy_repo: FixtureRepo) -> None:
    """A parse failure silently disables this validator, so coverage is asserted."""
    result = healthy_repo.run("VAL-011")
    assert result.status == "PASS"
    assert result.checked_items > 0
    assert "GLOSSARY_MISSING" not in warning_codes(result)


def test_missing_glossary_is_reported(healthy_repo: FixtureRepo) -> None:
    (healthy_repo.root / "docs/apex-repository-docs/registries/GLOSSARY.md").unlink()
    result = healthy_repo.run("VAL-011")
    assert "GLOSSARY_MISSING" in warning_codes(result)


# --- VAL-009 ADR consistency -----------------------------------------------


def test_adr_consumer_not_referencing_the_decision_is_reported(
    healthy_repo: FixtureRepo,
) -> None:
    healthy_repo.edit(
        "docs/apex-app-docs/runtime/orchestrator.md",
        lambda t: t.replace("DOC-0003", "DOC-0001").replace(
            "0001-fixture-decision.md", "unrelated.md"
        ),
    )
    result = healthy_repo.run("VAL-009")
    assert "ADR_NOT_ACKNOWLEDGED" in warning_codes(result)


# --- VAL-016 ownership -----------------------------------------------------


def test_non_owner_declaring_owned_domains_is_reported(healthy_repo: FixtureRepo) -> None:
    """The document keeps owned_domains while the registry demotes its role."""
    healthy_repo.edit(
        "docs/apex-repository-docs/registries/DOCUMENT-REGISTRY.md",
        lambda t: t.replace(
            "| DOC-0002 | docs/apex-app-docs/runtime/worker-pool.md | Worker Pool | "
            "Product Specification | Runtime | Specification | Canonical | Active | "
            "Runtime Team | 1.0.0 | Owner |",
            "| DOC-0002 | docs/apex-app-docs/runtime/worker-pool.md | Worker Pool | "
            "Product Specification | Runtime | Specification | Canonical | Active | "
            "Runtime Team | 1.0.0 | Reference |",
        ),
    )
    result = healthy_repo.run("VAL-016")
    assert "OWNED_DOMAIN_WITHOUT_OWNERSHIP" in warning_codes(result)


# --- VAL-015 cross-domain contradictions -----------------------------------


def test_conflicting_quantitative_claim_is_reported(repo: FixtureRepo) -> None:
    """The check that was previously dead code."""
    repo.add_doc(
        "DOC-0001",
        "docs/apex-app-docs/architecture/apex-kernel.md",
        domain="Architecture",
        body="# Kernel\n\n## Purpose\nP\n\n## Scope\nS\n\n"
        "## Notes\nKernel handshake window = 250ms\n",
    )
    repo.add_doc(
        "DOC-0002",
        "docs/apex-app-docs/runtime/orchestrator.md",
        domain="Runtime",
        body="# Orchestrator\n\n## Purpose\nP\n\n## Scope\nS\n\n"
        "## Notes\nKernel handshake window = 900ms\n",
    )
    repo.write()
    result = repo.run("VAL-015")
    assert "CROSS_DOMAIN_VALUE_CONFLICT" in warning_codes(result)


def test_scoped_claims_are_not_treated_as_conflicts(repo: FixtureRepo) -> None:
    """Qualified statements describe different cases, not a disagreement."""
    repo.add_doc(
        "DOC-0001",
        "docs/apex-app-docs/architecture/apex-kernel.md",
        domain="Architecture",
        body="# Kernel\n\n## Purpose\nP\n\n## Scope\nS\n\n"
        "## Notes\nKernel handshake window = 250ms for small deployments\n",
    )
    repo.add_doc(
        "DOC-0002",
        "docs/apex-app-docs/runtime/orchestrator.md",
        domain="Runtime",
        body="# Orchestrator\n\n## Purpose\nP\n\n## Scope\nS\n\n"
        "## Notes\nKernel handshake window = 900ms for large deployments\n",
    )
    repo.write()
    result = repo.run("VAL-015")
    assert "CROSS_DOMAIN_VALUE_CONFLICT" not in warning_codes(result)


# --- VAL-008 traceability --------------------------------------------------


def test_unresolvable_traceability_endpoint_is_rejected(healthy_repo: FixtureRepo) -> None:
    healthy_repo.edit(
        "docs/apex-repository-docs/registries/TRACEABILITY-REGISTRY.md",
        lambda t: t.replace("| DOC-0001 | Defines |", "| DOC-8888 | Defines |"),
    )
    result = healthy_repo.run("VAL-008")
    assert result.status == "FAIL"
    assert "TRACEABILITY_ID_UNRESOLVED" in codes(result)


def test_invalid_relationship_type_is_rejected(healthy_repo: FixtureRepo) -> None:
    healthy_repo.edit(
        "docs/apex-repository-docs/registries/TRACEABILITY-REGISTRY.md",
        lambda t: t.replace("| Defines |", "| Vibes |"),
    )
    result = healthy_repo.run("VAL-008")
    assert result.status == "FAIL"
    assert "INVALID_RELATIONSHIP_TYPE" in codes(result)
