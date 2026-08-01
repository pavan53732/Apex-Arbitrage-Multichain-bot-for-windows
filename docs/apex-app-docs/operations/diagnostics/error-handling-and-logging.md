---
metadata_schema_version: 1.0
document_id: DOC-0334
title: Error Handling and Logging
plane: Product Specification
domain: Operations
class: Specification
authority: Canonical
status: Active
owner: Ops Team
version: 1.0.0
canonical_source: docs/apex-app-docs/operations/diagnostics/error-handling-and-logging.md
related_concepts:
  - CONCEPT-0334
dependencies: []
consumers:
  - DOC-0362
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Operations
type: CONTRACT
purpose: "Defines the canonical error namespace map, error taxonomy, retry classifications, severity mappings tied to error codes, logging policy, redaction rules, and escalation behavior. This document is the single authoritative source for all error handling governance."
scope: None
---

# Error Handling and Logging

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.1.0 | **Status:** Canonical | **Last Updated:** 2026-07-27 | **Owner:** Ops Team

## Purpose
Defines the canonical error namespace map, error taxonomy, retry classifications, severity mappings tied to error codes, logging policy, redaction rules, and escalation behavior. This document is the single authoritative source for all error handling governance.

---

## 1. Error Namespace Map

All error codes follow a hierarchical namespace: `ERR-<DOMAIN>-<CATEGORY>-<NNNN>`

| Namespace | Domain | Owner Document | Count |
|-----------|--------|----------------|-------|
| `ERR-TRADE-*` | Trading errors | TRADING-ENGINE.md | 20+ |
| `ERR-EXEC-*` | Execution errors | EXECUTION-ENGINE.md | 15+ |
| `ERR-RISK-*` | Risk errors | RISK-ENGINE.md | 10+ |
| `ERR-AI-*` | AI errors | AI-PIPELINE.md | 15+ |
| `ERR-CONFIG-*` | Configuration errors | CONFIGURATION-REFERENCE.md | 10+ |
| `ERR-PLUGIN-*` | Plugin errors | PLUGIN-SANDBOX-CONTRACT.md | 10+ |
| `ERR-RPC-*` | RPC/network errors | RPC-MANAGER.md | 10+ |
| `ERR-DB-*` | Database errors | DATABASE-SCHEMA.md | 5+ |
| `ERR-SEC-*` | Security errors | SECURITY-CONTRACTS.md | 10+ |
| `ERR-RUNTIME-*` | Runtime errors | RUNTIME-OPERATIONS.md | 10+ |
| `ERR-WORKER-*` | Worker errors | WORKER-POOL.md | 5+ |
| `ERR-EVENT-*` | Event bus errors | EVENT-BUS.md | 5+ |
| `ERR-WALLET-*` | Wallet errors | WALLET-MANAGEMENT.md | 10+ |
| `ERR-MEMORY-*` | Memory/resource errors | MEMORY-LIFECYCLE.md | 5+ |

---

## 2. Error Taxonomy (Canonical)

