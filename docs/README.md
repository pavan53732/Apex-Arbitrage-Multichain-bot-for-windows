# APEX Arbitrage Multichain Bot - Documentation Index

> **Version:** 3.0.0
> **Platform:** Windows Desktop (.exe) - No Docker
> **AI Mode:** Cloud AI APIs Only (OpenAI-Compatible + Anthropic + Self-Hosted Local)
> **Last Updated:** July 25, 2026

---

## Documentation Map

### Core Architecture & Design
| # | Document | Purpose |
|---|----------|---------|
| 1 | [ARCHITECTURE.md](./ARCHITECTURE.md) | System architecture, layers, components, data flow |
| 2 | [AGENTS.md](./AGENTS.md) | 12 AI agents, full field schema, communication protocols |
| 3 | [DESIGNER-PROTOCOLS.md](./DESIGNER-PROTOCOLS.md) | UI/UX design system, component library, patterns |
| 4 | [SKILLS.md](./SKILLS.md) | 40+ skills across 10 categories |

### AI System
| # | Document | Purpose |
|---|----------|---------|
| 5 | [AI-PIPELINE.md](./AI-PIPELINE.md) | Cloud AI provider abstraction, streaming, function-calling, RAG, memory |
| 6 | [AI-SETTINGS.md](./AI-SETTINGS.md) | AI Configuration page (OpenAI / Anthropic / Self-Hosted / Custom) |
| 7 | [CLOUD-AI-INTEGRATION.md](./CLOUD-AI-INTEGRATION.md) | Provider integration reference |

### Platform & Operations
| # | Document | Purpose |
|---|----------|---------|
| 8 | [WINDOWS-DESKTOP.md](./WINDOWS-DESKTOP.md) | Windows .exe packaging, Electron, no Docker |
| 9 | [DEPLOYMENT.md](./DEPLOYMENT.md) | Build, release, code signing, auto-update |
| 10 | [SECURITY.md](./SECURITY.md) | Threat model, key handling, Electron hardening |
| 11 | [API-REFERENCE.md](./API-REFERENCE.md) | IPC + programmatic + (planned) webhook API |

### User-Facing
| # | Document | Purpose |
|---|----------|---------|
| 12 | [USER-GUIDE.md](./USER-GUIDE.md) | End-user guide (install, setup, trading) |
| 13 | [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) | Symptom-first troubleshooting |
| 14 | [FAQ.md](./FAQ.md) | 50+ Q&A |

### Extensibility
| # | Document | Purpose |
|---|----------|---------|
| 15 | [CHAIN-INTEGRATION.md](./CHAIN-INTEGRATION.md) | Adding a new EVM chain |
| 16 | [DEX-INTEGRATION.md](./DEX-INTEGRATION.md) | Adding a new DEX adapter |
| 17 | [BACKTESTING.md](./BACKTESTING.md) | Backtest engine, A/B, stress tests |
| 18 | [CONTRIBUTING.md](./CONTRIBUTING.md) | How to contribute |

### Roadmap & Process
| # | Document | Purpose |
|---|----------|---------|
| 19 | [ENHANCEMENT-ROADMAP.md](./ENHANCEMENT-ROADMAP.md) | Milestones, feature matrix |
| 20 | [CHANGELOG.md](./CHANGELOG.md) | Version history |

---

## Project Vision

APEX is a **Windows-native desktop application** (.exe) for multichain arbitrage
trading, powered by **cloud-based AI APIs** (OpenAI-compatible, Anthropic, and
**any self-hosted OpenAI-compatible server** like LM Studio, Ollama, vLLM,
llama.cpp). No Docker, no local LLM inference, no container orchestration.
The user downloads a single .exe, configures their AI provider keys in the
Settings page, and the bot handles everything through cloud AI calls.

## Core Principles

