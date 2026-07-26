# PERFORMANCE-TARGETS.md

## Purpose
Defines measurable latency, memory, startup, and throughput goals.

## Initial Targets
- cold start to interactive UI: <= 4s on supported Windows baseline
- IPC roundtrip: <= 100ms for normal settings/actions
- quote pipeline response: <= 2s under normal RPC conditions
- AI suggestion request: user-visible progress within 500ms, full response target <= 30s

## Cross-References
- [`MONITORING-OBSERVABILITY.md`](./MONITORING-OBSERVABILITY.md)
- [`NON-FUNCTIONAL-REQUIREMENTS.md`](./NON-FUNCTIONAL-REQUIREMENTS.md)
