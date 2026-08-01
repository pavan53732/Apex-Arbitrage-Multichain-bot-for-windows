"""
Validator SDK - Base classes and shared utilities for all validators.
"""

from __future__ import annotations
import json
import time
import sys
from abc import ABC, abstractmethod
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Optional
from datetime import datetime, timezone
import yaml


@dataclass
class ValidationError:
    """A validation error finding."""
    code: str
    file: str
    line: int
    column: int = 1
    message: str = ""
    severity: str = "ERROR"  # ERROR | CRITICAL
    rule: str = ""
    suggestion: str = ""
    validator_id: str = ""
    rule_id: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class ValidationWarning:
    """A validation warning finding."""
    code: str
    file: str
    line: int
    column: int = 1
    message: str = ""
    severity: str = "WARNING"
    rule: str = ""
    suggestion: str = ""
    validator_id: str = ""
    rule_id: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class ValidationResult:
    """Standardized output from every validator."""
    validator_id: str
    validator_name: str
    validator_version: str
    timestamp: str
    execution_time_ms: int
    status: str  # PASS | FAIL | ERROR
    severity: str  # INFO | WARNING | ERROR | CRITICAL
    checked_items: int
    errors: list[ValidationError] = field(default_factory=list)
    warnings: list[ValidationWarning] = field(default_factory=list)
    infos: list[ValidationWarning] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "validator_id": self.validator_id,
            "validator_name": self.validator_name,
            "validator_version": self.validator_version,
            "timestamp": self.timestamp,
            "execution_time_ms": self.execution_time_ms,
            "status": self.status,
            "severity": self.severity,
            "checked_items": self.checked_items,
            "errors": [e.to_dict() for e in self.errors],
            "warnings": [w.to_dict() for w in self.warnings],
            "infos": [i.to_dict() for i in self.infos],
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)

    @classmethod
    def get_schema(cls) -> dict:
        return {
            "type": "object",
            "required": [
                "validator_id", "validator_name", "validator_version",
                "timestamp", "execution_time_ms", "status", "severity",
                "checked_items", "errors", "warnings", "infos"
            ],
            "properties": {
                "validator_id": {"type": "string"},
                "validator_name": {"type": "string"},
                "validator_version": {"type": "string"},
                "timestamp": {"type": "string", "format": "date-time"},
                "execution_time_ms": {"type": "integer"},
                "status": {"type": "string", "enum": ["PASS", "FAIL", "ERROR"]},
                "severity": {"type": "string", "enum": ["INFO", "WARNING", "ERROR", "CRITICAL"]},
                "checked_items": {"type": "integer"},
                "errors": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["code", "file", "line", "column", "message", "severity", "rule", "suggestion", "validator_id", "rule_id"],
                        "properties": {
                            "code": {"type": "string"},
                            "file": {"type": "string"},
                            "line": {"type": "integer"},
                            "column": {"type": "integer"},
                            "message": {"type": "string"},
                            "severity": {"type": "string", "enum": ["ERROR", "CRITICAL"]},
                            "rule": {"type": "string"},
                            "suggestion": {"type": "string"},
                            "validator_id": {"type": "string"},
                            "rule_id": {"type": "string"},
                        }
                    }
                },
                "warnings": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["code", "file", "line", "column", "message", "severity", "rule", "suggestion", "validator_id", "rule_id"],
                        "properties": {
                            "code": {"type": "string"},
                            "file": {"type": "string"},
                            "line": {"type": "integer"},
                            "column": {"type": "integer"},
                            "message": {"type": "string"},
                            "severity": {"type": "string", "enum": ["WARNING"]},
                            "rule": {"type": "string"},
                            "suggestion": {"type": "string"},
                            "validator_id": {"type": "string"},
                            "rule_id": {"type": "string"},
                        }
                    }
                },
            }
        }


@dataclass
class ValidationContext:
    """Input provided to every validator."""
    repository_root: Path
    changed_files: list[Path]
    all_markdown_files: list[Path]
    concept_registry: dict
    document_registry: dict
    traceability_registry: dict
    config: ValidatorConfig
    previous_results: list[ValidationResult] = field(default_factory=list)


