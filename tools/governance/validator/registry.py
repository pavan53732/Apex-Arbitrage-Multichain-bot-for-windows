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


def list_validators() -> list[ValidatorDescriptor]:
    """Return the full validator registry, in stable declaration order."""
    return list(VALIDATOR_REGISTRY)


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
    same underlying document/graph pass.
    """
    results = []
    seen_in_engine = False
    for descriptor in list_validators():
        if descriptor.layer != "architecture-test":
            if seen_in_engine:
                continue
            seen_in_engine = True
        results.append(run_validator(descriptor, repo_root))
    return results
