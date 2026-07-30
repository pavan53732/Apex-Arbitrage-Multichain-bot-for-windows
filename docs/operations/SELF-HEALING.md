---
last_updated: 2026-07-29
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Self Healing documentation.
scope: Reference documentation.
canonical_source: docs/operations/SELF-HEALING.md
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
- `operations/HEALTHCHECKS.md`
- `PROVIDER-RESILIENCE.md`
- `operations/RECOVERY-AND-FAILOVER.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
