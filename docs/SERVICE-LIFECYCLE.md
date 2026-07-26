# Service Lifecycle

## Purpose
Defines the canonical lifecycle for all services.

## State machine
```mermaid
stateDiagram-v2
  [*] --> REGISTERED
  REGISTERED --> INITIALIZING
  INITIALIZING --> STARTING
  STARTING --> HEALTHY
  HEALTHY --> PAUSED
  PAUSED --> RESTARTING
  RESTARTING --> STARTING
  HEALTHY --> STOPPING
  STOPPING --> DISPOSED
```

## Cross-references
- `APEX-KERNEL.md`
- `ORCHESTRATOR.md`
- `HEALTHCHECKS.md`

## Operational Contract
Defines service registration, initialization, start, healthy, paused, restarting, stopping, and disposed transitions.

## Example
A worker service transitions to paused during maintenance.

## Windows service lifecycle
- Must define SCM states and recovery actions.

## Required details
- Define SCM lifecycle states and recovery actions.

## Windows SCM
- Define install, start, stop, restart, and recovery states under Windows SCM.
- Define delayed start and service account behavior.

## Service states
- Define install, start, stop, restart, and recovery states under Windows SCM.
- Define delayed start and service account behavior.
