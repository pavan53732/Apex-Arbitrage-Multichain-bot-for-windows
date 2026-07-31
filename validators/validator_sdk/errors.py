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
    UNTRACED_REQUIREMENT = "UNTRACED_REQUIREMENT"

    # Orphan errors
    ORPHANED_CANONICAL_DOCUMENT = "ORPHANED_CANONICAL_DOCUMENT"
    ORPHANED_ACTIVE_CONCEPT_WARN = "ORPHANED_ACTIVE_CONCEPT_WARN"
    DOMAIN_WITHOUT_README = "DOMAIN_WITHOUT_README"

    # Document class errors
    CLASS_MISMATCH = "CLASS_MISMATCH"
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
    ErrorCode.UNTRACED_REQUIREMENT: "Requirement {concept_id} has no traceability to implementation",

    ErrorCode.ORPHANED_CANONICAL_DOCUMENT: "Canonical document {doc_id} is not reachable from any domain README",
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