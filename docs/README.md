# APEX Arbitrage Multichain Bot - Documentation Index

> **Version:** 2.0.0
> **Platform:** Windows Desktop (.exe) - No Docker
> **AI Mode:** Cloud AI APIs Only (OpenAI-Compatible + Anthropic)
> **Last Updated:** July 25, 2026

---

## Documentation Map

| # | Document | Purpose |
|---|----------|---------|  
| 1 | ARCHITECTURE.md | Top-level system architecture, layers, data flow |
| 2 | AGENTS.md | AI Agent definitions, roles, communication protocols |
| 3 | DESIGNER-PROTOCOLS.md | UI/UX design system, component standards, theming |
| 4 | SKILLS.md | Bot skill registry, capabilities, skill lifecycle |
| 5 | AI-PIPELINE.md | Cloud AI pipeline, provider abstraction, routing |
| 6 | AI-SETTINGS.md | AI Settings page spec - OpenAI/Anthropic config |
| 7 | WINDOWS-DESKTOP.md | Windows .exe packaging, Electron config, no Docker |
| 8 | CLOUD-AI-INTEGRATION.md | Cloud AI API integration guide, endpoints, security |
| 9 | ENHANCEMENT-ROADMAP.md | Feature roadmap, priorities, milestones |
| 10 | SECURITY.md | API key handling, encryption, threat model |

---

## Project Vision

APEX is a **Windows-native desktop application** (.exe) for multichain arbitrage
trading, powered entirely by **cloud-based AI APIs**. No Docker, no local LLM
inference, no container orchestration. The user downloads a single .exe,
configures their AI provider keys in the Settings page, and the bot handles
everything through cloud AI calls.

## Core Principles

1. **Windows-First** - Native .exe via Electron, no Docker, no WSL required
2. **Cloud AI Only** - All AI inference via OpenAI-compatible or Anthropic APIs
3. **User-Controlled AI** - User sets base URL, model name, API key; can reset anytime
4. **Modular Agents** - Each AI capability is a discrete, composable agent
5. **Skill-Based** - Bot capabilities are registered as skills with metadata
6. **Secure by Default** - API keys encrypted at rest, never logged, never transmitted

---

*All documentation is maintained alongside the codebase. Update docs with every
feature change. Docs are the source of truth for design decisions.*