| Error Type | Code Pattern | Retryable? | Severity Range | Recovery | Owner |
|-----------|-------------|-----------|---------------|----------|-------|
| **ValidationError** | `ERR-*-VAL-*` | No | Low–High | Fix input; reject request | Config/AI |
| **AuthorizationError** | `ERR-SEC-AUTH-*` | No | High–Critical | Block access; audit; notify security | Security |
| **ConfigurationError** | `ERR-CONFIG-*` | No | Medium–High | Keep previous config; alert operator | Config |
| **ProviderError** | `ERR-AI-PROV-*` | Yes (transient) | Medium–High | Fallback provider; retry with backoff | AI |
| **RPCError** | `ERR-RPC-*` | Yes (transient) | Medium–High | Fallback endpoint; retry | Network |
| **QuoteStaleError** | `ERR-TRADE-STALE-*` | Yes (re-fetch) | Medium | Re-fetch price; skip opportunity if still stale | Market Data |
| **LiquidityError** | `ERR-RISK-LIQ-*` | No | Medium–High | Skip opportunity; alert | Risk |
| **RiskRejectedError** | `ERR-RISK-REJ-*` | No | Low–Medium | Log rejection; AI learns pattern | Risk |
| **ExecutionRejectedError** | `ERR-EXEC-REJ-*` | No | Medium–High | Abort trade; recovery if mid-leg | Execution |
| **ReconciliationError** | `ERR-TRADE-RECON-*` | Partial | High–Critical | Query chain; manual intervention if unresolved | Trading |
| **PersistenceError** | `ERR-DB-*` | Yes (retry) | Medium–High | Retry write; buffer in-memory; pause if buffer full | Database |
| **RecoverableTimeoutError** | `ERR-*-TIMEOUT-*` | Yes (retry) | Medium–High | Retry with backoff; fallback if available | Various |
| **UnrecoverableInvariantError** | `ERR-*-INV-*` | No | Critical | Fail closed; immediate halt; operator intervention | Various |
| **SecretError** | `ERR-SEC-SECRET-*` | No | High–Critical | Emergency rotation; security team paged | Security |
| **MemoryExhaustionError** | `ERR-MEMORY-*` | Partial | Critical | Force GC; throttle; Safe mode if persistent | Runtime |
| **PluginError** | `ERR-PLUGIN-*` | Partial | Low–Medium | Disable plugin; retry once | Plugin |
| **CircuitBreakerTripped** | `ERR-RISK-CB-*` | No (cooldown) | High | Wait for cooldown; resume when cleared | Risk |

---

## 3. Retry Classification Map

| Category | Retry Eligible? | Max Retries | Backoff Strategy | Backoff Cap | Fallback |
|----------|---------------|-------------|-----------------|-------------|----------|
| **Transient Network** (RPC timeout, 5xx, connection reset) | Yes | 3–5 | Exponential (1s, 2s, 4s, ...) | 30s | Fallback RPC endpoint |
| **Rate Limit** (429) | Yes | 1 | Wait per Retry-After header | Provider-specific | Secondary provider |
| **Provider Transient** (AI timeout, streaming error) | Yes | 3 | Exponential (1s, 2s, 4s) | 10s | Fallback provider chain |
| **Database Transient** (connection loss, lock timeout) | Yes | 5 | Linear (5s each) | 60s total | In-memory buffer |
| **Validation** (schema mismatch, invalid params) | No | 0 | — | — | Reject immediately |
| **Authorization** (unauthorized, forbidden) | No | 0 | — | — | Block + audit |
| **Invariant** (corrupted state, memory overflow) | No | 0 | — | — | Fail closed |
| **Security** (trust boundary violation, secret exposure) | No | 0 | — | — | Immediate isolation |

---

## 4. Severity Mapping (Error Code → Severity → Action)

| Severity | Error Examples | Automated Action | Operator Notification | SLA |
|----------|---------------|------------------|----------------------|-----|
| **Critical** | `ERR-SEC-AUTH-001` (key leak), `ERR-TRADE-INV-001` (invariant violation), `ERR-MEMORY-001` (OOM) | Immediate halt; fail closed; isolation; Safe mode | All channels (dashboard, notification, event log) | Ack: 15 min; Contain: 1 hr |
| **High** | `ERR-EXEC-REJ-001` (execution failure), `ERR-RPC-001` (RPC failure), `ERR-DB-001` (DB connection loss) | Retry + fallback; degrade if no fallback; circuit breaker | Dashboard notification + event log | Ack: 1 hr; Contain: 4 hr |
| **Medium** | `ERR-RISK-REJ-*` (risk rejection), `ERR-TRADE-STALE-*` (stale price), `ERR-PLUGIN-*` (plugin crash) | Log; skip opportunity; retry once for plugin | Dashboard notification | Ack: 4 hr |
| **Low** | `ERR-*-VAL-*` (validation), `ERR-CONFIG-*` (config mismatch) | Log warning; continue with safe default | Event log only | Next business day |

---

## 5. Logging Policy

### 5.1 Structured Log Format

Every log entry follows this schema:

