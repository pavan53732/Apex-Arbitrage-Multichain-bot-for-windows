# APEX AI Pipeline - Cloud AI Provider Abstraction, Routing, and Advanced Features (v3)

> **Version:** 3.0.0 | **Last Updated:** July 25, 2026
> **Scope:** The full request/response lifecycle, advanced features (streaming, function calling, RAG, memory, semantic cache), and operational concerns.

---

## 1. Overview

The AI Pipeline is the **abstraction layer** between agents/skills and cloud AI
endpoints. It owns: registration, formatting, parsing, failover, rate limiting,
caching, cost tracking, streaming, function-calling, RAG retrieval, and
agent memory. All inference is **cloud-based** (OpenAI-compatible, Anthropic
native, or Self-Hosted OpenAI-compatible). No Docker, no local model hosting.

### 1.1 Goals (v3)
1. **Provider-agnostic** — agents and skills know nothing about the underlying provider
2. **Failover-resilient** — automatic cascade on any recoverable failure
3. **Cost-aware** — pick the cheapest equivalent provider, enforce per-call caps
4. **Latency-optimized** — streaming, parallel fan-out, race patterns
5. **Cache-friendly** — multi-layer cache (memory + SQLite + semantic)
6. **Context-aware** — sliding window, summarization, long-term memory
7. **RAG-capable** — retrieve from local corpora to ground answers
8. **Tool-capable** — first-class function-calling across providers
9. **Observable** — every request traceable end-to-end

---

## 2. Architecture

```
┌────────────────────────────────────────────────────────────────┐
│                  AGENT ORCHESTRATOR / SKILL                     │
└──────────────────────────┬─────────────────────────────────────┘
                           │ Internal AIRequest
                           ▼
┌────────────────────────────────────────────────────────────────┐
│                       AI PIPELINE                               │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────────────┐  │
│  │ Context  │→ │ Memory   │→ │ RAG      │→ │ Prompt Builder │  │
│  │ Window   │  │ Loader   │  │ Retrieve │  │ (template)     │  │
│  └──────────┘  └──────────┘  └──────────┘  └───────┬────────┘  │
│                                                     │           │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌───────▼────────┐  │
│  │ Cache    │← │ Response │← │ Failover │← │ Router         │  │
│  │ Writer   │  │ Parser   │  │ Manager  │  │ (provider pick)│  │
│  └──────────┘  └──────────┘  └──────────┘  └───────┬────────┘  │
│                                                     │           │
└─────────────────────────────────────────────────────┼───────────┘
                                                      │ HTTPS
                              ┌───────────────────────┴──────────┐
                              ▼                                  ▼
                    ┌──────────────────┐               ┌──────────────────┐
                    │ OpenAI-Compatible│               │ Anthropic Native │
                    │ (cloud + local)  │               │                  │
                    └──────────────────┘               └──────────────────┘
```

### 2.1 Components
1. **Provider Registry** — dynamic, loaded from `ai_providers` table at startup
2. **Request Builder** — formats `AIRequest` into provider-specific HTTP body
3. **HTTP Client** — `fetch` with timeouts, abort signals, optional proxy
4. **Response Parser** — normalizes to `AIResponse` regardless of provider
5. **Failover Manager** — retry + cascade + circuit breaker
6. **Rate Limiter** — token bucket per provider (RPM + TPM)
7. **Response Cache** — three layers (memory / SQLite / semantic)
8. **Cost Tracker** — tokens × per-model pricing, per agent/skill
9. **Context Window Manager** — fits long conversations into the model's limit
10. **Memory Store** — long-term facts per agent, namespaced
11. **RAG Retriever** — local embeddings + vector search over corpora
12. **Tool Dispatcher** — executes function-calling tool calls, returns results
13. **Streaming Hub** — multiplexes SSE / chunked responses to subscribers

---

## 3. Internal Type Contracts

