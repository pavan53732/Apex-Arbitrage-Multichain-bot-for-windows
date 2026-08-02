"""
VAL-016: Ownership Fitness Validator
Checks that owner documents are authoritative — not stubs or superseded.
"""

from __future__ import annotations
from pathlib import Path
from validator_sdk import (
    BaseValidator, ValidationContext, ValidationError, ValidationWarning,
    ErrorCode, format_error, MetadataParser,
)

MIN_LINES = 30

class Validator(BaseValidator):
    VALIDATOR_ID = "VAL-016"
    NAME = "Ownership Fitness Validator"
    VERSION = "1.0.0"
    DESCRIPTION = "Verifies owner documents are authoritative, not stubs or superseded"
    CATEGORY = "ownership"
    SEVERITY = "WARNING"
    SUPPORTED_METADATA_SCHEMA_VERSIONS = ["1.0"]
    SUPPORTED_REPOSITORY_SPEC_VERSIONS = ["1.0"]

    def validate(self, context: ValidationContext) -> ValidationResult:
        self._start_timer()
        errors = []
        warnings = []
        checked = 0

        for doc_id, entry in context.document_registry.items():
            if entry.concept_role != "Owner":
                continue
            checked += 1
            path = entry.path
            md_file = context.repository_root / path

            if not md_file.exists():
                errors.append(ValidationError(
                    code="OWNER_FILE_MISSING", file=path, line=1,
                    message=f"Owner {doc_id} not found at {path}",
                    severity="ERROR",
                    rule="Owner documents must exist.", suggestion=f"Restore {path}.",
                ))
                continue

            if entry.status == "Superseded":
                errors.append(ValidationError(
                    code="OWNER_SUPERSEDED", file=path, line=1,
                    message=f"Owner {doc_id} is superseded",
                    severity="ERROR",
                    rule="Superseded docs cannot be owners.",
                    suggestion="Transfer ownership or change concept_role.",
                ))
                continue

            try:
                content = md_file.read_text(encoding="utf-8")
                _, body = MetadataParser.parse(md_file)
                bl = [l for l in body.split("\n") if l.strip() and not l.strip().startswith("#")]
                if len(bl) < MIN_LINES:
                    warnings.append(ValidationWarning(
                        code="OWNER_STUB", file=path, line=1,
                        message=f"Owner {doc_id} has {len(bl)} content lines (<{MIN_LINES})",
                        severity="WARNING",
                        rule="Owner docs must be substantial.", suggestion="Expand or reassign.",
                    ))
                if not entry.related_concepts or all(not c.strip() for c in entry.related_concepts):
                    warnings.append(ValidationWarning(
                        code="OWNER_NO_CONCEPT", file=path, line=1,
                        message=f"Owner {doc_id} has no related_concepts",
                        severity="WARNING",
                        rule="Owners must declare related concepts.",
                        suggestion="Add CONCEPT-ID.",
                    ))
            except Exception:
                warnings.append(ValidationWarning(
                    code="OWNER_READ_ERROR", file=path, line=1,
                    message=f"Cannot read {doc_id}", severity="WARNING",
                    rule="Owner docs must be readable.", suggestion="Check file.",
                ))

        if errors: return self._result_fail(checked, errors)
        return self._result_pass(checked, warnings)
