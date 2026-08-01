---
metadata_schema_version: 1.0
document_id: DOC-0107
title: AI Tool Invocation Contract
plane: Product Specification
domain: AI
class: Specification
authority: Canonical
status: Active
owner: AI Team
version: 1.0.0
canonical_source: docs/apex-app-docs/ai/tools/ai-tool-invocation-contract.md
related_concepts:
  - CONCEPT-0107
dependencies: []
consumers:
  - DOC-0409
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - AI
type: CONTRACT
purpose: "Defines when AI may call tools and under which priority, fallback, timeout, and retry policies. This contract is the single authoritative source for all tool invocation governance."
scope: Ai Tool Invocation Contract scope and boundaries.
---

# AI Tool Invocation Contract

## Document type
Document type: [CONTRACT]

## Version
**Version:** 0.2.0 | **Status:** Draft | **Last Updated:** 2026-07-27 | **Owner:** AI Team

## Purpose
Defines when AI may call tools and under which priority, fallback, timeout, and retry policies. This contract is the single authoritative source for all tool invocation governance.

---

## 1. Invocation Authority

The AI agent may invoke a tool if and only if **all** of the following conditions are met:

1. The tool is registered in the tool registry (`./ai-tools.md`).
2. The tool's required capabilities are available in the current context.
3. The tool invocation does not violate the current trust boundary (`../../security/trust-boundaries.md`).
4. The tool has not been rate-limited or circuit-broken.
5. The invoking AI has not exceeded its invocation budget (max calls per session / per minute).
6. The tool's preconditions (if any) evaluate to `true`.

---

## 2. Tool Priority & Selection

### Priority Tiers

| Tier | Priority | Selection Strategy | Examples |
|------|----------|--------------------|----------|
| 1 | **Mandatory** | Always invoked when preconditions match | `read_file`, `search_files`, `validate_config` |
| 2 | **Contextual** | Selected based on learned priority model | `web_search`, `terminal`, `execute_code` |
| 3 | **Fallback** | Only if Tier 1/2 tools fail or are unavailable | `delegate_task`, `clarify` |
| 4 | **Informational** | Passive; invoked only when explicitly requested | `memory`, `session_search` |

### Selection Algorithm

1. Build candidate set: all registered tools whose preconditions are met.
2. Sort by tier (1 → 4).
3. Within each tier, sort by learned priority rank (if `ai.tools.priority_config: learned`) or static rank (if `static`).
4. Select top N tools where N = `ai.tools.max_tools_per_call` (default: 10).
5. If `manual` mode, the AI explicitly selects tools based on the task.

---

## 3. Tool Fallback Chain

When a tool invocation fails:

```
Attempt tool → Timeout? → Retry (up to N) → [Fail] → Fallback tool? → Retry fallback → [All fail] → Report error
```

### Fallback Rules

| Condition | Action |
|-----------|--------|
| Primary tool fails (timeout, error, empty result) | Try fallback tool from same functional group |
| No fallback defined for the tool | Return error to AI; AI must decide next action |
| All fallbacks exhausted | Log failure, increment tool error counter, trigger circuit breaker if threshold exceeded |
| Fallback succeeds | Log fallback usage for telemetry |

### Built-in Fallback Groups

| Functional Group | Primary Tool | Fallback Tool |
|------------------|-------------|---------------|
| File reading | `read_file` | `terminal cat/head` (via `terminal`) |
| File search | `search_files` | `terminal grep/find` |
| Code execution | `execute_code` | `terminal python3` |
| Web search | `web_search` | `web_fetch` (falls back to search engine) |
| Process management | `process` | `terminal ps/top` |

---

## 4. Timeout Policy

| Parameter | Default | Range | Description |
|-----------|---------|-------|-------------|
| Per-tool timeout | `ai.tools.timeout_ms`: 15000ms | 1000–60000ms | Max wall-clock time per tool invocation |
| Per-call aggregate timeout | `ai.providers.timeout_ms`: 30000ms | 1000–120000ms | Max total time for all tools in one AI call |
| Idle timeout before first byte | 5000ms | 500–30000ms | Max time from invocation to first progress |

### Timeout Behavior

- If a tool exceeds its per-tool timeout, it is **cancelled** and treated as a failure.
- If the aggregate timeout is exceeded, all in-flight tools are cancelled and the AI call returns with a timeout error.
- Timeouts are logged with tool name, duration, and timeout value for observability.

---

## 5. Retry Policy

