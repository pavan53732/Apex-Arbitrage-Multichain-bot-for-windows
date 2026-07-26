# IPC Protocol

## Purpose
Defines canonical IPC channels, message families, payload rules, and security boundaries.

## Ownership
- Owns typed IPC channel naming, payload validation, event subscriptions, and permission gating.
- UI and preload clients must not invent ad-hoc channels.

## Channel groups
- app
- settings
- wallet
- portfolio
- strategy
- execution
- logs
- updater
- ai
- monitoring
- recovery
- market
- risk
- routing
- orders
- transactions

## Message rules
- Every request must have a correlation id.
- Every response must return a stable success or error shape.
- Events must be namespaced and versioned when breaking changes are introduced.
- Handlers must validate payloads before reaching business logic.
- Requests must be idempotent when they change durable state.

## Error consistency
- Error responses must include code, message, details, correlation id, and retryable flag.
- Stable error codes must be reused across all IPC handlers.
- Validation failures must be distinguishable from authorization or runtime failures.

## Event ownership
- `trading.*` events belong to the trading engine.
- `execution.*` events belong to the execution engine.
- `order.*` events belong to order management.
- `transaction.*` events belong to transaction lifecycle.
- `risk.*` events belong to risk engine.
- `route.*` events belong to routing engine.
- `market.*` events belong to market data and market intelligence.
- `monitoring.*` events belong to monitoring and observability.
- `recovery.*` events belong to runtime operations.

## Security boundaries
- Sensitive commands require explicit permission scope.
- Secrets and signing operations are never exposed directly to the renderer.
- File system operations must be allowlisted.
- Transaction submission and wallet unlock flows must require the owning subsystem to validate state.

## Persistence expectations
- IPC handlers that change durable state must persist before acknowledging success unless the owner explicitly defines eventual persistence.
- Event emissions for durable state changes must include the persisted entity id and terminal state.

## Cross-references
- `API-REFERENCE.md`
- `TRADING-ENGINE.md`
- `EXECUTION-ENGINE.md`
- `WALLET-MANAGEMENT.md`
- `RUNTIME-OPERATIONS.md`
