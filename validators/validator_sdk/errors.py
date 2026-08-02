"""
Standard error codes and messages for validators.
"""

from __future__ import annotations
from enum import Enum


class ErrorCode(str, Enum):
    """Standard error codes used across validators."""

    # Metadata errors
    MISSING_REQUIRED_FIELD = "MISSING_REQUIRED_FIELD"
    INVALID_ENUM_VALUE = "INVALID_ENUM_VALUE"
    INVALID_ID_FORMAT = "INVALID_ID_FORMAT"
    INVALID_SCHEMA_VERSION = "INVALID_SCHEMA_VERSION"
    INVALID_DATE_FORMAT = "INVALID_DATE_FORMAT"

    # Cross-reference errors
    UNRESOLVED_MARKDOWN_LINK = "UNRESOLVED_MARKDOWN_LINK"
    UNRESOLVED_DOC_REF = "UNRESOLVED_DOC_REF"
    UNRESOLVED_CONCEPT_REF = "UNRESOLVED_CONCEPT_REF"
    BROKEN_ANCHOR_LINK = "BROKEN_ANCHOR_LINK"

    # Registry errors
    REGISTRY_FILE_MISSING = "REGISTRY_FILE_MISSING"
    REGISTRY_FS_MISMATCH = "REGISTRY_FS_MISMATCH"
    UNREGISTERED_DOCUMENT = "UNREGISTERED_DOCUMENT"
    MISSING_CANONICAL_OWNER = "MISSING_CANONICAL_OWNER"
    TRACEABILITY_ID_UNRESOLVED = "TRACEABILITY_ID_UNRESOLVED"

    # Concept errors
    DUPLICATE_CONCEPT_OWNER = "DUPLICATE_CONCEPT_OWNER"
    ORPHANED_ACTIVE_CONCEPT = "ORPHANED_ACTIVE_CONCEPT"
    INVALID_ALIAS_CHAIN = "INVALID_ALIAS_CHAIN"

    # Traceability errors
    INVALID_RELATIONSHIP_TYPE = "INVALID_RELATIONSHIP_TYPE"
    CIRCULAR_DEPENDS_ON = "CIRCULAR_DEPENDS_ON"
    NO_INBOUND_TRACEABILITY_WARN = "NO_INBOUND_TRACEABILITY_WARN"

    # Orphan errors
    ORPHANED_CANONICAL_DOCUMENT = "ORPHANED_CANONICAL_DOCUMENT"
    CONCEPT_NOT_IN_DOMAIN_NAVIGATION_WARN = "CONCEPT_NOT_IN_DOMAIN_NAVIGATION_WARN"
    NO_INBOUND_DOCUMENT_TRACEABILITY_WARN = "NO_INBOUND_DOCUMENT_TRACEABILITY_WARN"
    DOMAIN_WITHOUT_README = "DOMAIN_WITHOUT_README"

    # Document class errors
    CLASS_MISMATCH = "CLASS_MISMATCH"
    INDEX_LAYOUT_HEURISTIC_WARN = "INDEX_LAYOUT_HEURISTIC_WARN"
    PLANE_BOUNDARY_VIOLATION = "PLANE_BOUNDARY_VIOLATION"
    FOLDER_CLASS_MISMATCH = "FOLDER_CLASS_MISMATCH"

    # Generated artifact errors
    PROHIBITED_TEMP_FILE = "PROHIBITED_TEMP_FILE"
    PROHIBITED_CICD_FILE = "PROHIBITED_CICD_FILE"
    MISCLASSIFIED_GENERATED_DOC = "MISCLASSIFIED_GENERATED_DOC"

    # Execution errors
    VALIDATOR_EXECUTION_ERROR = "VALIDATOR_EXECUTION_ERROR"
    VALIDATOR_TIMEOUT = "VALIDATOR_TIMEOUT"
    CONFIG_ERROR = "CONFIG_ERROR"

    # Coverage errors (VAL-018)
    COVERAGE_GAP = "COVERAGE_GAP"
    VALIDATOR_NO_COVERAGE = "VALIDATOR_NO_COVERAGE"
    COVERAGE_SUMMARY = "COVERAGE_SUMMARY"
    COVERAGE_GAP_COUNT = "COVERAGE_GAP_COUNT"

    # Completeness errors (VAL-010)
    MISSING_REQUIRED_SECTION = "MISSING_REQUIRED_SECTION"
    MISSING_RECOMMENDED_SECTION = "MISSING_RECOMMENDED_SECTION"
    COMPLETENESS_SCORE = "COMPLETENESS_SCORE"

    # ADR errors (VAL-009)
    ADR_NO_CONSUMERS = "ADR_NO_CONSUMERS"
    ADR_SUPERSEDED_NO_SUCCESSOR = "ADR_SUPERSEDED_NO_SUCCESSOR"
    ADR_CONSUMER_NOT_FOUND = "ADR_CONSUMER_NOT_FOUND"
    ADR_MISSING_SECTION = "ADR_MISSING_SECTION"

    # State machine errors (VAL-013)
    MISSING_STATE_MACHINE = "MISSING_STATE_MACHINE"
    MISSING_STATE_MACHINE_REF = "MISSING_STATE_MACHINE_REF"

    # Interface errors (VAL-014)
    ORPHAN_INTERFACE = "ORPHAN_INTERFACE"
    UNRESOLVED_CONSUMER = "UNRESOLVED_CONSUMER"
    NO_INTERFACE_REFERENCE = "NO_INTERFACE_REFERENCE"

    # Terminology errors (VAL-011)
    GLOSSARY_MISSING = "GLOSSARY_MISSING"
    POTENTIAL_TERM_CONFLICT = "POTENTIAL_TERM_CONFLICT"

    # Drift errors (VAL-012)
    DOCUMENT_STALE = "DOCUMENT_STALE"
    DEPENDENCY_DRIFT = "DEPENDENCY_DRIFT"
    DUPLICATE_CONTENT = "DUPLICATE_CONTENT"
    VERSION_DRIFT = "VERSION_DRIFT"
    SECTION_DRIFT = "SECTION_DRIFT"

    # Cross-domain errors (VAL-015)
    DERIVED_CANONICAL_UNRESOLVED = "DERIVED_CANONICAL_UNRESOLVED"
    DEPENDENCY_UNRESOLVED = "DEPENDENCY_UNRESOLVED"
    DEPENDENCY_ON_SUPERSEDED = "DEPENDENCY_ON_SUPERSEDED"
    CROSS_PLANE_DEPENDENCY = "CROSS_PLANE_DEPENDENCY"
    CONSUMER_UNRESOLVED = "CONSUMER_UNRESOLVED"

    # Ownership errors (VAL-016)
    OWNER_FILE_MISSING = "OWNER_FILE_MISSING"
    OWNER_SUPERSEDED = "OWNER_SUPERSEDED"
    OWNER_STUB = "OWNER_STUB"
    OWNER_NO_CONCEPT = "OWNER_NO_CONCEPT"
    OWNER_READ_ERROR = "OWNER_READ_ERROR"

    # Quality errors (VAL-017)
    QUALITY_SCORE = "QUALITY_SCORE"
    QUALITY_DEFICIENT = "QUALITY_DEFICIENT"
    DOMAIN_QUALITY = "DOMAIN_QUALITY"


