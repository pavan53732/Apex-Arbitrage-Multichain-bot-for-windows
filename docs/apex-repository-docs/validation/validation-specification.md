---
metadata_schema_version: 1.0
document_id: DOC-0066
title: Validation Specification
plane: Repository Operating Model
domain: Validation
class: Specification
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-repository-docs/validation/validation-specification.md
related_concepts:
  - CONCEPT-0004
  - CONCEPT-0066
dependencies:
  - DOC-0004
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Owner
owned_domains:
  - Validation
type: SPECIFICATION
purpose: Defines the validation families, execution order, failure semantics, pass criteria, and required outputs for repository knowledge validation.
scope: All validation performed locally by contributors and AI agents before committing changes.
---

# Validation Specification

## Purpose

This specification defines the complete validation model for the repository. It specifies what validators exist, their execution order, failure semantics, stop conditions, pass criteria, and required outputs. All validation is local-first and executed explicitly by contributors and AI agents.

## Validator Families

The repository defines eight validator families. Each family must be implemented as a separate, composable validation unit.

### 1. Cross-Reference Validator (VAL-001)

**Purpose**: Verify all links and references resolve to valid targets.

**Checks**:
- Internal markdown links resolve to existing files
- Document ID references (DOC-XXXX) resolve in Document Registry
- Concept ID references (CONCEPT-XXXX) resolve in Concept Registry
- Traceability ID references resolve in Traceability Registry
- No stale paths from moved/renamed documents
- No broken anchor links within documents

**Input**: All .md files in repository
**Output**: Report of unresolved references with file:line locations

**Failure Semantics**: 
- Each unresolved reference = 1 error
- Error threshold: 0 (any unresolved reference fails)

**Stop Condition**: None (complete all checks)

### 2. Metadata Validator (VAL-002)

**Purpose**: Verify all documents have complete, valid frontmatter metadata.

**Checks**:
- Required fields present: metadata_schema_version, document_id, title, plane, domain, class, authority, status, owner, version, canonical_source, concept_role
- Plane values: "Repository Operating Model" | "Product Specification"
- Domain values: valid domain from registry
- Class values: valid class from global taxonomy
- Authority values: "Canonical" | "Derived" | "Reference" | "Historical" | "Generated"
- Status values: "Draft" | "Review" | "Approved" | "Active" | "Deprecated" | "Archived" | "Superseded" | "Experimental"
- Document ID format: DOC-\d{4}
- Concept ID format in related_concepts: CONCEPT-\d{4}
- Canonical source path exists
- last_updated is valid ISO date

**Input**: All .md files with frontmatter
**Output**: Report of metadata violations with file:field locations

**Failure Semantics**:
- Missing required field = 1 error
- Invalid enum value = 1 error
- Malformed ID = 1 error
- Error threshold: 0

**Stop Condition**: None

### 3. Concept Uniqueness Validator (VAL-003)

**Purpose**: Ensure exactly one canonical owner per active concept.

**Checks**:
- For each active concept in Concept Registry, exactly one document has `concept_role: Owner`
- No two active documents claim ownership of same concept
- Superseded concepts have `canonical_concept_id` pointing to active concept
- No orphaned active concepts (concept with no Owner document)

**Input**: Concept Registry, all documents with concept_role
**Output**: Report of duplicate ownership, orphaned concepts, invalid aliases

**Failure Semantics**:
- Duplicate Owner for active concept = 1 error
- Orphaned active concept = 1 error
- Invalid alias chain = 1 error
- Error threshold: 0

**Stop Condition**: None

### 4. Registry Consistency Validator (VAL-004)

**Purpose**: Verify registries match actual repository state.

**Checks**:
- Document Registry: every registered document exists at registered path
- Document Registry: every .md file with DOC-ID is registered
- Concept Registry: every canonical owner document exists
- Concept Registry: every active concept has Owner document
- Traceability Registry: all source/target IDs resolve
- Registry version metadata present and consistent

