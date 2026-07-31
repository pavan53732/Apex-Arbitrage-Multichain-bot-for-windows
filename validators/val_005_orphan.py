"""
VAL-005: Orphan Detector
Ensures important documents are reachable from index surfaces.
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
    MarkdownDiscovery,
)


class Validator(BaseValidator):
    VALIDATOR_ID = "VAL-005"
    NAME = "Orphan Detector"
    VERSION = "1.0.0"
    DESCRIPTION = "Ensures important documents are reachable from index surfaces"
    CATEGORY = "orphan"
    SEVERITY = "ERROR"
    SUPPORTED_METADATA_SCHEMA_VERSIONS = ["1.0"]
    SUPPORTED_REPOSITORY_SPEC_VERSIONS = ["1.0"]

    def validate(self, context: ValidationContext) -> ValidationError:
        self._start_timer()
        errors = []
        warnings = []
        checked = 0

        document_registry = context.document_registry
        concept_registry = context.concept_registry
        traceability_registry = context.traceability_registry

        # 1. Build reachability map from domain READMEs
        reachable_docs = set()
        reachable_concepts = set()

        # Find all domain READMEs and their navigation
        for md_file in context.all_markdown_files:
            rel_path = md_file.relative_to(context.repository_root)
            rel_str = str(rel_path).replace("\\", "/")

            if rel_path.name == "README.md" and "README.md" in rel_str:
                # This is a domain/subdomain README
                metadata, body = MetadataParser.parse(md_file)
                # Parse Canonical Owner Map and Subdomain Navigation
                self._extract_reachable_from_readme(body, reachable_docs, reachable_concepts)

        # Also check Documentation Map
        doc_map_path = context.repository_root / "docs" / "repository-operating-model" / "documentation-lifecycle" / "documentation-map.md"
        if doc_map_path.exists():
            _, body = MetadataParser.parse(doc_map_path)
            self._extract_reachable_from_readme(body, reachable_docs, reachable_concepts)

        # 2. Check every Canonical document is reachable
        for doc_id, entry in document_registry.items():
            if entry.authority == "Canonical" and entry.status == "Active":
                checked += 1
                if doc_id not in reachable_docs:
                    errors.append(ValidationError(
                        code=ErrorCode.ORPHANED_CANONICAL_DOCUMENT,
                        file=entry.path,
                        line=1,
                        message=format_error(ErrorCode.ORPHANED_CANONICAL_DOCUMENT, doc_id=doc_id),
                        severity="ERROR",
                        rule="Every Canonical document must be reachable from domain README or Documentation Map",
                        suggestion=f"Add {doc_id} to appropriate domain README navigation"
                    ))

        # 3. Check every active concept is listed in at least one domain README
        for concept_id, concept in concept_registry.items():
            if concept.status == "Active":
                checked += 1
                if concept_id not in reachable_concepts:
                    # Allow some concepts to not be in READMEs (e.g., internal registry concepts)
                    if concept.domain not in ("Registries", "Standards", "Validation", "Traceability", "Workflows"):
                        warnings.append(ValidationWarning(
                            code=ErrorCode.ORPHANED_ACTIVE_CONCEPT_WARN,
                            file="",
                            line=1,
                            message=f"Active concept {concept_id} not listed in any domain README Canonical Owner Map",
                            severity="WARNING",
                            rule="Active concepts should be listed in domain README Canonical Owner Maps",
                            suggestion=f"Add {concept_id} to appropriate domain README"
                        ))

        # 4. Check no Active document has zero inbound traceability (unless standalone)
        inbound_traces = defaultdict(int)
        for trace in traceability_registry.values():
            inbound_traces[trace.target_id] += 1

        for doc_id, entry in document_registry.items():
            if entry.status == "Active" and entry.authority in ("Canonical", "Derived"):
                checked += 1
                if inbound_traces[doc_id] == 0:
                    # Check if it's explicitly standalone (e.g., root README, AGENTS.md)
                    if entry.path not in ("README.md", "AGENTS.md", "REBUILD-SYSTEM-SPECIFICATION.md", "REPOSITORY-EXECUTION-MODEL.md"):
                        warnings.append(ValidationWarning(
                            code=ErrorCode.ORPHANED_CANONICAL_DOCUMENT,
                            file=entry.path,
                            line=1,
                            message=f"Active document {doc_id} has no inbound traceability relationships",
                            severity="WARNING",
                            rule="Active documents should have traceability relationships",
                            suggestion=f"Add traceability from consuming documents to {doc_id}"
                        ))

        # 5. Check no domain folder without README
        domain_folders = set()
        for md_file in context.all_markdown_files:
            rel = md_file.relative_to(context.repository_root)
            parts = rel.parts
            if len(parts) >= 2 and parts[0] == "docs":
                domain = parts[1]
                domain_folders.add(domain)

        for domain in domain_folders:
            checked += 1
            readme_path = context.repository_root / "docs" / domain / "README.md"
            if not readme_path.exists():
                errors.append(ValidationError(
                    code=ErrorCode.DOMAIN_WITHOUT_README,
                    file=f"docs/{domain}/README.md",
                    line=1,
                    message=format_error(ErrorCode.DOMAIN_WITHOUT_README, domain=domain),
                    severity="ERROR",
                    rule="Every domain folder must have a README.md",
                    suggestion=f"Create docs/{domain}/README.md per README Governance Standard"
                ))

        if errors:
            return self._result_fail(checked, errors)
        return self._result_pass(checked, warnings)

    def _extract_reachable_from_readme(self, body: str, reachable_docs: set, reachable_concepts: set):
        """Extract DOC-IDs and CONCEPT-IDs from README navigation sections."""
        import re

        # Find DOC-IDs in markdown links
        doc_links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", body)
        for text, link in doc_links:
            # Check if link points to a document
            if ".md" in link:
                # Extract potential DOC-ID from path or nearby text
                pass

        # Find explicit DOC-ID references
        doc_ids = re.findall(r"DOC-\d{4}", body)
        reachable_docs.update(doc_ids)

        # Find explicit CONCEPT-ID references
        concept_ids = re.findall(r"CONCEPT-\d{4}", body)
        reachable_concepts.update(concept_ids)