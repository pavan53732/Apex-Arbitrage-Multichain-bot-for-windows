# 🤖 Apex Arbitrage Multichain Bot — Ultra Granular Autonomous Bot Blueprint (Subsystem Breakdown)

> **Master blueprint for AI agents and developers.  
> Read and follow before any code generation, editing, or review.  
> Recursively reference this file for every folder, file, and interface.**

---

## 1. Philosophy & Project Intent

- Zero-loss, atomic, cross-chain arbitrage and MEV (multi-path, fallback, auto-revert)
- AI/ML council for scoring, risk, volatility, RL, explainability, and operator guidance
- Full dashboard UI/UX, plugin hot-swap, 1-click controls, and pro analytics
- RAM-only secrets, audit, backup, recovery, CI, and rollback

All enabled networks are declared and toggled via `config/chains.json`; optional RPC overrides may be set in environment only as needed.

### Configuration flow
chains.json → protocols.json → adapters resolve by chainId → optional env RPC overrides

### Architectural Principles
- No hardcoded config—runtime must read `CHAINS_CONFIG`, `PROTOCOLS_CONFIG`, and `AI_CONFIG` from mounted files (compose/local dev), and must reject or warn if network IDs, RPC URLs, or protocol addresses are embedded in code paths; no hardcoded networks or addresses in code.

---

## 2. Top-Level Subsystem Breakdown

---

### 2.1. `ai-modules/` — **Autonomous AI/ML Council**

**Purpose:**  
All autonomous ML models, scoring, pattern learning, risk, and RL logic for trade, volatility, and route selection.

Defaults are the JS‑first council modules: `ai-engine.js`, `decisionMaker.js`, `patternLearner.js`, `modelRouter.js`, `scoreArbOpportunity.js`, `tokenReputationIndex.py`, `tradeOutcomeLogger.js`. External model names referenced in UI routes/examples are (optional integration/bridge). The council wiring is configured via `ai-modules/aiConfig.json`.

**Subfolders & Key Features:**

- `ai-engine.js`: Core ML orchestration, load/scoring pipeline, council voting
- `aiConfig.json`: Runtime toggles (model, mode, thresholds, fallback)
- `patternLearner.js`: Pattern recognition (LSTM/Transformer)
- `tokenReputationIndex.py`: Dynamic, cross-token risk/volatility scoring
- `scoreArbOpportunity.js`: Multivariate opportunity scoring (slippage, latency, gas, ROI, volatility)
- `tradeOutcomeLogger.js`: In-memory logs for on-the-fly feedback/retraining

**Agent Integration:**

- **All models in `models/modelWeights/` must be valid and loadable**
- `features/`: Each feature extractor is isolated, tested, and API-consumed by ai-engine
- `integration/`: Webhook/LLM/FinGPT bridge endpoints
- `simulation/`: Fork/test mode for AI action replay and error analysis
- `train/`: Pipeline for incremental, online, or CLI-triggered retraining
- **All config toggles must propagate live to backend and dashboard via API**
- **All outputs/logs are exportable and queryable for dashboard/ops**

**Agent Note:**  
Every function must have a test in `tests/`. Every model/config/weight is documented in `README.md` per subfolder.

#### Canonical AI paths
- `ai-modules/aiConfig.json` (AI wiring, toggles, thresholds)
- `ai-modules/models/modelWeights` (inference weights)
- `ai-modules/models/trainingOutputs` (training/export artifacts)

The council modules read configuration from `ai-modules/aiConfig.json` and must not assume hardcoded paths.

#### Smoke test requirement
At startup, a fixed scoring fixture must pass via `scoreArbOpportunity.js` to validate model load and path correctness (fails fast if weights/config paths are invalid).

---

### 2.2. `backend/` — **Engine, State, Plugins**

**Purpose:**  
All event loop logic, strategy, plugin orchestration, key state, and operator controls.

**Subfolders & Key Features:**

- `core/`: Main event loop, execution guard, rollback, state recovery
- `plugins/`: Each DEX, flashloan, oracle, bridge, AI module as plugin (hot-swappable, declare deps)
- `adapters/`: EVM contract wrappers, router/ABI bridge, multi-chain abstraction
- `state/`: In-memory + persistent state, recovery, checkpoint/rollback
- `utils/`: Shared helpers (gas, simulation, error, logs)
- `tests/`: Mirrors every core/plugin file; regression, fork, fuzz, MEV exploit tests

