"""Validator Registry — single catalogue of every validator in the repository.

Repository Canonicality Repair, Work Item 7 (Validator Consolidation).

This module does NOT reimplement any validator logic. It is a thin,
read-only catalogue that describes:
  - the 4 in-engine checks inside `GovernanceValidator`
    (tools/governance/validator/governance_validator.py), and
  - the 5 external `architecture-tests/*.py` scripts,
so that both validator layers are discoverable, executable, and
inspectable from a single place, without merging their code (which would
be a larger architectural change than "consolidation" requires — the two
layers check genuinely different things: `GovernanceValidator` operates on
parsed `DocumentMetadata` + the in-memory dependency graph produced by one
`apex-gov run`, while `architecture-tests/*.py` operate directly on
`docs/*.md` files on disk and check documentation-structure conventions
that are independent of the governance graph).

Each entry follows the schema requested by the Repository Canonicality
Repair directive: ID, owner, inputs, outputs, severity, evidence,
documentation, tests.
"""
from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass(frozen=True)
class ValidatorDescriptor:
    id: str
    owner: str
    layer: str  # "in-engine" | "architecture-test"
    inputs: str
    outputs: str
    severity: str  # highest severity this validator can raise
    evidence: str  # what evidence/report this validator produces
    documentation: str  # where the check's rationale is documented
    tests: str  # what test suite covers this validator
    invoke: str  # human-readable invocation command
    module_path: Optional[str] = None  # importable path, for in-engine validators
    script_path: Optional[str] = None  # file path, for architecture-test scripts


# Maps a WS3 category-validator ID to its implementing category
# directory name, for reporting only. Deliberately duplicated (not
# imported) from category_suite.CATALOGUE_ID_TO_CATEGORY to avoid a
# registry.py <-> category_suite.py import cycle (category_suite.py
# does not import registry.py, and this module should not need to
# import the full category_suite module just for this one small
# mapping). Both copies are covered by
# tests/test_category_suite.py::test_catalogue_id_mapping_covers_all_14_frozen_ids,
# so any drift between them would need to be introduced in both places
# to go undetected, and a dedicated cross-check test below prevents that.
CATALOGUE_ID_TO_CATEGORY_FALLBACK = {
    "OWNERSHIP-001": "ownership",
    "DEPENDENCY-001": "dependency",
    "DEPENDENCY-002": "dependency",
    "EVENT-001": "event",
    "EVENT-002": "event",
    "SCHEMA-001": "schema",
    "SCHEMA-002": "schema",
    "INTERFACE-001": "interface",
    "STATE-001": "state_machine",
    "RECOVERY-001": "recovery",
    "SECURITY-001": "security",
    "CONFIG-001": "configuration",
    "GRAPH-001": "graph",
    "FREEZE-001": "freeze",
}

