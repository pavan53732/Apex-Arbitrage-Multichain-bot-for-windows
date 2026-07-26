# APEX API Reference (v3)

> **Version:** 3.0.0 | **Last Updated:** July 25, 2026
> **Scope:** Public IPC API, programmatic skill/agent invocation, and code-level exports.

---

## 1. Overview

APEX exposes three layers of API:
1. **IPC API** — between the Electron renderer (UI) and main process
2. **Programmatic API** — for skill and agent authors writing internal code
3. **Webhook API** *(planned v3.2)* — for external integrations

All public APIs are versioned (`apiVersion` in responses, `X-APEX-API-Version` in headers for webhooks).

---

## 2. IPC API (Electron contextBridge)

All IPC channels are exposed via `window.apex.<namespace>.<method>(args)`.
Every channel is whitelisted in the preload; every handler validates input
against a Zod schema before processing.

### 2.1 Common Conventions
- All methods return `Promise<T>` where `T` is `{ ok: true, data: T } | { ok: false, error: { code, message, details? } }`
- All methods accept a single object argument
- All methods enforce a permission scope; some require `confirm()` in the UI

### 2.2 `window.apex.ai`

```ts
// Providers
ai.getProviders(): Promise<{ providers: AIProvider[] }>
ai.getProvider(id: string): Promise<{ provider: AIProvider }>
ai.saveProvider(input: AIProviderInput): Promise<{ provider: AIProvider }>
ai.deleteProvider(id: string): Promise<{ ok: true }>
ai.testConnection(id: string): Promise<{ ok: boolean, latency_ms: number, model: string, error?: string }>
ai.resetProvider(id: string): Promise<{ provider: AIProvider }>
ai.resetAll(): Promise<{ ok: true }>
ai.clearCache(): Promise<{ ok: true, entries_removed: number }>

// Templates
ai.getTemplates(): Promise<{ templates: ProviderTemplate[] }>

// Diagnostics
ai.getDiagnostics(): Promise<{ diagnostics: Diagnostics }>
ai.exportDiagnostics(): Promise<{ path: string }>  // triggers save dialog
```

### 2.3 `window.apex.agents`

```ts
agents.getAll(): Promise<{ agents: Agent[] }>
agents.get(id: string): Promise<{ agent: Agent }>
agents.saveOverride(id: string, override: AgentOverride): Promise<{ agent: Agent }>
agents.resetOverride(id: string): Promise<{ agent: Agent }>
agents.resetAllOverrides(): Promise<{ ok: true }>
agents.toggle(id: string, enabled: boolean): Promise<{ agent: Agent }>
agents.getLogs(id: string, limit?: number): Promise<{ logs: AgentLog[] }>
agents.invoke(id: string, input: any, options?: { stream?: boolean, correlation_id?: string }): Promise<{ response: AIResponse } | AsyncIterable<{ token: string }>>
```

### 2.4 `window.apex.skills`

```ts
skills.getAll(): Promise<{ skills: Skill[] }>
skills.get(id: string): Promise<{ skill: Skill }>
skills.toggle(id: string, enabled: boolean): Promise<{ skill: Skill }>
skills.saveConfig(id: string, config: Record<string, any>): Promise<{ skill: Skill }>
skills.resetConfig(id: string): Promise<{ skill: Skill }>
skills.runNow(id: string, input?: any): Promise<{ run_id: string }>
skills.getRuns(id: string, options?: { limit?: number, since?: string }): Promise<{ runs: SkillRun[] }>
skills.getRun(runId: string): Promise<{ run: SkillRun }>
skills.getLogs(id: string, limit?: number): Promise<{ logs: SkillLog[] }>
```

### 2.5 `window.apex.trades`

```ts
trades.getHistory(options?: { limit?: number, since?: string, status?: string, chain_id?: number }): Promise<{ trades: Trade[] }>
trades.get(id: string): Promise<{ trade: Trade }>
trades.getActive(): Promise<{ trades: Trade[] }>
trades.cancel(id: string): Promise<{ trade: Trade }>
trades.export(options: { format: 'csv'|'json', from: string, to: string }): Promise<{ path: string }>
```

### 2.6 `window.apex.opportunities`

