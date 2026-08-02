"""
VAL-018: Validator Coverage Validator
Reports which documents are covered by which validators and identifies gaps.
"""

from __future__ import annotations
from collections import defaultdict
from pathlib import Path
from validator_sdk import (
    BaseValidator,
    ValidationContext,
    ValidationError,
    ValidationWarning,
    ErrorCode,
    format_error,
    MetadataParser,
)


# Expected validators per document class and authority
CLASS_AUTHORITY_EXPECTATIONS = {
    ("Specification", "Canonical"): ["VAL-002", "VAL-001", "VAL-004", "VAL-005", "VAL-007", "VAL-010"],
    ("Specification", "Derived"):   ["VAL-002", "VAL-001", "VAL-004", "VAL-007"],
    ("Guide", "Canonical"):         ["VAL-002", "VAL-001", "VAL-004", "VAL-005", "VAL-007"],
    ("Guide", "Derived"):           ["VAL-002", "VAL-001", "VAL-004", "VAL-007"],
    ("Reference", "Canonical"):     ["VAL-002", "VAL-001", "VAL-004", "VAL-005", "VAL-007"],
    ("Reference", "Derived"):       ["VAL-002", "VAL-001", "VAL-004", "VAL-007"],
    ("Reference", "Reference"):     ["VAL-002", "VAL-001", "VAL-004", "VAL-007"],
    ("Index", "Canonical"):         ["VAL-002", "VAL-001", "VAL-004", "VAL-005", "VAL-007"],
    ("Index", "Derived"):           ["VAL-002", "VAL-001", "VAL-004", "VAL-007"],
    ("ADR", "Canonical"):           ["VAL-002", "VAL-001", "VAL-004", "VAL-007", "VAL-009"],
    ("Policy", "Canonical"):        ["VAL-002", "VAL-001", "VAL-004", "VAL-005", "VAL-007"],
    ("Policy", "Derived"):          ["VAL-002", "VAL-001", "VAL-004", "VAL-007"],
    ("Registry", "Canonical"):      ["VAL-002", "VAL-001", "VAL-004", "VAL-007"],
    ("Registry", "Derived"):        ["VAL-002", "VAL-001", "VAL-004", "VAL-007"],
    ("Workflow", "Canonical"):      ["VAL-002", "VAL-001", "VAL-004", "VAL-005", "VAL-007"],
    ("Historical", "Historical"):   ["VAL-002", "VAL-001", "VAL-004", "VAL-007"],
    ("Historical", "Derived"):      ["VAL-002", "VAL-001", "VAL-004", "VAL-007"],
}

ALL_VALIDATORS = [
    "VAL-001", "VAL-002", "VAL-003", "VAL-004", "VAL-005",
    "VAL-006", "VAL-007", "VAL-008", "VAL-009", "VAL-010",
    "VAL-011", "VAL-012", "VAL-013", "VAL-014", "VAL-015",
    "VAL-016", "VAL-017", "VAL-018",
]

VALIDATOR_DESCRIPTIONS = {
    "VAL-001": "Cross-Reference Validator",
    "VAL-002": "Metadata Validator",
    "VAL-003": "Concept Uniqueness Validator",
    "VAL-004": "Registry Consistency Validator",
    "VAL-005": "Orphan Detector",
    "VAL-006": "Generated Artifact Guard",
    "VAL-007": "Document Class Validator",
    "VAL-008": "Traceability Validator",
    "VAL-009": "ADR Consistency Validator",
    "VAL-010": "Specification Completeness Validator",
    "VAL-011": "Terminology Validator",
    "VAL-012": "Semantic Drift Validator",
    "VAL-013": "State Machine Coverage Validator",
    "VAL-014": "Interface Contract Validator",
    "VAL-015": "Cross-Domain Consistency Validator",
    "VAL-016": "Ownership Fitness Validator",
    "VAL-017": "Documentation Quality Validator",
    "VAL-018": "Validator Coverage Validator",
}


