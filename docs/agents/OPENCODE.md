---
last_updated: 2026-07-29
type: REFERENCE
owner: AI Team
status: Canonical
version: 1.0.0
purpose: OPENCODE AI tool documentation.
scope: OPENCODE reference.
canonical_source: OPENCODE.md
---

# OpenCode


## AI Guard
Before creating or modifying ANY markdown file, verify it complies with the 5 Prime Directives.
- Lifecycle docs must explicitly define initial state, terminal state, allowed transitions, forbidden transitions, recovery transitions, and failure transitions.
- Interface docs must explicitly define producer, consumer, payload, schema, validation, versioning, and failure behavior.
- Owner docs must explicitly state what they own and do not own.
- Cross-cutting docs must defer to canonical owners.
- Short docs must explicitly declare whether they are an [INDEX], [OVERVIEW], or [REFERENCE].
If a file fails any directive, abort and fix it before proceeding.

## Purpose
Guidance for OpenCode-based coding agents contributing to this repository.

## Gates
- Read the owner docs before making changes.
- Prefer explicit lifecycle and interface contracts over overview docs.
- Keep architecture, runtime, and trading boundaries separate.

## Required reading
- `AGENTS.md`
- `docs/ARCHITECTURE.md`
- `docs/RUNTIME-OPERATIONS.md`
- `docs/ai/runtime/AI-PIPELINE.md`
- `docs/CACHE-MANAGER.md`
- `docs/DATABASE-SCHEMA.md`
- `docs/security/SECURITY-CONTRACTS.md`

## Working rule
If the repo does not explicitly define the behavior, do not guess.
