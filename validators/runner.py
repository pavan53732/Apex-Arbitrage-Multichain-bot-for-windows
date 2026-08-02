"""
Validator Runner - Orchestrates validator execution in fixed order.
"""

from __future__ import annotations
import sys
import time
import json
import importlib
from pathlib import Path
from datetime import datetime, timezone
from typing import Any
from dataclasses import dataclass, field, asdict

from validator_sdk import (
    BaseValidator,
    ValidationContext,
    ValidationResult,
    ValidatorConfig,
    find_repo_root,
    setup_logger,
)


@dataclass
class AggregateResult:
    """Aggregate result from all validators."""
    overall_status: str  # PASS | FAIL
    timestamp: str
    total_execution_time_ms: int
    fail_fast_at: str | None
    results: list[ValidationResult]

    def to_dict(self) -> dict:
        return {
            "overall_status": self.overall_status,
            "timestamp": self.timestamp,
            "total_execution_time_ms": self.total_execution_time_ms,
            "fail_fast_at": self.fail_fast_at,
            "results": [r.to_dict() for r in self.results],
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)

    def summary(self) -> str:
        """Human-readable summary."""
        lines = [
            f"Validation Summary",
            f"==================",
            f"Overall: {self.overall_status}",
            f"Time: {self.total_execution_time_ms}ms",
            f"",
        ]

        for r in self.results:
            status_icon = "✓" if r.status == "PASS" else "✗"
            lines.append(f"  {status_icon} {r.validator_id} ({r.validator_name}): {r.status} ({r.execution_time_ms}ms) - {len(r.errors)} errors, {len(r.warnings)} warnings")

        if self.fail_fast_at:
            lines.append(f"\nFail-fast triggered at: {self.fail_fast_at}")

        return "\n".join(lines)

    def exit_code(self) -> int:
        """Determine exit code per standard."""
        if self.overall_status == "FAIL":
            return 2
        if any(r.severity == "WARNING" for r in self.results):
            return 1
        return 0