@dataclass
class ValidatorConfig:
    """Global validator configuration."""
    repository_root: Path
    registries_dir: Path
    ignored_paths: list[str]
    ignored_files: list[str]
    ignored_patterns: list[str]
    max_file_size_mb: int
    validator_timeout_seconds: int
    concept_registry_path: Path
    document_registry_path: Path
    traceability_registry_path: Path
    validator_configs: dict = field(default_factory=dict)

    @classmethod
    def load(cls, repo_root: Path) -> ValidatorConfig:
        """Load configuration from .validator-config.yaml with defaults."""
        config_path = repo_root / ".validator-config.yaml"
        defaults = cls.defaults(repo_root)

        if config_path.exists():
            with open(config_path) as f:
                data = yaml.safe_load(f) or {}
            return cls.from_dict(data, repo_root, defaults)
        return defaults

    @classmethod
    def defaults(cls, repo_root: Path) -> ValidatorConfig:
        return cls(
            repository_root=repo_root,
            registries_dir=repo_root / "docs" / "apex-repository-docs" / "registries",
            ignored_paths=[".git", "generated", "node_modules", "__pycache__", ".venv", "venv"],
            ignored_files=["README.md", "*.tmp", "*.bak", "*.old"],
            ignored_patterns=[],
            max_file_size_mb=10,
            validator_timeout_seconds=30,
            concept_registry_path=repo_root / "docs" / "apex-repository-docs" / "registries" / "CONCEPT-REGISTRY.md",
            document_registry_path=repo_root / "docs" / "apex-repository-docs" / "registries" / "DOCUMENT-REGISTRY.md",
            traceability_registry_path=repo_root / "docs" / "apex-repository-docs" / "registries" / "TRACEABILITY-REGISTRY.md",
        )

    @classmethod
    def from_dict(cls, data: dict, repo_root: Path, defaults: ValidatorConfig) -> ValidatorConfig:
        return cls(
            repository_root=repo_root,
            registries_dir=Path(data.get("registries_dir", defaults.registries_dir)),
            ignored_paths=data.get("ignored_paths", defaults.ignored_paths),
            ignored_files=data.get("ignored_files", defaults.ignored_files),
            ignored_patterns=data.get("ignored_patterns", defaults.ignored_patterns),
            max_file_size_mb=data.get("max_file_size_mb", defaults.max_file_size_mb),
            validator_timeout_seconds=data.get("validator_timeout_seconds", defaults.validator_timeout_seconds),
            concept_registry_path=Path(data.get("concept_registry", defaults.concept_registry_path)),
            document_registry_path=Path(data.get("document_registry", defaults.document_registry_path)),
            traceability_registry_path=Path(data.get("traceability_registry", defaults.traceability_registry_path)),
            validator_configs=data.get("validators", {}),
        )


