---
last_updated: 2026-07-29
type: CONTRACT
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Resource Manager documentation.
scope: Reference documentation.
canonical_source: docs/RESOURCE-MANAGER.md
---

# Resource Manager

## Document type
This document is an overview, reference, or index as noted below.

# Resource Manager

## Purpose
Defines unified resource lifecycle management for wallets, workers, chains, AI, plugins, RPC, storage, and queues.

## State machine
```mermaid
stateDiagram-v2
  [*] --> REGISTERED
  REGISTERED --> HEALTHY
  HEALTHY --> DEGRADED
  DEGRADED --> RECOVERING
  RECOVERING --> HEALTHY
  HEALTHY --> RETIRED
```

## Failure modes
Missing resource, stale version, health degradation, exhaustion.

## Recovery
Rebind resource, replace endpoint, restart service, or retire resource.

## Cross-references
- `APEX-KERNEL.md`
- `SERVICE-REGISTRY.md`
- `REGISTRY-SYSTEM.md`
- `WORKER-POOL.md`

## Operational Contract
Defines allocation, quotas, cleanup, contention handling, and resource lifecycle.

## Example
A worker is paused when resource usage exceeds limits.
