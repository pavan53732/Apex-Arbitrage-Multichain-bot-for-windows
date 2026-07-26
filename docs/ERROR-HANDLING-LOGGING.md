# ERROR-HANDLING-LOGGING.md

## Purpose
Defines the canonical error model, retry behavior, recovery flows, and logging standards for APEX.

## Scope
Covers application errors, domain errors, infrastructure failures, AI provider failures, IPC errors, user-facing error presentation, and structured logs.

## Related Documents
- [MONITORING-OBSERVABILITY.md](./MONITORING-OBSERVABILITY.md)
- [IPC-PROTOCOL.md](./IPC-PROTOCOL.md)
- [SECURITY.md](./SECURITY.md)
- [RISK-ENGINE.md](./RISK-ENGINE.md)

## Error Categories
- `ConfigurationError`
- `ValidationError`
- `ProviderError`
- `ChainConnectionError`
- `QuoteError`
- `ExecutionError`
- `RiskRejectionError`
- `IpcContractError`
- `PersistenceError`
- `SecurityPolicyError`

## Logging Standard
All logs must be structured JSON with:
- timestamp
- level
- domain
- event
- message
- correlationId
- entity identifiers when relevant
- sanitized context object

## Redaction Rules
- Never log API keys, seed phrases, private keys, raw auth headers, or decrypted secret values.
- Wallet addresses may be logged when necessary.
- RPC URLs should be masked when they contain credentials.

## Retry Policy
- AI provider: bounded exponential backoff, circuit breaker on repeated 429/5xx.
- RPC calls: retry idempotent reads only.
- Quote fetches: short retry budget; do not loop indefinitely.
- Trade execution: never blindly retry a signed transaction without nonce-aware safeguards.

## User-Facing Behavior
- Actionable errors should include cause, impact, and next step.
- Fatal startup errors must block execution with recovery instructions.
- Background recoverable failures should surface as status banners or log entries, not modal spam.

## AI Agent Guidance
- Every thrown error must map to a category in this document.
- Every retryable operation must define idempotency assumptions in code.