# Standard error messages
ERROR_MESSAGES = {
    ErrorCode.MISSING_REQUIRED_FIELD: "Required metadata field '{field}' is missing",
    ErrorCode.INVALID_ENUM_VALUE: "Field '{field}' has invalid value '{value}'. Must be one of: {options}",
    ErrorCode.INVALID_ID_FORMAT: "Field '{field}' has invalid format. Expected {expected}, got '{value}'",
    ErrorCode.INVALID_SCHEMA_VERSION: "metadata_schema_version must be '{expected}', got '{value}'",
    ErrorCode.INVALID_DATE_FORMAT: "Field '{field}' must be valid ISO date (YYYY-MM-DD), got '{value}'",

    ErrorCode.UNRESOLVED_MARKDOWN_LINK: "Markdown link '{target}' in '{file}' does not resolve to existing file",
    ErrorCode.UNRESOLVED_DOC_REF: "Reference to {doc_id} not found in Document Registry",
    ErrorCode.UNRESOLVED_CONCEPT_REF: "Reference to {concept_id} not found in Concept Registry",
    ErrorCode.BROKEN_ANCHOR_LINK: "Anchor link '#{anchor}' not found in target file",

    ErrorCode.REGISTRY_FILE_MISSING: "Registry file {path} does not exist",
    ErrorCode.REGISTRY_FS_MISMATCH: "Registry entry for {id} points to non-existent file {path}",
    ErrorCode.UNREGISTERED_DOCUMENT: "File {path} has DOC-ID but is not registered in Document Registry",
    ErrorCode.MISSING_CANONICAL_OWNER: "Active concept {concept_id} has no canonical owner document",
    ErrorCode.TRACEABILITY_ID_UNRESOLVED: "Traceability {trace_id} references unresolved {source_id} or {target_id}",

    ErrorCode.DUPLICATE_CONCEPT_OWNER: "Concept {concept_id} has multiple Owner documents: {docs}",
    ErrorCode.ORPHANED_ACTIVE_CONCEPT: "Active concept {concept_id} has no Owner document",
    ErrorCode.INVALID_ALIAS_CHAIN: "Concept {concept_id} alias chain is invalid",

    ErrorCode.INVALID_RELATIONSHIP_TYPE: "Traceability {trace_id} has invalid relationship type '{type}'",
    ErrorCode.CIRCULAR_DEPENDS_ON: "Circular DependsOn chain detected involving {concepts}",
    ErrorCode.NO_INBOUND_TRACEABILITY_WARN: "Concept {concept_id} has no inbound traceability relationship",

    ErrorCode.ORPHANED_CANONICAL_DOCUMENT: "Canonical document {doc_id} is not reachable from any domain README",
    ErrorCode.NO_INBOUND_DOCUMENT_TRACEABILITY_WARN: "Active document {doc_id} has no inbound traceability relationship",
    ErrorCode.CONCEPT_NOT_IN_DOMAIN_NAVIGATION_WARN: "Active concept {concept_id} is not listed in domain navigation",
    ErrorCode.INDEX_LAYOUT_HEURISTIC_WARN: "Index document {doc_id} has no recognized navigation layout",
    ErrorCode.DOMAIN_WITHOUT_README: "Domain {domain} has no README.md file",

    ErrorCode.CLASS_MISMATCH: "Document {doc_id} class '{current}' does not match expected '{expected}'",
    ErrorCode.PLANE_BOUNDARY_VIOLATION: "Document {doc_id} in {plane} plane contains content for other plane",
    ErrorCode.FOLDER_CLASS_MISMATCH: "Folder {path} contains documents with invalid class for this domain",

    ErrorCode.PROHIBITED_TEMP_FILE: "Prohibited temporary file detected: {file}",
    ErrorCode.PROHIBITED_CICD_FILE: "Prohibited CI/CD file detected: {file}",
    ErrorCode.MISCLASSIFIED_GENERATED_DOC: "Generated document {doc_id} not in generated/ folder",

    ErrorCode.VALIDATOR_EXECUTION_ERROR: "Validator execution failed: {message}",
    ErrorCode.VALIDATOR_TIMEOUT: "Validator exceeded {timeout}s timeout",
    ErrorCode.CONFIG_ERROR: "Configuration error: {message}",
}


def format_error(code: ErrorCode, **kwargs) -> str:
    """Format error message with parameters."""
    template = ERROR_MESSAGES.get(code, "{code}")
    return template.format(code=code.value, **kwargs)