---
metadata_schema_version: 1.0
document_id: DOC-0078
title: Validator Architecture Specification
plane: Repository Operating Model
domain: Validation
class: Specification
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/repository-operating-model/validation/validator-architecture-specification.md
related_concepts:
  - CONCEPT-0004
  - CONCEPT-0078
dependencies:
  - DOC-0004
  - DOC-0066
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Owner
owned_domains:
  - Validation
type: SPECIFICATION
purpose: Defines the implementation contract for all validators including SDK interface, runner orchestration, output schema, severity levels, exit codes, shared utilities, configuration, and versioning.
scope: All validators VAL-001 through VAL-008 and future validators.
---

# Validator Architecture Specification

## Purpose

This specification defines the implementation contract that all validators must follow. It ensures consistency, composability, and deterministic behavior across all eight validators (VAL-001 through VAL-008) and future validators.

---

## 1. Validator SDK / Base Contract

Every validator MUST implement the following interface:

### Required Interface

```python
class BaseValidator:
    """
    Base class for all validators.
    All validators must inherit from this and implement the interface.
    """
    
    # Identity (required class attributes)
    VALIDATOR_ID: str = "VAL-XXX"           # e.g., "VAL-001"
    NAME: str = "Validator Name"             # e.g., "Cross-Reference Validator"
    VERSION: str = "1.0.0"                   # Semantic version
    DESCRIPTION: str = "..."                 # One-line purpose
    CATEGORY: str = "metadata|crossref|registry|concept|traceability|orphan|class|generated"
    SEVERITY: str = "ERROR"                  # Default severity for failures
    
    # Metadata schema compatibility
    SUPPORTED_METADATA_SCHEMA_VERSIONS: list = ["1.0"]
    SUPPORTED_REPOSITORY_SPEC_VERSIONS: list = ["1.0"]
    
    def __init__(self, config: ValidatorConfig):
        self.config = config
        self.start_time = None
        self.end_time = None
    
    def validate(self, context: ValidationContext) -> ValidationResult:
        """
        Main validation entry point.
        Must be implemented by each validator.
        """
        raise NotImplementedError
    
    def get_schema(self) -> dict:
        """Return JSON schema for this validator's output."""
        return ValidationResult.get_schema()
```

### ValidationContext (Input)

```python
@dataclass
class ValidationContext:
    """Input provided to every validator."""
    repository_root: Path                    # Root of repository
    changed_files: list[Path]                # Files changed in this run (optional)
    all_markdown_files: list[Path]           # All .md files in repository
    concept_registry: ConceptRegistry        # Parsed concept registry
    document_registry: DocumentRegistry      # Parsed document registry
    traceability_registry: TraceabilityRegistry  # Parsed traceability registry
    config: ValidatorConfig                  # Global validator config
    previous_results: list[ValidationResult] # Results from earlier validators in sequence
```

### ValidationResult (Output)

```python
@dataclass
class ValidationResult:
    """Standardized output from every validator."""
    
    # Identity
    validator_id: str                        # e.g., "VAL-001"
    validator_name: str                      # e.g., "Cross-Reference Validator"
    validator_version: str                   # e.g., "1.0.0"
    
    # Execution metadata
    timestamp: str                           # ISO 8601 UTC
    execution_time_ms: int                   # Wall clock time
    
    # Status
    status: str                              # "PASS" | "FAIL" | "ERROR"
    severity: str                            # "INFO" | "WARNING" | "ERROR" | "CRITICAL"
    
    # Findings
    errors: list[ValidationError]            # Must be empty for PASS
    warnings: list[ValidationWarning]        # Allowed for PASS
    
    # Metrics
    checked_items: int                       # Files/entries checked
    
    # Machine-readable
    def to_json(self) -> str: ...
    def to_dict(self) -> dict: ...
```

### ValidationError / ValidationWarning

```python
@dataclass
class ValidationError:
    code: str                                # Machine-readable error code
    file: str                                # Relative path from repo root
    line: int                                # Line number (1-indexed)
    column: int                              # Column number (optional)
    message: str                             # Human-readable description
    severity: str                            # "ERROR" | "CRITICAL"
    rule: str                                # Which rule was violated
    suggestion: str                          # Optional fix suggestion

@dataclass
class ValidationWarning:
    code: str
    file: str
    line: int
    column: int
    message: str
    severity: str                            # "WARNING"
    rule: str
    suggestion: str
```

---

