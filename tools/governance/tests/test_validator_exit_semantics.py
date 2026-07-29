"""Regression tests for Remediation Item 3 (Validator Exit Semantics).

Prior to this fix, `apex-gov validate` never returned a non-zero exit
code regardless of findings count or severity (confirmed: 2,065 findings
including 11 HIGH-severity, exit code 0). This meant every "validators:
PASS" reported by IntegrityEngine and by ad hoc certification reports
verified only "the validator process did not crash", never "the
repository passed validation" -- two fundamentally different claims that
had been conflated.
"""
import subprocess
import sys
from pathlib import Path

from governance.validator.governance_validator import GovernanceValidator, Finding, Severity


def _repo_root() -> Path:
    return Path(__file__).parent.parent.parent.parent


def test_has_failing_findings_true_for_critical():
    findings = [Finding(path="x.md", severity=Severity.CRITICAL, message="m", rule="R")]
    assert GovernanceValidator.has_failing_findings(findings) is True


def test_has_failing_findings_true_for_high():
    findings = [Finding(path="x.md", severity=Severity.HIGH, message="m", rule="R")]
    assert GovernanceValidator.has_failing_findings(findings) is True


def test_has_failing_findings_false_for_medium_and_below():
    findings = [
        Finding(path="x.md", severity=Severity.MEDIUM, message="m", rule="R"),
        Finding(path="x.md", severity=Severity.LOW, message="m", rule="R"),
        Finding(path="x.md", severity=Severity.INFO, message="m", rule="R"),
    ]
    assert GovernanceValidator.has_failing_findings(findings) is False


def test_has_failing_findings_false_for_no_findings():
    assert GovernanceValidator.has_failing_findings([]) is False


def test_apex_gov_validate_exits_zero_when_no_failing_findings():
    """End-to-end: on the current (fixed) repository state, `apex-gov
    validate` must exit 0, and its own printed RESULT line must say PASS
    -- not merely "did not crash"."""
    result = subprocess.run(
        ["apex-gov", "validate"],
        cwd=_repo_root(),
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"expected exit 0, got {result.returncode}: {result.stdout[-500:]}"
    assert "RESULT: PASS" in result.stdout


def test_apex_gov_validate_prints_a_result_line():
    """Regression guard: the old implementation printed only a bare
    'Findings: N' line with no PASS/FAIL verdict at all."""
    result = subprocess.run(
        ["apex-gov", "validate"],
        cwd=_repo_root(),
        capture_output=True,
        text=True,
    )
    assert "RESULT:" in result.stdout
