# Cloud Ai Integration

## Document type
This document is an overview, reference, or index as noted below.

# APEX Cloud AI Integration Guide

> **Version:** 3.0.0 | **Last Updated:** July 25, 2026 | **Scope:** Provider Setup, Routing, Cost, Reliability

---

## 1. Overview

APEX uses cloud AI providers with paid API keys only. The application never ships an embedded model runtime and does not depend on local LLM inference, Docker, or WSL in production.

Supported integration classes:

- OpenAI-compatible cloud APIs
- Anthropic native API
- Custom provider templates for future cloud-compatible backends

---

## 2. Provider Categories

| Category | API Style | Typical Examples | Best Use |
|---------|-----------|------------------|----------|
| OpenAI-compatible | `/v1/chat/completions` or equivalent | OpenAI, Groq, Together, OpenRouter, DeepSeek, Mistral, Azure OpenAI-compatible gateways | Broadest compatibility and easiest abstraction |
| Anthropic native | `/v1/messages` | Anthropic Claude | High-quality long-context reasoning and tool planning |

---

## 3. Provider Comparison Matrix

| Provider Type | Auth Header | Streaming | Tool Calling | Strengths | Primary Caveats |
|--------------|-------------|-----------|--------------|-----------|-----------------|
| OpenAI-compatible | `Authorization: Bearer` | Usually SSE | Usually yes | Simple standardisation, broad ecosystem | Provider quirks vary widely |
| Anthropic native | `x-api-key` + `anthropic-version` | Yes | Yes, but schema differs | Strong reasoning, mature message API | Different request/response shape |

---

## 4. Configuration Model

Each configured provider record should contain:

| Field | Required | Purpose |
|------|----------|---------|
| `id` | Yes | Stable internal reference |
| `name` | Yes | Human-readable label |
| `provider_type` | Yes | `openai-compatible`, `anthropic`, or `custom` |
| `base_url` | Yes | Endpoint root URL |
| `api_key` / `key_blob` | Usually | Encrypted credential |
| `model` | Yes | Default model for requests |
| `temperature_default` | No | Per-provider default behaviour |
| `timeout_ms` | No | Request deadline |
| `enabled` | Yes | Routing eligibility |
| `priority` | No | Fallback ordering |

---

## 5. Setup Guides

### 5.1 OpenAI-Compatible Providers

Expected request shape:

```json
{
  "model": "provider-model-name",
  "messages": [
    { "role": "system", "content": "..." },
    { "role": "user", "content": "..." }
  ],
  "temperature": 0.2,
  "max_tokens": 1024
}
```

Recommended flow:

1. Enter provider name.
2. Enter HTTPS base URL.
3. Enter encrypted API key.
4. Select the default model.
5. Run a connection test.
6. Save only if request, auth, and parse checks succeed.

### 5.2 Anthropic Native

Anthropic differs in three key areas:

- system prompt is top-level rather than a normal message item
- auth uses `x-api-key`
- `max_tokens` is required

Representative request:

```json
{
  "model": "claude-model",
  "system": "...",
  "messages": [
    { "role": "user", "content": "..." }
  ],
  "max_tokens": 1024,
  "temperature": 0.2
}
```

### 5.3 Cloud Provider Endpoints

Cloud providers are treated as supported only if they reliably support the required subset:

- message-based chat completion
- deterministic JSON-friendly output when requested
- streaming, if enabled in APEX
- reasonable error codes

All providers should be marked clearly in the UI, including auth method, rate limits, cost class, and fallback role.

---

## 6. Internal Abstraction Layer

### 6.1 Normalised Request

```ts
interface AIRequest {
  providerId: string;
  systemPrompt?: string;
  userPrompt: string;
  messages?: Array<{ role: 'system' | 'user' | 'assistant' | 'tool'; content: string }>;
  model?: string;
  temperature?: number;
  maxTokens?: number;
  responseFormat?: 'text' | 'json';
  tools?: ToolDefinition[];
  stream?: boolean;
  timeoutMs?: number;
}
```

### 6.2 Normalised Response

```ts
interface AIResponse {
  content: string;
  model: string;
  providerId: string;
  tokens: { input: number; output: number; total: number };
  latencyMs: number;
  cached: boolean;
  toolCalls?: ToolInvocation[];
  finishReason?: string;
  costEstimate?: number;
}
```

Adapters translate between this internal contract and provider-specific wire formats.

---

## 7. Model Selection Guidance

| Task | Model Profile | Why |
|------|---------------|-----|
| Opportunity classification | Fast, low-cost reasoning model | High frequency, moderate complexity |
| Risk analysis | More capable reasoning model | Higher downside from bad judgement |
| Structured settings validation | Small deterministic model | Schema-first output, low cost |
| Strategy summarisation | Mid-tier model | Periodic operator-facing text |
| Tool orchestration | Model with reliable tool calling | Correct tool invocation matters more than prose quality |

### 7.1 Tiering Strategy

- **Tier 1 cheap/fast** — repetitive classification, low-risk enrichment.
- **Tier 2 balanced** — most agent workflows.
- **Tier 3 premium** — rare, high-value reasoning or fallback escalation.

---

## 8. Structured Output and Schema Enforcement

### 8.1 OpenAI-Compatible

Prefer explicit JSON-oriented response modes where supported.