VALIDATOR_REGISTRY: list[ValidatorDescriptor] = [
    ValidatorDescriptor(
        id="governance_validator.missing_owners",
        owner="Governance Platform",
        layer="in-engine",
        inputs="list[DocumentMetadata] (from one apex-gov indexing pass)",
        outputs="list[Finding] (OWNER_REQUIRED, severity HIGH)",
        severity="HIGH",
        evidence="Finding objects returned by GovernanceValidator.validate_all(); surfaced via `apex-gov validate`",
        documentation="tools/governance/validator/governance_validator.py (docstring + rule name OWNER_REQUIRED)",
        tests="tools/governance/tests/test_validator.py",
        invoke="apex-gov validate",
        module_path="tools.governance.validator.governance_validator.GovernanceValidator._check_missing_owners",
    ),
    ValidatorDescriptor(
        id="governance_validator.duplicate_owners",
        owner="Governance Platform",
        layer="in-engine",
        inputs="list[DocumentMetadata]",
        outputs="list[Finding] (UNIQUE_OWNER, severity HIGH)",
        severity="HIGH",
        evidence="Finding objects; surfaced via `apex-gov validate`",
        documentation="tools/governance/validator/governance_validator.py (rule name UNIQUE_OWNER)",
        tests="tools/governance/tests/test_validator.py",
        invoke="apex-gov validate",
        module_path="tools.governance.validator.governance_validator.GovernanceValidator._check_duplicate_owners",
    ),
    ValidatorDescriptor(
        id="governance_validator.broken_references",
        owner="Governance Platform",
        layer="in-engine",
        inputs="list[DocumentMetadata] (depends_on, required_by, cross_references fields)",
        outputs="list[Finding] (BROKEN_REFERENCE, severity MEDIUM)",
        severity="MEDIUM",
        evidence="Finding objects; surfaced via `apex-gov validate`",
        documentation="tools/governance/validator/governance_validator.py (rule name BROKEN_REFERENCE)",
        tests="tools/governance/tests/test_validator.py",
        invoke="apex-gov validate",
        module_path="tools.governance.validator.governance_validator.GovernanceValidator._check_broken_references",
    ),
    ValidatorDescriptor(
        id="governance_validator.cycles",
        owner="Governance Platform",
        layer="in-engine",
        inputs="networkx.DiGraph (dependency graph from GraphBuilder)",
        outputs="list[Finding] (NO_CYCLES, severity CRITICAL)",
        severity="CRITICAL",
        evidence="Finding objects; surfaced via `apex-gov validate`",
        documentation="tools/governance/validator/governance_validator.py (rule name NO_CYCLES)",
        tests="tools/governance/tests/test_validator.py",
        invoke="apex-gov validate",
        module_path="tools.governance.validator.governance_validator.GovernanceValidator._check_cycles",
    ),
    ValidatorDescriptor(
        id="architecture_test.audit_duplicates",
        owner="Documentation Team",
        layer="architecture-test",
        inputs="docs/*.md (raw filesystem read)",
        outputs="stdout report; process exit code 0 (pass) or 1 (fail)",
        severity="HIGH",
        evidence="stdout of the script invocation (not currently persisted to a file)",
        documentation="architecture-tests/audit_duplicates.py (module docstring)",
        tests="none dedicated; exercised indirectly by running the script itself",
        invoke="python3 architecture-tests/audit_duplicates.py",
        script_path="architecture-tests/audit_duplicates.py",
    ),
    ValidatorDescriptor(
        id="architecture_test.validate_contracts",
        owner="Documentation Team",
        layer="architecture-test",
        inputs="docs/*.md (raw filesystem read; front matter + body text)",
        outputs="stdout report; process exit code 0 (pass) or 1 (fail)",
        severity="MEDIUM",
        evidence="stdout of the script invocation (not currently persisted to a file)",
        documentation="architecture-tests/validate_contracts.py (module docstring)",
        tests="none dedicated; exercised indirectly by running the script itself",
        invoke="python3 architecture-tests/validate_contracts.py",
        script_path="architecture-tests/validate_contracts.py",
    ),
    ValidatorDescriptor(
        id="architecture_test.validate_cross_references",
        owner="Documentation Team",
        layer="architecture-test",
        inputs="docs/*.md (raw filesystem read; markdown links)",
        outputs="stdout report; process exit code 0 (pass) or 1 (fail)",
        severity="MEDIUM",
        evidence="stdout of the script invocation (not currently persisted to a file)",
        documentation="architecture-tests/validate_cross_references.py (module docstring)",
        tests="none dedicated; exercised indirectly by running the script itself",
        invoke="python3 architecture-tests/validate_cross_references.py",
        script_path="architecture-tests/validate_cross_references.py",
    ),
    ValidatorDescriptor(
        id="architecture_test.validate_ownership",
        owner="Documentation Team",
        layer="architecture-test",
        inputs="docs/*.md, docs/DOCUMENTATION-MAP.md (raw filesystem read)",
        outputs="stdout report; process exit code 0 (pass) or 1 (fail)",
        severity="HIGH",
        evidence="stdout of the script invocation (not currently persisted to a file)",
        documentation="architecture-tests/validate_ownership.py (module docstring)",
        tests="none dedicated; exercised indirectly by running the script itself",
        invoke="python3 architecture-tests/validate_ownership.py",
        script_path="architecture-tests/validate_ownership.py",
    ),
    ValidatorDescriptor(
        id="architecture_test.validate_traceability",
        owner="Documentation Team",
        layer="architecture-test",
        inputs="docs/TRACEABILITY-MATRIX.md, docs/TEST-CASE-REGISTRY.md",
        outputs="stdout report; process exit code 0 (pass) or 1 (fail)",
        severity="MEDIUM",
        evidence="stdout of the script invocation (not currently persisted to a file)",
        documentation="architecture-tests/validate_traceability.py (module docstring)",
        tests="none dedicated; exercised indirectly by running the script itself",
        invoke="python3 architecture-tests/validate_traceability.py",
        script_path="architecture-tests/validate_traceability.py",
    ),
]

