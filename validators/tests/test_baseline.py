"""The baseline fixture must be accepted by every validator.

This is the control for every other test in the suite. If a defect test asserts
that a validator rejects a mutated fixture, that assertion only means something
when the unmutated fixture is accepted — otherwise the rejection could be
incidental.
"""

from __future__ import annotations

import pytest

from conftest import FixtureRepo

from runner import ValidatorRunner


@pytest.mark.parametrize("validator_id", ValidatorRunner.VALIDATOR_SEQUENCE)
def test_healthy_repository_passes_every_validator(
    healthy_repo: FixtureRepo, validator_id: str
) -> None:
    result = healthy_repo.run(validator_id)
    assert result.status == "PASS", (
        f"{validator_id} rejected the healthy baseline: "
        + "; ".join(e.message for e in result.errors[:3])
    )


@pytest.mark.parametrize("validator_id", ValidatorRunner.VALIDATOR_SEQUENCE)
def test_every_validator_inspects_something(
    healthy_repo: FixtureRepo, validator_id: str
) -> None:
    """A validator that inspects nothing cannot report a meaningful pass."""
    result = healthy_repo.run(validator_id)
    assert result.checked_items > 0, f"{validator_id} inspected nothing"


@pytest.mark.parametrize("validator_id", ValidatorRunner.VALIDATOR_SEQUENCE)
def test_results_are_schema_compliant(
    healthy_repo: FixtureRepo, validator_id: str
) -> None:
    """Findings must sit in the channel their severity declares."""
    result = healthy_repo.run(validator_id)
    for error in result.errors:
        assert error.severity in ("ERROR", "CRITICAL"), (
            f"{validator_id} placed a {error.severity} finding in errors"
        )
    for warning in result.warnings:
        assert warning.severity == "WARNING", (
            f"{validator_id} placed a {warning.severity} finding in warnings"
        )


@pytest.mark.parametrize("validator_id", ValidatorRunner.VALIDATOR_SEQUENCE)
def test_every_finding_carries_a_rule_id(
    healthy_repo: FixtureRepo, validator_id: str
) -> None:
    """Findings bind to an immutable governance rule."""
    result = healthy_repo.run(validator_id)
    for finding in list(result.errors) + list(result.warnings):
        assert finding.rule_id.startswith("ROM-"), (
            f"{validator_id} emitted a finding without a ROM rule id"
        )
        assert finding.validator_id == validator_id


@pytest.mark.parametrize("validator_id", ValidatorRunner.VALIDATOR_SEQUENCE)
def test_validators_are_deterministic(
    healthy_repo: FixtureRepo, validator_id: str
) -> None:
    """Same input must produce the same output, per the implementation contract."""
    first = healthy_repo.run(validator_id)
    second = healthy_repo.run(validator_id)
    assert first.status == second.status
    assert first.checked_items == second.checked_items
    assert [e.message for e in first.errors] == [e.message for e in second.errors]
