# Repository Agent Gates

This repository uses root-level gate files to tell each coding assistant which canonical documents to read before making changes.

## First read
- `AGENTS.md` for the general gate.
- `ARCHITECTURE.md` for system boundaries.
- `AI-PIPELINE.md` for AI behavior.
- `RUNTIME-OPERATIONS.md` for runtime behavior.
- `TRADING-LIFECYCLE.md` and `EXECUTION-LIFECYCLE.md` for trade and execution behavior.
- `DATABASE-SCHEMA.md` for persistence structure.
- `SECURITY-CONTRACTS.md` for security rules.

## Assistant-specific gates
- `CLAUDE.md`
- `GEMINI.md`
- `OPENCODE.md`
- `KILO-CODE.md`
- `CLINE.md`
- `ANTIGRAVITY.md`
- `AIDER.md`
- `CODEBUFF.md`
- `COPILOT.md`
- `CURSOR.md`
- `QODO.md`
- `RAYCAST.md`
- `ROO-CODE.md`
- `TABNINE.md`
- `WARP.md`
- `WINDSURF.md`
- `ZED.md`
- `QWEN.md`
- `OLLAMA.md`
- `LLAMA-CPP.md`
- `GITHUB-COPILOT-CLI.md`
- `GOOGLE-CODE-ASSISTANT.md`
- `PERPLEXITY.md`
- `CHATGPT.md`

## Rule
If a behavior is not explicit in the authoritative docs, the assistant should stop and ask rather than guess.