### 3.1 `AIRequest`
```ts
interface AIRequest {
  // Identity
  request_id: string;          // uuid v4
  correlation_id: string;      // shared across an orchestrated workflow
  agent_id: string;            // which agent is asking
  skill_id?: string;           // optional skill context

  // Prompt
  system_prompt: string;
  user_prompt: string;
  few_shot_examples?: { role: 'user'|'assistant'; content: string }[];

  // Generation params
  temperature?: number;        // 0-2 (or 0-1 for anthropic)
  top_p?: number;              // 0-1
  max_tokens: number;          // required for anthropic
  stop_sequences?: string[];
  response_format?: 'text' | 'json_object' | 'json_schema';
  json_schema?: object;        // when response_format=json_schema

  // Tool / function calling
  tools?: ToolDefinition[];
  tool_choice?: 'auto' | 'any' | 'none' | { name: string };

  // Context, memory, RAG
  context_strategy?: 'stateless' | 'sliding_window' | 'summary_then_recent' | 'rag_only';
  context_window_tokens?: number;
  memory_namespace?: string;
  rag_namespace?: string;
  rag_top_k?: number;

  // Execution control
  priority?: 1 | 2 | 3 | 4 | 5;
  timeout_ms?: number;
  stream?: boolean;
  deadline?: number;           // epoch ms

  // Provider pinning
  provider_binding?: {
    mode: 'auto' | 'pinned' | 'fallback-chain';
    provider_id?: string;
    fallback_chain?: string[];
  };

  // Cost control
  cost_cap_usd?: number;
}
```

### 3.2 `AIResponse`
```ts
interface AIResponse {
  request_id: string;
  provider_id: string;
  provider_type: 'openai_compatible' | 'anthropic_native' | 'self_hosted';
  model: string;

  content: string;             // text content (or JSON string if response_format=json)
  content_blocks?: ContentBlock[];  // for multimodal, tool_use blocks
  structured?: object;         // parsed when response_format=json_*

  tool_calls?: ToolCall[];     // function-calling results
  finish_reason: 'stop' | 'length' | 'tool_use' | 'content_filter' | 'error';

  usage: {
    input_tokens: number;
    output_tokens: number;
    total_tokens: number;
  };
  cost_estimate_usd: number;
  latency_ms: number;
  cached: boolean;             // true if returned from cache
  cache_layer?: 'memory' | 'sqlite' | 'semantic';

  // Streaming metadata (when stream=true)
  stream?: {
    first_token_ms: number;
    tokens_per_second: number;
  };
}
```

### 3.3 `AIError`
```ts
interface AIError {
  request_id: string;
  provider_id?: string;
  class: 'auth' | 'rate_limit' | 'server' | 'timeout' | 'network'
       | 'invalid_request' | 'invalid_response' | 'tool_error' | 'unknown';
  status?: number;             // HTTP status if any
  message: string;             // sanitized (no keys)
  retriable: boolean;
  cause?: string;
  timestamp: number;
}
```

---

## 4. Provider Interface

### 4.1 Common Fields
- `provider_id`, `provider_type` (`openai_compatible` | `anthropic_native` | `self_hosted`)
- `base_url`, `api_key` (encrypted), `model_name`
- `max_tokens`, `temperature`, `is_enabled`, `priority`
- `rate_limit_rpm`, `rate_limit_tpm`, `timeout_ms`
- `custom_headers[]`, `proxy_url` (optional)

### 4.2 OpenAI-Compatible (Cloud)
- `POST {base_url}/v1/chat/completions`
- `Authorization: Bearer {api_key}`
- Body: `model, messages[{role,content}], temperature, max_tokens, top_p, stop, response_format, tools, tool_choice, stream`
- Response: `choices[0].message.{content, tool_calls}, usage.{prompt,completion,total}_tokens`
- Compatible providers: OpenAI, Azure, Groq, Together, OpenRouter, DeepSeek, Mistral, Perplexity, Fireworks, Anyscale, custom

### 4.3 OpenAI-Compatible (Self-Hosted / Local)
- Same wire format as 4.2
- Base URL is `http://localhost:<port>/v1` typically
- API key optional
- Streaming supported by most servers (LM Studio, Ollama, vLLM, llama.cpp)
- Function-calling support varies by backend; APEX gracefully degrades if absent (passes request, ignores tool_calls if model emits none, retries without tools after 1 cycle)

