# APEX Architecture - Windows Desktop Multichain Arbitrage Bot (v3)

> **Version:** 3.0.0 | **Target:** Windows 10/11 x64 (.exe) | **AI:** Cloud APIs Only (OpenAI-Compatible + Anthropic + Self-Hosted Local)

---

## 1. System Overview

APEX is a Windows-native desktop application (single .exe, no Docker, no WSL)
for detecting and executing cross-chain and intra-chain arbitrage opportunities.
All AI/ML inference is performed via **cloud API calls** to user-configured
endpoints. The user can use OpenAI, Anthropic, **any OpenAI-compatible cloud
service (Groq, Together, OpenRouter, DeepSeek, Mistral, Azure, etc.)**, or a
**self-hosted local server (LM Studio, Ollama, vLLM, llama.cpp, LocalAI, etc.)**
that exposes an OpenAI-compatible endpoint.

### 1.1 High-Level Layers

```
┌────────────────────────────────────────────────────────────┐
│  PRESENTATION LAYER                                         │
│  Electron Renderer (React 18 + TypeScript + Vite)          │
│  Tailwind + shadcn/ui + Zustand + Recharts                 │
│  Pages: Dashboard, Trades, Opportunities, Skills,          │
│         Agents, Settings (incl. AI Configuration)           │
└──────────────────────────┬─────────────────────────────────┘
                           │ IPC (contextBridge, validated)
┌──────────────────────────▼─────────────────────────────────┐
│  DESKTOP SHELL LAYER                                        │
│  Electron Main Process (Node.js 20+)                       │
│  - WindowManager, Tray, Auto-Updater, SafeStorage,         │
│  - IPC handlers, Windows events (sleep/resume/network)      │
│  - Hosts all backend services in-process                   │
└──────────────────────────┬─────────────────────────────────┘
                           │ in-process call
┌──────────────────────────▼─────────────────────────────────┐
│  APPLICATION LAYER                                          │
│  AgentOrchestrator, SkillManager, StrategyEngine,          │
│  RiskManager, ExecutionEngine, PortfolioManager,           │
│  EventBus, Scheduler                                        │
└──────────────────────────┬─────────────────────────────────┘
                           │ in-process call
┌──────────────────────────▼─────────────────────────────────┐
│  AI PIPELINE LAYER (Cloud)                                  │
│  ProviderRegistry, RequestBuilder, ResponseParser,         │
│  FailoverManager, RateLimiter, Cache (L1/L2/L3),           │
│  CostTracker, ContextWindowManager, MemoryStore,           │
│  RAGRetriever, ToolDispatcher, StreamingHub                │
└──────────────────────────┬─────────────────────────────────┘
                           │ HTTPS / loopback HTTP
┌──────────────────────────▼─────────────────────────────────┐
│  AI PROVIDERS                                               │
│  OpenAI | Anthropic | Groq | Together | OpenRouter |       │
│  DeepSeek | Mistral | Perplexity | Azure | Custom |        │
│  Self-Hosted (LM Studio, Ollama, vLLM, llama.cpp, ...)      │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│  CHAIN LAYER                                                │
│  MultiChain RPC, WebSocket price feeds, DEX ABIs,         │
│  Flash loan providers, Bridges, Oracles, Explorers         │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│  DATA LAYER                                                 │
│  better-sqlite3 (settings, skills, agents, trades,         │
│  ai_providers, cache, memory, rag, logs)                   │
│  Electron safeStorage (encrypted API keys, DPAPI)          │
│  Worker-thread caches                                      │
└────────────────────────────────────────────────────────────┘
```

---

## 2. Component Architecture

### 2.1 Electron Desktop Shell
- **Main Process:** Node.js runtime hosting all backend services; no separate backend process
- **Renderer Process:** React SPA, sandboxed, contextIsolation true
- **IPC Bridge:** Whitelisted channels via `contextBridge`; every handler validates input
- **Packaging:** `electron-builder` producing NSIS `.exe` per-user installer for Windows x64
- **Auto-Update:** `electron-updater` checking GitHub Releases; code-signed (planned)
- **No Docker:** All services run as Node.js modules in the Electron main process

### 2.2 Agent Orchestrator
- Receives tasks from Skill Manager and Strategy Engine
- Routes to AI agents via AI Pipeline Router
- Maintains per-agent conversation context (sliding window or summary)
- Supports orchestration patterns: sequential, parallel fan-out, race, conditional, feedback loop, escalation

### 2.3 AI Pipeline Router
- **Provider Registry:** Dynamic; loaded from `ai_providers` table; user-managed in AI Settings
- **Request Builder:** Converts `AIRequest` → provider-specific HTTP body
- **Response Parser:** Normalizes any provider response to `AIResponse`
- **Fallback Chain:** Cascade to secondary/tertiary on retriable failure
- **Rate Limiter:** Token bucket per provider (RPM + TPM)
- **Cache:** 3 layers (memory / SQLite / semantic)
- **Streaming:** First-class, with `AbortController` cancellation
- **Function Calling:** OpenAI + Anthropic format translation
- **Memory & RAG:** Long-term facts + retrieved context per agent

