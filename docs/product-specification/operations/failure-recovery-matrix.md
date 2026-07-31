---
metadata_schema_version: 1.0
document_id: DOC-0341
title: Failure Recovery Matrix
plane: Product Specification
domain: Operations
class: Index
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/operations/failure-recovery-matrix.md
related_concepts:
  - CONCEPT-0341
dependencies:
  - DOC-0051
consumers:
  - DOC-0049
  - DOC-0342
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: INDEX
purpose: Failure Recovery Matrix documentation.
scope: Reference documentation.
---

# Failure Recovery Matrix

## Document type
Document type: [REFERENCE]

## Purpose
Maps failure types to recovery behaviours.

## Matrix
- Timeout -> bounded retry.
- Invariant breach -> fail closed.

## Cross-References
- `../../historical/traceability-matrix.md`
