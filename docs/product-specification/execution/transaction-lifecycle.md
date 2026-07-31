---
metadata_schema_version: 1.0
document_id: DOC-0299
title: Transaction Lifecycle
plane: Product Specification
domain: Execution
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/execution/transaction-lifecycle.md
related_concepts:
  - CONCEPT-0299
dependencies:
  - DOC-0266
  - DOC-0280
  - DOC-0301
  - DOC-0315
consumers:
  - DOC-0031
  - DOC-0049
  - DOC-0285
  - DOC-0291
  - DOC-0301
  - DOC-0302
  - DOC-0315
  - DOC-0321
  - DOC-0322
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: Transaction Lifecycle documentation.
scope: Reference documentation.
---

# Transaction Lifecycle

## Document type
This document is an overview, reference, or index as noted below.

# Transaction Lifecycle

## Purpose
Defines submission, confirmation, replacement, cancellation, and finality handling for chain transactions.

## Ownership
- Owns transaction state, receipt tracking, replacement, cancellation, and finality boundaries.
- Does not own trade ranking or risk policy.

## Missing details covered
- Replacement logic must define nonce bumping and retry limits.
- Persistence must define how state survives Windows restarts.
- Recovery must define reorg, pending, and failed transaction handling.

## Cross-references
- `./execution-engine.md`
- `../data/database-schema.md`
- `../market/gas-optimisation.md`
- `./wallet-management.md`

## Required details
- Define replacement logic, persistence, and Windows restart recovery.

## Recovery
- Replacement and nonce bump rules must be explicit.
- Pending state must persist across app restarts.

## Transaction rules
- Define submission, pending, confirmation, replacement, cancellation, and finality.
- Define persistence and recovery across restarts.

## Lifecycle model
- Initial state: defined by the lifecycle owner.
- Terminal state: defined by the lifecycle owner.
- Allowed transitions: explicitly listed by the lifecycle owner.
- Forbidden transitions: explicitly listed by the lifecycle owner.
- Recovery transitions: explicitly listed by the lifecycle owner.
- Failure transitions: explicitly listed by the lifecycle owner.