### 2.4 Strategy Engine
- Pluggable strategy modules (intra-chain, cross-chain, triangular, flash-loan, etc.)
- Each scans its target venue/protocol set
- Calculates profit net of gas, slippage, bridge fees
- Uses AI agents (Opportunity Scanner, Risk Assessor) for ranking
- Outputs ranked opportunity list to Execution Engine

### 2.5 Risk Manager
- Pre-trade checks: position sizing, max drawdown, stop-loss/take-profit
- Continuous portfolio monitoring
- Anomaly detection + circuit breaker (can halt all execution skills)
- AI-assisted scoring via cloud API

### 2.6 Execution Engine
- Builds and signs transactions locally (encrypted key storage)
- Submits via RPC with gas optimization (Gas Forecaster)
- MEV protection via Flashbots / private mempools (when configured)
- Monitors status, handles reorgs and stuck transactions

### 2.7 Skill Manager
- Registry of bot capabilities (see `SKILLS.md`)
- Skills enabled/disabled by user; bulk operations supported
- Each skill declares required agents/tools; dependencies visualized
- Built-in and (future) user-defined skills

### 2.8 Portfolio Manager
- Aggregates balances across chains
- Tracks P&L (realized + unrealized)
- Rebalancing strategies
- Tax-export ready trade log

### 2.9 Event Bus
- In-process pub/sub (Node `EventEmitter`)
- Typed events with schemas
- Decouples skills (e.g. circuit-breaker → all execution skills)
- Audit log persisted

---

## 3. Data Flow

```
User configures AI providers in AI Settings
  └→ Saved to ai_providers table (key in safeStorage BLOB)

Strategy Engine scans chains
  └→ Raw market data + opportunities

Agent Orchestrator routes to agents
  └→ AI Pipeline Router selects provider
      └→ Cache check (L1 → L2 → L3 semantic)
      └→ Context build + memory + RAG
      └→ HTTP call to cloud/local endpoint
      └→ Parse + validate response
      └→ Cache write + cost log

Risk Manager validates each opportunity
  └→ If approved → Execution Engine
  └→ If rejected → log + learn

Execution Engine builds/sends tx
  └→ Wait for confirmation
  └→ Update trade + portfolio tables
  └→ Emit trade_executed event

Dashboard listens to events
  └→ Real-time updates via IPC
```

---

## 4. Technology Stack (v3)

| Layer | Technology | Version | Notes |
|-------|-----------|---------|-------|
| Desktop Shell | Electron | 31+ | Bundled Node.js + Chromium |
| UI Framework | React | 18+ | + TypeScript strict |
| Build | Vite | 5+ | Fast HMR |
| Styling | Tailwind CSS | 3+ | + shadcn/ui (Radix) |
| State | Zustand | 4+ | + TanStack Query for server-cache |
| Charts | Recharts | 2+ | + lightweight-charts (TradingView) for tickers |
| Animation | Framer Motion | 11+ | For page transitions |
| Backend Runtime | Node.js | 20+ | LTS, Electron main |
| Database | better-sqlite3 | 11+ | Sync, fast, embedded |
| Vector Search | sqlite-vec | latest | Local RAG |
| Key Storage | Electron safeStorage | built-in | DPAPI on Windows |
| Blockchain | ethers.js | v6 | EVM RPC + contracts |
| Optional | Viem | 2+ | Faster, tree-shakable |
| Smart Contracts | Solidity | 0.8.24+ | + Hardhat + OpenZeppelin |
| AI Providers | OpenAI, Anthropic, any OpenAI-compatible, any self-hosted OpenAI-compatible | — | No local inference |
| HTTP Client | Native `fetch` | — | + `AbortController`, `undici` for proxy |
| Streaming | Native `ReadableStream` | — | SSE + newline-delimited |
| Packaging | electron-builder | 24+ | NSIS .exe |
| Auto-Update | electron-updater | 6+ | GitHub Releases |
| Testing | Vitest | 1+ | Unit + integration |
| E2E | Playwright | 1+ | Renderer flows |
| Contract Tests | Hardhat | 2+ | + mainnet-fork |

### 4.1 Why No Docker
- APEX is a **single-user desktop app**; the Docker overhead is unjustified
- All services fit comfortably in the Electron main process with worker threads
- No container orchestration needed
- Simpler distribution: one `.exe`, no prerequisites
- Smaller attack surface (no container runtime)

### 4.2 Why Cloud-Only AI
- **No GPU required** for the user
- **Always up-to-date** models (no manual model management)
- **No model storage** cost on user disk
- **Provider flexibility** — user picks the model/price they want
- **Self-hosting supported** for users who already have a local LLM server (LM Studio, Ollama, vLLM, llama.cpp)

---

## 5. Windows-Specific

