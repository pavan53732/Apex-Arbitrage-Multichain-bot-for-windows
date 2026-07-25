# APEX AI Agents - Definitions, Roles, Field Schema, and Communication Protocols

> **Version:** 3.0.0 | **Last Updated:** July 25, 2026
> **Scope:** Complete field reference for every agent, plus how agents talk to each other.

---

## 1. Agent System Overview

APEX uses a modular AI agent architecture. Each agent is a specialized unit
that handles a specific aspect of the arbitrage workflow. Agents are
prompt-engineered personas executing via cloud AI API calls (OpenAI-compatible
or Anthropic native — see `AI-SETTINGS.md` and `AI-PIPELINE.md`).

### 1.1 Agent Lifecycle (extended)

1. **Registration** — Metadata persisted in SQLite `agents` table, schema-validated
2. **Activation** — Trigger condition met (skill requests, schedule fires, event)
3. **Context Load** — Conversation history + memory slice loaded into request
4. **Execution** — Structured prompt built, sent via AI Pipeline Router
5. **Response** — Parsed against `output_schema`; on mismatch, retry once with correction
6. **Memory Write** — Important facts appended to long-term memory (if `memory_enabled`)
7. **Deactivation** — Context released; conversation retained per `context_ttl`
8. **Logging** — Interaction logged (no API keys, no full PII) to `agent_logs` table

### 1.2 Agent vs Skill vs Strategy

| Concept | What it is | Composed of |
|---------|-----------|-------------|
| **Agent** | Single AI persona with one focused job | One cloud AI call |
| **Skill** | User-facing capability (toggleable) | One or more agents + data transforms |
| **Strategy** | On-chain profit logic | Skills + contracts + execution |

---

## 2. Agent Registry - Complete Field Schema

This is the authoritative field reference. Every agent in APEX conforms to this schema.

```jsonc
{
  "agent_id":          "string, kebab-case, unique. e.g. 'market-analyst'",
  "name":              "string, human-readable display name",
  "role":              "string, one-line description of the agent's job",
  "version":           "semver string, e.g. '1.0.0'",
  "category":          "enum: 'analysis' | 'risk' | 'execution' | 'learning' | 'meta'",
  "enabled":           "boolean, default true",
  "system_prompt":     "string, the agent's persona + instructions (see §5)",
  "input_schema":      "JSON Schema (draft-07) describing accepted inputs",
  "output_schema":     "JSON Schema (draft-07) describing returned outputs",
  "examples":          "array of {input, output} few-shot examples (max 5)",

  // Provider / Model binding
  "provider_binding": {
    "mode":            "enum: 'auto' | 'pinned' | 'fallback-chain'",
    "provider_id":     "string|null, FK to ai_providers.id when pinned",
    "fallback_chain":  "array of provider_id strings, ordered, when mode=fallback-chain"
  },
  "model_preference":  "string|null, e.g. 'gpt-4o', 'claude-sonnet-4-20250514', or null",

  // Generation parameters
  "temperature":       "number 0.0-2.0, default 0.2",
  "top_p":             "number 0.0-1.0, default 1.0",
  "max_tokens":        "integer 1-128000, default 4096",
  "stop_sequences":    "array of strings, optional",
  "response_format":   "enum: 'text' | 'json_object' | 'json_schema'",
  "json_schema":       "object|null, JSON Schema when response_format=json_schema",

  // Tool / function calling
  "tools":             "array of tool definitions (see §6)",
  "tool_choice":       "enum: 'auto' | 'any' | 'none' | {name: string}",

  // Context & memory
  "context_strategy":  "enum: 'stateless' | 'sliding_window' | 'summary_then_recent' | 'rag_only'",
  "context_window_tokens": "integer, target token budget for the request",
  "memory_enabled":    "boolean, persist conversation across activations",
  "memory_namespace":  "string|null, e.g. 'market:eth-usdc' for scoped memory",
  "memory_ttl_days":   "integer 0-365, 0 = forever",
  "rag_enabled":       "boolean, augment with retrieved documents",
  "rag_top_k":         "integer 1-20, default 5",
  "rag_namespace":     "string|null, RAG corpus scope",

  // Behavior
  "priority":          "integer 1-5 (1 = highest)",
  "timeout_ms":        "integer 1000-120000, default 30000",
  "retry_policy": {
    "max_retries":     "integer 0-5, default 2",
    "backoff_ms":      "array of integers, default [1000, 2000, 4000]",
    "retry_on":        "array of error classes, default ['timeout','5xx','429']"
  },

  // Cost & quotas
  "cost_cap_usd_per_call": "number|null, soft cap, alert when exceeded",
  "daily_call_quota":  "integer|null, max invocations per 24h",
  "monthly_cost_cap_usd": "number|null, hard stop when reached",

  // Streaming
  "streaming":         "boolean, enable token-by-token streaming",

  // Observability
  "log_inputs":        "boolean, log input (default false for privacy)",
  "log_outputs":       "boolean, log output (default true)",
  "tags":              "array of strings, for filtering/grouping",

  // Lifecycle metadata
  "author":            "string, who created this agent",
  "created_at":        "ISO 8601 timestamp",
  "updated_at":        "ISO 8601 timestamp",
  "deprecated":        "boolean, default false",
  "deprecation_message": "string|null"
}
```