| Parameter | Default | Range | Description |
|-----------|---------|-------|-------------|
| Max attempts | `ai.providers.retry.max_attempts`: 3 | 0–10 | Total attempts (1 initial + N-1 retries) |
| Backoff | `ai.providers.retry.backoff_ms`: 1000ms | 100–60000ms | Initial backoff duration |
| Backoff multiplier | `ai.providers.retry.backoff_multiplier`: 2.0 | 1.0–5.0 | Exponential multiplier |
| Jitter | `ai.providers.retry.jitter_ms`: 200ms | 0–5000ms | Random jitter added to backoff |

### Retry Eligibility

| Error Category | Retry Eligible? | Notes |
|----------------|-----------------|-------|
| Network / timeout | Yes | Transient failures benefit most |
| Rate limit (429) | Yes | Use exponential backoff with jitter |
| Server error (5xx) | Yes | Server-side transient |
| Client error (4xx, non-429) | No | Invalid request; fix before retry |
| Validation error | No | Tool preconditions not met |
| Safety violation | No | Must be handled by safety layer |

### Circuit Breaker

If a tool fails (all retries exhausted) more than:

- **5 times** in a 60-second window → circuit opens
- Circuit open duration: `120 seconds`
- After cooldown: half-open (1 probe attempt allowed)
- Probe success → circuit closes
- Probe failure → circuit reopens for another 120s

---

## 6. Safety & Guardrails

| Rule | Enforcement |
|------|-------------|
| No tool may access sensitive paths outside the workspace | Checked at invocation time against allowed path list |
| No tool may modify system files | Denied by tool capability registry |
| No tool may access secrets directly | All secret access must go through `secret-manager` tool |
| No tool may execute unsigned code | Only registered tools/scripts in allowed directories |
| No tool may invoke another AI agent without explicit safety check | `delegate_task` requires safety approval gate |

### Safety Violation Handling

1. First violation: log warning, retry with safer parameters (max `ai.safety.max_retries_on_safety_violation`: 2).
2. Repeated violation: abort entire AI call, log security event, notify security subsystem.
3. Violation triggers `security.violation` event (see `../../interfaces/events/event-ownership-matrix.md`).

---

## 7. Observability

Every tool invocation produces:

| Field | Description |
|-------|-------------|
| `tool_name` | Name of the invoked tool |
| `tier` | Priority tier (1–4) |
| `invocation_id` | Unique ID for this call |
| `started_at` | Timestamp (UTC) |
| `duration_ms` | Wall-clock duration |
| `retry_count` | Number of retries (0 if first attempt succeeded) |
| `result` | `success`, `failure`, `timeout`, `cancelled`, `safety_blocked` |
| `fallback_used` | Name of fallback tool if primary failed |
| `error_code` | Error code if failed (from `../../operations/diagnostics/error-codes.md`) |
| `tokens_consumed` | Estimated tokens used by tool IO |

All invocation events are emitted as `ai.tool.invoked` / `ai.tool.result` events (see `../../interfaces/events/event-ownership-matrix.md`) and stored in the audit log.

---

## 8. Tool Parameter Contract

Each tool invocation carries a parameter block validated against its schema:

```typescript
interface ToolInvocation {
  tool: string;
  params: Record<string, unknown>;
  context: {
    session_id: string;
    user_id?: string;
    invocation_id: string;
    trace_id: string;
  };
  constraints: {
    timeout_ms: number;
    max_retries: number;
    allowed_fallbacks: string[];
  };
}
```

- Tools must declare their parameter schema in the tool registry.
- Parameters are validated at invocation time; invalid params are rejected without execution.
- Sensitive parameters (secrets, paths) are redacted in logs.

---

## Cross-References

- **AI-TOOLS.md** — Tool registry and definitions.
- **TRACEABILITY-MATRIX.md** — Requirement-to-document mapping and governance validation.
- **AI-PIPELINE.md** — AI decision pipeline orchestration.
- **AI-SAFETY-BOUNDARY.md** — Safety boundary enforcement.
- **TRUST-BOUNDARIES.md** — Trust domain rules for tool access.
- **ERROR-CODES.md** — Tool error codes and meanings.
- **EVENT-OWNERSHIP-MATRIX.md** — Tool invocation event ownership.
- **CONFIGURATION-REFERENCE.md** — Tool config keys (`ai.tools.*`).
- **PROMPT-LIFECYCLE.md** — Prompt lifecycle that consumes tool results.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 0.2.0 | 2026-07-27 | Full contract with priority, fallback, timeout, retry, safety, observability | AI Team |
| 0.1.0 | 2026-07-27 | Initial stub created | AI Team |