- **No Docker, No WSL** — pure native Windows
- **DPAPI** — API keys encrypted via Windows Data Protection API
- **System Tray** — minimize to tray, continue monitoring
- **Optional Startup** — Windows startup via `HKCU\...\Run` registry
- **NSIS Installer** — per-user install, no admin required
- **Portable Mode** — `portable.flag` file → data in app directory
- **Code Signing** — planned; unsigned `.exe` shows SmartScreen warning (documented in `USER-GUIDE.md`)
- **Windows Hello** — planned for wallet unlock

---

## 6. Security (cross-ref `SECURITY.md`)

- API keys via Electron `safeStorage` (DPAPI); never plaintext, never logged
- Private keys encrypted with user passphrase (Argon2id) + safeStorage layer
- All AI calls over HTTPS, or HTTP only to loopback
- No telemetry by default
- CSP enforced in renderer; no inline scripts
- Node integration disabled; contextIsolation true; sandbox true
- IPC via contextBridge only; whitelisted channels; input validation
- `will-navigate` blocked; `new-window` blocked; external links open in default browser

---

## 7. Performance Budgets

| Metric | Target |
|--------|--------|
| Startup (cold) | < 3s |
| Startup (warm) | < 1s |
| Idle memory | < 200MB |
| Active memory | < 500MB |
| UI frame rate | 60fps sustained |
| Installer size | < 150MB |
| Installed size | < 400MB |
| Skill execution p95 | < 2s (excluding AI call) |
| AI call p95 (cached) | < 50ms |
| AI call p95 (uncached, cloud) | < 3s |
| AI call p95 (uncached, local) | < 6s |

Optimizations:
- **Worker threads** for CPU-intensive tasks (encoding, parsing)
- **Connection pooling** for RPC (per chain)
- **Batch AI calls** where possible
- **Caching** at all layers
- **Debouncing** UI updates
- **Lazy loading** routes
- **DB indexes** on hot paths
- **Virtual scrolling** for long lists

---

## 8. Repository Layout (planned)

```
apex/
├── packages/
│   └── desktop/                # Electron app
│       ├── electron/           # Main process
│       │   ├── main.ts
│       │   ├── preload.ts
│       │   ├── ipc/
│       │   ├── safe-storage.ts
│       │   ├── window-manager.ts
│       │   ├── tray.ts
│       │   └── updater.ts
│       ├── src/                # Renderer (React)
│       │   ├── pages/
│       │   ├── components/
│       │   ├── stores/
│       │   ├── hooks/
│       │   └── lib/
│       ├── electron-builder.yml
│       ├── vite.config.ts
│       └── package.json
├── packages/
│   ├── ai/                     # AI pipeline package
│   │   ├── providers/          # OpenAI, Anthropic, Self-Hosted adapters
│   │   ├── pipeline/           # Router, failover, rate-limit
│   │   ├── memory/             # Agent memory
│   │   ├── rag/                # RAG retriever
│   │   └── tools/              # Tool library
│   ├── agents/                 # Built-in agents
│   ├── skills/                 # Built-in skills
│   ├── chains/                 # Chain adapters
│   ├── strategies/             # Strategy modules
│   └── contracts/              # Solidity contracts (Hardhat)
├── docs/                       # This documentation
├── scripts/
├── .github/workflows/
└── README.md
```

---

## 9. Architecture Patterns Adopted (v3)

- **Event-Driven** — In-process event bus decouples modules
- **CQRS** — Separate read models (Dashboard queries) from write models (Execution)
- **Plugin Architecture** — Skills, agents, providers, tools all pluggable
- **Observer** — Price feeds, chain events
- **State Machine** — Trade lifecycle: `discovered → simulated → approved → submitted → confirmed → settled/failed`
- **Repository Pattern** — All data access via repositories (no raw SQL in app code)
- **Strategy** — Pluggable strategy modules (see [`STRATEGIES.md`](./STRATEGIES.md))
- **Circuit Breaker** — Per-provider AI circuit breaker; per-skill error circuit breaker
- **Bulkhead** — Concurrency limits per skill prevent resource exhaustion
- **Saga** — Multi-step on-chain flows (flash loan → swap → repay) compensated on failure

---

## 10. Observability (cross-ref `AI-PIPELINE.md` §15)

- **Structured logging** — pino, JSON, daily rotation, 7-day retention
- **Metrics** — In-memory + persisted; per provider, per agent, per skill
- **Traces** — End-to-end request traces for AI calls (request_id, correlation_id)
- **Health endpoint** — IPC channel `app.health` returns system snapshot
- **Crash reports** — Optional, user-consented; uploaded to user's own endpoint (planned)

---

## 11. Build & Release (cross-ref `DEPLOYMENT.md`)

- Tag `v*` → GitHub Actions
- Node 20, `npm ci`
- `npm run build` (Vite + TypeScript)
- `electron-rebuild` for native modules (better-sqlite3)
- `electron-builder --win nsis`
- Upload `.exe` + `latest.yml` to GitHub Releases
- Code-signing: planned (currently unsigned; SmartScreen warning documented)

---

*This is the architectural foundation. Every implementation must align with these layers, contracts, and patterns.*
