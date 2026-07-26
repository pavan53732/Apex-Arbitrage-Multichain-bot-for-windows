# Execution Lifecycle

## Purpose
Defines execution state transitions from queued order to final chain outcome.

## State machine
```mermaid
stateDiagram-v2
  [*] --> PENDING
  PENDING --> QUEUED
  QUEUED --> SIGNING
  SIGNING --> BROADCASTING
  BROADCASTING --> CONFIRMING
  CONFIRMING --> FINALIZED
  CONFIRMING --> REVERTED
  REVERTED --> QUEUED
```

## Allowed transitions
- PENDING -> QUEUED.
- QUEUED -> SIGNING.
- SIGNING -> BROADCASTING.
- BROADCASTING -> CONFIRMING.
- CONFIRMING -> FINALIZED or REVERTED.
- REVERTED -> QUEUED.

## Forbidden transitions
- PENDING -> BROADCASTING.
- SIGNING -> FINALIZED.
- FINALIZED -> CONFIRMING.

## Recovery
- REVERTED may return to QUEUED after retry policy succeeds.

## Cross-references
- `TRADING-LIFECYCLE.md`
- `ORCHESTRATOR.md`
- `DOMAIN-MODEL.md`

## Operational Contract
Defines the lifecycle from pre-checks through simulation, approval, submission, confirmation, and post-trade reconciliation.

## Example
Execution pauses if confirmations are not received within policy.

## Required details
- Define preflight, send, pending, confirm, replace, cancel, and finality rules.
