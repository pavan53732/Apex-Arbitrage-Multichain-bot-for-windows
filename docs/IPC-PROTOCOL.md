# IPC Protocol

## Purpose
Defines typed inter-process commands, events, payload shapes, and reliability rules between renderer, main process, workers, and subsystems.

## Ownership
- Owns channel naming, payload contracts, request/response flows, and event semantics.
- Does not own business logic.

## Contract rules
- Every IPC channel must have one authoritative owner and one payload schema.
- Channel names must be stable, namespaced, and versioned when breaking changes occur.
- Requests must include correlation id and schema version.
- Responses must include success or error state, reason code, and payload.
- Events must be immutable and replay-safe.

## Major channel families
- trading.
- execution.
- risk.
- ai.
- market.
- monitoring.
- runtime.
- settings.
- simulation.
- session.
- wallet.
- chain.
- diagnostics.
- backup.
- restore.

## Reliability rules
- Handlers must validate payloads before execution.
- Invalid requests must fail with typed errors, not partial work.
- Duplicate request detection must use correlation id or idempotency key where applicable.
- Long-running operations must emit progress and completion events.

## Event semantics
- State transition events must reflect authoritative durable state.
- Monitoring events must never mutate state.
- Recovery events must describe what was reconciled, not what is hoped for.

## Cross-references
- `TRADING-ENGINE.md`
- `EXECUTION-ENGINE.md`
- `AI-PIPELINE.md`
- `MARKET-DATA.md`
- `MARKET-INTELLIGENCE.md`
- `MONITORING-OBSERVABILITY.md`
- `RUNTIME-OPERATIONS.md`

## Operational Contract
Defines IPC transport rules, envelope format, routing, acknowledgement, retry, and version negotiation.

## Example
A UI request is acknowledged, routed, and confirmed with a correlation id.