### 8.2 Anthropic

Use prompt-constrained JSON output or tool-use where available.

### 8.3 Validation Flow

1. request structured output
2. parse response
3. validate against schema
4. retry once with corrective prompt if invalid
5. fail with typed error if still invalid

Structured output is mandatory for execution-adjacent decisions where free-form text is unsafe.

---

## 9. Tool Calling and Function Dispatch

### 9.1 Purpose

Function calling allows agents to invoke deterministic application tools instead of hallucinating operational state.

### 9.2 Dispatch Rules

- Tool names are resolved from an allowlisted registry.
- Arguments are schema-validated before execution.
- Tool results return to the model only after sanitisation.
- No provider can invoke arbitrary local code paths.

### 9.3 Translation Layer

OpenAI-compatible and Anthropic tool schemas differ, so the provider adapter must:

- map internal tool definitions into provider-specific format
- normalise returned tool invocations
- preserve correlation ids for auditability

---

## 10. Streaming Support

### 10.1 Goals

- faster perceived responsiveness
- live agent trace display
- cancellation support

### 10.2 Requirements

- support server-sent events or chunked transfer where available
- aggregate partial tokens into a stable response buffer
- expose cancellation via `AbortController`
- gracefully downgrade when a provider does not support streaming

---

## 11. Rate Limiting and Throughput Control

### 11.1 Per-Provider Controls

Recommended controls:

- requests per minute
- tokens per minute
- max concurrent requests
- cooldown after repeated failure

### 11.2 Scheduler Policy

- high-priority execution-critical requests preempt lower-priority enrichment requests
- repeated failures trigger provider-specific backoff
- long-running summarisation jobs should not starve latency-sensitive workflows

---

## 12. Cost Optimisation

### 12.1 Primary Methods

- multi-layer cache
- model tiering by task difficulty
- prompt truncation and summarisation
- batching compatible classification workloads
- rule-based shortcuts before AI escalation

### 12.2 Cache Layers

| Layer | Scope | Best For |
|------|-------|----------|
| L1 memory | current session | ultra-low-latency repeated lookups |
| L2 SQLite | local durable cache | repeated requests across restarts |
| L3 semantic cache | approximate reuse | similar prompts with acceptable reuse tolerance |

---

## 13. Fallback Routing

### 13.1 Fallback Strategy

```text
primary cloud provider
  -> retry if transient failure
  -> secondary cloud provider
  -> tertiary cloud provider
  -> rule-based degraded mode
```

### 13.2 When to Fail Over

- timeout
- 429 with sustained overload
- 5xx provider instability
- invalid structured output after retry
- connection/auth incompatibility detected by health checks

### 13.3 When Not to Fail Over

- user misconfiguration requiring intervention
- unsupported feature gap that every fallback would also fail
- security validation failure on endpoint URL or certificate

---

## 14. Error Handling

| Error Class | Typical Action |
|------------|----------------|
| 400-series request error | no blind retry; surface actionable configuration message |
| 401/403 auth error | disable provider until corrected |
| 429 rate limit | exponential backoff or route to fallback |
| 500/502/503 | retry with jitter, then fail over |
| timeout | cancel, record latency breach, try fallback |
| schema parse failure | repair prompt once, then fail typed |

All provider errors should be normalised into internal error codes so the rest of the system does not branch on vendor-specific semantics.

---

## 15. Security and Key Management

- Provider keys are stored only in encrypted form.
- Keys are attached to headers, never URL parameters.
- External providers require HTTPS.
- Prompt payloads must never contain provider keys, wallet keys, or decrypted secret material.
- Connection tests must confirm both reachability and response-shape compatibility.

---

## 16. Local vs Cloud Guidance

| Dimension | Cloud Provider | Self-Hosted Compatible |
|----------|----------------|------------------------|
| Setup friction | Low | Medium to high |
| Ongoing cost | Variable usage billing | Hardware/power/admin overhead |
| Privacy boundary | Data leaves machine | Can stay local |
| Performance consistency | Usually predictable | Depends on host machine |
| Feature completeness | Usually highest | Often partial or uneven |

Use cloud providers for reliability and broad capability. Use self-hosted compatible providers when privacy, experimentation, or marginal request cost matters more than operational simplicity.

---

## 17. Operational Recommendations

- Keep at least one secondary provider configured.
- Test structured JSON output during setup, not only plain text completion.
- Separate cheap classification workloads from premium reasoning workloads.
- Track provider latency and cost in the dashboard.
- Expose a clear “degraded mode” state when AI is unavailable.

---

A strong provider abstraction is essential because APEX depends on AI for orchestration, ranking, and operator-facing intelligence, but it must never depend on any single vendor implementation detail.


## Production policy
- Production AI must use approved cloud providers with paid API keys only.
- Local LLM inference is unsupported in production.
- Experimental local or self-hosted adapters, if ever added, must remain outside the production routing set.

## Cross-references
- `AI-PIPELINE.md`
- `AI-SETTINGS.md`
- `CONFIGURATION.md`
- `SECURITY.md`
- `MONITORING-OBSERVABILITY.md`
- `PERFORMANCE-TARGETS.md`
- `AI-CAPABILITY-MATRIX.md`
- `AI-COST-MANAGEMENT.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.
