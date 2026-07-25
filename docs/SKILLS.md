# APEX Bot Skills - Registry, Capabilities, and Lifecycle (v3)

> **Version:** 3.0.0 | **Last Updated:** July 25, 2026
> **Scope:** Every skill shipped with APEX, full schema, lifecycle, and user management.

---

## 1. Overview

A **Skill** is a discrete, composable capability the user can toggle on or off.
Skills orchestrate one or more AI agent calls, data transforms, and (sometimes)
on-chain actions. They are registered with rich metadata, versioned, and
exposed in the UI with status, metrics, and configuration.

**Mental model:**
- **Agent** = single AI persona → one cloud AI call
- **Skill** = user-facing capability → one or more agents + data + actions
- **Strategy** = on-chain profit logic → skills + contracts + execution

A skill is **what the user sees and toggles**. An agent is the AI brain inside it.

---

## 2. Skill Metadata Schema

```ts
interface SkillDefinition {
  // Identity
  skill_id:          string;            // kebab-case, unique
  name:              string;            // human-readable
  version:           string;            // semver
  description:       string;            // one-line, shown in UI
  long_description?: string;            // markdown, shown in detail view
  category:          SkillCategory;
  tags?:             string[];
  icon?:             string;            // lucide icon name
  author:            string;
  homepage_url?:     string;

  // Composition
  required_agents:   string[];          // agent_id[]
  optional_agents?:  string[];
  required_tools?:   string[];          // tool names
  inputs_schema:     JSONSchema;        // what the skill accepts as input
  outputs_schema:    JSONSchema;        // what the skill returns

  // Targeting
  chains?:           number[];          // chain ids where this skill operates; empty = chain-agnostic
  protocols?:        string[];          // e.g. ['uniswap-v3', 'aave-v3']
  risk_level:        'low' | 'medium' | 'high' | 'critical';

  // Runtime behavior
  enabled:           boolean;
  priority:          1 | 2 | 3 | 4 | 5; // higher = scheduled earlier
  schedule?:         ScheduleSpec;      // optional cron/interval
  triggers?:         TriggerSpec[];     // optional event triggers
  cooldown_ms:       number;            // min time between invocations
  max_concurrent:    number;            // parallelism cap (1 = serial)
  timeout_ms:        number;            // hard deadline per invocation

  // Cost & limits
  cost_cap_usd_per_call?: number;
  daily_call_quota?:      number;
  monthly_cost_cap_usd?:  number;

  // UI
  configurable_params: ConfigParam[];   // user-tunable parameters
  docs_url?:           string;           // link to skill-specific docs section
  changelog_url?:      string;
  deprecated?:         boolean;
  deprecation_message?: string;
  experimental?:       boolean;          // shows "beta" badge in UI
}

type SkillCategory =
  | 'arbitrage'
  | 'analysis'
  | 'risk'
  | 'execution'
  | 'learning'
  | 'monitoring'
  | 'portfolio'
  | 'bridge'
  | 'yield'
  | 'meta';        // user-assistant, configuration helpers

interface ConfigParam {
  key:         string;          // kebab-case
  label:       string;
  type:        'number' | 'string' | 'boolean' | 'select' | 'multiselect' | 'json';
  default:     any;
  min?: number; max?: number;
  options?: { value: any; label: string }[];
  description: string;
  advanced?: boolean;           // hidden by default in UI
}
```

---

## 3. Skill Categories (visual grouping in UI)

| Category | Icon | Color |
|----------|------|-------|
| Arbitrage | `zap` | accent |
| Analysis | `bar-chart-3` | info |
| Risk | `shield-alert` | warning |
| Execution | `send` | success |
| Learning | `graduation-cap` | secondary |
| Monitoring | `activity` | info |
| Portfolio | `wallet` | accent |
| Bridge | `arrow-left-right` | secondary |
| Yield | `coins` | success |
| Meta | `bot` | secondary |

---

## 4. Core Skills (v3 Registry)

Each entry: `id — name (risk level) — Category`. Risk level drives the UI badge and confirmation requirements.

