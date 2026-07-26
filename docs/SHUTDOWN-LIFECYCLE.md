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
- `RUNTIME-OPERATIONS.md`
- `ORCHESTRATOR.md`

## Operational Contract
Defines graceful shutdown, queue flushing, state persistence, worker stop order, and final disposal.

## Example
Execution stops before caches are flushed and state is saved.
