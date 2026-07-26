# IPC Protocol

## Purpose
Defines canonical IPC channels, message families, payload rules, and security boundaries.

## Rules
- Every IPC channel is owned by one subsystem document.
- Inputs are validated at the preload or main boundary.
- All messages are typed, serializable, versioned, and permission-scoped.
- Renderer-initiated calls must not mutate authoritative state directly.

## Channel families
- `trading.*` owned by `docs/TRADING-ENGINE.md`
- `execution.*` owned by `docs/EXECUTION-ENGINE.md`
- `strategy.*` owned by `docs/STRATEGIES.md`
- `wallet.*` owned by `docs/WALLET-MANAGEMENT.md`
- `portfolio.*` owned by `docs/PORTFOLIO-MANAGEMENT.md`
- `settings.*` owned by `docs/CONFIGURATION.md`
- `app.*` owned by `docs/RUNTIME-OPERATIONS.md`
- `events.*` owned by `docs/STATE-MANAGEMENT.md`

## Cross-references
- `docs/API-CONTRACTS.md`
- `docs/API-REFERENCE.md`
- `docs/STATE-MANAGEMENT.md`
- `docs/RUNTIME-OPERATIONS.md`
