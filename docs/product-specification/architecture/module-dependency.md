---
metadata_schema_version: 1.0
document_id: DOC-0083
title: Module Dependency
plane: Product Specification
domain: Architecture
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/architecture/module-dependency.md
related_concepts:
  - CONCEPT-0083
dependencies:
  - DOC-0079
  - DOC-0085
consumers:
  - DOC-0049
  - DOC-0068
  - DOC-0080
  - DOC-0085
  - DOC-0225
  - DOC-0251
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: Module Dependency documentation.
scope: Reference documentation.
---

# Module Dependency

## Document type
This document is an overview, reference, or index as noted below.

# Module Dependency

## Purpose
Defines the dependency graph and import rules between modules and packages.

## Ownership
- Import dependency policy only.

## Cross-references
- `./project-structure.md`
- `./architecture.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
