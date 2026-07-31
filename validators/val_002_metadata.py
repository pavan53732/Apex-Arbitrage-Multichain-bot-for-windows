"""
VAL-002: Metadata Validator
Validates all documents have complete, valid frontmatter metadata.
"""

from __future__ import annotations
from pathlib import Path
import re
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
    VALIDATOR_ID = "VAL-002"
    NAME = "Metadata Validator"
    VERSION = "1.0.0"
    DESCRIPTION = "Verifies all documents have complete, valid frontmatter metadata"
    CATEGORY = "metadata"
    SEVERITY = "ERROR"
    SUPPORTED_METADATA_SCHEMA_VERSIONS = ["1.0"]
    SUPPORTED_REPOSITORY_SPEC_VERSIONS = ["1.0"]

    def validate(self, context: ValidationContext) -> ValidationError:
        self._start_timer()
        errors = []
        warnings = []
        checked = 0

        schema_version = "1.0"
        vc = context.config.validator_configs.get("VAL-002", {})
        strict = vc.get("strict_enum_validation", True)

        for md_file in context.all_markdown_files:
            checked += 1
            rel_path = md_file.relative_to(context.repository_root)
            rel_str = str(rel_path).replace("\\", "/")

            # Parse metadata
            metadata, body = MetadataParser.parse(md_file)

            # Skip files without frontmatter (they'll be caught as missing required fields)
            if not metadata:
                errors.append(ValidationError(
                    code=ErrorCode.MISSING_REQUIRED_FIELD,
                    file=rel_str,
                    line=1,
                    message=format_error(ErrorCode.MISSING_REQUIRED_FIELD, field="frontmatter"),
                    severity="ERROR",
                    rule="All documents must have YAML frontmatter",
                    suggestion="Add frontmatter with all required fields"
                ))
                continue

            # Validate metadata
            validation_errors = MetadataParser.validate(metadata, schema_version)

            for field, expected, actual in validation_errors:
                if field == "document_id" and not re.match(r"^DOC-\d{4}$", str(actual)):
                    errors.append(ValidationError(
                        code=ErrorCode.INVALID_ID_FORMAT,
                        file=rel_str,
                        line=1,
                        message=format_error(ErrorCode.INVALID_ID_FORMAT, field=field, expected="DOC-XXXX", value=actual),
                        severity="ERROR",
                        rule="Document ID must be DOC-XXXX format",
                        suggestion=f"Change {field} to valid DOC-XXXX format"
                    ))
                elif field == "metadata_schema_version":
                    errors.append(ValidationError(
                        code=ErrorCode.INVALID_SCHEMA_VERSION,
                        file=rel_str,
                        line=1,
                        message=format_error(ErrorCode.INVALID_SCHEMA_VERSION, expected=expected, value=actual),
                        severity="ERROR",
                        rule=f"metadata_schema_version must be {expected}",
                        suggestion=f"Set metadata_schema_version to {expected}"
                    ))
                elif field in ("plane", "authority", "status", "class"):
                    if strict:
                        errors.append(ValidationError(
                            code=ErrorCode.INVALID_ENUM_VALUE,
                            file=rel_str,
                            line=1,
                            message=format_error(ErrorCode.INVALID_ENUM_VALUE, field=field, value=actual, options=expected),
                            severity="ERROR",
                            rule=f"{field} must be valid enum value",
                            suggestion=f"Change {field} to one of: {expected}"
                        ))
                    else:
                        warnings.append(ValidationWarning(
                            code=ErrorCode.INVALID_ENUM_VALUE,
                            file=rel_str,
                            line=1,
                            message=format_error(ErrorCode.INVALID_ENUM_VALUE, field=field, value=actual, options=expected),
                            rule=f"{field} should be valid enum value",
                            suggestion=f"Change {field} to one of: {expected}"
                        ))
                else:
                    errors.append(ValidationError(
                        code=ErrorCode.MISSING_REQUIRED_FIELD,
                        file=rel_str,
                        line=1,
                        message=format_error(ErrorCode.MISSING_REQUIRED_FIELD, field=field),
                        severity="ERROR",
                        rule=f"Required field {field} is missing",
                        suggestion=f"Add {field} to frontmatter"
                    ))

            # Additional checks for DOC-ID format in related_concepts
            related = metadata.get("related_concepts", [])
            if isinstance(related, list):
                for concept in related:
                    if not re.match(r"^CONCEPT-\d{4}$", str(concept)):
                        errors.append(ValidationError(
                            code=ErrorCode.INVALID_ID_FORMAT,
                            file=rel_str,
                            line=1,
                            message=format_error(ErrorCode.INVALID_ID_FORMAT, field="related_concepts", expected="CONCEPT-XXXX", value=concept),
                            severity="ERROR",
                            rule="related_concepts must be CONCEPT-XXXX format",
                            suggestion=f"Fix concept ID format: {concept}"
                        ))

            # Check dependencies
            deps = metadata.get("dependencies", [])
            if isinstance(deps, list):
                for dep in deps:
                    if not re.match(r"^DOC-\d{4}$", str(dep)):
                        errors.append(ValidationError(
                            code=ErrorCode.INVALID_ID_FORMAT,
                            file=rel_str,
                            line=1,
                            message=format_error(ErrorCode.INVALID_ID_FORMAT, field="dependencies", expected="DOC-XXXX", value=dep),
                            severity="ERROR",
                            rule="dependencies must be DOC-XXXX format",
                            suggestion=f"Fix dependency ID format: {dep}"
                        ))

            # Check supersedes/superseded_by
            for field in ("supersedes", "superseded_by"):
                items = metadata.get(field, [])
                if isinstance(items, list):
                    for item in items:
                        if not re.match(r"^DOC-\d{4}$", str(item)):
                            errors.append(ValidationError(
                                code=ErrorCode.INVALID_ID_FORMAT,
                                file=rel_str,
                                line=1,
                                message=format_error(ErrorCode.INVALID_ID_FORMAT, field=field, expected="DOC-XXXX", value=item),
                                severity="ERROR",
                                rule=f"{field} must be DOC-XXXX format",
                                suggestion=f"Fix {field} ID format: {item}"
                            ))

            # Check last_updated format
            last_updated = metadata.get("last_updated")
            if last_updated and not re.match(r"^\d{4}-\d{2}-\d{2}$", str(last_updated)):
                errors.append(ValidationError(
                    code=ErrorCode.INVALID_DATE_FORMAT,
                    file=rel_str,
                    line=1,
                    message=format_error(ErrorCode.INVALID_DATE_FORMAT, field="last_updated", value=last_updated),
                    severity="ERROR",
                    rule="last_updated must be YYYY-MM-DD format",
                    suggestion="Fix date format to YYYY-MM-DD"
                ))

        if errors:
            return self._result_fail(checked, errors)
        return self._result_pass(checked, warnings)