# Worker Architecture

## Purpose
Owns worker lifecycle, process model, concurrency boundaries, and worker-to-queue coordination.

## Responsibilities
- Define worker roles and lifecycles.
- Map tasks to worker classes.
- Bound concurrency and isolation.
- Coordinate startup, shutdown, draining, and recovery.

## Cross-references
- `RUNTIME-OPERATIONS.md`
- `MONITORING-OBSERVABILITY.md`
- `IPC-PROTOCOL.md`
