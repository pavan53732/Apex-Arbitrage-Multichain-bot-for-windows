"""
Validator SDK - Base classes and shared utilities for all validators.
"""

from .base import (
    BaseValidator,
    ValidationContext,
    ValidationResult,
    ValidationError,
    ValidationWarning,
    ValidatorConfig,
)
from .registry import (
    RegistryLoader,
    ConceptEntry,
    DocumentEntry,
    TraceabilityEntry,
)
from .markdown import (
    MarkdownDiscovery,
    MetadataParser,
    LinkResolver,
    ParsedMarkdown,
)
from .paths import (
    find_repo_root,
    normalize_path,
    ensure_within_repo,
)
from .json_output import (
    validate_json_output,
    write_json_result,
    read_json_result,
)
from .logging import (
    setup_logger,
    get_validator_logger,
)
from .errors import (
    ErrorCode,
    ERROR_MESSAGES,
    format_error,
)

__all__ = [
    "BaseValidator",
    "ValidationContext",
    "ValidationResult",
    "ValidationError",
    "ValidationWarning",
    "ValidatorConfig",
    "RegistryLoader",
    "ConceptEntry",
    "DocumentEntry",
    "TraceabilityEntry",
    "MarkdownDiscovery",
    "MetadataParser",
    "LinkResolver",
    "ParsedMarkdown",
    "find_repo_root",
    "normalize_path",
    "ensure_within_repo",
    "validate_json_output",
    "write_json_result",
    "read_json_result",
    "setup_logger",
    "get_validator_logger",
    "ErrorCode",
    "ERROR_MESSAGES",
    "format_error",
]