## 2. Validator Runner (Orchestrator)

### Execution Order (Fixed)

```
validate (entry point)
    │
    ├─► VAL-006  Generated Artifact Guard     (FAIL-FAST)
    ├─► VAL-002  Metadata Validator
    ├─► VAL-001  Cross-Reference Validator
    ├─► VAL-004  Registry Consistency Validator
    ├─► VAL-003  Concept Uniqueness Validator
    ├─► VAL-008  Traceability Validator
    ├─► VAL-005  Orphan Detector
    └─► VAL-007  Document-Class Validator
```

### Runner Behavior

```python
class ValidatorRunner:
    """Orchestrates validator execution in fixed order."""
    
    VALIDATOR_SEQUENCE = [
        "VAL-006",  # FAIL-FAST: stop entire run if this fails
        "VAL-002",
        "VAL-001",
        "VAL-004",
        "VAL-003",
        "VAL-008",
        "VAL-005",
        "VAL-007",
    ]
    
    FAIL_FAST_VALIDATORS = {"VAL-006"}  # Stop entire pipeline on failure
    
    def run(self, context: ValidationContext) -> AggregateResult:
        results = []
        
        for validator_id in self.VALIDATOR_SEQUENCE:
            validator = self.load_validator(validator_id)
            result = validator.validate(context)
            results.append(result)
            
            # Add to context for downstream validators
            context.previous_results.append(result)
            
            # Fail-fast check
            if validator_id in self.FAIL_FAST_VALIDATORS and result.status == "FAIL":
                return AggregateResult(
                    overall_status="FAIL",
                    fail_fast_at=validator_id,
                    results=results
                )
        
        # Determine overall status
        overall_status = "PASS" if all(r.status == "PASS" for r in results) else "FAIL"
        
        return AggregateResult(
            overall_status=overall_status,
            results=results
        )
```

### AggregateResult

```python
@dataclass
class AggregateResult:
    overall_status: str                      # "PASS" | "FAIL"
    timestamp: str
    total_execution_time_ms: int
    fail_fast_at: str | None                 # Validator ID if fail-fast triggered
    results: list[ValidationResult]
    
    def to_json(self) -> str: ...
    def summary(self) -> str: ...
```

---

## 3. Standard Output Schema (JSON)

Every validator MUST emit this exact JSON structure:

```json
{
  "validator_id": "VAL-001",
  "validator_name": "Cross-Reference Validator",
  "validator_version": "1.0.0",
  "timestamp": "2026-07-31T15:30:00Z",
  "execution_time_ms": 1250,
  "status": "FAIL",
  "severity": "ERROR",
  "checked_items": 353,
  "errors": [
    {
      "code": "UNRESOLVED_DOC_REF",
      "file": "docs/domain/doc.md",
      "line": 42,
      "column": 10,
      "message": "Reference to DOC-999 not found in Document Registry",
      "severity": "ERROR",
      "rule": "All DOC-ID references must resolve to registered document",
      "suggestion": "Add DOC-999 to Document Registry or fix reference"
    }
  ],
  "warnings": []
}
```

**Rules:**
- `status`: "PASS" (no errors), "FAIL" (errors present), "ERROR" (execution failure)
- `severity`: Overall severity = highest severity among errors/warnings
- `errors`: Array (empty for PASS)
- `warnings`: Array (allowed for PASS)
- All timestamps UTC ISO 8601
- All paths relative to repository root

---

## 4. Severity Levels (Shared Taxonomy)

| Level | Value | Meaning | Exit Code Impact |
| --- | --- | --- | --- |
| **INFO** | "INFO" | Informational, no action needed | 0 (PASS) |
| **WARNING** | "WARNING" | Potential issue, allowed to pass | 1 (WARNINGS ONLY) |
| **ERROR** | "ERROR" | Validation failure, must fix | 2 (FAILED) |
| **CRITICAL** | "CRITICAL" | Blocking issue, repository invalid | 2 (FAILED) |

**Mapping:**
- Validator with only INFO/WARNING → status "PASS", exit code 1
- Validator with any ERROR/CRITICAL → status "FAIL", exit code 2
- Validator crashes → status "ERROR", exit code 3

---

## 5. Exit Code Standard

| Exit Code | Meaning | When |
| --- | --- | --- |
| **0** | PASS | All validators PASS (no errors, no warnings) |
| **1** | WARNINGS ONLY | All validators PASS but some have WARNINGS |
| **2** | VALIDATION FAILED | At least one validator has ERROR/CRITICAL |
| **3** | EXECUTION ERROR | Validator crashed, timeout, or invalid invocation |

