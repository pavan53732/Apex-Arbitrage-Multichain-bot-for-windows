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
- `DASHBOARD-WORKSPACES.md`

## Operational Contract
Defines the live system view of active chains, plugins, workers, wallets, provider capabilities, health, and metrics.

## Example
The dashboard reads runtime knowledge to show active workers and healthy providers.

## Windows runtime context
- Must define tray, notifications, and service state visibility.