### 4.1 Arbitrage
- **`intra-chain-arb`** — Intra-Chain Arbitrage (high) — Scans DEXs on a single chain for price discrepancies. Agents: market-analyst, opportunity-scanner. Cooldown 1000ms.
- **`cross-chain-arb`** — Cross-Chain Arbitrage (critical) — Cross-chain via bridges. Agents: market-analyst, opportunity-scanner, risk-assessor, bridge-advisor. Cooldown 5000ms.
- **`triangular-arb`** — Triangular Arbitrage (high) — A→B→C→A paths. Agents: opportunity-scanner. Cooldown 500ms.
- **`flash-loan-arb`** — Flash Loan Arbitrage (critical) — Zero-capital flash loan trades. Agents: opportunity-scanner, execution-planner, risk-assessor, contract-auditor. Cooldown 2000ms.
- **`stable-arb`** — Stablecoin Arbitrage (medium) — Stable/peg arbitrage and depeg detection. Agents: market-analyst, opportunity-scanner. Cooldown 2000ms.
- **`multi-hop-arb`** — Multi-Hop Arbitrage (high) — N-hop routing. Agents: opportunity-scanner, execution-planner. Cooldown 750ms.
- **`liquidity-imbalance`** — Liquidity Imbalance Detection (medium) — Detects pools out of balance. Agents: market-analyst. Cooldown 60s.
- **`oracle-divergence`** — Oracle Divergence Monitor (medium) — Flags price divergence between on-chain oracles and CEX/DEX. Agents: risk-assessor, anomaly-detector. Cooldown 30s.

### 4.2 Analysis
- **`market-sentiment`** — Market Sentiment (low) — News/social/on-chain sentiment scoring. Agents: sentiment-analyst, market-analyst. RAG enabled. Cooldown 5m.
- **`liquidity-depth`** — Liquidity Depth Analyzer (low) — Pool depth and max tradeable size. Agents: market-analyst. Cooldown 30s.
- **`gas-optimization`** — Gas Optimization Advisor (low) — Gas timing and pricing. Agents: market-analyst, gas-forecaster. Cooldown 12s.
- **`whale-watcher`** — Whale Activity Watcher (low) — Large transfer detection. Agents: sentiment-analyst. Cooldown 30s.
- **`token-fundamentals`** — Token Fundamentals Scorer (low) — LLM-scored token quality. Agents: sentiment-analyst, market-analyst. RAG enabled. Cooldown 1h.
- **`narrative-tracker`** — Narrative & Trend Tracker (low) — Emerging narrative detection. Agents: sentiment-analyst. RAG enabled. Cooldown 15m.
- **`correlation-mapper`** — Cross-Token Correlation Mapper (low) — Rolling correlation matrix. Agents: market-analyst. Cooldown 5m.
- **`volatility-forecaster`** — Volatility Forecaster (low) — Predicted vol surface. Agents: market-analyst, gas-forecaster. Cooldown 1m.

### 4.3 Risk
- **`pre-trade-risk`** — Pre-Trade Risk Check (low) — Pre-trade evaluation. Agents: risk-assessor, anomaly-detector. Runs before every execution skill.
- **`portfolio-risk-monitor`** — Portfolio Risk Monitor (medium) — Continuous portfolio monitoring. Agents: risk-assessor, portfolio-optimizer. Schedule: every 60s.
- **`anomaly-circuit-breaker`** — Anomaly + Circuit Breaker (critical) — Detects anomalies, halts trading. Agents: anomaly-detector. Schedule: every 5s, runs always.
- **`rug-pull-detector`** — Rug-Pull Detector (medium) — Token launch safety. Agents: contract-auditor, sentiment-analyst. RAG enabled. Trigger: on new token in watchlist.
- **`protocol-health`** — Protocol Health Monitor (low) — TVL, volume, audit status. Agents: contract-auditor. Schedule: hourly.
- **`mev-risk-scorer`** — MEV Risk Scorer (medium) — Per-tx MEV exposure. Agents: risk-assessor, anomaly-detector. Runs pre-execution.
- **`correlation-risk`** — Correlation Risk (medium) — Detects over-correlation in portfolio. Agents: portfolio-optimizer, risk-assessor. Schedule: every 5m.

