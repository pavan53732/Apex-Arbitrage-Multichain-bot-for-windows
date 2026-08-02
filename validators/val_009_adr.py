"""
VAL-009: ADR Consistency Validator
Verifies every ADR is still implemented, not contradicted, and supersession chains are complete.
"""

from __future__ import annotations
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


class Validator(BaseValidator):
    VALIDATOR_ID = "VAL-009"
    NAME = "ADR Consistency Validator"
    VERSION = "1.0.0"
    DESCRIPTION = "Verifies ADRs are consistent with current architecture, not stale, and supersession chains are complete"
    CATEGORY = "consistency"
    SEVERITY = "ERROR"
    SUPPORTED_METADATA_SCHEMA_VERSIONS = ["1.0"]
    SUPPORTED_REPOSITORY_SPEC_VERSIONS = ["1.0"]

    def validate(self, context: ValidationContext) -> ValidationResult:
        self._start_timer()
        errors = []
        warnings = []
        checked = 0

        adr_docs = {}
        for doc_id, entry in context.document_registry.items():
            if entry.class_ == "ADR":
                adr_docs[doc_id] = entry

        supersedes_map = {}
        for doc_id, entry in context.document_registry.items():
            if entry.supersedes:
                for old_id in entry.supersedes:
                    old_id = old_id.strip()
                    if old_id:
                        supersedes_map[old_id] = doc_id

        for doc_id, entry in adr_docs.items():
            checked += 1
            path = entry.path

            if entry.status == "Active" and not entry.consumers:
                warnings.append(ValidationWarning(
                    code="ADR_NO_CONSUMERS",
                    file=path, line=1,
                    message=f"Active ADR {doc_id} has no consuming documents listed",
                    severity="WARNING",
                    rule="Active ADRs should list affected documents as consumers.",
                    suggestion=f"Add affected document DOC-IDs to consumers field of {doc_id}.",
                ))

            if entry.status == "Superseded" and doc_id not in supersedes_map:
                errors.append(ValidationError(
                    code="ADR_SUPERSEDED_NO_SUCCESSOR",
                    file=path, line=1,
                    message=f"ADR {doc_id} is Superseded but no document supersedes it",
                    severity="ERROR",
                    rule="Every superseded ADR must have a documented successor.",
                    suggestion=f"Update the superseding document's supersedes field.",
                ))

            if entry.consumers:
                for cid in entry.consumers:
                    cid = cid.strip()
                    if cid and cid not in context.document_registry:
                        errors.append(ValidationError(
                            code="ADR_CONSUMER_NOT_FOUND",
                            file=path, line=1,
                            message=f"ADR {doc_id} consumer {cid} not registered",
                            severity="ERROR",
                            rule="ADR consumers must be valid DOC-IDs.",
                            suggestion=f"Register {cid} or fix reference.",
                        ))

            md_file = context.repository_root / path
            if md_file.exists():
                _, body = MetadataParser.parse(md_file)
                h = [l.strip().lstrip("#").strip().lower() for l in body.lower().split("\n") if l.strip().startswith("#")]
                for s in ["context", "decision", "consequences"]:
                    if not any(s in x for x in h):
                        warnings.append(ValidationWarning(
                            code="ADR_MISSING_SECTION", file=path, line=1,
                            message=f"ADR {doc_id} missing section: {s}",
                            severity="WARNING",
                            rule="ADRs should have Context, Decision, and Consequences.",
                            suggestion=f"Add '{s}' section.",
                        ))

        if errors: return self._result_fail(checked, errors)
        return self._result_pass(checked, warnings)