---

## 3. Core Agents - Extended Definitions

Each entry below is a concrete instance of the schema in §2. All defaults shown
can be overridden by the user in **AI Settings → Agent Overrides**.

### 3.1 Market Analyst — `market-analyst`
- **Category:** analysis
- **Role:** Analyzes real-time market data across DEXs and chains
- **Inputs:** `{tokens: string[], chains: number[], window_minutes: number}`
- **Outputs:** `{market_score: 0-100, trend: 'bullish'|'bearish'|'sideways', volatility: 'low'|'med'|'high', liquidity: 'shallow'|'normal'|'deep', notes: string}`
- **Tools:** `fetch_token_prices`, `fetch_pool_depth`
- **Temperature:** 0.2
- **Memory:** scoped to `market:{chain_id}:{token_pair}`, TTL 1 day
- **RAG:** enabled, corpus = recent market analyses, top_k 3

### 3.2 Opportunity Scanner — `opportunity-scanner`
- **Category:** analysis
- **Role:** Identifies and ranks arbitrage opportunities
- **Inputs:** `{price_feeds: PriceFeed[], gas_estimates: GasMap, bridge_fees: BridgeFeeMap, slippage_estimates: SlippageMap}`
- **Outputs:** `{opportunities: Opportunity[]}` where `Opportunity = {id, path, expected_profit_usd, risk_score, gas_cost_usd, net_profit_usd, confidence: 0-1}`
- **Tools:** `fetch_price_feeds`, `simulate_route`
- **Temperature:** 0.1
- **Streaming:** true (so UI can show top opportunities as they emerge)

### 3.3 Risk Assessor — `risk-assessor`
- **Category:** risk
- **Role:** Evaluates risk for each opportunity or open position
- **Inputs:** `{target: Opportunity|Position, portfolio: Portfolio, historical_loss_data: LossRecord[]}`
- **Outputs:** `{risk_score: 0-100, recommended_size_usd, stop_loss_pct, take_profit_pct, hard_reject: boolean, reasons: string[]}`
- **Tools:** `lookup_protocol_tvl`, `lookup_recent_exploits`
- **Temperature:** 0.1
- **Hard reject on:** liquidity < threshold, recent exploit, oracle divergence > 2%

### 3.4 Execution Planner — `execution-planner`
- **Category:** execution
- **Role:** Plans optimal execution strategy for an approved opportunity
- **Inputs:** `{opportunity: Opportunity, gas: GasInfo, mev_risk: MEVRisk}`
- **Outputs:** `{steps: ExecutionStep[], tx_ordering: string[], gas_strategy: 'slow'|'standard'|'fast'|'private', timing: {wait_blocks: number}}`
- **Tools:** `estimate_gas`, `check_flashbots_availability`
- **Temperature:** 0.2
- **Cost cap:** $0.05 per call (cheap deterministic task)

### 3.5 Sentiment Analyst — `sentiment-analyst`
- **Category:** analysis
- **Role:** Analyzes market sentiment from news, social, on-chain signals
- **Inputs:** `{tokens: string[], lookback_hours: number, sources: string[]}`
- **Outputs:** `{sentiment_score: -100..+100, key_events: Event[], confidence: 0-1}`
- **Tools:** `fetch_news`, `fetch_social_signals`, `fetch_whale_movements`
- **Temperature:** 0.4
- **RAG:** enabled, corpus = past sentiment calls for calibration

### 3.6 Portfolio Optimizer — `portfolio-optimizer`
- **Category:** meta
- **Role:** Optimizes capital allocation across chains and strategies
- **Inputs:** `{portfolio: Portfolio, performance_history: TradeResult[], risk_tolerance: 'conservative'|'balanced'|'aggressive', capital_usd: number}`
- **Outputs:** `{allocations: {chain_id: pct, strategy: pct}, rebalance_actions: Action[]}`
- **Temperature:** 0.3