### 4.4 Execution
- **`smart-order-routing`** — Smart Order Routing (high) — Optimal DEX routing. Agents: execution-planner. Runs on demand.
- **`mev-protection`** — MEV Protection (high) — Flashbots/private mempool. Agents: execution-planner, anomaly-detector. Runs on demand.
- **`bridge-execution`** — Bridge Execution (critical) — Cross-chain bridge transfers. Agents: execution-planner, risk-assessor, bridge-advisor. Cooldown 30s.
- **`flash-loan-execution`** — Flash Loan Execution (critical) — Flash loan orchestration. Agents: execution-planner, contract-auditor. Cooldown 5s.
- **`limit-order-manager`** — Limit Order Manager (medium) — Off-chain limit orders, on-chain settlement. Agents: execution-planner, market-analyst. Schedule: every 10s.
- **`dca-executor`** — DCA Executor (medium) — Dollar-cost averaging over time. Agents: execution-planner. Schedule: cron-configurable.
- **`sl-tp-manager`** — Stop-Loss / Take-Profit Manager (medium) — Per-position SL/TP. Agents: execution-planner, market-analyst. Schedule: every 5s for open positions.
- **`gas-bidder`** — Gas Bidder (low) — Dynamic gas pricing strategy. Agents: gas-forecaster, execution-planner. Schedule: every block.

### 4.5 Learning
- **`trade-review`** — Trade Review (low) — Performance insights. Agents: learning-agent. Schedule: daily at 00:05 UTC.
- **`strategy-calibration`** — Strategy Calibration (medium) — Parameter adjustment. Agents: learning-agent, portfolio-optimizer. Schedule: weekly.
- **`prompt-optimizer`** — Prompt Optimizer (low) — A/B tests system prompts for agents. Agents: learning-agent. Experimental. Schedule: weekly.
- **`backtest-runner`** — Backtest Runner (low) — Replay historical data through strategies. Agents: learning-agent, market-analyst. See `BACKTESTING.md`.

### 4.6 Monitoring
- **`chain-health`** — Chain Health Monitor (low) — RPC latency, block height, gas. Schedule: every 10s. Always on.
- **`gas-alerts`** — Gas Price Alerts (low) — Notify on gas threshold. Agents: gas-forecaster. Trigger: threshold crossed.
- **`price-alerts`** — Price Alerts (low) — User-defined price triggers. Agents: market-analyst. Trigger: price crosses level.
- **`whale-alerts`** — Whale Alerts (low) — Large transfer notifications. Agents: sentiment-analyst. Trigger: amount threshold.
- **`liquidation-watch`** — Liquidation Watch (medium) — Tracks lending protocol liquidations. Agents: market-analyst, risk-assessor. Schedule: every 30s.
- **`gas-burn-tracker`** — Gas Burn Tracker (low) — Tracks APEX's cumulative gas spent. Schedule: every 10s.

### 4.7 Portfolio
- **`portfolio-aggregator`** — Portfolio Aggregator (low) — Aggregates balances across chains. Schedule: every 60s.
- **`rebalancer`** — Portfolio Rebalancer (high) — Rebalances to target allocation. Agents: portfolio-optimizer, execution-planner. Schedule: cron or trigger.
- **`pnl-reporter`** — P&L Reporter (low) — Daily / weekly / monthly P&L. Agents: learning-agent. Schedule: cron.
- **`tax-export`** — Tax Export (low) — Generates tax-ready trade CSV. Trigger: manual.
- **`wallet-sync`** — Wallet Sync (low) — Syncs new wallets when added. Trigger: on wallet add.

### 4.8 Bridge
- **`bridge-quote-aggregator`** — Bridge Quote Aggregator (low) — Best bridge rate across providers. Agents: bridge-advisor. Cooldown 10s.
- **`bridge-time-optimizer`** — Bridge Time Optimizer (low) — Picks fastest route considering current congestion. Agents: bridge-advisor, gas-forecaster. Cooldown 30s.
- **`bridge-fee-forecaster`** — Bridge Fee Forecaster (low) — Predicts near-future bridge fees. Agents: bridge-advisor, learning-agent. Schedule: every 5m.

