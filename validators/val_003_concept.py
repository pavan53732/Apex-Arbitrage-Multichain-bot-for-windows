"""
VAL-003: Concept Uniqueness Validator
Ensures exactly one canonical owner per active concept.
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


class Validator(BaseValidator):
    VALIDATOR_ID = "VAL-003"
    NAME = "Concept Uniqueness Validator"
    VERSION = "1.0.0"
    DESCRIPTION = "Ensures exactly one canonical owner per active concept"
    CATEGORY = "concept"
    SEVERITY = "ERROR"
    SUPPORTED_METADATA_SCHEMA_VERSIONS = ["1.0"]
    SUPPORTED_REPOSITORY_SPEC_VERSIONS = ["1.0"]

    def validate(self, context: ValidationContext) -> ValidationError:
        self._start_timer()
        errors = []
        warnings = []
        checked = 0

        concept_registry = context.concept_registry
        document_registry = context.document_registry

        # 1. Build concept -> owner documents map from registry
        concept_owners = defaultdict(list)
        for doc_id, entry in document_registry.items():
            if entry.concept_role == "Owner":
                for concept in entry.related_concepts:
                    if concept.startswith("CONCEPT-"):
                        concept_owners[concept].append(doc_id)

        # 2. Check each active concept has exactly one Owner
        for concept_id, concept in concept_registry.items():
            if concept.status == "Active":
                checked += 1
                owners = concept_owners.get(concept_id, [])

                if len(owners) == 0:
                    # Check if registry has canonical_document
                    if concept.canonical_document:
                        # Registry says there's an owner but document registry doesn't reflect it
                        errors.append(ValidationError(
                            code=ErrorCode.MISSING_CANONICAL_OWNER,
                            file="",
                            line=1,
                            message=format_error(ErrorCode.MISSING_CANONICAL_OWNER, concept_id=concept_id),
                            severity="ERROR",
                            rule="Active concept must have exactly one Owner document",
                            suggestion=f"Update document registry for {concept.canonical_document} to set concept_role: Owner"
                        ))
                    else:
                        errors.append(ValidationError(
                            code=ErrorCode.ORPHANED_ACTIVE_CONCEPT,
                            file="",
                            line=1,
                            message=format_error(ErrorCode.ORPHANED_ACTIVE_CONCEPT, concept_id=concept_id),
                            severity="ERROR",
                            rule="Every active concept must have exactly one Owner document",
                            suggestion=f"Assign canonical owner document for {concept_id}"
                        ))

                elif len(owners) > 1:
                    errors.append(ValidationError(
                        code=ErrorCode.DUPLICATE_CONCEPT_OWNER,
                        file="",
                        line=1,
                        message=format_error(ErrorCode.DUPLICATE_CONCEPT_OWNER, concept_id=concept_id, docs=", ".join(owners)),
                        severity="ERROR",
                        rule="Each active concept must have exactly one Owner document",
                        suggestion=f"Resolve duplicate ownership: keep one as Owner, change others to Reference"
                    ))

        # 3. Check superseded concepts have canonical_concept_id
        for concept_id, concept in concept_registry.items():
            if concept.status in ("Superseded", "Merged"):
                checked += 1
                if not concept.canonical_concept_id:
                    errors.append(ValidationError(
                        code=ErrorCode.INVALID_ALIAS_CHAIN,
                        file="",
                        line=1,
                        message=format_error(ErrorCode.INVALID_ALIAS_CHAIN, concept_id=concept_id),
                        severity="ERROR",
                        rule="Superseded/Merged concepts must have canonical_concept_id pointing to active concept",
                        suggestion=f"Set canonical_concept_id for {concept_id}"
                    ))
                elif concept.canonical_concept_id not in concept_registry:
                    errors.append(ValidationError(
                        code=ErrorCode.INVALID_ALIAS_CHAIN,
                        file="",
                        line=1,
                        message=f"Concept {concept_id} points to non-existent canonical_concept_id {concept.canonical_concept_id}",
                        severity="ERROR",
                        rule="canonical_concept_id must reference an existing concept",
                        suggestion=f"Fix canonical_concept_id for {concept_id}"
                    ))
                elif concept_registry[concept.canonical_concept_id].status != "Active":
                    errors.append(ValidationError(
                        code=ErrorCode.INVALID_ALIAS_CHAIN,
                        file="",
                        line=1,
                        message=f"Concept {concept_id} points to non-active concept {concept.canonical_concept_id}",
                        severity="ERROR",
                        rule="canonical_concept_id must point to an Active concept",
                        suggestion=f"Fix canonical_concept_id chain for {concept_id}"
                    ))

        # 4. Check for orphaned active concepts (registry has owner but document doesn't exist)
        for concept_id, concept in concept_registry.items():
            if concept.status == "Active" and concept.canonical_document:
                checked += 1
                if concept.canonical_document in document_registry:
                    doc_entry = document_registry[concept.canonical_document]
                    doc_path = context.repository_root / doc_entry.path
                    if not doc_path.exists():
                        errors.append(ValidationError(
                            code=ErrorCode.MISSING_CANONICAL_OWNER,
                            file=doc_entry.path,
                            line=1,
                            message=format_error(ErrorCode.MISSING_CANONICAL_OWNER, concept_id=concept_id),
                            severity="ERROR",
                            rule="Canonical owner document must exist on filesystem",
                            suggestion=f"Restore {doc_entry.path} or update registry"
                        ))

        # 5. Cross-check: documents with concept_role: Owner must match registry
        for doc_id, entry in document_registry.items():
            if entry.concept_role == "Owner":
                checked += 1
                for concept in entry.related_concepts:
                    if concept in concept_registry:
                        reg_concept = concept_registry[concept]
                        if reg_concept.canonical_document != doc_id:
                            warnings.append(ValidationWarning(
                                code=ErrorCode.DUPLICATE_CONCEPT_OWNER,
                                file=entry.path,
                                line=1,
                                message=f"Document {doc_id} claims Owner for {concept} but registry has different canonical_document",
                                severity="WARNING",
                                rule="Document Owner role should match Concept Registry canonical_document",
                                suggestion="Sync Document Registry and Concept Registry"
                            ))

        if errors:
            return self._result_fail(checked, errors)
        return self._result_pass(checked, warnings)