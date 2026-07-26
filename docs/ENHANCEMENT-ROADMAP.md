# APEX Enhancement Roadmap

> **Version:** 3.0.0 | **Last Updated:** July 25, 2026 | **Status:** Living planning document

---

## 1. Roadmap Principles

The roadmap exists to translate the architecture into a staged delivery plan. It should align implementation order with the highest-risk dependencies first: trusted desktop runtime, provider abstraction, risk controls, execution correctness, and observability.

Planning principles:

- security and correctness before breadth
- vertical slices over disconnected feature spikes
- execution safety before strategy count expansion
- operator clarity before visual polish

---

## 2. Milestone Summary

| Milestone | Version Target | Focus |
|----------|----------------|-------|
| M1 | v3.0 | Desktop shell + local foundations |
| M2 | v3.1 | AI provider layer + settings + agent orchestration core |
| M3 | v3.2 | Strategy execution, risk engine, and first live trading path |
| M4 | v3.3 | Observability, backtesting, and operator workflow depth |
| M5 | v4.0 | Extensibility, plugins, advanced execution, multi-wallet maturity |

---

## 3. Milestone Details

### 3.1 M1 — Foundation

Primary deliverables:

- Electron shell
- SQLite integration
- secure storage foundation
- preload and IPC structure
- documentation baseline
- initial settings framework

Success criteria:

- packaged Windows build starts reliably
- config persists locally
- no privileged renderer shortcuts exist

### 3.2 M2 — AI Intelligence Layer

Primary deliverables:

- provider registry
- AI Settings page
- OpenAI-compatible adapter
- Anthropic adapter
- request/response normalisation
- failover and cache skeleton
- initial agent orchestrator

Success criteria:

- two provider classes work end-to-end
- structured output validation works
- provider latency and cost are visible

### 3.3 M3 — Trading Core

Primary deliverables:

- strategy registry
- opportunity scanning
- risk engine v1
- execution engine v1
- transaction lifecycle state machine
- chain and DEX adapter base layer

Success criteria:

- paper or controlled live path works end-to-end
- circuit breaker can halt unsafe execution
- trade records are stored consistently

### 3.4 M4 — Operational Depth

Primary deliverables:

- backtesting framework
- dashboards for health, cost, and agent traces
- troubleshooting and diagnostics depth
- simulation and replay improvements
- richer notifications and operator controls

Success criteria:

- historical strategy evaluation is usable
- operator can identify most failures without reading raw logs

### 3.5 M5 — Extensibility and Scale

Primary deliverables:

- plugin-ready skill and strategy model
- multi-wallet management
- hardware wallet support
- API/webhook surface expansion
- advanced execution patterns and more chains/DEXes

Success criteria:

- new skill/strategy/provider integrations no longer require core rewrites
- operational isolation is strong enough for broader usage

---

## 4. Priority Matrix

| Item | Impact | Effort | Risk | Priority |
|------|--------|--------|------|----------|
| Secure desktop shell | Critical | High | High | P0 |
| AI provider abstraction | Critical | High | High | P0 |
| Risk engine v1 | Critical | Medium | High | P0 |
| Transaction execution core | Critical | High | High | P0 |
| Observability baseline | High | Medium | Medium | P1 |
| Backtesting | High | Medium | Medium | P1 |
| Multi-chain expansion | High | High | High | P1 |
| Plugin system | Medium | High | Medium | P2 |
| Hardware wallet support | Medium | High | High | P2 |
| Public API/webhooks | Medium | Medium | Medium | P2 |

---

## 5. Feature Tracks

### 5.1 Desktop Platform Track

- installer and update reliability
- tray and background lifecycle
- secure secret handling
- diagnostics and recovery UX

### 5.2 AI Platform Track

- provider abstraction
- prompt and tool pipeline quality
- caching and rate-limiting
- cost tracking and fallback routing

### 5.3 Trading Core Track

- market ingestion
- strategy detection
- risk approval
- execution simulation and settlement tracking

### 5.4 Operator Experience Track

- settings clarity
- dashboards
- logs and troubleshooting
- agent and skill management

---

## 6. Technical Debt Register

| Debt Item | Why It Matters | Planned Milestone |
|-----------|----------------|-------------------|
| Thin security implementation notes | Security claims need backing detail | M1/M2 |
| Missing strategy specification | Core extension point is underdefined | M2 |
| Missing schema documentation | Local data model cannot be reviewed cleanly | M1 |
| Incomplete IPC contract documentation | Security and testing are harder without it | M1 |
| Legacy architecture wording in root spec | Risks design confusion | M1 |

---

## 7. Architecture Evolution Path

### 7.1 Near Term

- stabilise monorepo package boundaries
- keep shared types centralised
- document all contracts before broad implementation spread

### 7.2 Mid Term

- isolate providers, strategies, skills, and chains behind registries
- reduce cross-package coupling
- harden background workers and event-driven flows

### 7.3 Long Term

- plugin-safe extension model
- stronger execution isolation
- multiple deployment modes without fragmenting architecture

---

## 8. Delivery Timeline Guidance

```text
M1  [####........] foundation and shell
M2  [..####......] AI provider layer and orchestration core
M3  [....####....] execution, risk, and first trading path
M4  [......###...] observability and backtesting depth
M5  [.........###] extensibility and advanced features
```

This timeline is indicative rather than fixed. Security blockers and execution correctness issues override schedule pressure.

---

## 9. Long-Term Vision

APEX should evolve from a documented architecture into a modular desktop DeFi execution platform with strong local control, flexible AI routing, and production-grade safety controls. Growth should come from better execution correctness, clearer operator workflows, and extensible strategy infrastructure rather than from adding superficial features first.

---

## 10. Roadmap Governance

- Review milestones monthly.
- Re-rank priorities when a dependency or threat model changes.
- Add a feature only if its architecture owner and operational cost are understood.
- Keep this roadmap synchronised with `docs/README.md`, `CHANGELOG.md`, and the root architecture map.

---

A roadmap is useful only if it preserves architectural intent while exposing real delivery order. This document should stay tightly coupled to implementation risk, not aspiration alone.