### 4.4 Anthropic Native
- `POST {base_url}/v1/messages`
- Headers: `x-api-key: {api_key}`, `anthropic-version: {anthropic_version}`, optional `anthropic-beta`
- Body: `model, system (top-level string or array), messages[{role,content}], temperature (0-1), max_tokens (REQUIRED), top_p, top_k, stop_sequences, tools, tool_choice`
- Response: `content[{type:'text'|'tool_use', text|input, id, name}], usage.{input_tokens, output_tokens}, stop_reason`
- Differences from OpenAI:
  - `system` is top-level, not a message
  - `max_tokens` is required
  - Temperature max 1.0
  - Tool use blocks: `type: 'tool_use', id, name, input` (input is the parsed args object)

---

## 5. Request Lifecycle (12 Steps)

1. **Receive `AIRequest`** from Agent Orchestrator / Skill
2. **Context Build**
   - If `context_strategy=sliding_window`: load last N messages from conversation store
   - If `context_strategy=summary_then_recent`: summarize old messages via cheap model, keep recent
   - If `context_strategy=rag_only`: skip conversation, retrieve from RAG
3. **Memory Load** (if `memory_namespace` set): query long-term memory for relevant facts; top-k by recency × relevance
4. **RAG Retrieve** (if `rag_namespace` set): embed query, vector search, return top-k passages, inject into system prompt
5. **Cache Check**: compute SHA-256(provider+model+system+user+temp+format); check L1 (memory) → L2 (SQLite) → L3 (semantic via embedding similarity ≥ 0.95)
6. **Provider Selection** (if `provider_binding.mode='auto'`): filter enabled → drop over quota → drop unsupported models → score by `w1*(1/cost) + w2*(1/latency_p50) + w3*priority` → pick top
7. **Format Request**: convert `AIRequest` to provider-specific body; translate `tools` between OpenAI and Anthropic schemas
8. **Rate Limit Check**: token-bucket deduct (RPM + TPM); if exhausted, queue or fail over
9. **HTTP Call**: `fetch` with `AbortSignal.timeout(timeout_ms)`, optional proxy, custom headers, optional SSE parsing for streaming
10. **Parse Response**: extract `content` + `tool_calls` + `usage`; validate against `output_schema` if `response_format=json_*`; on mismatch, retry once with correction prompt
11. **Cache Write**: L1 always; L2 for TTL > 60s; L3 (semantic) for high-traffic queries
12. **Return `AIResponse`**: enrich with cost, latency, metadata; emit telemetry event

### 5.1 Failover Flow
- On error: if `retriable=true` and retry budget left → retry same provider with backoff
- If still failing or `retriable=false` → next provider in fallback chain
- Max 3 failovers per request; if all fail → return `AIError` with `class='all_providers_failed'`
- Circuit breaker per provider: 5 errors in 60s → open for 120s → half-open test → close or reopen

### 5.2 Streaming Flow
- Caller sets `stream: true`
- HTTP client uses `ReadableStream`, parses SSE / newline-delimited chunks
- Tokens pushed to a `StreamHandle`; subscribers (UI, agent, log) receive via callback
- `stream.first_token_ms` and `tokens_per_second` measured for latency metrics
- "Stop" button triggers `AbortController.abort()`; partial content preserved with `cancelled: true` flag

---

## 6. Rate Limiting

### 6.1 Token Bucket
- Two buckets per provider: **RPM** and **TPM**
- Bucket fills at `rate / 60` per second
- Each request deducts `1` from RPM and `prompt_tokens + max_output_tokens` from TPM
- On exhaustion: queue request up to 5s, then fail over

### 6.2 Defaults
| Provider | RPM | TPM |
|----------|-----|-----|
| OpenAI | 500 | 150,000 |
| Anthropic | 300 | 100,000 |
| Azure OpenAI | user-set | user-set |
| Self-Hosted | 1000 | 1,000,000 |
| Custom | user-set | user-set |

User-overridable in AI Settings.

### 6.3 Backoff
- 429 with `Retry-After` header: honor it exactly
- 429 without header: 1s, 2s, 4s exponential, jitter ±20%

---

## 7. Caching (3 Layers)

### 7.1 L1 — In-Memory
- LRU map, 1000 entries
- TTL: 60s for prices, 300s for analysis, configurable per request
- Key: `SHA-256(provider_type|model|system_prompt|user_prompt|temperature|response_format)`