**Agent Integration:**

- All plugins/adapters export standardized interfaces
- **pluginManager.js** auto-registers, hot-swaps, and emits all state changes/events
- RAM-only key manager; no key is ever written to disk—violations are fatal errors
- Logs/alerts to `/data/` and `/dashboard/` via WebSocket/API
- All error, anomaly, and failover triggers to `/watchdog/`
- **Core must be 100% covered by tests.**

---

### 2.3. `contracts/` — **On-Chain Execution Logic**

**Purpose:**  
Solidity contracts for atomic flashloan, swap, fallback, upgrade, multi-path, MEV/arb execution.

**Subfolders & Key Features:**

- `interfaces/`: Standardized ABI/contract types for all DEXs/Flashloan/Oracle
- `deploy/`, `migrations/`: Upgrade/fork/deploy/test scripts (Hardhat, Anvil, Foundry)
- `tests/`: Full on-chain coverage (unit, fork, simulation, reorg/attack tests)

**Agent Integration:**

- Contracts must be fully verified, upgradable, and ABI-exported to `/types/`
- Must assert on-chain profit, revert on non-atomic execution
- All changes, deploys, and rollbacks logged to `/archive/` and `/data/logs/`

---

### 2.4. `dashboard/` — **Operator UI / UX / Analytics**

**Purpose:**  
Operator/AI control panel: live status, settings, analytics, plugin swaps, AR/XAI overlays.

**Subfolders & Key Features:**

- `pages/`, `components/`: All controls, widgets, panels, overlays
- `api/`: Backend API bridge (hot-swap plugins, config, key mgmt, analytics)
- `settings/`: UI runtime plugin/config controls, presets
- `__tests__/`: Full UI test suite, snapshot and integration
- AR overlays and XAI explainability hooks (future-proofed)

**Agent Integration:**

- All controls wire directly to backend (API/WS)
- All logs, errors, state, and plugin events are live, queryable, and exportable
- **UI coverage must be 90%+**
- All onboarding, docs, and playbooks must be discoverable from dashboard

---

### 2.5. `watchdog/` — **Resilience, Failover, Anomaly Detection**

**Purpose:**  
Continuous runtime safety, failover, circuit breaker, kill switch, and anomaly response.

**Subfolders & Key Features:**

- `watchdogController.js`: Loads and coordinates all monitors/guards
- `mempoolAnomalyDetector.js`, `volatilityWatchdog.js`, `latencySpikeDetector.js`, etc.: Specialized monitors for every vector
- `autoRestart.js`, `killSwitch.js`: Recovery and manual/auto halt routines
- `watchdogConfig.json`: Central schema for toggles, thresholds, triggers
- All triggers/events routed to `/dashboard/` and `/data/logs/`
- Test harness in `integrationTestWatchdog.js`

**Agent Integration:**

- Every monitor must have fork/test simulation in `/tests/` and/or `integrationTestWatchdog.js`
- All thresholds/guards are hot-configurable from dashboard or config
- Any fatal error auto-pauses execution, exports logs, and reports

**Health & Drift Guards:**
- Health probes enumerate enabled chains from `CHAINS_CONFIG` and verify RPC reachability, head movement, and latency thresholds on each run.
- On startup, log enabled chains from `chains.json` and verify they match dashboard toggles and backend logs; fail fast or warn if divergent.

---

### 2.6. `config/` — **Global Config/Presets/Chains/Tokens**

**Purpose:**  
All chains, tokens, DEXes, strategy, risk, plugin, analytics, compliance, and presets.

**Agent Integration:**

- All config is JSON/YAML, validated by schema, editable from dashboard
- All runtime changes auto-update backend and UI (live, never restart)
- **No config value is hardcoded in code.**

**Runtime mounts & env (compose/local dev):**
- Backend (and UI if applicable) rely on compose mounts for `./config` and `./ai-modules` and the following environment variables:
	- `CHAINS_CONFIG=/app/config/chains.json`
	- `PROTOCOLS_CONFIG=/app/config/protocols.json`
	- `AI_CONFIG=/app/ai-modules/aiConfig.json`

> Examples are illustrative; the actual set of enabled chains is read from `config/chains.json` at runtime.

---

### 2.7. `data/` + `storage/` — **Logs, Backups, DB, Secrets**