**Runner Exit Code:**
- If any validator returns 2 or 3 → runner returns 2
- Else if any validator returns 1 → runner returns 1
- Else → runner returns 0

---

## 6. Shared Utilities (No Duplication)

### Required Shared Modules

```python
# validator_sdk/
# ├── __init__.py
# ├── base.py              # BaseValidator, ValidationContext, ValidationResult
# ├── config.py            # ValidatorConfig, load_config()
# ├── registry.py          # RegistryLoader (concept, document, traceability)
# ├── markdown.py          # MarkdownDiscovery, MetadataParser, LinkResolver
# ├── paths.py             # Path normalization, repo root detection
# ├── json_output.py       # JSON serialization, schema validation
# ├── logging.py           # Structured logging
# └── errors.py            # Error codes, standard messages
```

### RegistryLoader

```python
class RegistryLoader:
    """Single source for loading all three registries."""
    
    @staticmethod
    def load_concept_registry(repo_root: Path) -> ConceptRegistry: ...
    @staticmethod
    def load_document_registry(repo_root: Path) -> DocumentRegistry: ...
    @staticmethod
    def load_traceability_registry(repo_root: Path) -> TraceabilityRegistry: ...
    @staticmethod
    def load_all(repo_root: Path) -> tuple: ...
```

### MarkdownDiscovery

```python
class MarkdownDiscovery:
    """Discover all markdown files with filtering."""
    
    @staticmethod
    def find_all(repo_root: Path, ignored_patterns: list[str]) -> list[Path]: ...
    @staticmethod
    def find_changed(repo_root: Path, since_commit: str) -> list[Path]: ...
```

### MetadataParser

```python
class MetadataParser:
    """Parse and validate YAML frontmatter."""
    
    @staticmethod
    def parse(file_path: Path) -> tuple[dict, str]:  # (metadata, body)
    @staticmethod
    def validate(metadata: dict, schema_version: str) -> list[ValidationError]: ...
```

### LinkResolver

```python
class LinkResolver:
    """Resolve internal markdown links and DOC-ID/CONCEPT-ID references."""
    
    @staticmethod
    def resolve_markdown_link(link: str, from_file: Path, repo_root: Path) -> Path | None: ...
    @staticmethod
    def resolve_doc_id(doc_id: str, document_registry: DocumentRegistry) -> Path | None: ...
    @staticmethod
    def resolve_concept_id(concept_id: str, concept_registry: ConceptRegistry) -> ConceptEntry | None: ...
```

---

## 7. Validator Configuration

### Single Config File: `.validator-config.yaml`

```yaml
# Validator Configuration
# Location: Repository root

metadata_schema_version: "1.0"

# Paths
repository_root: "."
registries_dir: "docs/repository-operating-model/registries"

# Discovery
ignored_paths:
  - ".git"
  - "generated"
  - "node_modules"
  - "__pycache__"
  - ".venv"
  - "venv"

ignored_files:
  - "README.md"              # Root README handled specially
  - "*.tmp"
  - "*.bak"
  - "*.old"

# Validation thresholds
max_file_size_mb: 10
validator_timeout_seconds: 30

# Registry locations (relative to repo root)
concept_registry: "docs/repository-operating-model/registries/CONCEPT-REGISTRY.md"
document_registry: "docs/repository-operating-model/registries/DOCUMENT-REGISTRY.md"
traceability_registry: "docs/repository-operating-model/registries/TRACEABILITY-REGISTRY.md"

# Per-validator config (optional overrides)
validators:
  VAL-001:
    check_anchors: true
    check_external_urls: false
  VAL-002:
    strict_enum_validation: true
  VAL-006:
    prohibited_patterns:
      - "AUDIT.md"
      - "REVIEW.md"
      - "REPORT.md"
      - "SUMMARY.md"
      - "ANALYSIS.md"
      - "FINDINGS.md"
      - "NOTES.md"
      - "PLAN.md"
      - "TODO.md"
      - "MIGRATION.md"
      - "IMPLEMENTATION-REPORT.md"
      - "COMPLETION-REPORT.md"
      - "STATUS.md"
      - "LOG.md"
      - "RESULT.md"
    prohibited_extensions:
      - ".tmp"
      - ".bak"
      - ".old"
    prohibited_dirs:
      - ".github/workflows"
      - ".gitlab-ci.yml"
```