class Validator(BaseValidator):
    VALIDATOR_ID = "VAL-018"
    NAME = "Validator Coverage Validator"
    VERSION = "1.0.0"
    DESCRIPTION = "Reports validator coverage for each document and identifies gaps"
    CATEGORY = "governance"
    SEVERITY = "INFO"
    SUPPORTED_METADATA_SCHEMA_VERSIONS = ["1.0"]
    SUPPORTED_REPOSITORY_SPEC_VERSIONS = ["1.0"]

    def validate(self, context: ValidationContext) -> ValidationResult:
        self._start_timer()
        infos = []
        checked = 0

        coverage_map: dict[str, list[str]] = defaultdict(list)
        uncovered_validators: dict[str, int] = defaultdict(int)
        doc_count = 0

        for md_file in context.all_markdown_files:
            checked += 1
            rel_path = md_file.relative_to(context.repository_root)
            rel_str = str(rel_path).replace("\\", "/")

            metadata, _ = MetadataParser.parse(md_file)
            if not metadata:
                continue

            doc_id = metadata.get("document_id", "unknown")
            doc_class = metadata.get("class", "")
            authority = metadata.get("authority", "")
            declared = metadata.get("validator_coverage", [])

            if not isinstance(declared, list):
                declared = []

            # Record actual coverage
            coverage_map[doc_id] = declared
            doc_count += 1

            # Get expected coverage
            expected = CLASS_AUTHORITY_EXPECTATIONS.get((doc_class, authority), [])
            if not expected:
                continue

            # Check for gaps: expected but not declared
            gaps = [v for v in expected if v not in declared]
            if gaps:
                rel_str_short = rel_str
                for v in gaps:
                    uncovered_validators[v] += 1
                    infos.append(ValidationWarning(
                        code="COVERAGE_GAP",
                        file=rel_str_short,
                        line=1,
                        message=f"Document {doc_id} ({rel_str_short}) is not covered by {v} ({VALIDATOR_DESCRIPTIONS.get(v, v)}). "
                                f"Expected coverage for class={doc_class}, authority={authority}.",
                        severity="INFO",
                        rule=f"Documents of class {doc_class} with authority {authority} should be covered by {', '.join(expected)}.",
                        suggestion=f"Add {v} to validator_coverage or verify it does not apply to this document.",
                    ))

        # Summary: how many documents are covered by each validator
        validator_doc_count: dict[str, int] = defaultdict(int)
        for doc_id, covered in coverage_map.items():
            for v in covered:
                validator_doc_count[v] += 1

        # Report zero-coverage validators
        for v in ALL_VALIDATORS:
            if v.startswith("VAL-0") and int(v.split("-")[1]) <= 8 and validator_doc_count.get(v, 0) == 0:
                infos.append(ValidationWarning(
                    code="VALIDATOR_NO_COVERAGE",
                    file="",
                    line=1,
                    message=f"Existing validator {v} ({VALIDATOR_DESCRIPTIONS.get(v, v)}) has zero documents declaring coverage.",
                    severity="WARNING",
                    rule="All existing validators should be referenced by the documents they cover.",
                    suggestion=f"Update validator_coverage on relevant documents to include {v}.",
                ))

        # Report coverage statistics
        covered_docs = len([d for d, c in coverage_map.items() if c])
        infos.append(ValidationWarning(
            code="COVERAGE_SUMMARY",
            file="",
            line=1,
            message=f"Coverage summary: {covered_docs}/{doc_count} documents have declared validator_coverage. "
                    f"{doc_count - covered_docs} documents have no validator_coverage.",
            severity="INFO",
            rule="All documents should declare which validators cover them.",
            suggestion="Add validator_coverage to documents that currently have an empty list.",
        ))

        # Per-validator gap counts
        for v, count in sorted(uncovered_validators.items(), key=lambda x: -x[1]):
            infos.append(ValidationWarning(
                code="COVERAGE_GAP_COUNT",
                file="",
                line=1,
                message=f"Validator {v} ({VALIDATOR_DESCRIPTIONS.get(v, v)}) is missing from {count} documents that should include it.",
                severity="INFO",
                rule="Each validator should cover all documents of the appropriate class and authority.",
                suggestion=f"Review {count} documents and add {v} to their validator_coverage if applicable.",
            ))

        return self._result_pass(checked, infos)
