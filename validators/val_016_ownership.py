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
    VERSION = "1.1.0"
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

        # Declared domain ownership must agree with the registry.
        #
        # `owned_domains` is an authority declaration: it states that a document
        # owns concepts within a domain. The field is only meaningful when it
        # agrees with the document's registered concept role and domain,
        # otherwise it silently asserts an authority the registry does not
        # recognise. Nothing previously read this field at all.
        for doc_id, entry in context.document_registry.items():
            md_file = context.repository_root / entry.path
            if not md_file.exists():
                continue
            metadata, _ = MetadataParser.parse(md_file)
            if not metadata:
                continue
            declared = metadata.get("owned_domains") or []
            if not isinstance(declared, list):
                continue
            declared = [str(d).strip() for d in declared if str(d).strip()]

            if entry.concept_role == "Owner":
                if not declared:
                    checked += 1
                    warnings.append(ValidationWarning(
                        code="OWNED_DOMAIN_UNDECLARED",
                        file=entry.path, line=1,
                        message=f"Owner {doc_id} declares no owned_domains",
                        severity="WARNING",
                        rule="A document with concept_role Owner should declare the domain it owns concepts in.",
                        suggestion=f"Add '{entry.domain}' to owned_domains in {entry.path}.",
                    ))
                for domain in declared:
                    if domain != entry.domain:
                        checked += 1
                        warnings.append(ValidationWarning(
                            code="OWNED_DOMAIN_MISMATCH",
                            file=entry.path, line=1,
                            message=(
                                f"Owner {doc_id} declares owned_domains '{domain}' but is "
                                f"registered in domain '{entry.domain}'"
                            ),
                            severity="WARNING",
                            rule="Declared owned_domains must match the document's registered domain.",
                            suggestion=(
                                f"Align owned_domains with '{entry.domain}', or move {doc_id} "
                                f"into the '{domain}' domain if that is its true home."
                            ),
                        ))
            elif declared:
                checked += 1
                warnings.append(ValidationWarning(
                    code="OWNED_DOMAIN_WITHOUT_OWNERSHIP",
                    file=entry.path, line=1,
                    message=(
                        f"Document {doc_id} has concept_role '{entry.concept_role}' but "
                        f"declares owned_domains {declared}"
                    ),
                    severity="WARNING",
                    rule="Only documents with concept_role Owner may declare owned_domains.",
                    suggestion=(
                        f"Clear owned_domains in {entry.path}, or correct its concept role "
                        f"if it genuinely owns concepts."
                    ),
                ))

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
