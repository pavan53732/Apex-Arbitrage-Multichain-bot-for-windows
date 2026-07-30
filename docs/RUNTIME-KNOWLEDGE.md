---
last_updated: 2026-07-29
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Runtime Knowledge documentation.
scope: Reference documentation.
canonical_source: docs/RUNTIME-KNOWLEDGE.md
---

# Runtime Knowledge

## Document type
This document is an overview, reference, or index as noted below.

# Runtime Knowledge

## Purpose
Defines what the running system knows about itself at runtime.

## Contents
Active chains, loaded plugins, running workers, connected wallets, provider capabilities, health state, runtime metrics.

## State machine
```mermaid
stateDiagram-v2
  [*] --> COLLECTING
  COLLECTING --> INDEXING
  INDEXING --> SERVING
  SERVING --> REFRESHING
  REFRESHING --> COLLECTING
```

## Failure modes
Stale knowledge, missing runtime state, inconsistent service view.

## Recovery
Refresh from kernel, registries, health probes, and event stream.

## Cross-references
- `APEX-KERNEL.md`
- `HEALTHCHECKS.md`
- `MONITORING-OBSERVABILITY.md`
- `dashboard/DASHBOARD-WORKSPACES.md`

## Operational Contract
Defines the live system view of active chains, plugins, workers, wallets, provider capabilities, health, and metrics.

## Example
The dashboard reads runtime knowledge to show active workers and healthy providers.

## Windows runtime context
- Must define tray, notifications, and service state visibility.

## Required details
- Define runtime state and Windows surfaces.

## Runtime rules
- Define service state, tray state, and Windows notification visibility.
- Define how runtime knowledge survives restarts.