class ValidatorRunner:
    """Orchestrates validator execution in fixed order."""

    # Fixed execution order per Validation Specification
    VALIDATOR_SEQUENCE = [
        "VAL-006",  # Generated Artifact Guard (FAIL-FAST)
        "VAL-002",  # Metadata Validator
        "VAL-001",  # Cross-Reference Validator
        "VAL-004",  # Registry Consistency Validator
        "VAL-003",  # Concept Uniqueness Validator
        "VAL-008",  # Traceability Validator
        "VAL-005",  # Orphan Detector
        "VAL-007",  # Document-Class Validator
        "VAL-018",  # Validator Coverage (INFO-only)
        "VAL-010",  # Specification Completeness
        "VAL-013",  # State Machine Coverage
        "VAL-014",  # Interface Contract
        "VAL-009",  # ADR Consistency
        "VAL-016",  # Ownership Fitness
        "VAL-011",  # Terminology
        "VAL-012",  # Semantic Drift
        "VAL-015",  # Cross-Domain Consistency
        "VAL-017",  # Documentation Quality
    ]
    FAIL_FAST_VALIDATORS = {"VAL-006"}

    # Minimum inspection expected of each validator, expressed as a fraction of
    # the discovered markdown corpus.
    #
    # A validator that inspects nothing reports PASS, because a run with no
    # findings is indistinguishable from a run that never looked. That makes a
    # silently broken validator invisible: replacing its document loop with an
    # empty sequence produces a green suite. The floor closes that hole by
    # asserting each validator actually did work proportional to the corpus.
    #
    # Fractions rather than absolute counts, so the floor scales as documents
    # are added and does not have to be revised on every corpus change.
    #
    # Values are per-validator because inspection counts are not uniform. A
    # validator iterating every markdown file reaches a ratio of 1.0, while one
    # driven by registry entries or a narrow document class reaches far less.
    # Applying a single fraction to all of them would either misfire on the
    # selective validators or be too weak to detect a broken one.
    #
    # Each floor is set to roughly half the ratio observed on both the real
    # corpus and the test fixture, which detects a validator that has stopped
    # working while tolerating normal variation in repository composition.
    COVERAGE_FLOOR: dict[str, float] = {
        "VAL-001": 0.50,   # every markdown file
        "VAL-002": 0.50,   # every markdown file
        "VAL-003": 0.50,   # registry-driven, scales with concepts
        "VAL-004": 1.00,   # multiple passes per registered document
        "VAL-005": 1.00,   # several reachability passes per document
        "VAL-006": 0.50,   # every markdown file
        "VAL-007": 0.60,   # multiple class checks per registered document
        "VAL-008": 0.15,   # traceability relationships only
        "VAL-010": 0.50,   # every markdown file
        "VAL-011": 0.50,   # every markdown file
        "VAL-012": 0.50,   # every registered document
        "VAL-013": 0.50,   # every markdown file
        "VAL-014": 0.50,   # every registered document
        "VAL-015": 0.10,   # cross-domain pairs and derived documents only
        "VAL-016": 0.15,   # owner documents only
        "VAL-017": 0.50,   # every markdown file
        "VAL-018": 0.50,   # every markdown file
        # VAL-009 is excluded deliberately: it inspects ADRs only. A
        # corpus-proportional floor is meaningless for a validator scoped to a
        # fixed handful of documents.
    }

    # Absolute floor for validators whose scope is a small fixed set.
    ABSOLUTE_COVERAGE_FLOOR: dict[str, int] = {
        "VAL-009": 1,      # at least one ADR must be inspected
    }

    # Module mapping
    VALIDATOR_MODULES = {
        "VAL-001": "val_001_crossref",
        "VAL-002": "val_002_metadata",
        "VAL-003": "val_003_concept",
        "VAL-004": "val_004_registry",
        "VAL-005": "val_005_orphan",
        "VAL-006": "val_006_generated",
        "VAL-007": "val_007_class",
        "VAL-008": "val_008_traceability",
        "VAL-009": "val_009_adr",
        "VAL-010": "val_010_completeness",
        "VAL-011": "val_011_terminology",
        "VAL-012": "val_012_drift",
        "VAL-013": "val_013_statemachine",
        "VAL-014": "val_014_interfaces",
        "VAL-015": "val_015_crossdomain",
        "VAL-016": "val_016_ownership",
        "VAL-017": "val_017_quality",
        "VAL-018": "val_018_coverage",
    }

    def __init__(self, repo_root: Path | None = None, config: ValidatorConfig | None = None):
        self.repo_root = repo_root or find_repo_root()
        self.config = config or ValidatorConfig.load(self.repo_root)
        self.logger = setup_logger("validator.runner")

    def load_validator(self, validator_id: str) -> BaseValidator:
        """Load validator class and instantiate."""
        module_name = self.VALIDATOR_MODULES.get(validator_id)
        if not module_name:
            raise ValueError(f"Unknown validator: {validator_id}")

        try:
            module = importlib.import_module(module_name)
            # Find the validator class (should be named Validator)
            validator_class = getattr(module, "Validator", None)
            if not validator_class:
                # Try to find class with matching VALIDATOR_ID
                for name in dir(module):
                    obj = getattr(module, name)
                    if isinstance(obj, type) and issubclass(obj, BaseValidator) and obj != BaseValidator:
                        if getattr(obj, "VALIDATOR_ID", "") == validator_id:
                            validator_class = obj
                            break

            if not validator_class:
                raise ValueError(f"No validator class found in {module_name} for {validator_id}")

            return validator_class(self.config)
        except ImportError as e:
            raise ImportError(f"Failed to load validator {validator_id}: {e}")

    def build_context(self, changed_files: list[Path] = None) -> ValidationContext:
        """Build validation context with all registries and files."""
        from validator_sdk import RegistryLoader, MarkdownDiscovery

        concept_registry, document_registry, traceability_registry = RegistryLoader.load_all(self.repo_root)
        all_markdown = MarkdownDiscovery.find_all(self.repo_root, self.config)

        return ValidationContext(
            repository_root=self.repo_root,
            changed_files=changed_files or [],
            all_markdown_files=all_markdown,
            concept_registry=concept_registry,
            document_registry=document_registry,
            traceability_registry=traceability_registry,
            config=self.config,
            previous_results=[],
        )

    def expected_coverage(self, validator_id: str, corpus_size: int) -> int:
        """Minimum `checked_items` expected of a validator for this corpus.

        Returns 0 when no floor is configured, which disables the check for
        that validator rather than failing it.
        """
        absolute = self.ABSOLUTE_COVERAGE_FLOOR.get(validator_id)
        if absolute is not None:
            return absolute
        fraction = self.COVERAGE_FLOOR.get(validator_id)
        if fraction is None:
            return 0
        return int(corpus_size * fraction)

    def _enforce_coverage_floor(
        self,
        validator: BaseValidator,
        validator_id: str,
        result: ValidationResult,
        corpus_size: int,
    ) -> ValidationResult:
        """Convert an under-inspecting validator into an execution error.

        A validator that reports PASS while having inspected nothing has not
        validated anything; it has merely declined to look. Treating that as a
        pass lets a silently broken validator hide behind a green suite, so it
        is reported as an execution error (exit code 3 territory) rather than
        as a passing result.

        The check is skipped when the corpus itself is empty, since inspecting
        nothing is then the correct outcome.
        """
        if corpus_size == 0:
            return result
        if result.status == "ERROR":
            return result

        expected = self.expected_coverage(validator_id, corpus_size)
        if expected <= 0 or result.checked_items >= expected:
            return result

        self.logger.error(
            f"{validator_id} inspected {result.checked_items} items, "
            f"below the expected floor of {expected} for a corpus of {corpus_size}"
        )
        return validator._result_error(
            result.checked_items,
            f"Coverage floor breached: {validator_id} inspected "
            f"{result.checked_items} item(s) against an expected minimum of "
            f"{expected} for a corpus of {corpus_size} markdown file(s). A "
            f"validator that inspects nothing cannot report a meaningful pass; "
            f"this usually means its discovery loop is broken or misconfigured.",
        )

    def run(self, changed_files: list[Path] = None) -> AggregateResult:
        """Run all validators in sequence."""
        self.logger.info("Starting validation run")
        start_time = time.perf_counter()

        context = self.build_context(changed_files)
        corpus_size = len(context.all_markdown_files)
        results = []
        fail_fast_at = None

        for validator_id in self.VALIDATOR_SEQUENCE:
            self.logger.info(f"Running {validator_id}")
            validator = self.load_validator(validator_id)

            try:
                result = validator.validate(context)
            except Exception as e:
                self.logger.error(f"Validator {validator_id} crashed: {e}")
                result = validator._result_error(0, str(e))
            else:
                result = self._enforce_coverage_floor(validator, validator_id, result, corpus_size)

            results.append(result)
            context.previous_results.append(result)

            # Log result
            status_icon = "✓" if result.status == "PASS" else "✗"
            self.logger.info(f"  {status_icon} {validator_id}: {result.status} ({result.execution_time_ms}ms) - {len(result.errors)} errors, {len(result.warnings)} warnings")

            # Fail-fast check
            if validator_id in self.FAIL_FAST_VALIDATORS and result.status == "FAIL":
                self.logger.warning(f"Fail-fast triggered at {validator_id}")
                fail_fast_at = validator_id
                break

        total_time = int((time.perf_counter() - start_time) * 1000)
        overall_status = "PASS" if all(r.status == "PASS" for r in results) else "FAIL"

        aggregate = AggregateResult(
            overall_status=overall_status,
            timestamp=datetime.now(timezone.utc).isoformat(),
            total_execution_time_ms=total_time,
            fail_fast_at=fail_fast_at,
            results=results,
        )

        self.logger.info(f"Validation complete: {overall_status} ({total_time}ms)")
        return aggregate

    def run_single(self, validator_id: str, changed_files: list[Path] = None) -> ValidationResult:
        """Run a single validator."""
        context = self.build_context(changed_files)
        validator = self.load_validator(validator_id)
        return validator.validate(context)


def main():
    """Main entry point for runner."""
    import argparse

    parser = argparse.ArgumentParser(description="Repository Validator Runner")
    parser.add_argument("--validator", help="Run single validator (e.g., VAL-001)")
    parser.add_argument("--changed", nargs="+", help="Changed files to validate")
    parser.add_argument("--repo-root", help="Repository root path")
    parser.add_argument("--json", action="store_true", help="Output JSON only")
    parser.add_argument("--verbose", action="store_true", help="Verbose logging")

    args = parser.parse_args()

    repo_root = Path(args.repo_root) if args.repo_root else None
    runner = ValidatorRunner(repo_root)

    if args.verbose:
        import logging
        logging.getLogger().setLevel(logging.DEBUG)

    changed_files = [Path(f) for f in args.changed] if args.changed else None

    if args.validator:
        result = runner.run_single(args.validator, changed_files)
        output = result.to_json()
    else:
        aggregate = runner.run(changed_files)
        output = aggregate.to_json() if args.json else aggregate.summary()

    print(output)

    # Exit with appropriate code
    if args.validator:
        sys.exit(0 if result.status == "PASS" else (1 if result.severity == "WARNING" else 2))
    else:
        sys.exit(aggregate.exit_code())


if __name__ == "__main__":
    main()