```ts
opportunities.getActive(options?: { chain_id?: number, min_profit?: number }): Promise<{ opportunities: Opportunity[] }>
opportunities.subscribe(callback: (opp: Opportunity) => void): () => void  // returns unsubscribe
opportunities.execute(id: string, options?: { slippage_pct?: number }): Promise<{ trade_id: string }>
```

### 2.7 `window.apex.portfolio`

```ts
portfolio.getSummary(): Promise<{ summary: PortfolioSummary }>
portfolio.getBalances(): Promise<{ balances: Balance[] }>
portfolio.getPnL(options: { from: string, to: string, granularity: 'hour'|'day'|'week' }): Promise<{ series: PnLPoint[] }>
portfolio.rebalance(): Promise<{ run_id: string }>
portfolio.exportTax(options: { year: number, format: 'csv'|'form8949' }): Promise<{ path: string }>
```

### 2.8 `window.apex.wallets`

```ts
wallets.getAll(): Promise<{ wallets: Wallet[] }>
wallets.add(input: AddWalletInput): Promise<{ wallet: Wallet }>
wallets.remove(id: string): Promise<{ ok: true }>
wallets.rename(id: string, name: string): Promise<{ wallet: Wallet }>
wallets.unlock(id: string, passphrase: string): Promise<{ ok: true, session: string }>
wallets.lock(id: string): Promise<{ ok: true }>
wallets.export(id: string): Promise<{ wallet: Wallet }>  // no key included
```

### 2.9 `window.apex.settings`

```ts
settings.get<T = any>(key: string): Promise<{ value: T }>
settings.set(key: string, value: any): Promise<{ ok: true }>
settings.getAll(): Promise<{ settings: Record<string, any> }>
settings.resetSection(section: string): Promise<{ ok: true }>
settings.resetAll(): Promise<{ ok: true }>
settings.exportBackup(): Promise<{ path: string }>
settings.importBackup(path: string): Promise<{ ok: true }>
```

### 2.10 `window.apex.app`

```ts
app.getVersion(): Promise<{ version: string, api_version: string }>
app.getHealth(): Promise<{ health: HealthSnapshot }>
app.checkUpdate(): Promise<{ update: UpdateInfo | null }>
app.installUpdate(): Promise<{ ok: true }>
app.openExternal(url: string): Promise<{ ok: true }>  // validates URL allowlist
app.showItemInFolder(path: string): Promise<{ ok: true }>
app.restartServices(): Promise<{ ok: true }>
app.quit(): Promise<void>
```

### 2.11 `window.apex.events` (subscriptions)

```ts
events.on(channel: EventChannel, callback: (payload: any) => void): () => void
events.off(channel: EventChannel, callback: (payload: any) => void): void
```

Channels (excerpt):
- `trade.executed`, `trade.failed`, `trade.settled`
- `opportunity.discovered`, `opportunity.expired`
- `skill.started`, `skill.completed`, `skill.failed`
- `agent.started`, `agent.completed`, `agent.failed`
- `ai.call.started`, `ai.call.completed`, `ai.call.failed`
- `circuit.opened`, `circuit.closed`
- `wallet.balance_changed`
- `chain.health.changed`
- `app.update_available`

---

## 3. Programmatic API (for internal skill/agent code)

This is the API used by code running inside the Electron main process.

### 3.1 AI Pipeline

```ts
import { ai } from '@/ai';

// Send a single request
const response = await ai.complete({
  agent_id: 'market-analyst',
  system_prompt: '...',
  user_prompt: '...',
  temperature: 0.2,
  max_tokens: 1024,
  // optional:
  response_format: 'json_schema',
  json_schema: { ... },
  tools: [...],
  provider_binding: { mode: 'auto' },
  memory_namespace: 'market:eth',
  rag_namespace: 'market_analyses',
});

// Streaming
const handle = ai.stream({
  agent_id: 'user-assistant',
  system_prompt: '...',
  user_prompt: '...',
  stream: true,
});
for await (const chunk of handle) {
  if (chunk.type === 'token') process.stdout.write(chunk.text);
  if (chunk.type === 'done') break;
}

// Function-calling loop (handled automatically when tools provided)
const final = await ai.complete({ ..., tools: [...] });
// `final.tool_calls` may contain calls; APEX auto-executes and re-prompts
// up to 8 iterations.
```

### 3.2 Memory