### 4.9 Yield
- **`yield-scanner`** — Yield Scanner (low) — Best yield opportunities across protocols. Agents: market-analyst, risk-assessor. Cooldown 5m.
- **`lp-position-monitor`** — LP Position Monitor (low) — Impermanent loss + fee tracking. Agents: market-analyst. Schedule: every 5m.
- **`auto-compound`** — Auto-Compound (medium) — Compounds yield positions. Agents: execution-planner. Schedule: cron.
- **`vault-allocation`** — Vault Allocation (medium) — Allocates to optimal yield vaults. Agents: portfolio-optimizer, risk-assessor. Schedule: hourly.

### 4.10 Meta
- **`user-assistant`** — User Assistant (low) — Conversational helper. Agents: user-assistant. Always on.
- **`config-wizard`** — Configuration Wizard (low) — First-run + change-provider helpers. Agents: user-assistant. Trigger: manual.
- **`diagnostics-runner`** — Diagnostics Runner (low) — On-demand health snapshot. Agents: anomaly-detector, chain-health. Trigger: manual.
- **`update-notifier`** — Update Notifier (low) — Notifies on app/skill updates. Trigger: on app start + 4h.

---

## 5. Skill Lifecycle (extended)

1. **Registration** — `SkillRegistry.register(skillDef)`; validates against schema; inserts/updates `skills` table
2. **Activation Gate** — Trigger condition (schedule/event/user) AND cooldown elapsed AND concurrency available AND enabled
3. **Pre-flight** — Validate inputs against `inputs_schema`; check that all `required_agents` are registered and enabled
4. **Memory + RAG Load** — Pull relevant facts and retrieved context per agent
5. **Execution** — Orchestrate agents (per their patterns in `AGENTS.md` §4.2); dispatch tools; handle errors
6. **Output Validation** — Validate final output against `outputs_schema`; retry once with correction if mismatch
7. **Post-flight** — Persist results to relevant tables; update metrics; emit events for UI
8. **Cooldown Start** — Lock the skill for `cooldown_ms` before next eligible invocation
9. **Error Path** — On error: retry per `retry_policy`, then circuit-breaker; partial results returned with `partial: true` flag
10. **Deprecation** — When `deprecated=true`: still runs but UI shows "Deprecated" banner and suggests replacement

---

## 6. User Management

### 6.1 Skill Library Page
- List view grouped by category, sortable by name / risk / last-run / success rate
- Each card: icon, name, description, status (idle / running / error / disabled), risk badge, toggle, kebab menu
- Filter chips: All / Enabled / Experimental / Deprecated
- Search bar with live filter

### 6.2 Skill Detail Drawer
- Long description (markdown)
- Required agents (linked to Agent detail)
- Configurable params (form, with help text)
- Recent invocations (last 20, with success/fail)
- Metrics: success rate, p50/p95 latency, total cost
- "Run Now" button (manual invocation with optional input)
- "Export Logs" button
- "Reset to Defaults" button

### 6.3 Bulk Actions
- Enable/disable all in a category
- "Enable only safe skills" preset (excludes high/critical)
- "Disable all experimental"

### 6.4 Custom Skills (v3.1+)
- User-authored skills via JSON editor (YAML planned)
- Stored in `user_skills` table; same schema as built-in
- Sandboxed: cannot override built-in skills; cannot add tools not in the library
- Share via Export/Import (no API keys)

---

## 7. Skill Metrics & Observability

Per skill, tracked continuously:
- **Invocation count** (1h, 24h, 7d, 30d)
- **Success rate** (%)
- **p50 / p95 / p99 latency** (ms)
- **Cost** (rolling 1h, 24h, 7d, 30d)
- **Token usage** (input/output)
- **Top errors** (class + sanitized message)
- **Last successful run** timestamp
- **Last error** timestamp
- **Average confidence** (when agents return one)

Surface in:
- Skill Library card (summary)
- Skill Detail drawer (full)
- Dashboard → Skills tab
- Logs page (JSON export)

---

## 8. Cross-Skill Coordination

Skills can subscribe to events from other skills. Example:
- `anomaly-circuit-breaker` emits `circuit_open` → all `*arb` skills pause
- `portfolio-aggregator` emits `balance_changed` → `rebalancer` re-evaluates
- `chain-health` emits `chain_degraded` → `bridge-execution` fails over to alternate bridge

The event bus is in-process (Node `EventEmitter`); events are typed and validated.