**Purpose:**  
Logs (trade, profit, alerts, errors, crash), operator state, audit, simulation results, backups.

**Agent Integration:**

- `/data/db/`: All SQLite/NoSQL DBs for trade/profit/logs; queryable from dashboard
- `/data/logs/`: All logs, rotated and exportable
- `/storage/`: RAM-only secret/key vault (zero disk persistence), snapshot/rollback files
- All backup/restore/test hooks are automated (dashboard, scripts)

#### Security & Operations Policies
- RAM‑only secrets; no secrets in config JSON; do not back up `.env` offsite; backups must set `include_env_files=false` per root policy.

#### Backups
- Backups must include `ai-modules/aiConfig.json`, `ai-modules/models/modelWeights`, `ai-modules/models/trainingOutputs`, and canonical evidence stores `data/analytics`, `data/audit-trails`, `data/compliance-archive`.
- Root SQLite mirrors are optional read‑only compaction artifacts.

---

### 2.8. `archive/`, `presets/`, `migrations/`, `benchmarks/`, `wall-of-fame/`

**Purpose:**  
- `/archive/`: All deprecated, old, or superseded modules/configs; must be recoverable
- `/presets/`: Strategy/config templates, demo configs for onboarding
- `/migrations/`: Contract/db/schema migration scripts, rollback and recovery
- `/benchmarks/`: Latency/gas/profitability test suites, profiling, hardware test logs
- `/wall-of-fame/`: Contributor and operator logs, recognitions, testimonials

---

### 2.9. `tests/`, `docs/`, `.github/`, `ci/`, `scripts/`

**Purpose:**  
- `tests/`: Full coverage (unit, integration, E2E, fork, fuzz, AI, contract)
- `docs/`: Whitepapers, playbooks, API refs, threat models, operator guides
- `.github/`, `ci/`: All CI/CD/test runners, security, PR review, lint, coverage
- `scripts/`: Automation (setup, quickstart, recovery, export, tree, manifest)

**Agent Integration:**

- Every new module/file must have a matching test and doc
- All scripts are fully documented, idempotent, and discoverable via dashboard/docs
- CI validates `config/chains.json` and `config/protocols.json` against JSON Schemas; invalid `chainId`/address/RPC breaks the build to protect codegen and adapters.
- Two lint scopes: Node/TS lint at root; React/Next lint only in `dashboard/.eslintrc` to avoid plugin bleed‑through across packages.

---

## Discoverability

UI architecture (layouts/locales/modals/overlays/pages/notifications) is documented under `dashboard`; Next/React linting rules live in `dashboard/.eslintrc` only; operator onboarding and runbooks are discoverable from dashboard help/docs pages.

---

## 3. End-to-End Integration & Agent Guidance

- **Recursively walk this blueprint, root README.md, and all per-folder README.md/config for 100% module discovery and codegen**
- **All agent code must be production-grade, modular, documented, and runtime validated**
- **Every edge case, hot-swap, rollback, failover, or AI path must be discoverable and covered by tests**
- **If any missing, ambiguous, or conflicting config, agent must HALT and request operator input before proceeding**

---

## 4. Agent Self-Validation Protocol

- Validate all cross-folder imports, paths, and config usage at codegen
- Lint and test every new file on generation
- After build, scan project tree vs. `/manifest/` for orphaned or missing files/folders
- Output a manifest and error/fix report for operator review

---

## 5. Author/Contact

- **Name:** Korukonda Pavan Kumar (Apex Creator)
- **Email:** pavan53732@gmail.com
- **Version:** 1.0.0
- **License:** MIT

---

> Let the Apex Arbitrage Multichain Bot run. Fully autonomous, always evolving. 🧠⚡

---

## Final Checklist

- Runtime reads `CHAINS_CONFIG`/`PROTOCOLS_CONFIG`/`AI_CONFIG` from mounted files; no hardcoded networks or addresses in code.
- Examples are illustrative; actual chains are read from `config/chains.json`.
- AI council is wired via `ai-modules/aiConfig.json`; models located in `ai-modules/models/modelWeights` and `ai-modules/models/trainingOutputs`.
- Health probes iterate all enabled chains; drift guard compares `chains.json` vs dashboard/backend on startup.
- Backups exclude `.env`, include AI config/weights/trainingOutputs and `data/analytics`, `data/audit-trails`, `data/compliance-archive`.
