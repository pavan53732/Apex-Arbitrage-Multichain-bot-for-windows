---
last_updated: 2026-07-29
type: INDEX
owner: Trading Team
status: Canonical
version: 1.0.0
purpose: Agent Index documentation.
scope: Reference documentation.
canonical_source: docs/AGENT-INDEX.md
---

# Agent Index


## AI Guard
Before creating or modifying ANY markdown file, verify it complies with the 5 Prime Directives.
- Lifecycle docs must explicitly define initial state, terminal state, allowed transitions, forbidden transitions, recovery transitions, and failure transitions.
- Interface docs must explicitly define producer, consumer, payload, schema, validation, versioning, and failure behavior.
- Owner docs must explicitly state what they own and do not own.
- Cross-cutting docs must defer to canonical owners.
- Short docs must explicitly declare whether they are an [INDEX], [OVERVIEW], or [REFERENCE].
If a file fails any directive, abort and fix it before proceeding.

## Document type
This document is an overview, reference, or index as noted below.

# Agent Index

| File | Purpose |
|---|---|
| [AGENTS.md](../AGENTS.md) | General navigation and safety gate for all coding agents. |
| [CLAUDE.md](../CLAUDE.md) | Claude-specific coding gate. |
| [GEMINI.md](../GEMINI.md) | Gemini-specific coding gate. |
| [OPENCODE.md](../OPENCODE.md) | OpenCode-specific coding gate. |
| [KILO-CODE.md](../KILO-CODE.md) | Kilo Code-specific coding gate. |
| [CLINE.md](../CLINE.md) | Cline-specific coding gate. |
| [ANTIGRAVITY.md](../ANTIGRAVITY.md) | Antigravity-specific coding gate. |
| [AIDER.md](../AIDER.md) | Aider-specific coding gate. |
| [CODEBUFF.md](../CODEBUFF.md) | Codebuff-specific coding gate. |
| [COPILOT.md](../COPILOT.md) | Copilot-specific coding gate. |
| [CURSOR.md](../CURSOR.md) | Cursor-specific coding gate. |
| [QODO.md](../QODO.md) | Qodo-specific coding gate. |
| [RAYCAST.md](../RAYCAST.md) | Raycast-specific coding gate. |
| [ROO-CODE.md](../ROO-CODE.md) | Roo Code-specific coding gate. |
| [TABNINE.md](../TABNINE.md) | Tabnine-specific coding gate. |
| [WARP.md](../WARP.md) | Warp-specific coding gate. |
| [WINDSURF.md](../WINDSURF.md) | Windsurf-specific coding gate. |
| [ZED.md](../ZED.md) | Zed-specific coding gate. |
| [QWEN.md](../QWEN.md) | Qwen-specific coding gate. |
| [OLLAMA.md](../OLLAMA.md) | Ollama-specific coding gate. |
| [LLAMA-CPP.md](../LLAMA-CPP.md) | llama.cpp-specific coding gate. |
| [GITHUB-COPILOT-CLI.md](../GITHUB-COPILOT-CLI.md) | GitHub Copilot CLI-specific coding gate. |
| [GOOGLE-CODE-ASSISTANT.md](../GOOGLE-CODE-ASSISTANT.md) | Google Code Assist-specific coding gate. |
| [PERPLEXITY.md](../PERPLEXITY.md) | Perplexity-specific coding gate. |
| [CHATGPT.md](../CHATGPT.md) | ChatGPT-specific coding gate. |

## Rule
Use these files as the first stop for assistant-specific behavior. Use the canonical owner docs for actual implementation contracts.