---

## 9. Skill Dependency Graph

Built at runtime from `required_agents` and `required_tools`. Used to:
- Disable cascading: if a required agent is disabled, dependent skills show a warning
- Order initialization: agents load before skills; skills load in dependency order
- Impact analysis: "If I disable X, these skills will be affected"

Visualized in **Settings → Skills → Dependency Graph** as a force-directed graph.

---

## 10. Versioning & Updates

- Each skill carries its own `version`
- APEX auto-checks for new skill versions on app start + every 24h (no network call; checks bundled index)
- New versions show "Update Available" badge in Skill Library
- Updates preserve user config (params, enabled state) where schema-compatible
- Breaking changes require user confirmation; show diff

---

## 11. Example Skill Definition (Full)

```json
{
  "skill_id": "flash-loan-arb",
  "name": "Flash Loan Arbitrage",
  "version": "1.2.0",
  "description": "Zero-capital arbitrage using flash loans",
  "long_description": "Scans for arbitrage opportunities that can be executed with borrowed capital via flash loans, with no upfront capital required.",
  "category": "arbitrage",
  "tags": ["flash-loan", "zero-capital", "advanced"],
  "icon": "zap",
  "author": "APEX",
  "required_agents": ["opportunity-scanner", "execution-planner", "risk-assessor", "contract-auditor"],
  "required_tools": ["simulate_route", "estimate_gas", "check_flashbots_availability"],
  "inputs_schema": {
    "type": "object",
    "properties": {
      "min_profit_usd": { "type": "number", "default": 5 },
      "max_gas_gwei":   { "type": "number", "default": 100 }
    }
  },
  "outputs_schema": {
    "type": "object",
    "properties": {
      "executed":  { "type": "boolean" },
      "tx_hash":   { "type": "string" },
      "profit_usd":{ "type": "number" },
      "gas_used":  { "type": "number" }
    }
  },
  "chains": [1, 56, 137, 42161, 10, 8453],
  "risk_level": "critical",
  "enabled": false,
  "priority": 1,
  "cooldown_ms": 2000,
  "max_concurrent": 1,
  "timeout_ms": 60000,
  "cost_cap_usd_per_call": 0.10,
  "daily_call_quota": 500,
  "configurable_params": [
    { "key": "min_profit_usd", "label": "Min profit (USD)", "type": "number", "default": 5, "min": 0.1, "max": 1000, "description": "Skip if expected net profit is below this" },
    { "key": "max_gas_gwei",   "label": "Max gas (gwei)",  "type": "number", "default": 100, "min": 1,   "max": 2000, "description": "Skip if gas exceeds this" },
    { "key": "use_private_pool","label": "Use private mempool", "type": "boolean", "default": true, "description": "Route through Flashbots when available" },
    { "key": "allowed_dexes",  "label": "Allowed DEXes",   "type": "multiselect", "default": ["uniswap-v3","sushiswap","pancakeswap"], "options": [{"value":"uniswap-v3","label":"Uniswap V3"}, {"value":"sushiswap","label":"SushiSwap"}, {"value":"pancakeswap","label":"PancakeSwap"}], "description": "Limit to these DEXes", "advanced": true }
  ]
}
```

---

## 12. Adding a New Skill — Checklist

1. Pick a unique `skill_id` (kebab-case)
2. Write `description` and `long_description` (markdown ok)
3. Author `inputs_schema` and `outputs_schema` (JSON Schema draft-07, validate)
4. Decide `category` and `risk_level`
5. Pick `required_agents` (verify each exists in `AGENTS.md`)
6. Pick `required_tools` (verify each in `AI-PIPELINE.md` §10.2)
7. Define `configurable_params` with sensible defaults
8. Implement the skill in `src/skills/<id>/index.ts` exporting a `Skill` class
9. Register in `SkillRegistry.register()`
10. Add to UI Skill Library (automatic via registry)
11. Add to docs (this file) with full definition
12. Add unit tests (≥ 3 cases: happy, schema mismatch, agent failure)
13. Add integration test against a local fork (see `BACKTESTING.md`)
14. Add to changelog

---

*Skills are how users experience APEX's intelligence. Each must be focused, safe, observable, and worth toggling on.*