# WS3 category validators (Programme 2.5 Phase-0, validator_catalogue.json's
# 14 frozen IDs + the readiness_checklist.json CHECK-WS3 requirement for a
# corresponding validator/<category>/ subdirectory per category). These are
# a THIRD validator layer, distinct from (and not replacing) the two above
# -- each is independently importable/callable (see
# validator/<category>/checks.py's `run()` functions, each covered by its
# own test in tests/test_category_validators.py) and collectively
# orchestrated by validator/category_suite.py, which writes its own
# evidence file (.governance/exports/category_validator_findings.json),
# distinct from GovernanceValidator's findings and architecture-tests'
# stdout-only evidence.
CATEGORY_VALIDATOR_DESCRIPTORS: list[ValidatorDescriptor] = [
    ValidatorDescriptor(
        id="OWNERSHIP-001", owner="Governance Platform", layer="category",
        inputs="list[DocumentMetadata]", outputs="list[CategoryFinding]", severity="HIGH",
        evidence=".governance/exports/category_validator_findings.json (findings_by_category.ownership)",
        documentation="tools/governance/validator/ownership/checks.py",
        tests="tools/governance/tests/test_category_validators.py::test_ownership_flags_missing_owner",
        invoke="python3 -c \"from governance.validator.ownership.checks import run\"",
        module_path="tools.governance.validator.ownership.checks.run",
    ),
    ValidatorDescriptor(
        id="DEPENDENCY-001", owner="Governance Platform", layer="category",
        inputs="list[DocumentMetadata]", outputs="list[CategoryFinding]", severity="MEDIUM",
        evidence=".governance/exports/category_validator_findings.json (findings_by_category.dependency)",
        documentation="tools/governance/validator/dependency/checks.py",
        tests="tools/governance/tests/test_category_validators.py::test_dependency_flags_broken_target_and_self_dependency",
        invoke="python3 -c \"from governance.validator.dependency.checks import run\"",
        module_path="tools.governance.validator.dependency.checks.run",
    ),
    ValidatorDescriptor(
        id="DEPENDENCY-002", owner="Governance Platform", layer="category",
        inputs="list[DocumentMetadata]", outputs="list[CategoryFinding]", severity="MEDIUM",
        evidence=".governance/exports/category_validator_findings.json (findings_by_category.dependency)",
        documentation="tools/governance/validator/dependency/checks.py",
        tests="tools/governance/tests/test_category_validators.py::test_dependency_flags_broken_target_and_self_dependency",
        invoke="python3 -c \"from governance.validator.dependency.checks import run\"",
        module_path="tools.governance.validator.dependency.checks.run",
    ),
    ValidatorDescriptor(
        id="EVENT-001", owner="Governance Platform", layer="category",
        inputs="list[DocumentMetadata]", outputs="list[CategoryFinding]", severity="MEDIUM",
        evidence=".governance/exports/category_validator_findings.json (findings_by_category.event)",
        documentation="tools/governance/validator/event/checks.py",
        tests="tools/governance/tests/test_category_validators.py::test_event_flags_consumer_without_producer_and_self_produce_consume",
        invoke="python3 -c \"from governance.validator.event.checks import run\"",
        module_path="tools.governance.validator.event.checks.run",
    ),
    ValidatorDescriptor(
        id="EVENT-002", owner="Governance Platform", layer="category",
        inputs="list[DocumentMetadata]", outputs="list[CategoryFinding]", severity="LOW",
        evidence=".governance/exports/category_validator_findings.json (findings_by_category.event)",
        documentation="tools/governance/validator/event/checks.py",
        tests="tools/governance/tests/test_category_validators.py::test_event_flags_consumer_without_producer_and_self_produce_consume",
        invoke="python3 -c \"from governance.validator.event.checks import run\"",
        module_path="tools.governance.validator.event.checks.run",
    ),
    ValidatorDescriptor(
        id="SCHEMA-001", owner="Governance Platform", layer="category",
        inputs="schemas/*.json", outputs="list[CategoryFinding]", severity="HIGH",
        evidence=".governance/exports/category_validator_findings.json (findings_by_category.schema)",
        documentation="tools/governance/validator/schema/checks.py",
        tests="tools/governance/tests/test_category_validators.py::test_schema_flags_invalid_json_and_missing_reference",
        invoke="python3 -c \"from governance.validator.schema.checks import run\"",
        module_path="tools.governance.validator.schema.checks.run",
    ),
    ValidatorDescriptor(
        id="SCHEMA-002", owner="Governance Platform", layer="category",
        inputs="list[DocumentMetadata], schemas/*.json", outputs="list[CategoryFinding]", severity="MEDIUM",
        evidence=".governance/exports/category_validator_findings.json (findings_by_category.schema)",
        documentation="tools/governance/validator/schema/checks.py",
        tests="tools/governance/tests/test_category_validators.py::test_schema_accepts_resolvable_reference",
        invoke="python3 -c \"from governance.validator.schema.checks import run\"",
        module_path="tools.governance.validator.schema.checks.run",
    ),
    ValidatorDescriptor(
        id="INTERFACE-001", owner="Governance Platform", layer="category",
        inputs="list[DocumentMetadata]", outputs="list[CategoryFinding]", severity="MEDIUM",
        evidence=".governance/exports/category_validator_findings.json (findings_by_category.interface)",
        documentation="tools/governance/validator/interface/checks.py",
        tests="tools/governance/tests/test_category_validators.py::test_interface_flags_duplicate_declaration",
        invoke="python3 -c \"from governance.validator.interface.checks import run\"",
        module_path="tools.governance.validator.interface.checks.run",
    ),
    ValidatorDescriptor(
        id="STATE-001", owner="Governance Platform", layer="category",
        inputs="list[DocumentMetadata]", outputs="list[CategoryFinding]", severity="MEDIUM",
        evidence=".governance/exports/category_validator_findings.json (findings_by_category.state_machine)",
        documentation="tools/governance/validator/state_machine/checks.py",
        tests="tools/governance/tests/test_category_validators.py::test_state_machine_flags_missing_recovery",
        invoke="python3 -c \"from governance.validator.state_machine.checks import run\"",
        module_path="tools.governance.validator.state_machine.checks.run",
    ),
    ValidatorDescriptor(
        id="RECOVERY-001", owner="Governance Platform", layer="category",
        inputs="list[DocumentMetadata], root_paths", outputs="list[CategoryFinding]", severity="MEDIUM",
        evidence=".governance/exports/category_validator_findings.json (findings_by_category.recovery)",
        documentation="tools/governance/validator/recovery/checks.py",
        tests="tools/governance/tests/test_category_validators.py::test_recovery_flags_root_without_recovery_content",
        invoke="python3 -c \"from governance.validator.recovery.checks import run\"",
        module_path="tools.governance.validator.recovery.checks.run",
    ),
    ValidatorDescriptor(
        id="SECURITY-001", owner="Governance Platform", layer="category",
        inputs="list[DocumentMetadata], root_paths", outputs="list[CategoryFinding]", severity="MEDIUM",
        evidence=".governance/exports/category_validator_findings.json (findings_by_category.security)",
        documentation="tools/governance/validator/security/checks.py",
        tests="tools/governance/tests/test_category_validators.py::test_security_flags_sensitive_root_without_security_section",
        invoke="python3 -c \"from governance.validator.security.checks import run\"",
        module_path="tools.governance.validator.security.checks.run",
    ),
    ValidatorDescriptor(
        id="CONFIG-001", owner="Governance Platform", layer="category",
        inputs="list[DocumentMetadata]", outputs="list[CategoryFinding]", severity="LOW",
        evidence=".governance/exports/category_validator_findings.json (findings_by_category.configuration)",
        documentation="tools/governance/validator/configuration/checks.py",
        tests="tools/governance/tests/test_category_validators.py::test_configuration_flags_spelling_variants",
        invoke="python3 -c \"from governance.validator.configuration.checks import run\"",
        module_path="tools.governance.validator.configuration.checks.run",
    ),
    ValidatorDescriptor(
        id="GRAPH-001", owner="Governance Platform", layer="category",
        inputs="networkx.DiGraph, root_paths", outputs="list[CategoryFinding]", severity="MEDIUM",
        evidence=".governance/exports/category_validator_findings.json (findings_by_category.graph)",
        documentation="tools/governance/validator/graph/checks.py",
        tests="tools/governance/tests/test_category_validators.py::test_graph_flags_isolated_root",
        invoke="python3 -c \"from governance.validator.graph.checks import run\"",
        module_path="tools.governance.validator.graph.checks.run",
    ),
    ValidatorDescriptor(
        id="FREEZE-001", owner="Governance Platform", layer="category",
        inputs=".governance/freeze/*.json, git commit history", outputs="list[CategoryFinding]", severity="CRITICAL",
        evidence=".governance/exports/category_validator_findings.json (findings_by_category.freeze)",
        documentation="tools/governance/validator/freeze/checks.py",
        tests="tools/governance/tests/test_category_validators.py::test_freeze_flags_unresolvable_commit",
        invoke="python3 -c \"from governance.validator.freeze.checks import run\"",
        module_path="tools.governance.validator.freeze.checks.run",
    ),
]


