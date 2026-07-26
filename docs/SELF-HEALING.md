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
- `HEALTHCHECKS.md`
- `PROVIDER-RESILIENCE.md`
- `RECOVERY-AND-FAILOVER.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
