---
metadata_schema_version: 1.0
document_id: DOC-0289
title: Execution Lifecycle
plane: Product Specification
domain: Execution
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/execution/execution-lifecycle.md
related_concepts:
  - CONCEPT-0289
dependencies:
  - DOC-0087
  - DOC-0252
  - DOC-0298
consumers:
  - DOC-0005
  - DOC-0020
  - DOC-0021
  - DOC-0022
  - DOC-0023
  - DOC-0025
  - DOC-0026
  - DOC-0027
  - DOC-0028
  - DOC-0029
  - DOC-0030
  - DOC-0031
  - DOC-0032
  - DOC-0033
  - DOC-0035
  - DOC-0036
  - DOC-0037
  - DOC-0038
  - DOC-0039
  - DOC-0040
  - DOC-0041
  - DOC-0042
  - DOC-0043
  - DOC-0049
  - DOC-0079
  - DOC-0283
  - DOC-0285
  - DOC-0287
  - DOC-0290
  - DOC-0298
  - DOC-0328
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: Execution Lifecycle documentation.
scope: Reference documentation.
---

# Execution Lifecycle

## Document type
This document is a reference.

# Execution Lifecycle

## Purpose
Defines execution state transitions from queued order to final chain outcome.

## State machine
```mermaid
stateDiagram-v2
  [*] --> PENDING
  PENDING --> QUEUED
  QUEUED --> SIGNING
  SIGNING --> BROADCASTING
  BROADCASTING --> CONFIRMING
  CONFIRMING --> FINALIZED
  CONFIRMING --> REVERTED
  REVERTED --> QUEUED
```

## Allowed transitions
- PENDING -> QUEUED.
- QUEUED -> SIGNING.
- SIGNING -> BROADCASTING.
- BROADCASTING -> CONFIRMING.
- CONFIRMING -> FINALIZED or REVERTED.
- REVERTED -> QUEUED.

## Forbidden transitions
- PENDING -> BROADCASTING.
- SIGNING -> FINALIZED.
- FINALIZED -> CONFIRMING.

## Recovery
- REVERTED may return to QUEUED after retry policy succeeds.

## Cross-references
- `./trading-lifecycle.md`
- `../runtime/orchestrator.md`
- `../interfaces/domain-model.md`

## Operational Contract
Defines the lifecycle from pre-checks through simulation, approval, submission, confirmation, and post-trade reconciliation.

## Example
Execution pauses if confirmations are not received within policy.

## Required details
- Define preflight, send, pending, confirm, replace, cancel, and finality rules.

## Execution flow
- Preflight, send, pending, confirm, replace, cancel, and finality must be explicit.

## Lifecycle model
- Initial state: defined by the lifecycle owner.
- Terminal state: defined by the lifecycle owner.
- Allowed transitions: explicitly listed by the lifecycle owner.
- Forbidden transitions: explicitly listed by the lifecycle owner.
- Recovery transitions: explicitly listed by the lifecycle owner.
- Failure transitions: explicitly listed by the lifecycle owner.

## Initial state
- PENDING.

## Terminal state
- FINALIZED.
- REVERTED is terminal for the failed attempt and may transition to QUEUED only via recovery.

## Recovery transitions
- REVERTED -> QUEUED.
- BROADCASTING -> QUEUED when broadcast must be retried before confirmation.

## Failure transitions
- SIGNING -> REVERTED.
- BROADCASTING -> REVERTED.
- CONFIRMING -> REVERTED.
