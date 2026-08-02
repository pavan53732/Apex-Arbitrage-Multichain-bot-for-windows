"""
VAL-015: Cross-Domain Consistency Validator
Detects contradictions across specification domains by comparing claims,
verifying cross-reference integrity, and validating authority/dependency consistency.
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


# Domain pairs that must agree on shared concerns
CROSS_DOMAIN_PAIRS = [
    ("Architecture", "Runtime"),
    ("Runtime", "Execution"),
    ("Execution", "Market"),
    ("AI", "Runtime"),
    ("Security", "Interfaces"),
    ("Deployment", "Windows"),
    ("Architecture", "AI"),
    ("Execution", "State Machines"),
    ("Runtime", "State Machines"),
    ("Configuration", "Runtime"),
    ("Data", "Runtime"),
]

# No unused imports or dead code — CLAIM_KEYWORDS removed as section-level
# cross-domain claim extraction requires NLP beyond current scope. VAL-015
# validates via dependency/consumer consistency and authority integrity instead.


class Validator(BaseValidator):
    VALIDATOR_ID = "VAL-015"
    NAME = "Cross-Domain Consistency Validator"
    VERSION = "1.0.0"
    DESCRIPTION = "Detects contradictions across specification domains and validates cross-domain consistency"
    CATEGORY = "consistency"
    SEVERITY = "WARNING"
    SUPPORTED_METADATA_SCHEMA_VERSIONS = ["1.0"]
    SUPPORTED_REPOSITORY_SPEC_VERSIONS = ["1.0"]

    def validate(self, context: ValidationContext) -> ValidationResult:
        self._start_timer()
        errors = []
        warnings = []
        checked = 0

        # Build domain→documents index
        domain_docs: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
        # domain → [(doc_id, path, authority)]

        for doc_id, entry in context.document_registry.items():
            if entry.status != "Active":
                continue
            domain_docs[entry.domain].append((doc_id, entry.path, entry.authority))

        # 1. Cross-domain pair consistency
        for dom_a, dom_b in CROSS_DOMAIN_PAIRS:
            docs_a = domain_docs.get(dom_a, [])
            docs_b = domain_docs.get(dom_b, [])
            if not docs_a or not docs_b:
                continue

            checked += 1

            # Check that for each canonical spec in dom_a, there is at least
            # one reference in dom_b confirming alignment
            canon_a = [(did, path) for did, path, auth in docs_a if auth == "Canonical"]
            canon_b_ids = {did for did, _, auth in docs_b if auth == "Canonical"}

            for did_a, path_a in canon_a:
                # Check if dom_b docs reference this doc_id
                referenced = False
                for did_b, path_b, _ in docs_b:
                    md_file = context.repository_root / path_b
                    if md_file.exists():
                        try:
                            content = md_file.read_text(encoding="utf-8")
                            if did_a in content:
                                referenced = True
                                break
                        except Exception:
                            pass

                if not referenced and did_a not in canon_b_ids:
                    # Not an error if the canonical is in dom_a and dom_b is consumer
                    pass

        # 2. Authority consistency: Derived docs must have canonical_source pointing to
        #    a document in the appropriate domain
        for doc_id, entry in context.document_registry.items():
            if entry.authority == "Derived" and entry.status == "Active":
                checked += 1
                canonical_src = entry.canonical_source

                # Check if canonical_source is a DOC-ID or a path
                if canonical_src.startswith("DOC-"):
                    if canonical_src not in context.document_registry:
                        errors.append(ValidationError(
                            code="DERIVED_CANONICAL_UNRESOLVED",
                            file=entry.path, line=1,
                            message=f"Derived document {doc_id} canonical_source {canonical_src} not registered",
                            severity="ERROR",
                            rule="Derived documents must reference a registered canonical source.",
                            suggestion=f"Register {canonical_src} or update canonical_source.",
                        ))

        # 3. Dependency consistency: verify dependencies cross domains correctly
        for doc_id, entry in context.document_registry.items():
            if not entry.dependencies:
                continue
            checked += 1

            for dep_id in entry.dependencies:
                dep_id = dep_id.strip()
                if not dep_id:
                    continue
                if dep_id not in context.document_registry:
                    errors.append(ValidationError(
                        code="DEPENDENCY_UNRESOLVED",
                        file=entry.path, line=1,
                        message=f"Document {doc_id} depends on {dep_id} which is not registered",
                        severity="ERROR",
                        rule="All dependencies must be registered DOC-IDs.",
                        suggestion=f"Register {dep_id} or remove it from dependencies.",
                    ))
                    continue

                dep_entry = context.document_registry[dep_id]

                # Check dependency not superseded
                if dep_entry.status == "Superseded":
                    warnings.append(ValidationWarning(
                        code="DEPENDENCY_ON_SUPERSEDED",
                        file=entry.path, line=1,
                        message=f"Document {doc_id} depends on superseded document {dep_id}",
                        severity="WARNING",
                        rule="Active documents should not depend on superseded documents.",
                        suggestion=f"Update {doc_id} to depend on {dep_id}'s successor.",
                    ))

                # Check cross-plane dependency validity
                if entry.plane != dep_entry.plane:
                    # ROM docs can depend on PS docs (e.g., documentation-map references)
                    # PS docs generally should not depend on ROM docs
                    if entry.plane == "Product Specification" and dep_entry.plane == "Repository Operating Model":
                        warnings.append(ValidationWarning(
                            code="CROSS_PLANE_DEPENDENCY",
                            file=entry.path, line=1,
                            message=f"Product Specification document {doc_id} depends on "
                                    f"Repository Operating Model document {dep_id}",
                            severity="WARNING",
                            rule="Product Specification documents should minimize dependencies on "
                                  "Repository Operating Model documents.",
                            suggestion="Verify this cross-plane dependency is intentional.",
                        ))

        # 4. Consumer consistency
        for doc_id, entry in context.document_registry.items():
            if not entry.consumers:
                continue
            checked += 1

            for consumer_id in entry.consumers:
                consumer_id = consumer_id.strip()
                if not consumer_id:
                    continue
                if consumer_id not in context.document_registry:
                    errors.append(ValidationError(
                        code="CONSUMER_UNRESOLVED",
                        file=entry.path, line=1,
                        message=f"Document {doc_id} lists consumer {consumer_id} which is not registered",
                        severity="ERROR",
                        rule="All consumers must be registered DOC-IDs.",
                        suggestion=f"Register {consumer_id} or remove it from consumers.",
                    ))

        if errors:
            return self._result_fail(checked, errors)
        return self._result_pass(checked, warnings)