**Input**: All three registries, filesystem
**Output**: Report of registry/filesystem mismatches

**Failure Semantics**:
- Missing registered file = 1 error
- Unregistered DOC-ID file = 1 warning
- Missing canonical owner = 1 error
- Unresolved traceability ID = 1 error
- Error threshold: 0

**Stop Condition**: None

### 5. Orphan Detector (VAL-005)

**Purpose**: Ensure important documents are reachable from index surfaces.

**Checks**:
- Every Canonical document reachable from domain README or Documentation Map
- Every active concept listed in at least one domain README Canonical Owner Map
- No Active document with zero inbound traceability relationships (unless explicitly standalone)
- No domain folder without a README

**Input**: Document Registry, domain READMEs, Documentation Map, Traceability Registry
**Output**: List of orphaned documents/concepts with reachability paths

**Failure Semantics**:
- Orphaned Canonical document = 1 error
- Orphaned active concept = 1 error
- Domain without README = 1 error
- Error threshold: 0

**Stop Condition**: None

### 6. Generated-Artifact Guard (VAL-006)

**Purpose**: Prevent generated/temporary artifacts from being committed.

**Checks**:
- No files matching generated patterns in committed paths:
  - AUDIT.md, REVIEW.md, REPORT.md, SUMMARY.md, ANALYSIS.md, FINDINGS.md, NOTES.md, PLAN.md, TODO.md, MIGRATION.md, IMPLEMENTATION-REPORT.md, COMPLETION-REPORT.md, STATUS.md, LOG.md, RESULT.md
  - Any file in generated/ folders (unless explicitly promoted)
  - Files with `authority: Generated` not in generated/ folder
  - CI/CD files: .github/workflows/, .gitlab-ci.yml, jenkins*, .circleci/
- Generated documents have `authority: Generated` and `status: Experimental` or `Archived`

**Input**: Git status, all .md files
**Output**: List of prohibited generated artifacts

**Failure Semantics**:
- Prohibited generated file = 1 error
- Misclassified generated document = 1 warning
- Error threshold: 0

**Stop Condition**: None

### 7. Documentation-Class Validator (VAL-007)

**Purpose**: Verify documents are assigned correct class and plane separation is maintained.

**Checks**:
- Class matches document content/function
- Repository Operating Model documents do not contain Product Specification content
- Product Specification documents do not contain Repository Operating Model content
- Registry documents only in registry folders
- Historical documents only in historical folders
- Generated documents only in generated folders
- ADR documents only in adr/ folder with ADR class

**Input**: All documents with class/plane metadata
**Output**: Report of class/plane mismatches

**Failure Semantics**:
- Class mismatch = 1 error
- Plane boundary violation = 1 error
- Folder/class mismatch = 1 error
- Error threshold: 0

**Stop Condition**: None

### 8. Traceability Validator (VAL-008)

**Purpose**: Verify traceability relationships form valid chains.

**Checks**:
- Every traceability relationship has valid source and target IDs
- Relationship types from allowed set: Implements, Consumes, Produces, Related, ValidatedBy, TestedBy, DependsOn, Supersedes, DerivedFrom
- No circular dependency chains in DependsOn relationships
- Requirements traced to at least one implementation
- Validators traced to at least one document
- Tests traced to at least one requirement

**Input**: Traceability Registry
**Output**: Report of invalid relationships, orphaned traces, circular chains

**Failure Semantics**:
- Unresolved traceability ID = 1 error
- Invalid relationship type = 1 error
- Circular DependsOn chain = 1 error
- Untraced requirement = 1 warning
- Error threshold: 0

**Stop Condition**: None

## Execution Order

Validators must execute in the following sequence. Each validator completes fully before the next begins.