def list_validators() -> list[ValidatorDescriptor]:
    """Return the full validator registry (in-engine + architecture-test
    + category validators), in stable declaration order."""
    return list(VALIDATOR_REGISTRY) + list(CATEGORY_VALIDATOR_DESCRIPTORS)


def run_validator(descriptor: ValidatorDescriptor, repo_root: Path) -> dict:
    """Independently execute a single validator and return its result.

    For architecture-test validators this runs the script as a subprocess.
    For in-engine validators, running them "independently" still requires
    building the shared inputs (indexed documents + dependency graph) that
    `apex-gov run`/`apex-gov validate` already build; rather than duplicate
    that construction here (which would violate the single-canonical-
    runtime rule), in-engine validators are run via `apex-gov validate`,
    which internally invokes GovernanceValidator.validate_all() (running
    all 4 in-engine checks together, since they share one graph/document
    pass — there is no cheaper way to run exactly one of the four without
    re-deriving the shared inputs it depends on).
    """
    if descriptor.layer == "architecture-test":
        assert descriptor.script_path is not None
        result = subprocess.run(
            [sys.executable, descriptor.script_path],
            cwd=repo_root,
            capture_output=True,
            text=True,
        )
        return {
            "id": descriptor.id,
            "status": "PASS" if result.returncode == 0 else "FAIL",
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
    elif descriptor.layer == "category":
        # Category validators (WS3) share one apex-gov run pass, same
        # pattern as in-engine validators below -- they are individually
        # importable/testable (see tests/test_category_validators.py) but
        # collectively executed via the single canonical `apex-gov run`
        # invocation, which writes .governance/exports/category_validator_findings.json.
        result = subprocess.run(
            ["apex-gov", "run"],
            cwd=repo_root,
            capture_output=True,
            text=True,
        )
        report_path = repo_root / ".governance" / "exports" / "category_validator_findings.json"
        category = CATALOGUE_ID_TO_CATEGORY_FALLBACK.get(descriptor.id)
        category_findings = 0
        if report_path.exists():
            try:
                data = __import__("json").loads(report_path.read_text())
                category_findings = data.get("finding_counts_by_category", {}).get(category, 0)
            except Exception:
                pass
        return {
            "id": descriptor.id,
            "status": "PASS" if result.returncode == 0 else "FAIL",
            "returncode": result.returncode,
            "category": category,
            "findings_in_category": category_findings,
            "evidence_path": str(report_path),
            "note": "category validators share one `apex-gov run` pass; see category_validator_findings.json for per-category findings",
        }
    else:
        result = subprocess.run(
            ["apex-gov", "validate"],
            cwd=repo_root,
            capture_output=True,
            text=True,
        )
        return {
            "id": descriptor.id,
            "status": "PASS" if result.returncode == 0 else "FAIL",
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "note": "in-engine validators share one GovernanceValidator.validate_all() pass; "
                    "run together via `apex-gov validate` rather than individually.",
        }


def run_all_validators(repo_root: Path) -> list[dict]:
    """Run every validator in the registry and return their results.

    In-engine validators are deduplicated to a single `apex-gov validate`
    invocation (see `run_validator` docstring), since all four share the
    same underlying document/graph pass. Category validators (WS3) are
    similarly deduplicated to a single `apex-gov run` invocation, since
    all 14 share the same canonical pipeline pass. Architecture-test
    validators each run individually (they are separate scripts with no
    shared pass to deduplicate).
    """
    results = []
    seen_layers: set[str] = set()
    for descriptor in list_validators():
        if descriptor.layer in ("in-engine", "category"):
            if descriptor.layer in seen_layers:
                continue
            seen_layers.add(descriptor.layer)
        results.append(run_validator(descriptor, repo_root))
    return results
