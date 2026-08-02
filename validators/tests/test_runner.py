"""Tests for the runner's coverage floor and result routing.

The coverage floor exists because a validator that inspects nothing reports
PASS, making a silently broken validator invisible. These tests hold that
protection in place.
"""

from __future__ import annotations

import pytest

from conftest import FixtureRepo

from runner import ValidatorRunner
from validator_sdk import ValidationError, ValidationWarning
from validator_sdk.base import BaseValidator, ValidationResult


class _Stub(BaseValidator):
    """A validator whose inspection count and findings are dictated by a test."""

    VALIDATOR_ID = "VAL-002"
    NAME = "Stub"
    VERSION = "1.0.0"
    DESCRIPTION = "stub"
    CATEGORY = "test"
    SEVERITY = "ERROR"
    SUPPORTED_METADATA_SCHEMA_VERSIONS = ["1.0"]
    SUPPORTED_REPOSITORY_SPEC_VERSIONS = ["1.0"]

    def __init__(self, config, checked: int = 0, findings=None):
        super().__init__(config)
        self._checked = checked
        self._findings = findings or []

    def validate(self, context):  # pragma: no cover - not used directly
        self._start_timer()
        return self._result_pass(self._checked, self._findings)


@pytest.fixture
def runner(healthy_repo: FixtureRepo) -> ValidatorRunner:
    return ValidatorRunner(healthy_repo.root)


def test_expected_coverage_scales_with_corpus(runner: ValidatorRunner) -> None:
    assert runner.expected_coverage("VAL-002", 300) == 150
    assert runner.expected_coverage("VAL-002", 10) == 5


def test_absolute_floor_used_for_narrowly_scoped_validators(
    runner: ValidatorRunner,
) -> None:
    """A corpus fraction is meaningless for a validator scoped to ADRs."""
    assert runner.expected_coverage("VAL-009", 1_000) == 1


def test_unconfigured_validator_has_no_floor(runner: ValidatorRunner) -> None:
    assert runner.expected_coverage("VAL-999", 300) == 0


def test_validator_inspecting_nothing_becomes_an_execution_error(
    runner: ValidatorRunner, healthy_repo: FixtureRepo
) -> None:
    """The central protection: a dead validator must not report PASS."""
    stub = _Stub(runner.config, checked=0)
    result = stub._result_pass(0, [])
    assert result.status == "PASS"

    enforced = runner._enforce_coverage_floor(stub, "VAL-002", result, corpus_size=300)
    assert enforced.status == "ERROR"
    assert "Coverage floor breached" in enforced.errors[0].message


def test_validator_meeting_the_floor_is_untouched(runner: ValidatorRunner) -> None:
    stub = _Stub(runner.config, checked=300)
    result = stub._result_pass(300, [])
    enforced = runner._enforce_coverage_floor(stub, "VAL-002", result, corpus_size=300)
    assert enforced.status == "PASS"
    assert enforced is result


def test_partial_coverage_below_the_floor_is_caught(runner: ValidatorRunner) -> None:
    stub = _Stub(runner.config, checked=10)
    result = stub._result_pass(10, [])
    enforced = runner._enforce_coverage_floor(stub, "VAL-002", result, corpus_size=300)
    assert enforced.status == "ERROR"


def test_empty_corpus_disables_the_floor(runner: ValidatorRunner) -> None:
    """Inspecting nothing is correct when there is nothing to inspect."""
    stub = _Stub(runner.config, checked=0)
    result = stub._result_pass(0, [])
    enforced = runner._enforce_coverage_floor(stub, "VAL-002", result, corpus_size=0)
    assert enforced.status == "PASS"


def test_existing_execution_error_is_preserved(runner: ValidatorRunner) -> None:
    """A crash reason must not be replaced by a coverage message."""
    stub = _Stub(runner.config)
    crashed = stub._result_error(0, "original crash")
    enforced = runner._enforce_coverage_floor(stub, "VAL-002", crashed, corpus_size=300)
    assert enforced is crashed
    assert "original crash" in enforced.errors[0].message


def test_every_sequenced_validator_has_a_floor() -> None:
    """A validator without a floor is unprotected; that must be deliberate."""
    configured = set(ValidatorRunner.COVERAGE_FLOOR) | set(
        ValidatorRunner.ABSOLUTE_COVERAGE_FLOOR
    )
    missing = set(ValidatorRunner.VALIDATOR_SEQUENCE) - configured
    assert not missing, f"validators without a coverage floor: {sorted(missing)}"


def test_full_run_passes_on_the_healthy_fixture(healthy_repo: FixtureRepo) -> None:
    """End to end: the floor must not fire on a legitimate repository."""
    result = ValidatorRunner(healthy_repo.root).run()
    errored = [r.validator_id for r in result.results if r.status == "ERROR"]
    assert not errored, f"coverage floor misfired on: {errored}"


def test_full_run_detects_a_gutted_validator(
    healthy_repo: FixtureRepo, monkeypatch: pytest.MonkeyPatch
) -> None:
    """The regression this protection was built for."""
    import val_002_metadata

    def blind_validate(self, context):
        self._start_timer()
        return self._result_pass(0, [])

    monkeypatch.setattr(val_002_metadata.Validator, "validate", blind_validate)

    aggregate = ValidatorRunner(healthy_repo.root).run()
    val_002 = next(r for r in aggregate.results if r.validator_id == "VAL-002")
    assert val_002.status == "ERROR"
    assert aggregate.overall_status == "FAIL"


# --- SDK result routing ----------------------------------------------------


def test_findings_route_by_severity(runner: ValidatorRunner) -> None:
    """Severity determines the channel, so the published schema holds."""
    stub = _Stub(runner.config)
    stub._start_timer()
    result = stub._create_result(
        "PASS",
        "INFO",
        1,
        [],
        [
            ValidationWarning(
                code="X", file="f", line=1, message="warn",
                severity="WARNING", rule="r", suggestion="s",
            ),
            ValidationWarning(
                code="Y", file="f", line=1, message="info",
                severity="INFO", rule="r", suggestion="s",
            ),
        ],
    )
    assert len(result.warnings) == 1
    assert len(result.infos) == 1


def test_fail_status_downgrades_when_no_errors_remain(runner: ValidatorRunner) -> None:
    """A result must not claim FAIL on the strength of advisory findings."""
    stub = _Stub(runner.config)
    stub._start_timer()
    result = stub._create_result(
        "FAIL",
        "ERROR",
        1,
        [
            ValidationError(
                code="Z", file="f", line=1, message="downgraded",
                severity="WARNING", rule="r", suggestion="s",
            )
        ],
        [],
    )
    assert result.status == "PASS"
    assert result.errors == []
    assert len(result.warnings) == 1
