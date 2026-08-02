"""
VAL-010: Specification Completeness Validator
Checks that specification-class documents have required sections.
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


# Required sections per document class
REQUIRED_SECTIONS = {
    "Specification": [
        "Purpose", "Scope", "Dependencies", "Consumers",
        "Architecture", "State Machine", "Failure Handling",
        "Security", "Performance", "Interfaces", "Testing",
    ],
    "Guide": [
        "Purpose", "Scope", "Prerequisites", "Steps",
        "Examples",
    ],
    "ADR": [
        "Context", "Decision", "Consequences",
        "Affected Components", "Status",
    ],
    "Policy": [
        "Purpose", "Scope", "Rules", "Enforcement", "Exceptions",
    ],
    "Reference": [
        "Purpose", "Scope", "Description", "Examples", "Related Documents",
    ],
}

SECTION_WEIGHTS = {
    "Purpose": 10,
    "Scope": 10,
    "Dependencies": 8,
    "Consumers": 8,
    "Architecture": 8,
    "State Machine": 5,
    "Failure Handling": 10,
    "Security": 8,
    "Performance": 5,
    "Interfaces": 8,
    "Testing": 5,
    "Prerequisites": 8,
    "Steps": 8,
    "Examples": 5,
    "Context": 8,
    "Decision": 10,
    "Consequences": 8,
    "Affected Components": 8,
    "Status": 5,
    "Rules": 10,
    "Enforcement": 8,
    "Exceptions": 5,
    "Description": 8,
    "Related Documents": 3,
}


class Validator(BaseValidator):
    VALIDATOR_ID = "VAL-010"
    NAME = "Specification Completeness Validator"
    VERSION = "1.0.0"
    DESCRIPTION = "Checks specification-class documents for required sections"
    CATEGORY = "completeness"
    SEVERITY = "WARNING"
    SUPPORTED_METADATA_SCHEMA_VERSIONS = ["1.0"]
    SUPPORTED_REPOSITORY_SPEC_VERSIONS = ["1.0"]

    def validate(self, context: ValidationContext) -> ValidationResult:
        self._start_timer()
        errors = []
        warnings = []
        infos = []
        checked = 0

        for md_file in context.all_markdown_files:
            checked += 1
            rel_path = md_file.relative_to(context.repository_root)
            rel_str = str(rel_path).replace("\\", "/")

            metadata, body = MetadataParser.parse(md_file)
            if not metadata:
                continue

            doc_id = metadata.get("document_id", "unknown")
            doc_class = metadata.get("class", "")
            authority = metadata.get("authority", "")
            plane = metadata.get("plane", "")
            domain = metadata.get("domain", "")

            required = REQUIRED_SECTIONS.get(doc_class, [])
            if not required:
                continue

            # Extract all headings from body
            headings = self._extract_headings(body)

            # Check each required section
            missing = []
            present = []
            for section in required:
                if self._has_section(section, headings):
                    present.append(section)
                else:
                    missing.append(section)

            completeness_pct = (len(present) / len(required)) * 100 if required else 100

            if missing and authority == "Canonical" and doc_class == "Specification":
                for section in missing:
                    errors.append(ValidationError(
                        code="MISSING_REQUIRED_SECTION",
                        file=rel_str,
                        line=1,
                        message=f"Canonical {doc_class} document {doc_id} ({doc_class}, {domain}) is missing required section: '{section}'",
                        severity="ERROR" if SECTION_WEIGHTS.get(section, 5) >= 8 else "WARNING",
                        rule=f"All Canonical Specification documents must have a '{section}' section.",
                        suggestion=f"Add a '{section}' section to {rel_str}.",
                    ))

            elif missing:
                for section in missing:
                    severity = "WARNING" if SECTION_WEIGHTS.get(section, 5) >= 8 else "INFO"
                    if severity == "WARNING":
                        warnings.append(ValidationWarning(
                            code="MISSING_RECOMMENDED_SECTION",
                            file=rel_str,
                            line=1,
                            message=f"{doc_class} document {doc_id} is missing recommended section: '{section}'",
                            severity="WARNING",
                            rule=f"Documents of class {doc_class} should have a '{section}' section.",
                            suggestion=f"Consider adding a '{section}' section to {rel_str}.",
                        ))

            # Add completeness score info
            infos.append(ValidationWarning(
                code="COMPLETENESS_SCORE",
                file=rel_str,
                line=1,
                message=f"Document {doc_id}: {completeness_pct:.0f}% complete ({len(present)}/{len(required)} sections present)",
                severity="INFO",
                rule="Completeness measured against required sections for document class.",
                suggestion="",
            ))

        if errors:
            return self._result_fail(checked, errors)
        return self._result_pass(checked, warnings + infos)

    def _extract_headings(self, body: str) -> list[tuple[int, str]]:
        headings = []
        for line in body.split("\n"):
            stripped = line.strip()
            if stripped.startswith("#"):
                level = len(stripped) - len(stripped.lstrip("#"))
                text = stripped.lstrip("#").strip().lower()
                headings.append((level, text))
        return headings

    def _has_section(self, section: str, headings: list[tuple[int, str]]) -> bool:
        target = section.lower()
        for _, text in headings:
            if target in text or text in target:
                return True
        return False
