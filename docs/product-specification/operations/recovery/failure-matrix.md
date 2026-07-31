---
metadata_schema_version: 1.0
document_id: DOC-0340
title: Failure Matrix
plane: Product Specification
domain: Operations
class: Index
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/operations/recovery/failure-matrix.md
related_concepts:
  - CONCEPT-0340
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Operations
type: INDEX
purpose: Failure Matrix documentation.
scope: Reference documentation.
---

# Failure Matrix

## Document type
Document type: [REFERENCE]

## Purpose
Maps failures to actions.

## Examples
- RPC timeout -> retry -> provider switch -> cooldown -> operator intervention.
