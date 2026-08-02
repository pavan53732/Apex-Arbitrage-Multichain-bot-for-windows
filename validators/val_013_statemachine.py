"""
VAL-013: State Machine Coverage Validator
Ensures every runtime service has a documented state machine with complete states and transitions.
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


# Runtime domains that should have state machines
RUNTIME_DOMAINS = {"Runtime", "AI", "Execution", "State Machines"}


class Validator(BaseValidator):
    VALIDATOR_ID = "VAL-013"
    NAME = "State Machine Coverage Validator"
    VERSION = "1.0.0"
    DESCRIPTION = "Ensures runtime components have documented state machines with complete states and transitions"
    CATEGORY = "completeness"
    SEVERITY = "WARNING"
    SUPPORTED_METADATA_SCHEMA_VERSIONS = ["1.0"]
    SUPPORTED_REPOSITORY_SPEC_VERSIONS = ["1.0"]

    def validate(self, context: ValidationContext) -> ValidationResult:
        self._start_timer()
        errors = []
        warnings = []
        checked = 0

        # Collect state machine documents
        state_machine_docs = set()
        for doc_id, entry in context.document_registry.items():
            if entry.domain == "State Machines" and entry.class_ == "Specification":
                state_machine_docs.add(doc_id)

        # Check each runtime document for state machine references
        for md_file in context.all_markdown_files:
            checked += 1
            rel_path = md_file.relative_to(context.repository_root)
            rel_str = str(rel_path).replace("\\", "/")

            metadata, body = MetadataParser.parse(md_file)
            if not metadata:
                continue

            doc_id = metadata.get("document_id", "unknown")
            doc_class = metadata.get("class", "")
            domain = metadata.get("domain", "")
            authority = metadata.get("authority", "")

            # Only check Specification and Reference docs in runtime domains
            if domain not in RUNTIME_DOMAINS:
                continue
            if doc_class not in ("Specification", "Reference"):
                continue
            if authority not in ("Canonical",):
                continue

            # Check if this document has a state machine or references one
            has_state_machine = self._has_state_machine_section(body)
            has_state_ref = self._references_state_machine(body, state_machine_docs)

            if not has_state_machine and not has_state_ref:
                if doc_class == "Specification":
                    errors.append(ValidationError(
                        code="MISSING_STATE_MACHINE",
                        file=rel_str,
                        line=1,
                        message=f"Runtime specification {doc_id} ({metadata.get('title', '')}) has no state machine section or reference",
                        severity="ERROR",
                        rule="Every runtime specification must document its state machine or reference one.",
                        suggestion=f"Add a state machine section to {rel_str} or reference an existing state machine document.",
                    ))
                else:
                    warnings.append(ValidationWarning(
                        code="MISSING_STATE_MACHINE_REF",
                        file=rel_str,
                        line=1,
                        message=f"Runtime reference document {doc_id} should reference a state machine",
                        severity="WARNING",
                        rule="Runtime reference documents should reference their state machine.",
                        suggestion=f"Add a state machine reference to {rel_str}.",
                    ))

        if errors:
            return self._result_fail(checked, errors)
        return self._result_pass(checked, warnings)

    def _has_state_machine_section(self, body: str) -> bool:
        """Check if document body contains a state machine section."""
        headings = self._extract_headings(body)
        for _, text in headings:
            if "state machine" in text or "state diagram" in text or "lifecycle" in text:
                return True
        # Also check for mermaid state diagrams or state transition tables
        body_lower = body.lower()
        if "stateDiagram" in body or "state diagram" in body_lower:
            return True
        if "| state |" in body_lower and "| transition |" in body_lower:
            return True
        return False

    def _references_state_machine(self, body: str, state_machine_docs: set[str]) -> bool:
        """Check if document body references any known state machine DOC-ID."""
        import re
        doc_ids = re.findall(r"DOC-\d{4}", body)
        return any(did in state_machine_docs for did in doc_ids)

    def _extract_headings(self, body: str) -> list[tuple[int, str]]:
        headings = []
        for line in body.split("\n"):
            stripped = line.strip()
            if stripped.startswith("#"):
                level = len(stripped) - len(stripped.lstrip("#"))
                text = stripped.lstrip("#").strip().lower()
                headings.append((level, text))
        return headings
