"""
VAL-004: Registry Consistency Validator
Verifies registries match actual repository state.
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
    RegistryLoader,
    MarkdownDiscovery,
    MetadataParser,
)


class Validator(BaseValidator):
    VALIDATOR_ID = "VAL-004"
    NAME = "Registry Consistency Validator"
    VERSION = "1.0.0"
    DESCRIPTION = "Verifies registries match actual repository state"
    CATEGORY = "registry"
    SEVERITY = "ERROR"
    SUPPORTED_METADATA_SCHEMA_VERSIONS = ["1.0"]
    SUPPORTED_REPOSITORY_SPEC_VERSIONS = ["1.0"]

    def validate(self, context: ValidationContext) -> ValidationError:
        self._start_timer()
        errors = []
        warnings = []
        checked = 0

        # Load current registries
        concept_registry = context.concept_registry
        document_registry = context.document_registry
        traceability_registry = context.traceability_registry

        # 1. Document Registry: every registered document exists at registered path
        for doc_id, entry in document_registry.items():
            checked += 1
            doc_path = context.repository_root / entry.path
            if not doc_path.exists():
                errors.append(ValidationError(
                    code=ErrorCode.REGISTRY_FS_MISMATCH,
                    file=entry.path,
                    line=1,
                    message=format_error(ErrorCode.REGISTRY_FS_MISMATCH, id=doc_id, path=entry.path),
                    severity="ERROR",
                    rule="Every registered document must exist at its registered path",
                    suggestion=f"Restore {entry.path} or remove {doc_id} from Document Registry"
                ))

        # 2. Document Registry: every .md file with DOC-ID is registered
        for md_file in context.all_markdown_files:
            checked += 1
            rel_path = md_file.relative_to(context.repository_root)
            rel_str = str(rel_path).replace("\\", "/")

            metadata, _ = MetadataParser.parse(md_file)
            doc_id = metadata.get("document_id")

            if doc_id and doc_id not in document_registry:
                warnings.append(ValidationWarning(
                    code=ErrorCode.UNREGISTERED_DOCUMENT,
                    file=rel_str,
                    line=1,
                    message=format_error(ErrorCode.UNREGISTERED_DOCUMENT, path=rel_str),
                    severity="WARNING",
                    rule="All documents with DOC-ID should be registered",
                    suggestion=f"Add {doc_id} to Document Registry"
                ))

        # 3. Concept Registry: every canonical owner document exists
        for concept_id, concept in concept_registry.items():
            if concept.status == "Active" and concept.canonical_document:
                checked += 1
                owner_doc_id = concept.canonical_document
                if owner_doc_id in document_registry:
                    owner_entry = document_registry[owner_doc_id]
                    owner_path = context.repository_root / owner_entry.path
                    if not owner_path.exists():
                        errors.append(ValidationError(
                            code=ErrorCode.MISSING_CANONICAL_OWNER,
                            file=owner_entry.path,
                            line=1,
                            message=format_error(ErrorCode.MISSING_CANONICAL_OWNER, concept_id=concept_id),
                            severity="ERROR",
                            rule="Active concepts must have existing canonical owner documents",
                            suggestion=f"Restore {owner_entry.path} or update Concept Registry"
                        ))
                else:
                    errors.append(ValidationError(
                        code=ErrorCode.MISSING_CANONICAL_OWNER,
                        file="",
                        line=1,
                        message=format_error(ErrorCode.MISSING_CANONICAL_OWNER, concept_id=concept_id),
                        severity="ERROR",
                        rule="Active concepts must have registered canonical owner documents",
                        suggestion=f"Register {owner_doc_id} in Document Registry"
                    ))

        # 4. Concept Registry: every active concept has Owner document
        active_concepts = {cid: c for cid, c in concept_registry.items() if c.status == "Active"}
        for concept_id, concept in active_concepts.items():
            checked += 1
            if not concept.canonical_document:
                errors.append(ValidationError(
                    code=ErrorCode.MISSING_CANONICAL_OWNER,
                    file="",
                    line=1,
                    message=format_error(ErrorCode.MISSING_CANONICAL_OWNER, concept_id=concept_id),
                    severity="ERROR",
                    rule="Every active concept must have a canonical owner document",
                    suggestion=f"Assign canonical_document for {concept_id} in Concept Registry"
                ))

        # 5. Traceability Registry: all source/target IDs resolve
        for trace_id, trace in traceability_registry.items():
            checked += 1
            source_ok = trace.source_id in document_registry or trace.source_id in concept_registry
            target_ok = trace.target_id in document_registry or trace.target_id in concept_registry

            if not source_ok or not target_ok:
                errors.append(ValidationError(
                    code=ErrorCode.TRACEABILITY_ID_UNRESOLVED,
                    file="",
                    line=1,
                    message=format_error(ErrorCode.TRACEABILITY_ID_UNRESOLVED, trace_id=trace_id, source_id=trace.source_id, target_id=trace.target_id),
                    severity="ERROR",
                    rule="Traceability relationships must reference valid IDs",
                    suggestion=f"Fix source/target IDs in traceability {trace_id}"
                ))

        # 6. Registry version metadata present
        for reg_name, reg_path in [
            ("Concept Registry", context.repository_root / "docs" / "apex-repository-docs" / "registries" / "CONCEPT-REGISTRY.md"),
            ("Document Registry", context.repository_root / "docs" / "apex-repository-docs" / "registries" / "DOCUMENT-REGISTRY.md"),
            ("Traceability Registry", context.repository_root / "docs" / "apex-repository-docs" / "registries" / "TRACEABILITY-REGISTRY.md"),
        ]:
            checked += 1
            if not reg_path.exists():
                errors.append(ValidationError(
                    code=ErrorCode.REGISTRY_FILE_MISSING,
                    file=str(reg_path.relative_to(context.repository_root)).replace("\\", "/"),
                    line=1,
                    message=format_error(ErrorCode.REGISTRY_FILE_MISSING, path=reg_path.name),
                    severity="ERROR",
                    rule="All three registries must exist",
                    suggestion=f"Create missing {reg_name}"
                ))

        if errors:
            return self._result_fail(checked, errors)
        return self._result_pass(checked, warnings)