### 3.7 Anomaly Detector — `anomaly-detector`
- **Category:** risk
- **Role:** Detects unusual conditions, exploits, system errors
- **Inputs:** `{price_feeds: PriceFeed[], tx_patterns: TxPattern[], contract_events: Event[], health_metrics: HealthSnapshot}`
- **Outputs:** `{anomaly: boolean, severity: 'low'|'med'|'high'|'critical', description: string, action: 'none'|'alert'|'pause'|'shutdown'}`
- **Temperature:** 0.1
- **Action mapping:** critical → 'shutdown', high → 'pause', med → 'alert'

### 3.8 Learning Agent — `learning-agent`
- **Category:** learning
- **Role:** Reviews past trades, extracts lessons, suggests parameter adjustments
- **Inputs:** `{trade_history: TradeResult[], pnl_series: number[], market_conditions_at_trade: MarketSnapshot[]}`
- **Outputs:** `{insights: Insight[], strategy_adjustments: Adjustment[], calibration_notes: string}`
- **Temperature:** 0.5
- **Schedule:** Runs daily at 00:05 UTC and after every 100 trades

### 3.9 Contract Auditor — `contract-auditor` *(new in v3)*
- **Category:** risk
- **Role:** Reviews a smart contract's surface before APEX interacts with it
- **Inputs:** `{chain_id: number, address: string, abi: ABIFragment, bytecode_hash: string}`
- **Outputs:** `{risk_grade: 'A'|'B'|'C'|'D'|'F', findings: Finding[], approval_recommendation: 'approve'|'review'|'reject'}`
- **Tools:** `fetch_contract_source`, `fetch_recent_exploits_for_address`
- **Temperature:** 0.0 (fully deterministic)
- **Runs before:** any new DEX or pool is added to registry

### 3.10 Gas Forecaster — `gas-forecaster` *(new in v3)*
- **Category:** meta
- **Role:** Predicts near-future gas prices to time execution
- **Inputs:** `{chain_id: number, history: GasPoint[], horizon_minutes: number}`
- **Outputs:** `{forecast: GasPoint[], recommended_gwei: number, confidence: 0-1}`
- **Temperature:** 0.0
- **Schedule:** every 12 seconds per chain

### 3.11 Bridge Advisor — `bridge-advisor` *(new in v3)*
- **Category:** execution
- **Role:** Chooses the best bridge route for a cross-chain transfer
- **Inputs:** `{from_chain: number, to_chain: number, token: string, amount_usd: number}`
- **Outputs:** `{bridge: string, route: BridgeStep[], est_time_minutes: number, est_cost_usd: number, risk_score: 0-100}`
- **Temperature:** 0.1
- **Tools:** `query_bridge_quotes`

### 3.12 User Assistant — `user-assistant` *(new in v3)*
- **Category:** meta
- **Role:** In-app conversational helper. Answers questions, configures skills, explains trades
- **Inputs:** `{user_message: string, context: {page: string, recent_trades: TradeResult[]}}`
- **Outputs:** `{reply: string, action_request: ActionRequest|null}`
- **Temperature:** 0.7
- **Streaming:** true
- **Tools:** `query_skill_registry`, `query_trade_history`, `toggle_skill`

---

## 4. Communication Protocol

### 4.1 Message Envelope
```jsonc
{
  "envelope_version":  "1.0",
  "message_id":        "uuid v4",
  "correlation_id":    "uuid v4, shared across an orchestrated workflow",
  "timestamp":         "ISO 8601 with millis",
  "source_agent":      "string, agent_id or 'orchestrator' | 'user' | 'skill'",
  "target_agent":      "string, agent_id or 'broadcast'",
  "message_type":      "enum: 'request' | 'response' | 'event' | 'error' | 'cancel'",
  "priority":          "integer 1-5 (1 = highest)",
  "payload":           "object matching target agent's input_schema",
  "context_refs":      "array of memory/rag references attached",
  "deadline_ms":       "integer, hard deadline from now"
}
```

### 4.2 Orchestration Patterns
- **Sequential:** A → B → C → D (e.g. Market Analyst → Opportunity Scanner → Risk Assessor → Execution Planner)
- **Parallel Fan-Out:** Orchestrator → [A, B, C] → Orchestrator (waits for all)
- **Parallel Race:** Orchestrator → [A, B, C] → first response wins, cancel rest
- **Conditional:** Risk Assessor → if score < 30: Execute; else: reduce size
- **Feedback Loop:** Learning Agent → Strategy Engine → next cycle
- **Escalation:** Skill fails twice → User Assistant asks user for guidance
- **Watchdog:** Anomaly Detector observes every execution, can fire `pause` action