class BaseValidator(ABC):
    """Base class for all validators. All validators must inherit from this."""

    # Identity (required class attributes)
    VALIDATOR_ID: str = "VAL-XXX"
    NAME: str = "Validator Name"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = ""
    CATEGORY: str = "general"
    SEVERITY: str = "ERROR"

    # Version compatibility
    SUPPORTED_METADATA_SCHEMA_VERSIONS: list[str] = ["1.0"]
    SUPPORTED_REPOSITORY_SPEC_VERSIONS: list[str] = ["1.0"]

    def __init__(self, config: ValidatorConfig):
        self.config = config
        self.start_time: float = 0
        self.end_time: float = 0

    @abstractmethod
    def validate(self, context: ValidationContext) -> ValidationResult:
        """Main validation entry point. Must be implemented by each validator."""
        pass

    def _start_timer(self):
        self.start_time = time.perf_counter()

    def _stop_timer(self) -> int:
        self.end_time = time.perf_counter()
        return int((self.end_time - self.start_time) * 1000)

    def _create_result(
        self,
        status: str,
        severity: str,
        checked_items: int,
        errors: list[ValidationError],
        warnings: list[ValidationWarning]
    ) -> ValidationResult:
        # Every finding is bound to its producing validator and an immutable
        # Repository Operating Model rule. This keeps output machine-readable
        # while preserving each validator's human-readable rule explanation.
        rule_ids = {
            "MISSING_REQUIRED_FIELD": "ROM-005", "INVALID_ENUM_VALUE": "ROM-005", "INVALID_ID_FORMAT": "ROM-002", "INVALID_SCHEMA_VERSION": "ROM-005", "INVALID_DATE_FORMAT": "ROM-005",
            "UNRESOLVED_MARKDOWN_LINK": "ROM-006", "UNRESOLVED_DOC_REF": "ROM-006", "UNRESOLVED_CONCEPT_REF": "ROM-006", "BROKEN_ANCHOR_LINK": "ROM-006",
            "REGISTRY_FILE_MISSING": "ROM-004", "REGISTRY_FS_MISMATCH": "ROM-004", "UNREGISTERED_DOCUMENT": "ROM-004", "MISSING_CANONICAL_OWNER": "ROM-001", "TRACEABILITY_ID_UNRESOLVED": "ROM-007",
            "DUPLICATE_CONCEPT_OWNER": "ROM-001", "ORPHANED_ACTIVE_CONCEPT": "ROM-001", "INVALID_ALIAS_CHAIN": "ROM-003",
            "INVALID_RELATIONSHIP_TYPE": "ROM-007", "CIRCULAR_DEPENDS_ON": "ROM-007", "NO_INBOUND_TRACEABILITY_WARN": "ROM-007",
            "ORPHANED_CANONICAL_DOCUMENT": "ROM-004", "CONCEPT_NOT_IN_DOMAIN_NAVIGATION_WARN": "ROM-004", "NO_INBOUND_DOCUMENT_TRACEABILITY_WARN": "ROM-007", "DOMAIN_WITHOUT_README": "ROM-004",
            "CLASS_MISMATCH": "ROM-008", "INDEX_LAYOUT_HEURISTIC_WARN": "ROM-008", "PLANE_BOUNDARY_VIOLATION": "ROM-008", "FOLDER_CLASS_MISMATCH": "ROM-008",
            "PROHIBITED_TEMP_FILE": "ROM-012", "PROHIBITED_CICD_FILE": "ROM-011", "MISCLASSIFIED_GENERATED_DOC": "ROM-010",
        }
        for finding in [*errors, *warnings]:
            finding.validator_id = self.VALIDATOR_ID
            finding.rule_id = rule_ids.get(str(finding.code).split(".")[-1], "ROM-004")
        exec_time = self._stop_timer()
        return ValidationResult(
            validator_id=self.VALIDATOR_ID,
            validator_name=self.NAME,
            validator_version=self.VERSION,
            timestamp=datetime.now(timezone.utc).isoformat(),
            execution_time_ms=exec_time,
            status=status,
            severity=severity,
            checked_items=checked_items,
            errors=errors,
            warnings=warnings,
        )

    def _result_pass(self, checked_items: int, warnings: list[ValidationWarning] = None) -> ValidationResult:
        warnings = warnings or []
        severity = "WARNING" if warnings else "INFO"
        return self._create_result("PASS", severity, checked_items, [], warnings)

    def _result_fail(self, checked_items: int, errors: list[ValidationError]) -> ValidationResult:
        max_severity = "CRITICAL" if any(e.severity == "CRITICAL" for e in errors) else "ERROR"
        return self._create_result("FAIL", max_severity, checked_items, errors, [])

    def _result_error(self, checked_items: int, message: str) -> ValidationResult:
        return self._create_result("ERROR", "CRITICAL", checked_items, [
            ValidationError(
                code="VALIDATOR_EXECUTION_ERROR",
                file="",
                line=0,
                message=message,
                severity="CRITICAL",
                rule="Validator must not crash",
                suggestion="Check validator implementation"
            )
        ], [])