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
    VERSION = "1.1.0"
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

            # Conformance: a document an ADR names as governed must acknowledge
            # the decision. An ADR that records a binding architectural choice
            # while the governed specification never references it leaves the
            # decision unenforced, and a reader of that specification alone has
            # no way to know the constraint exists.
            if entry.status == "Active" and entry.consumers:
                for cid in entry.consumers:
                    cid = cid.strip()
                    if not cid or cid not in context.document_registry:
                        continue
                    consumer = context.document_registry[cid]
                    consumer_file = context.repository_root / consumer.path
                    if not consumer_file.exists():
                        continue
                    checked += 1
                    try:
                        consumer_text = consumer_file.read_text(encoding="utf-8")
                    except Exception:
                        continue
                    # The decision may be cited by ADR identity or by filename.
                    adr_name = Path(path).name
                    if doc_id in consumer_text or adr_name in consumer_text:
                        continue
                    warnings.append(ValidationWarning(
                        code="ADR_NOT_ACKNOWLEDGED",
                        file=consumer.path, line=1,
                        message=(
                            f"Document {cid} is governed by Active ADR {doc_id} "
                            f"but does not reference it"
                        ),
                        severity="WARNING",
                        rule="A document governed by an Active ADR must reference that decision.",
                        suggestion=(
                            f"Reference {doc_id} ({adr_name}) in {consumer.path}, or remove "
                            f"{cid} from the ADR's consumers if it is not governed by the decision."
                        ),
                    ))

        if errors: return self._result_fail(checked, errors)
        return self._result_pass(checked, warnings)
