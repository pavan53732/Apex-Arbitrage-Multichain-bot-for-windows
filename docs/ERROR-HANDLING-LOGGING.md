# Error Handling Logging

## Document type
This document is an overview, reference, or index as noted below.

# Error Handling and Logging

## Purpose
Defines the canonical error taxonomy, logging policy, recovery paths, and escalation behavior.

## Ownership
- Owns error codes, log structure, redaction policy, escalation rules, and failure categories.
- Every subsystem must reuse these codes rather than inventing local variants when possible.

## Error taxonomy
- ValidationError.
- AuthorizationError.
- ConfigurationError.
- ProviderError.
- RPCError.
- QuoteStaleError.
- LiquidityError.
- RiskRejectedError.
- ExecutionRejectedError.
- ReconciliationError.
- PersistenceError.
- RecoverableTimeoutError.
- UnrecoverableInvariantError.

## Logging policy
- Logs must be structured with subsystem, severity, correlation id, and stable code.
- Logs must never include secrets, private keys, raw seed phrases, or raw signing material.
- Repeated errors should be rate limited and aggregated.

## Error-code consistency
- Each error type must map to a stable machine-readable code.
- Codes must be documented and reused across IPC, logging, and monitoring.
- Validation, authorization, and runtime errors must be distinguishable.

## Recovery rules
- Recoverable errors may retry within bounded policy.
- Invariant or security errors fail closed and may trigger emergency stop.
- Errors that affect execution state must produce a reconciliation task.

## IPC and event behavior
- IPC handlers must return structured errors using the canonical codes.
- Monitoring must aggregate errors by code and subsystem.
- Recovery workflows must subscribe to `recovery.*` or `monitoring.alert.*` events as appropriate.

## Persistence expectations
- Critical errors and halts must be persisted with correlation ids, codes, and minimal contextual fields.
- Transient, low-severity errors may be kept in rolling logs rather than long-term storage.

## Escalation
- Operator-facing alerts are required for wallet, execution, security, and chain health failures.
- User-facing messages must be concise and actionable.

## Cross-references
- `MONITORING-OBSERVABILITY.md`
- `SECURITY.md`
- `RUNTIME-OPERATIONS.md`
- `IPC-PROTOCOL.md`
- `VERSIONING.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
