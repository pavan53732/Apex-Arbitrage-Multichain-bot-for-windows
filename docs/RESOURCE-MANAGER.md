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
