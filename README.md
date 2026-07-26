# Repository Agent Gates

This repository uses root-level gate files to tell each coding assistant which canonical documents to read before making changes.

## First read
- [AGENTS.md](./AGENTS.md) for the general gate.
- [docs/ARCHITECTURE.md](./docs/ARCHITECTURE.md) for system boundaries.
- [docs/AI-PIPELINE.md](./docs/AI-PIPELINE.md) for AI behavior.
- [docs/RUNTIME-OPERATIONS.md](./docs/RUNTIME-OPERATIONS.md) for runtime behavior.
- [docs/TRADING-LIFECYCLE.md](./docs/TRADING-LIFECYCLE.md) and [docs/EXECUTION-LIFECYCLE.md](./docs/EXECUTION-LIFECYCLE.md) for trade and execution behavior.
- [docs/DATABASE-SCHEMA.md](./docs/DATABASE-SCHEMA.md) for persistence structure.
- [docs/SECURITY-CONTRACTS.md](./docs/SECURITY-CONTRACTS.md) for security rules.

## Assistant-specific gates
- [CLAUDE.md](./CLAUDE.md)
- [GEMINI.md](./GEMINI.md)
- [OPENCODE.md](./OPENCODE.md)
- [KILO-CODE.md](./KILO-CODE.md)
- [CLINE.md](./CLINE.md)
- [ANTIGRAVITY.md](./ANTIGRAVITY.md)
- [AIDER.md](./AIDER.md)
- [CODEBUFF.md](./CODEBUFF.md)
- [COPILOT.md](./COPILOT.md)
- [CURSOR.md](./CURSOR.md)
- [QODO.md](./QODO.md)
- [RAYCAST.md](./RAYCAST.md)
- [ROO-CODE.md](./ROO-CODE.md)
- [TABNINE.md](./TABNINE.md)
- [WARP.md](./WARP.md)
- [WINDSURF.md](./WINDSURF.md)
- [ZED.md](./ZED.md)
- [QWEN.md](./QWEN.md)
- [OLLAMA.md](./OLLAMA.md)
- [LLAMA-CPP.md](./LLAMA-CPP.md)
- [GITHUB-COPILOT-CLI.md](./GITHUB-COPILOT-CLI.md)
- [GOOGLE-CODE-ASSISTANT.md](./GOOGLE-CODE-ASSISTANT.md)
- [PERPLEXITY.md](./PERPLEXITY.md)
- [CHATGPT.md](./CHATGPT.md)

## Validation
Run `scripts/validate_markdown_refs.sh` before committing documentation changes to catch broken local markdown references early.

## Rule
If a behavior is not explicit in the authoritative docs, the assistant should stop and ask rather than guess.