1. **Windows-First** — Native .exe via Electron, no Docker, no WSL required
2. **Cloud AI Only** — All AI inference via OpenAI-compatible or Anthropic APIs
3. **Self-Hosted Friendly** — Local OpenAI-compatible servers (LM Studio, Ollama, vLLM, llama.cpp) work seamlessly
4. **User-Controlled AI** — User sets base URL, model name, API key; can reset anytime
5. **Modular Agents** — Each AI capability is a discrete, composable agent
6. **Skill-Based** — Bot capabilities registered as skills with metadata
7. **Secure by Default** — API keys encrypted at rest, never logged, never transmitted

## Quick Start

- **New user?** Read [USER-GUIDE.md](./USER-GUIDE.md)
- **Got an error?** Check [TROUBLESHOOTING.md](./TROUBLESHOOTING.md)
- **Looking for something specific?** Try [FAQ.md](./FAQ.md)
- **Contributing code?** Read [CONTRIBUTING.md](./CONTRIBUTING.md)
- **Adding a chain/DEX?** See [CHAIN-INTEGRATION.md](./CHAIN-INTEGRATION.md) / [DEX-INTEGRATION.md](./DEX-INTEGRATION.md)
- **Architect?** Start with [ARCHITECTURE.md](./ARCHITECTURE.md)
- **AI engineer?** Start with [AI-PIPELINE.md](./AI-PIPELINE.md) + [AGENTS.md](./AGENTS.md)
- **Designer?** Read [DESIGNER-PROTOCOLS.md](./DESIGNER-PROTOCOLS.md)
- **Security researcher?** Read [SECURITY.md](./SECURITY.md)

---

*All documentation is maintained alongside the codebase. Update docs with every
feature change. Docs are the source of truth for design decisions.*


---

## Expanded & New Core Documentation (v3.1)

| Document | Purpose |
|----------|---------|
| [SECURITY.md](./SECURITY.md) | Full threat model, encryption, credential lifecycle, IPC security, CSP, incident response |
| [CLOUD-AI-INTEGRATION.md](./CLOUD-AI-INTEGRATION.md) | Provider setup, comparison matrix, rate limits, cost optimisation, fallback routing |
| [WINDOWS-DESKTOP.md](./WINDOWS-DESKTOP.md) | Electron architecture, NSIS installer, auto-update, portable mode, code signing |
| [ENHANCEMENT-ROADMAP.md](./ENHANCEMENT-ROADMAP.md) | Versioned milestones, priority matrix, technical debt, architecture evolution |
| [STRATEGIES.md](./STRATEGIES.md) | Strategy interface, lifecycle, built-in strategies, custom strategy development |
| [DATABASE-SCHEMA.md](./DATABASE-SCHEMA.md) | Complete SQLite schema, indexes, migrations, data lifecycle |
| [IPC-PROTOCOL.md](./IPC-PROTOCOL.md) | IPC channel catalogue, request/response schemas, validation, error codes |
| [TESTING-GUIDE.md](./TESTING-GUIDE.md) | Unit, integration, Playwright, Hardhat, coverage, CI strategy |
| [RISK-ENGINE.md](./RISK-ENGINE.md) | Position sizing, exposure limits, circuit breakers, drawdown, emergency shutdown |

> These documents close the documentation gaps identified in the v3 consistency review. Treat them as authoritative for their respective domains.


## Specification Expansion (v3.2)

### Build Blueprint
- [PROJECT-STRUCTURE.md](./PROJECT-STRUCTURE.md)
- [CODING-STANDARDS.md](./CODING-STANDARDS.md)
- [CONFIGURATION.md](./CONFIGURATION.md)
- [STATE-MANAGEMENT.md](./STATE-MANAGEMENT.md)
- [ERROR-HANDLING-LOGGING.md](./ERROR-HANDLING-LOGGING.md)
- [MONITORING-OBSERVABILITY.md](./MONITORING-OBSERVABILITY.md)
- [BUILD-RELEASE-CICD.md](./BUILD-RELEASE-CICD.md)
- [GLOSSARY.md](./GLOSSARY.md)