| Order | Validator | Rationale |
| --- | --- | --- |
| 1 | VAL-006 Generated-Artifact Guard | Fail fast on prohibited commits |
| 2 | VAL-002 Metadata Validator | Structural validity required for all downstream |
| 3 | VAL-001 Cross-Reference Validator | References must resolve for registry/traceability checks |
| 4 | VAL-004 Registry Consistency Validator | Registries must be consistent before concept/traceability checks |
| 5 | VAL-003 Concept Uniqueness Validator | Depends on registry consistency |
| 6 | VAL-008 Traceability Validator | Depends on registry and concept validity |
| 7 | VAL-005 Orphan Detector | Depends on complete registry and traceability state |
| 8 | VAL-007 Documentation-Class Validator | Final semantic check |

## Failure Semantics Summary

| Validator | Error Threshold | Warning Threshold | Stop on Error |
| --- | --- | --- | --- |
| VAL-001 | 0 | N/A | No |
| VAL-002 | 0 | N/A | No |
| VAL-003 | 0 | N/A | No |
| VAL-004 | 0 | N/A | No |
| VAL-005 | 0 | N/A | No |
| VAL-006 | 0 | N/A | No |
| VAL-007 | 0 | N/A | No |
| VAL-008 | 0 | 0 (warnings allowed) | No |

**Overall Pass Criteria**: All 8 validators must pass (0 errors each). Warnings allowed only for VAL-008 untraced requirements.

**Overall Stop Condition**: None. All validators run to completion. Aggregate results reported at end.

## Required Outputs

Each validator must produce a structured output:

```json
{
  "validator_id": "VAL-XXX",
  "validator_name": "Cross-Reference Validator",
  "timestamp": "2026-07-31T15:30:00Z",
  "duration_ms": 1250,
  "files_checked": 353,
  "errors": [
    {
      "code": "UNRESOLVED_REF",
      "file": "docs/domain/doc.md",
      "line": 42,
      "message": "Reference to DOC-999 not found in Document Registry",
      "severity": "error"
    }
  ],
  "warnings": [],
  "passed": false
}
```

**Aggregate Report**: A single validation summary combining all validators:
- Total files checked
- Total errors by validator
- Total warnings by validator
- Overall pass/fail
- Duration per validator

## Implementation Requirements

- Validators must be executable as standalone commands
- Validators must not require network access
- Validators must complete within 30 seconds each
- Validators must be deterministic (same input = same output)
- Validators must output machine-parseable JSON
- Validators must be versioned with the repository

## Integration with Workflow

Per AGENTS.md and REPOSITORY-EXECUTION-MODEL.md:
1. Contributors/agents run full validation suite before committing
2. Validation is not automated via CI/CD
3. Failed validation blocks commit (contributor responsibility)
4. Validation results may be shared in PR description for review

## Future Extension Points

- VAL-009: Naming convention validator (when naming standard exists)
- VAL-010: Folder split policy validator (enforces 15/20/25 thresholds)
- VAL-011: README governance validator (enforces this standard)
- VAL-012: Dependency authority validator (enforces dependency-authority-rules.md)

These are reserved IDs; implementation deferred until corresponding standards exist.

## Governance Version and Immutable Rules

**Governance Version: 2.0.0.** Major versions are reserved for rare breaking governance-model changes; minor versions add append-only rules or validator capabilities; patch versions cover wording, clarifications, heuristic improvements, validator messages, and documentation corrections.

Governance rule IDs are immutable, append-only, never renumbered, reused, or reassigned:

- ROM-001 — exactly one canonical owner per concept.
- ROM-002 — every tracked document has a stable Document ID.
- ROM-003 — every tracked concept has a stable Concept ID.
- ROM-004 — registries and canonical navigation reflect repository state.
- ROM-005 — required metadata is complete and valid.
- ROM-006 — cross-references resolve.
- ROM-007 — traceability endpoints and relationship types are valid.
- ROM-008 — plane, domain, authority, class, and placement comply.
- ROM-009 — canonical authority is consistent.
- ROM-010 — generated execution artifacts are not canonical sources.
- ROM-011 — CI/CD and GitHub Actions are prohibited.
- ROM-012 — temporary execution artifacts and workspace clutter are prohibited.