### Config Loading

```python
def load_config(repo_root: Path) -> ValidatorConfig:
    """Load config from .validator-config.yaml with defaults."""
    config_path = repo_root / ".validator-config.yaml"
    if config_path.exists():
        with open(config_path) as f:
            return ValidatorConfig.from_yaml(f.read())
    return ValidatorConfig.defaults()
```

---

## 8. Validator Versioning

### Required Version Fields

Every validator MUST include:

```python
VALIDATOR_ID = "VAL-001"
VERSION = "1.0.0"                    # Validator implementation version
SUPPORTED_METADATA_SCHEMA_VERSIONS = ["1.0"]
SUPPORTED_REPOSITORY_SPEC_VERSIONS = ["1.0", "2.0"]
```

### Version Compatibility Rules

| Validator Version | Compatible Metadata Schema | Compatible Repo Spec |
| --- | --- | --- |
| 1.0.x | 1.0 | 1.0 |
| 1.1.x | 1.0, 1.1 | 1.0, 2.0 |
| 2.0.x | 1.1, 2.0 | 2.0 |

**Runner Check**: Before execution, runner verifies validator supports current repository metadata schema and spec versions.

---

## 9. Local-First Execution Rules (Mandatory)

Every validator MUST comply with:

| Rule | Requirement |
| --- | --- |
| **No Network Access** | Zero HTTP/HTTPS/DNS calls. No GitHub API, no cloud services. |
| **Read-Only by Default** | Never modify repository contents. Repair is separate explicit mode. |
| **Diagnostics Only** | Return findings only. No auto-fix unless `--repair` flag. |
| **Deterministic** | Identical input → identical output. No randomness, no timestamps in logic. |
| **No Hidden State** | No caching between runs. No persistent local DB. |
| **Timeout** | Must complete within 30 seconds (configurable). |
| **Exit Codes** | Must use standard exit codes (0/1/2/3). |

---

## 10. Implementation Language & Distribution

### Language: Python 3.11+
- Standard library only where possible
- Minimal dependencies: `pyyaml`, `jsonschema`, `pathspec`
- Single-file per validator for simplicity

### Entry Point Pattern

```bash
# Each validator executable as:
python -m validator_sdk.run VAL-001

# Or direct:
python validators/val_001_crossref.py

# Runner:
python -m validator_sdk.runner
```

### Directory Structure

```
validators/
├── validator_sdk/
│   ├── __init__.py
│   ├── base.py
│   ├── config.py
│   ├── registry.py
│   ├── markdown.py
│   ├── paths.py
│   ├── json_output.py
│   ├── logging.py
│   └── errors.py
├── val_001_crossref.py
├── val_002_metadata.py
├── val_003_concept.py
├── val_004_registry.py
├── val_005_orphan.py
├── val_006_generated.py
├── val_007_class.py
├── val_008_traceability.py
├── runner.py
├── .validator-config.yaml
└── requirements.txt
```

---

## 11. Implementation Priority (Per Validation Specification)

| Priority | Validator | Key Dependencies |
| --- | --- | --- |
| 1 | **VAL-006** Generated Artifact Guard | MarkdownDiscovery, config.prohibited_patterns |
| 2 | **VAL-002** Metadata Validator | MetadataParser, schema validation |
| 3 | **VAL-001** Cross-Reference Validator | LinkResolver, DocumentRegistry, ConceptRegistry |
| 4 | **VAL-004** Registry Consistency Validator | RegistryLoader, MarkdownDiscovery |
| 5 | **VAL-003** Concept Uniqueness Validator | ConceptRegistry, DocumentRegistry |
| 6 | **VAL-008** Traceability Validator | TraceabilityRegistry, ConceptRegistry |
| 7 | **VAL-005** Orphan Detector | DocumentRegistry, MarkdownDiscovery, READMEs |
| 8 | **VAL-007** Document Class Validator | MetadataParser, DomainOwnershipMatrix |

---

## 12. Testing Requirements

Each validator must have:
- Unit tests for each error code
- Integration test with sample repository
- Performance test (< 30s on 500 files)
- Determinism test (same input → same output 100x)

---

## Related Documents
- [Validation Specification](../validation/validation-specification.md)
- [REPOSITORY-EXECUTION-MODEL.md](../../../REPOSITORY-EXECUTION-MODEL.md)
- [AGENTS.md](../../../AGENTS.md)