```json
{
  "timestamp_utc": "2026-07-27T12:00:00Z",
  "level": "debug|info|warn|error|critical",
  "subsystem": "trading_engine|risk_engine|...",
  "error_code": "ERR-TRADE-001",
  "error_type": "ValidationError",
  "severity": "medium",
  "message": "Trade rejected: slippage exceeded",
  "correlation_id": "trade-123",
  "trace_id": "trace-456",
  "details": {
    "value": 1.5,
    "limit": 1.0,
    "check_name": "slippage"
  },
  "redacted": false,
  "stack_trace": null
}
```

### 5.2 Redaction Rules

| Must Redact | Detection Method | Replacement |
|-------------|-----------------|-------------|
| Private keys / seed phrases | Regex: `0x[0-9a-fA-F]{64}`, seed phrase patterns | `[REDACTED_KEY]` |
| API keys / tokens | Regex: `ghp_*`, `sk-*`, `key_*` patterns | `[REDACTED_TOKEN]` |
| Wallet addresses (in error logs only) | Regex: `0x[0-9a-fA-F]{40}` | `[REDACTED_ADDRESS]` |
| Passwords / secrets | Config key names matching `security.secret.*` | `[REDACTED_SECRET]` |
| IP addresses (optional) | Regex: IPv4/IPv6 patterns | `[REDACTED_IP]` |

### 5.3 Rate Limiting and Aggregation

- Repeated identical errors (same error_code + subsystem) are aggregated after 3 occurrences.
- Aggregation: `{error_code, subsystem, count, first_seen, last_seen}` (no individual messages).
- Critical errors are NEVER aggregated (every occurrence logged individually).
- Log buffer: 10 MB ring buffer; flushed to disk every `runtime.log.flush_interval_ms` (5s).

---

## 6. Escalation Rules

| Condition | Escalation Level | Action |
|-----------|-----------------|--------|
| Single Critical error | Security team paged | Isolate + audit |
| 3+ High errors in same subsystem within 5 min | Auto-recovery triggered | Per RECOVERY-PLAYBOOK.md |
| 5+ Medium errors in same subsystem within 10 min | Dashboard warning | Operator review recommended |
| Unresolved Critical error after 30 min | Executive notification | Full incident response |
| Error rate exceeds 10/min for any subsystem | Throttle subsystem | Rate-limit processing; consider Safe mode |

---

## 7. IPC Error Contract

| Error Source | IPC Response | Consumer Action |
|-------------|-------------|-----------------|
| Validation error | `{success: false, error_code: "ERR-*-VAL-*", message, details}` | Fix input; retry with corrected params |
| Authorization error | `{success: false, error_code: "ERR-SEC-AUTH-*", message}` | No retry; check permissions |
| Transient error | `{success: false, error_code: "ERR-*-TIMEOUT-*", retryable: true, message}` | Retry with backoff + fallback |
| Invariant error | `{success: false, error_code: "ERR-*-INV-*", retryable: false, severity: "critical"}` | No retry; escalate to operator |
| Rate limit | `{success: false, error_code: "ERR-*-RATE-*", retry_after_ms: 5000}` | Wait + retry |

---

## Cross-References

- **ERROR-CATALOG.md** — Full error code catalog (authoritative for error definitions).
- **ERROR-CODES.md** — Stable machine-readable error codes (authoritative for code enumeration).
- **FAILURE-MATRIX.md** — Failure mode definitions (authoritative for failure catalog).
- **FAILURE-RECOVERY-MATRIX.md** — Failure-to-recovery mapping (authoritative for recovery actions).
- **RECOVERY-PLAYBOOK.md** — Per-failure-class recovery procedures.
- **RECOVERY-COORDINATION.md** — Multi-failure recovery coordination.
- **SECURITY.md** — Security error handling and incident response.
- **MONITORING-OBSERVABILITY.md** — Error metric aggregation and alerting.
- **IPC-PROTOCOL.md** — IPC error response contract.
- **TRACEABILITY-MATRIX.md** — Error handling requirements.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.1.0 | 2026-07-27 | Full error namespace map, taxonomy, retry classification, severity mapping, structured logging, redaction rules, escalation, IPC error contract | Ops Team |
| 1.0.0 | 2025-01-15 | Initial stub | Ops Team |