### 7.2 L2 — SQLite
- Table: `ai_cache(key TEXT PK, value BLOB, expires_at INTEGER, hits INTEGER)`
- TTL: 3600s for analysis, 86400s for static, 30s for streaming (don't cache streamed)
- Periodic vacuum to keep size bounded

### 7.3 L3 — Semantic Cache
- Embeds each prompt with a local embedding model (e.g. `nomic-embed-text` via Ollama, or a fast cloud model)
- Stores in `ai_semantic_cache` (sqlite-vec)
- On lookup: embed query, find neighbors with cosine ≥ 0.95, return most recent
- TTL: 24h
- Disabled by default; user enables in AI Settings → Performance

### 7.4 Cache Invalidation
- "Clear AI Cache" button in AI Settings wipes all three
- Per-provider reset wipes only that provider's cache
- Schema version bump invalidates the L2 prefix

---

## 8. Cost Tracking

### 8.1 Pricing Table (per 1M tokens, USD)
| Model | Input | Output |
|-------|-------|--------|
| gpt-4o | $2.50 | $10.00 |
| gpt-4o-mini | $0.15 | $0.60 |
| o1 | $15.00 | $60.00 |
| o1-mini | $3.00 | $12.00 |
| claude-sonnet-4-20250514 | $3.00 | $15.00 |
| claude-opus-4-20250514 | $15.00 | $75.00 |
| claude-3-5-haiku-20241022 | $0.80 | $4.00 |
| Self-Hosted | $0.00 | $0.00 (configurable electricity cost) |

User can override per-model pricing in AI Settings → Cost; defaults update via app updates.

### 8.2 Rollups
- Per request: stored in `ai_call_log` with provider, model, agent, skill, tokens, cost, timestamp
- Aggregations: by hour, day, week, month, per agent, per skill, per provider
- Surface in Dashboard → Cost tab and AI Settings → Diagnostics

### 8.3 Budgets & Caps
- Per-call cap (`cost_cap_usd_per_call` in agent/skill): if estimated cost > cap, downgrade to cheaper model or fail with `class='cost_cap_exceeded'`
- Per-agent daily quota (`daily_call_quota`): when reached, agent pauses until next UTC day
- Per-agent monthly cost cap (`monthly_cost_cap_usd`): hard stop; user must raise to resume
- Global monthly cap: alert at 80%, hard stop at 100% (configurable)

---

## 9. Context Window Management

### 9.1 Strategies
- **stateless** — no history; each request is independent
- **sliding_window** — last N messages until token budget exhausted
- **summary_then_recent** — older messages summarized via cheap model (e.g. haiku/mini), recent kept verbatim
- **rag_only** — no conversation history; everything is retrieved from memory + RAG

### 9.2 Token Counting
- Use provider's tokenizer when available (tiktoken for OpenAI-compatible, anthropic tokenizer for Claude)
- Fallback: heuristic `~4 chars = 1 token` for unknown models
- Always reserve `max_tokens` for the response when computing the budget

### 9.3 Overflow Handling
- If system + user + reserved > context_window: apply strategy, then truncate oldest first with `[TRUNCATED]` marker
- If still over after truncation: fail with `class='context_overflow'` and suggest reducing context

---

## 10. Tool / Function Calling

### 10.1 Tool Definition
```ts
interface ToolDefinition {
  name: string;                 // kebab-case, ≤ 64 chars
  description: string;          // clear, concise; model reads this
  parameters: {                 // JSON Schema (draft-07)
    type: 'object';
    properties: Record<string, any>;
    required?: string[];
  };
  execution: 'main-process' | 'renderer' | 'service-worker';
  requires_auth?: boolean;
  rate_limit_rpm?: number;
  cached_ttl_s?: number;
}
```

### 10.2 Built-in Tool Library (initial)
- `fetch_token_prices` — current spot prices across DEXs
- `fetch_pool_depth` — pool reserves and max tradeable size
- `fetch_gas_estimates` — current + forecast gas per chain
- `fetch_news` — filtered news for a token list
- `fetch_social_signals` — Twitter/Reddit/Discord sentiment counts
- `fetch_whale_movements` — large transfers in last N hours
- `fetch_contract_source` — verified source from explorer
- `fetch_recent_exploits_for_address` — exploit history
- `query_skill_registry` — read available skills
- `query_trade_history` — last N trades, filtered
- `toggle_skill` — enable/disable a skill (gated, prompts user first)
- `query_bridge_quotes` — get bridge quotes
- `simulate_route` — dry-run a swap path
- `estimate_gas` — precise gas for a tx
- `check_flashbots_availability` — for MEV protection

Custom tools can be registered by skills (user-gated in v3.1).

### 10.3 Cross-Provider Translation
- **OpenAI format:** `{type: 'function', function: {name, description, parameters}}`, choice is `tool_choice: 'auto'|'any'|{type:'function', function:{name}}`, response `tool_calls[{id, type:'function', function:{name, arguments}}]`
- **Anthropic format:** `{name, description, input_schema}`, choice is `tool_choice: 'auto'|'any'|{type:'tool', name}`, response `content[{type:'tool_use', id, name, input}]`
- The pipeline translates both directions; agents write provider-agnostic tool calls

### 10.4 Loop
- Agent returns `tool_calls[]`
- Pipeline dispatches each (parallel when independent, serial when dependent)
- Results fed back as `role: 'tool'` (OpenAI) or `role: 'user'` with `tool_result` blocks (Anthropic)
- Loop until model returns no `tool_calls` or `max_tool_iterations` reached (default 8)

### 10.5 Errors
- Tool timeout: return `{ok: false, error: 'timeout'}` to model; model can retry or proceed
- Tool permission denied: model receives error, user prompted in UI
- Tool not found: model gets error, can adjust

---

## 11. RAG (Retrieval-Augmented Generation)

### 11.1 Overview
- Local-first vector store over user's domain (trade history, market analyses, on-chain events, docs)
- Embeddings generated by a local or cloud embedding model (user-chosen in AI Settings)
- Retriever injects top-k passages into the system prompt under a `## Retrieved Context` header

### 11.2 Configuration (AI Settings → RAG)
- **Embedding Provider:** OpenAI (`text-embedding-3-small`), Cohere, Self-Hosted (Ollama `nomic-embed-text`)
- **Embedding Model:** selectable per provider
- **Chunk Size:** 500 / 1000 / 2000 tokens (default 1000)
- **Chunk Overlap:** 10% / 20% / 30% (default 20%)
- **Top K:** 1-20, default 5
- **Min Similarity:** 0.0-1.0, default 0.7
- **Namespaces:** separate corpora; agents declare which to use

### 11.3 Built-in Corpora
- `trade_history` — every trade, summary + outcome
- `market_analyses` — past Market Analyst outputs
- `onchain_events` — curated events (exploits, governance, listings)
- `user_notes` — anything the user adds (manual import or in-app note)

### 11.4 Storage
- `rag_documents` table: `(id, namespace, source, content, metadata_json, created_at)`
- `rag_embeddings` virtual table via `sqlite-vec` (or in-memory HNSW if user prefers)
- Periodic re-embed job when embedding model changes

---

## 12. Agent Memory

### 12.1 Two Tiers
- **Short-term (conversation):** last N turns per agent session, TTL configurable
- **Long-term (facts):** extracted or explicitly written, scoped by `memory_namespace`, with TTL

### 12.2 Write Triggers
- Explicit: agent calls a `remember_fact` tool
- Implicit: at conversation end, a cheap model extracts top-K facts and writes them
- Manual: user adds a note in AI Settings → Memory tab

### 12.3 Read
- On each agent call, the top-K most relevant facts (by embedding similarity to current query) are appended to system prompt under `## Remembered Facts`

### 12.4 Schema
```sql
CREATE TABLE agent_memory (
  id INTEGER PRIMARY KEY,
  agent_id TEXT NOT NULL,
  namespace TEXT NOT NULL,
  fact TEXT NOT NULL,
  embedding BLOB,
  created_at TEXT NOT NULL,
  expires_at TEXT,                -- nullable for permanent
  source TEXT                     -- 'agent'|'user'|'extracted'
);
CREATE INDEX idx_memory_lookup ON agent_memory(agent_id, namespace, expires_at);
```

### 12.5 Privacy
- Memory is local-only (no cloud sync)
- "Forget" button per fact, "Clear Memory" per namespace, "Wipe All" global
- Never includes API keys, private keys, or wallet addresses

---

## 13. Streaming

### 13.1 When to Stream
- User-initiated chat (User Assistant agent)
- Long agent outputs (e.g. Opportunity Scanner returning many opportunities)
- Skill "Explain" actions

### 13.2 When NOT to Stream
- Tight programmatic loops (slower than batch due to overhead)
- Cached responses
- Background skills (batched, then summarized)

### 13.3 Implementation
- `ReadableStream` over `fetch`
- Parse SSE / Anthropic event-stream
- Emit `onToken` callback; UI renders incrementally
- Cancellation: `AbortController` propagated through pipeline
- Metrics: `first_token_ms`, `tokens_per_second`, total chunks

### 13.4 UI Integration
- See `DESIGNER-PROTOCOLS.md` §5.13 — `StreamingText` component
- "Stop" button in card header
- Footer on completion: latency, tokens, cost

---

## 14. Multi-Model Consensus (optional, advanced)

For high-stakes decisions (e.g. cross-chain arbitrage execution), the user can
enable **consensus mode**: the same prompt is sent to N providers (configurable,
default 2), and the pipeline returns a synthesized answer.

Modes:
- **vote** — pick the most common answer (for categorical outputs)
- **average** — average numeric scores
- **adjudicate** — a third, more expensive model reviews all answers and picks

Default: off. Enable in AI Settings → Advanced.

---

## 15. Observability

### 15.1 Trace Per Request
- `request_id`, `correlation_id`, agent, skill, provider, model
- All hops logged: cache check, rate limit check, HTTP call, parser, retries, failover
- Stored in `ai_request_traces` table, retention 30 days, sampled for longer

### 15.2 Metrics
- Per provider: p50/p95/p99 latency, success rate, error rate by class
- Per agent: call count, success rate, avg latency, total cost
- Global: requests/sec, cost/min, cache hit rate

### 15.3 Surfaced In
- AI Settings → Diagnostics (real-time for the current user)
- Dashboard → Cost tab (rolled up)
- Logs page (advanced, JSON export)

---

## 16. Security (cross-ref `SECURITY.md`)

- API keys decrypted only in main process, only at call time, zeroed with `Buffer.fill(0)` after
- Custom headers are sandboxed: cannot override `Authorization` (for cloud) or `x-api-key` (for Anthropic)
- HTTPS required for non-loopback; HTTP only for loopback (localhost, 127.0.0.1, ::1)
- Certificate validation enforced; user can opt into custom CA bundle
- Request/response bodies are NOT persisted (only metadata); cache stores content separately
- Logs never include keys, full prompts (configurable), or PII

---

## 17. Failure Modes & Degradation

| Condition | Behavior |
|-----------|----------|
| All providers down | Alert user, enter "rule-based mode" (heuristics only), retry every 30s, auto-resume when providers return |
| Provider slow (> 5s) | Stream starts after first token; UI shows "thinking..." with elapsed |
| Rate limited everywhere | Queue with backoff, surface "AI is rate-limited" banner |
| Cost cap hit | Pause agent/skill; user can raise cap or downgrade model |
| Context overflow | Apply summarization, then truncate; if still over, fail with reason |
| Tool not supported by provider | Pipeline strips tools, retries once; if model emits tool_call anyway, drop with warning |
| Self-hosted server offline | Failover to cloud; surface "Local provider offline" status |

---

## 18. Extending the Pipeline

To add a new provider type:
1. Add type to `provider_type` enum in `ai_providers` table constraint
2. Implement `BaseProvider` interface: `formatRequest()`, `parseResponse()`, `parseError()`, `streamResponse()`
3. Register in `ProviderFactory`
4. Add UI template in AI Settings
5. Add to failover chain
6. Update `AI-PIPELINE.md` and `AI-SETTINGS.md`

---

*This is the nervous system of APEX's intelligence. Every call goes through here, and every call is observable, accountable, and overridable.*