### Additional Developer Specifications
- [MODULE-DEPENDENCY.md](./MODULE-DEPENDENCY.md)
- [DATA-FLOW.md](./DATA-FLOW.md)
- [EVENT-FLOW.md](./EVENT-FLOW.md)
- [COMPONENT-DIAGRAMS.md](./COMPONENT-DIAGRAMS.md)
- [API-CONTRACTS.md](./API-CONTRACTS.md)
- [IPC-MESSAGE-CATALOG.md](./IPC-MESSAGE-CATALOG.md)
- [PERMISSION-MODEL.md](./PERMISSION-MODEL.md)
- [FILE-STORAGE.md](./FILE-STORAGE.md)
- [PERFORMANCE-TARGETS.md](./PERFORMANCE-TARGETS.md)
- [NON-FUNCTIONAL-REQUIREMENTS.md](./NON-FUNCTIONAL-REQUIREMENTS.md)
- [UI-COMPONENT-SPEC.md](./UI-COMPONENT-SPEC.md)
- [DESIGN-SYSTEM.md](./DESIGN-SYSTEM.md)
- [FEATURE-MATRIX.md](./FEATURE-MATRIX.md)
- [IMPLEMENTATION-ROADMAP.md](./IMPLEMENTATION-ROADMAP.md)
- [DECISION-LOG.md](./DECISION-LOG.md)
- [KNOWN-LIMITATIONS.md](./KNOWN-LIMITATIONS.md)


## Single Source of Truth Model
The documentation set is the authoritative implementation specification for APEX. AI agents and developers must implement the system from these documents without inventing undocumented architecture, state flow, storage rules, or package structure.

## Specification Documents Added for AI-Driven Implementation
### Repository and Architecture Ownership
- [PROJECT-STRUCTURE.md](./PROJECT-STRUCTURE.md)
- [MODULE-DEPENDENCY.md](./MODULE-DEPENDENCY.md)
- [DATA-FLOW.md](./DATA-FLOW.md)
- [EVENT-FLOW.md](./EVENT-FLOW.md)
- [COMPONENT-DIAGRAMS.md](./COMPONENT-DIAGRAMS.md)
- [NON-FUNCTIONAL-REQUIREMENTS.md](./NON-FUNCTIONAL-REQUIREMENTS.md)
- [DECISION-LOG.md](./DECISION-LOG.md)
- [KNOWN-LIMITATIONS.md](./KNOWN-LIMITATIONS.md)

### Implementation Standards
- [CODING-STANDARDS.md](./CODING-STANDARDS.md)
- [CONFIGURATION.md](./CONFIGURATION.md)
- [STATE-MANAGEMENT.md](./STATE-MANAGEMENT.md)
- [ERROR-HANDLING-LOGGING.md](./ERROR-HANDLING-LOGGING.md)
- [MONITORING-OBSERVABILITY.md](./MONITORING-OBSERVABILITY.md)
- [BUILD-RELEASE-CICD.md](./BUILD-RELEASE-CICD.md)
- [PERFORMANCE-TARGETS.md](./PERFORMANCE-TARGETS.md)

### Contracts, Permissions, and UI Specs
- [API-CONTRACTS.md](./API-CONTRACTS.md)
- [IPC-MESSAGE-CATALOG.md](./IPC-MESSAGE-CATALOG.md)
- [PERMISSION-MODEL.md](./PERMISSION-MODEL.md)
- [FILE-STORAGE.md](./FILE-STORAGE.md)
- [UI-COMPONENT-SPEC.md](./UI-COMPONENT-SPEC.md)
- [DESIGN-SYSTEM.md](./DESIGN-SYSTEM.md)
- [FEATURE-MATRIX.md](./FEATURE-MATRIX.md)
- [IMPLEMENTATION-ROADMAP.md](./IMPLEMENTATION-ROADMAP.md)
- [GLOSSARY.md](./GLOSSARY.md)