### 4.3 Error Handling
- **Timeout (30s default):** retry once, then escalate to User Assistant
- **Malformed response:** validate against `output_schema`, retry once with correction prompt
- **Provider failure:** AI Pipeline handles failover (see `AI-PIPELINE.md`)
- **Tool call failure:** retry with backoff, then return partial result with `tool_errors[]`
- **Circuit breaker:** 3 consecutive agent-level failures → agent disabled for 5 min, alert user

---

## 5. System Prompt Engineering Standards

Every `system_prompt` should follow this template:

```
# ROLE
You are {name}, a {role} for APEX, an autonomous DeFi execution platform.

# CONTEXT
You operate on chain(s): {chains}. Current block: ~{block}.
Trading capital: ${capital_usd}. Risk tolerance: {tolerance}.

# TASK
{precise description of what the agent must do}

# INPUTS
You will receive a JSON object with the following fields:
{input_schema human-readable summary}

# OUTPUT FORMAT
Return a JSON object matching this schema exactly:
{output_schema human-readable summary}
Do not include any text outside the JSON. Do not wrap in markdown.

# CONSTRAINTS
- Never invent on-chain data; if missing, set field to null and explain in 'notes'
- Never recommend an action that violates the user's risk_tolerance
- Never log or echo API keys, private keys, or full wallet addresses
- Always include a 'confidence' field when the schema requires it

# EXAMPLES
Example 1:
Input: {...}
Output: {...}

Example 2:
Input: {...}
Output: {...}
```

Token budget guideline: system < 1500 tokens, user < 4000, response 1000-4096.

---

## 6. Tool / Function Calling

Each tool defined in the agent's `tools[]` follows:

```jsonc
{
  "name":         "fetch_token_prices",
  "description":  "Fetches current prices for given tokens across supported DEXs",
  "parameters": {
    "type": "object",
    "properties": {
      "tokens":     {"type": "array", "items": {"type": "string"}},
      "chain_ids":  {"type": "array", "items": {"type": "integer"}}
    },
    "required": ["tokens", "chain_ids"]
  },
  "execution":    "main-process",  // or 'renderer' | 'service-worker'
  "requires_auth": false,
  "rate_limit_rpm": 60,
  "cached_ttl_s":  10
}
```

Built-in tool library: see `AI-PIPELINE.md` §10 for the full registry. Custom
tools can be registered by skills, gated by user permission.

---

## 7. User Configuration Surface

In **AI Settings → Agents** tab, the user can:

- See all agents with category, status (active/idle/error), last called, calls today
- Toggle `enabled` per agent
- Override `provider_binding`, `model_preference`, `temperature`, `max_tokens`
- Set `daily_call_quota` and `monthly_cost_cap_usd`
- View last 20 interactions per agent (input summary + output + tokens + latency)
- Reset single agent to defaults, or "Reset All Agents"
- Import/Export agent configs as JSON (no API keys embedded — those stay local)

---

## 8. Adding a New Agent — Checklist

1. Pick a unique kebab-case `agent_id`
2. Write the system prompt following §5 template
3. Author JSON Schemas for `input_schema` and `output_schema` (validate with a tool)
4. Add up to 5 few-shot examples
5. List required tools; ensure they're in the tool library
6. Decide memory / RAG strategy
7. Set conservative defaults (`temperature ≤ 0.3`, `max_tokens` sized for output)
8. Register in code: `AgentRegistry.register(agentDef)`
9. Add to Agent Orchestrator workflows if used by skills
10. Add UI toggle in AI Settings → Agents
11. Update this file (AGENTS.md) with the new agent's full definition
12. Write at least 3 unit tests covering happy path, schema mismatch, tool failure
13. Document the agent in the user guide if user-facing

---

## 9. Agent Selection / Auto-Routing

When `provider_binding.mode = 'auto'`, the AI Pipeline picks a provider using:

1. Filter to `enabled` providers
2. Drop providers over rate limit or daily quota
3. Drop providers that don't support the model needed
4. Score remaining: `score = w1 * (1/cost) + w2 * (1/latency_p50) + w3 * priority`
5. Pick highest score; on failure, cascade to next

Weights (`w1`, `w2`, `w3`) are user-configurable in AI Settings.

---

## 10. Agent Observability

Per agent, APEX tracks:
- Total invocations, success rate, p50/p95/p99 latency
- Token usage (input, output) and cost (rolling 1h, 24h, 7d, 30d)
- Top error classes and recent error samples (sanitized)
- Drift indicator: distribution shift between recent outputs and training-time outputs

Surfaces in **Dashboard → Agents** view, with exportable CSV.

---

*Every agent is focused, schema-bounded, observable, and overridable. No black boxes.*
