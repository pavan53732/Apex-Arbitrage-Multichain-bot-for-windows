# EVENT-FLOW.md

## Purpose
Defines event-driven behaviour across runtime layers.

## Event Sources
- UI commands
- scheduled jobs
- provider callbacks
- chain state changes
- updater events
- error events

## Event Handling Rules
- Every event has one owner.
- Events crossing process boundaries must use typed IPC contracts.
- High-risk events require audit logging.

## Cross-References
- [`IPC-PROTOCOL.md`](./IPC-PROTOCOL.md)
- [`STATE-MANAGEMENT.md`](./STATE-MANAGEMENT.md)