```ts
import { memory } from '@/ai/memory';

await memory.remember({
  agent_id: 'market-analyst',
  namespace: 'market:eth',
  fact: 'ETH broke $4000 on 2026-07-25 with 2x normal volume',
  source: 'extracted',
  ttl_days: 30,
});

const facts = await memory.recall({
  agent_id: 'market-analyst',
  namespace: 'market:eth',
  query: 'recent ETH price action',
  top_k: 5,
});

await memory.forget({ agent_id, namespace, fact_id });
await memory.clear({ agent_id, namespace });
```

### 3.3 RAG

```ts
import { rag } from '@/ai/rag';

await rag.addDocuments({
  namespace: 'market_analyses',
  documents: [{ source: 'agent:market-analyst:2026-07-25', content: '...', metadata: {} }],
});

const results = await rag.retrieve({
  namespace: 'market_analyses',
  query: 'What was ETH volatility last week?',
  top_k: 5,
  min_similarity: 0.7,
});
```

### 3.4 Skill Manager

```ts
import { skillManager } from '@/skills';

skillManager.register(skillDef);
await skillManager.invoke('flash-loan-arb', { min_profit_usd: 10 });
skillManager.on('flash-loan-arb.completed', (result) => { ... });
```

### 3.5 Agent Registry

```ts
import { agentRegistry } from '@/agents';

agentRegistry.register(agentDef);
const agent = agentRegistry.get('market-analyst');
agentRegistry.override('market-analyst', { temperature: 0.1 });
```

### 3.6 Chain Adapters

```ts
import { chains } from '@/chains';

const arb = await chains.arbitrum.getProvider();
const block = await arb.getBlockNumber();
const prices = await arb.fetchPrices({ tokens: ['ETH', 'USDC'] });
```

---

## 4. Webhook API (planned v3.2)

External services can subscribe to APEX events via signed webhooks.

### 4.1 Configuration
**Settings → Integrations → Webhooks** → Add Endpoint
- URL (HTTPS required)
- Events to subscribe to
- Secret (for HMAC signature)

### 4.2 Payload Format
```json
{
  "api_version": "1.0",
  "event": "trade.executed",
  "timestamp": "2026-07-25T12:34:56.789Z",
  "delivery_id": "uuid",
  "data": { /* event-specific */ }
}
```

### 4.3 Signature
`X-APEX-Signature: sha256=<HMAC-SHA256(secret, body)>`

### 4.4 Retry
Exponential backoff: 1s, 5s, 30s, 5m, 1h. After 5 failed attempts, the
webhook is disabled and the user is notified.

---

## 5. Error Codes

Standard error code format: `E_<CATEGORY>_<SPECIFIC>`.

| Code | HTTP/IPC | Meaning |
|------|----------|---------|
| `E_AUTH` | 401 | Auth failed |
| `E_FORBIDDEN` | 403 | Permission denied |
| `E_NOT_FOUND` | 404 | Resource not found |
| `E_RATE` | 429 | Rate limited |
| `E_VALIDATION` | 400 | Invalid input |
| `E_TIMEOUT` | 408 | Timed out |
| `E_CONFLICT` | 409 | State conflict |
| `E_RPC` | 502 | Upstream RPC error |
| `E_AI` | 502 | AI provider error |
| `E_CONTRACT` | 500 | Smart contract error |
| `E_CIRCUIT` | 503 | Circuit breaker open |
| `E_INTERNAL` | 500 | Internal bug |
| `E_NOT_IMPLEMENTED` | 501 | Not yet implemented |

---

## 6. Versioning

- `apiVersion` in every response: `"3.0.0"`
- Webhook `X-APEX-API-Version` header
- Breaking changes bump the major version; deprecated methods continue to work for one major version with a warning header

---

## 7. Security Notes

- All IPC channels validate input via Zod
- All IPC handlers check user permission (e.g. wallet operations require the wallet to be unlocked)
- The renderer cannot invoke arbitrary code; only the channels in §2 are exposed
- API keys are never returned over IPC; only `has_key: true/false` and `key_fingerprint` (last 4 chars) for display

---

*This is the contract. Breaking changes require a major version bump and a migration window.*

## Cross-references
- `API-CONTRACTS.md`
- `IPC-PROTOCOL.md`
- `PROJECT-STRUCTURE.md`
- `ERROR-HANDLING-LOGGING.md`
