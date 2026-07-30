---
last_updated: 2026-07-29
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Live Architecture Viewer documentation.
scope: Reference documentation.
canonical_source: docs/LIVE-ARCHITECTURE-VIEWER.md
---

# Live Architecture Viewer

## Document type
This document is an overview, reference, or index as noted below.

# Live Architecture Viewer

## Purpose
Defines the authoritative live topology and runtime visualization layer for modules, queues, events, and health.

## Scope
Strategies, workers, AI, chains, DEXs, wallets, providers, queues, and event routes.

## State machine
```mermaid
stateDiagram-v2
  [*] --> DISCOVERING
  DISCOVERING --> RENDERING
  RENDERING --> SYNCED
  SYNCED --> STALE
  STALE --> REFRESHING
  REFRESHING --> SYNCED
```

## Failure modes
Stale graph, missing node, invalid edge, render failure.

## Recovery
Refresh topology from kernel, requery registries, and fall back to cached graph.

## Cross-references
- `APEX-KERNEL.md`
- `DEPENDENCY-GRAPH.md`
- `HEALTHCHECKS.md`
- `dashboard/UI-DASHBOARD-SPEC.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Canonical ownership
This document defers to the canonical owners for implementation, policy, and schema details.
