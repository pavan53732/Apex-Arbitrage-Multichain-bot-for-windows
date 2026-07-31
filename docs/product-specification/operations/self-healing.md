---
metadata_schema_version: 1.0
document_id: DOC-0351
title: Self Healing
plane: Product Specification
domain: Operations
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/operations/self-healing.md
related_concepts:
  - CONCEPT-0351
dependencies:
  - DOC-0335
  - DOC-0347
  - DOC-0349
consumers:
  - DOC-0049
  - DOC-0342
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: Self Healing documentation.
scope: Reference documentation.
---

# Self Healing

## Document type
This document is an overview, reference, or index as noted below.

# Self-Healing

## Purpose
Defines the canonical recovery actions for workers, RPC, providers, caches, wallets, and queues.

## State machine
```mermaid
stateDiagram-v2
  [*] --> DETECTING
  DETECTING --> TRIAGING
  TRIAGING --> RECOVERING
  RECOVERING --> VERIFYING
  VERIFYING --> STABLE
  VERIFYING --> FAILED
```

## Failure modes
Transient failure, repeated failure, unrecoverable failure.

## Recovery
Restart worker, reconnect RPC, switch provider, reload cache, recover queue, notify operators.

## Cross-references
- `./healthchecks.md`
- `./provider-resilience.md`
- `./recovery-and-failover.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
