# APEX Changelog

> **Version:** 3.0.0 | **Format:** [Keep a Changelog](https://keepachangelog.com/) | **Versioning:** [SemVer](https://semver.org/)

All notable changes to APEX are documented in this file. Dates are ISO 8601.

---

## [Unreleased]

### Planned for 3.1.0
- Code signing (Authenticode) — eliminates SmartScreen warnings
- Custom user-authored skills (JSON editor)
- Paper trading mode (simulated execution against live data)
- Hardware wallet support (Ledger via WebHID)
- Telegram / Discord notification webhooks
- Light theme (currently dark-only)
- Additional chains: Avalanche C-Chain, Linea, Scroll, zkSync Era, Mantle
- More built-in skills (see `SKILLS.md` §4 for full list)

### Planned for 3.2.0
- Trezor support
- Mobile companion app (read-only monitoring, iOS + Android)
- Email digests
- In-app skill marketplace (curated community skills)
- Tax-export integrations (CoinTracker, Koinly, TokenTax)

### Planned for 4.0.0
- Non-EVM chains (Solana, Sui, Aptos)
- Statistical arbitrage strategies
- Market making strategies
- Plugin system v2 (3rd-party skills, sandboxed)

---

## [3.0.0] - 2026-07-25

### Documentation Overhaul
This is a **major documentation release**. The product is still pre-code (no
application source committed yet), so the v3.0 release is a complete
re-architecting of the documentation to reflect the v3 product vision.

### Added (Documentation)

#### Major rewrites
- **`docs/AGENTS.md`** — Complete field schema for every agent, expanded from 8 to 12 agents (added: Contract Auditor, Gas Forecaster, Bridge Advisor, User Assistant), full prompt engineering standards, tool calling spec, agent observability
- **`docs/AI-SETTINGS.md`** — Full v3 page spec with **Self-Hosted / Local Congo-compatible** provider type (LM Studio, Ollama, vLLM, llama.cpp, LocalAI, Jan, LMDeploy), preset templates, advanced fields (proxy, custom headers, request timeout), three-tab layout (Providers / Agent Overrides / Diagnostics)
- **`docs/AI-PIPELINE.md`** — Deep pipeline spec: streaming, function calling (OpenAI + Anthropic translation), RAG, agent memory, semantic cache (3 layers), multi-model consensus, observability, full type contracts (`AIRequest`, `AIResponse`, `AIError`)
- **`docs/SKILLS.md`** — Expanded from 14 to 40+ skills across 10 categories (Arbitrage, Analysis, Risk, Execution, Learning, Monitoring, Portfolio, Bridge, Yield, Meta), full skill schema, dependency graph, custom skill roadmap
- **`docs/DESIGNER-PROTOCOLS.md`** — Full component library, 13 component types, AI-specific components (StreamingText, ConfidenceBar, ToolCallCard, AgentStatusPill, ReasoningTrace, CostBadge), patterns section, accessibility deep-dive
- **`docs/ARCHITECTURE.md`** — Updated to v3: layer diagram, 9 component sections, technology stack table, repository layout, 10 architecture patterns
- **`docs/ENHANCEMENT-ROADMAP.md`** — Updated to v3
- **`docs/SECURITY.md`** — Minor updates for v3
- **`docs/WINDOWS-DESKTOP.md`** — Minor updates
- **`docs/CLOUD-AI-INTEGRATION.md`** — Aligned with new `AI-PIPELINE.md`
- **`docs/README.md`** — Updated doc index

#### New documents
- **`docs/USER-GUIDE.md`** — End-user guide (install, first-run, AI config, wallets, skills, dashboard, troubleshooting, uninstall)
- **`docs/TROUBLESHOOTING.md`** — Symptom-first troubleshooting across install, AI, trading, skills, performance, data, updates
- **`docs/FAQ.md`** — 50+ Q&A across general, tech, cost, security, trading, AI, wallets, roadmap
- **`docs/CHANGELOG.md`** — This file
- **`docs/API-REFERENCE.md`** — IPC channel reference, programmatic skill invocation, public exports
- **`docs/DEPLOYMENT.md`** — Build, release, distribution, code signing roadmap
- **`docs/CHAIN-INTEGRATION.md`** — How to add a new EVM chain adapter
- **`docs/DEX-INTEGRATION.md`** — How to add a new DEX adapter
- **`docs/BACKTESTING.md`** — Backtest engine spec
- **`docs/CONTRIBUTING.md`** — Contribution guide (code, docs, skills, agents)

### Changed
- All docs now share a consistent header format (Version, Last Updated, Scope)
- Cross-references between docs explicit
- All design decisions in `DESIGNER-PROTOCOLS.md` use design tokens, not hex codes
- AI provider terminology standardized: "OpenAI-Compatible (Cloud)" / "Anthropic Native" / "Self-Hosted Local"

### Removed
- Inconsistent field naming across docs (consolidated to snake_case in DB, camelCase in TS)
- Ad-hoc AI fields per doc (now centralized in `AI-SETTINGS.md` §3)

### Security
- Documented HTTP-over-non-loopback rejection at validation layer
- Documented custom header restrictions (cannot override `Authorization` for cloud)
- Documented key zeroing in memory after use

---

## [2.0.0] - 2026-07-25

### Added
- Initial v2 documentation suite across 10 docs
- Concept of modular agents, skills, and AI pipeline
- Windows-desktop-only positioning
- Cloud-AI-only positioning
- OpenAI + Anthropic + custom OpenAI-compatible support
- safeStorage-based key encryption
- System tray, auto-update, NSIS installer planning

---

## [1.0.0] - 2026-07-25

### Added
- Initial `APEX-ARCHITECTURE.md` (Parts 1-6) — comprehensive project spec
- High-level system architecture, modules, smart contract layer, AI system, multi-chain architecture, supported strategies, technology stack, design goals

---

## Versioning Policy

- **MAJOR** (x.0.0): Breaking changes to public API, data model, or user-facing workflows
- **MINOR** (0.x.0): New features, backward-compatible
- **PATCH** (0.0.x): Bug fixes, docs, internal refactors

Docs are versioned with the product. A doc version bump is a doc-only release.

---

## Links

- [Keep a Changelog](https://keepachangelog.com/)
- [Semantic Versioning](https://semver.org/)
- [GitHub Releases](https://github.com/pavan53732/Apex-Arbitrage-Multichain-bot-for-windows/releases)
