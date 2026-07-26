# ERROR-HANDLING-LOGGING.md

## Purpose
Defines the error model, logging standards, retry policies, and recovery behaviour for APEX.

## Scope
Application errors across AI, chain adapters, DEX adapters, IPC, database, updater, and UI surfaces.

## Error Hierarchy
- `AppError` (base typed error)
- `ConfigError`
- `ValidationError`
- `SecurityError`
- `ProviderError`
- `RateLimitError`
- `ChainConnectionError`
- `QuoteExpiredError`
- `ExecutionRejectedError`
- `RiskViolationError`
- `PersistenceError`
- `IpcContractError`

## Error Metadata Requirements
Every typed error should carry:
- machine-readable code,
- category,
- user-safe message,
- internal diagnostic message,
- retriable flag,
- severity,
- optional causal chain.

## Logging Format
Structured JSON logs for machine ingestion with fields:
- timestamp
- level
- service
- module
- event
- correlationId
- requestId/taskId when applicable
- chainId / provider / strategyId when applicable
- redacted error object

## Redaction Rules
Never log:
- API keys,
- wallet private keys or seed phrases,
- raw Authorization headers,
- full account addresses if policy later requires masking,
- unredacted user prompts when marked sensitive.

## Retry Policy
| Category | Retry? | Strategy |
|---|---|---|
| Rate limit | yes | exponential backoff with jitter |
| network timeout | yes | bounded retries |
| schema validation | no | fail fast and alert developer/user |
| risk violation | no | immediate halt/reject |
| stale quote | maybe | re-quote once if within timing budget |
| DB locked | limited | short bounded retry |

## User-Facing Behaviour
- Errors shown in UI must be safe, concise, and actionable.
- Provide retry action only when safe.
- Critical risk/security events should be sticky and visible until acknowledged.
- Background warnings should not block the entire UI.

## Recovery Flows
- provider failure -> fallback provider if policy allows,
- quote failure -> refresh quote path,
- chain RPC failure -> failover to backup RPC,
- DB corruption suspicion -> read-only safe mode,
- preload/IPC contract mismatch -> block execution path and require update.

## Diagnostics and Support Bundles
Support export should include:
- recent redacted logs,
- app version,
- OS version,
- enabled providers/chains,
- config summary without secrets,
- error timeline.

## Cross-References
- [`MONITORING-OBSERVABILITY.md`](./MONITORING-OBSERVABILITY.md)
- [`SECURITY.md`](./SECURITY.md)
- [`IPC-PROTOCOL.md`](./IPC-PROTOCOL.md)
- [`NON-FUNCTIONAL-REQUIREMENTS.md`](./NON-FUNCTIONAL-REQUIREMENTS.md)
