---
metadata_schema_version: 1.0
document_id: DOC-0097
title: Shutdown Lifecycle
plane: Product Specification
domain: Runtime
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/runtime/shutdown-lifecycle.md
related_concepts:
  - CONCEPT-0097
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Runtime
type: REFERENCE
purpose: Shutdown Lifecycle documentation.
scope: Reference documentation.
---

# Shutdown Lifecycle

## Document type
This document is an overview, reference, or index as noted below.

# Shutdown Lifecycle

## Purpose
Defines controlled shutdown behavior.

## State machine
```mermaid
stateDiagram-v2
  [*] --> GRACEFUL_DRAIN
  GRACEFUL_DRAIN --> CHECKPOINT_WORKERS
  CHECKPOINT_WORKERS --> FLUSH_QUEUES
  FLUSH_QUEUES --> CLOSE_CONNECTIONS
  CLOSE_CONNECTIONS --> EXIT
```

## Allowed transitions
- GRACEFUL_DRAIN -> CHECKPOINT_WORKERS.
- CHECKPOINT_WORKERS -> FLUSH_QUEUES.
- FLUSH_QUEUES -> CLOSE_CONNECTIONS.
- CLOSE_CONNECTIONS -> EXIT.

## Forbidden transitions
- GRACEFUL_DRAIN -> EXIT.
- CHECKPOINT_WORKERS -> EXIT.
- FLUSH_QUEUES -> CHECKPOINT_WORKERS.

## Recovery
- If checkpoint fails, the process remains in GRACEFUL_DRAIN and retries checkpointing.

## Cross-references
- `../operations/runtime-operations.md`
- `./orchestrator.md`

## Operational Contract
Defines graceful shutdown, queue flushing, state persistence, worker stop order, and final disposal.

## Example
Execution stops before caches are flushed and state is saved.

## Required details
- Define graceful stop, drain, flush, and forced shutdown behavior.

## Lifecycle model
- Initial state: defined by the lifecycle owner.
- Terminal state: defined by the lifecycle owner.
- Allowed transitions: explicitly listed by the lifecycle owner.
- Forbidden transitions: explicitly listed by the lifecycle owner.
- Recovery transitions: explicitly listed by the lifecycle owner.
- Failure transitions: explicitly listed by the lifecycle owner.
