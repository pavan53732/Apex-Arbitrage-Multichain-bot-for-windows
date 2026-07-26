# EVENT-FLOW.md

## Purpose
Defines event-driven behavior across the desktop runtime.

## Related Documents
- [DATA-FLOW.md](./DATA-FLOW.md)
- [IPC-PROTOCOL.md](./IPC-PROTOCOL.md)

## Core Event Classes
- user intent events
- configuration events
- strategy lifecycle events
- quote/market data events
- execution events
- risk events
- updater events
- diagnostics events

## Rules
- Events must be named in past-tense or domain-action format consistently.
- Events sent to renderer must be sanitized and typed.
- Event ordering requirements must be documented for critical workflows.
