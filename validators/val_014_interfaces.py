"""
VAL-014: Interface Contract Validator
Verifies every interface producer has a consumer and every consumer references an existing contract.
"""

from __future__ import annotations
from pathlib import Path
from collections import defaultdict
from validator_sdk import (
    BaseValidator,
    ValidationContext,
    ValidationError,
    ValidationWarning,
    ErrorCode,
    format_error,
    MetadataParser,
)


INTERFACE_DOMAINS = {"Interfaces", "API", "IPC", "Events", "Messages"}


class Validator(BaseValidator):
    VALIDATOR_ID = "VAL-014"
    NAME = "Interface Contract Validator"
    VERSION = "1.0.0"
    DESCRIPTION = "Verifies interface producers have consumers and consumers reference existing contracts"
    CATEGORY = "completeness"
    SEVERITY = "WARNING"
    SUPPORTED_METADATA_SCHEMA_VERSIONS = ["1.0"]
    SUPPORTED_REPOSITORY_SPEC_VERSIONS = ["1.0"]

    def validate(self, context: ValidationContext) -> ValidationResult:
        self._start_timer()
        errors = []
        warnings = []
        checked = 0

        # Build interface producer and consumer maps
        producer_docs = []  # (doc_id, path, consumers_field)
        consumer_map = defaultdict(list)  # doc_id -> [consuming doc_ids]

        for doc_id, entry in context.document_registry.items():
            # Documents in interface domains or with interface-related content
            if entry.domain in INTERFACE_DOMAINS or entry.class_ == "Specification":
                if entry.consumers:
                    consumers = [c.strip() for c in entry.consumers if c.strip()]
                    if consumers:
                        producer_docs.append((doc_id, entry.path, consumers))
                        for c in consumers:
                            consumer_map[c].append(doc_id)

        # Check each producer has at least one consumer
        for doc_id, path, consumers in producer_docs:
            checked += 1
            rel_str = path

            if not consumers:
                errors.append(ValidationError(
                    code="ORPHAN_INTERFACE",
                    file=rel_str,
                    line=1,
                    message=f"Interface producer {doc_id} has no consumers. Every interface must have at least one consumer.",
                    severity="WARNING",
                    rule="Every interface producer must have at least one consumer.",
                    suggestion=f"Register consumers for {doc_id} in the Document Registry or mark it as deprecated.",
                ))

            # Verify each consumer exists in document registry
            for consumer_id in consumers:
                if consumer_id not in context.document_registry:
                    errors.append(ValidationError(
                        code="UNRESOLVED_CONSUMER",
                        file=rel_str,
                        line=1,
                        message=f"Consumer {consumer_id} of {doc_id} is not registered in Document Registry",
                        severity="ERROR",
                        rule="All consumers must be registered DOC-IDs.",
                        suggestion=f"Register {consumer_id} or fix the consumer reference.",
                    ))

        # Check documents in runtime domains reference an interface contract
        runtime_domains = {"Runtime", "Execution", "AI", "Market", "Windows", "Plugins"}
        for md_file in context.all_markdown_files:
            checked += 1
            rel_path = md_file.relative_to(context.repository_root)
            rel_str = str(rel_path).replace("\\", "/")

            metadata, body = MetadataParser.parse(md_file)
            if not metadata:
                continue

            doc_id = metadata.get("document_id", "unknown")
            domain = metadata.get("domain", "")
            authority = metadata.get("authority", "")

            if domain not in runtime_domains:
                continue
            if authority not in ("Canonical",):
                continue

            # Check if document has any interface references
            import re
            doc_refs = re.findall(r"DOC-\d{4}", body)
            interface_refs = [
                ref for ref in doc_refs
                if ref in context.document_registry
                and context.document_registry[ref].domain in INTERFACE_DOMAINS
            ]

            if not interface_refs and "Specification" in metadata.get("class", ""):
                warnings.append(ValidationWarning(
                    code="NO_INTERFACE_REFERENCE",
                    file=rel_str,
                    line=1,
                    message=f"Runtime specification {doc_id} has no references to interface contracts",
                    severity="WARNING",
                    rule="Runtime specifications should reference their interface contracts.",
                    suggestion=f"Add interface contract references (IPC, API, events) to {rel_str}.",
                ))

        if errors:
            return self._result_fail(checked, errors)
        return self._result_pass(checked, warnings)
