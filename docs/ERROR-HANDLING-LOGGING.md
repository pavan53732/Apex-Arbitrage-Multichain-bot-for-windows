# Error Handling and Logging

## Purpose
Defines canonical error taxonomy, logging format, retry classification, escalation, and recovery behavior.

## Responsibilities
- Classify errors as transient, permanent, or safety-critical.
- Define retry/backoff and fatal handling.
- Standardize structured logs.

## Error taxonomy
Each error must declare subsystem, severity, retryability, operator action, and recovery path.

## Logging
Logs must carry correlation IDs, timestamps, subsystem names, and actionable messages.

## Cross-references
- `MONITORING-OBSERVABILITY.md`
- `RUNTIME-OPERATIONS.md`
- `SECURITY.md`
