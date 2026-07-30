---
last_updated: 2026-07-29
type: REFERENCE
owner: AI Team
status: Canonical
version: 1.0.0
purpose: CLAUDE AI tool documentation.
scope: CLAUDE reference.
canonical_source: CLAUDE.md
---

# Claude


## AI Guard
Before creating or modifying ANY markdown file, verify it complies with the 5 Prime Directives.
- Lifecycle docs must explicitly define initial state, terminal state, allowed transitions, forbidden transitions, recovery transitions, and failure transitions.
- Interface docs must explicitly define producer, consumer, payload, schema, validation, versioning, and failure behavior.
- Owner docs must explicitly state what they own and do not own.
- Cross-cutting docs must defer to canonical owners.
- Short docs must explicitly declare whether they are an [INDEX], [OVERVIEW], or [REFERENCE].
If a file fails any directive, abort and fix it before proceeding.

## Purpose
Guidance for Claude-based coding agents contributing to this repository.

## Gates
Before editing code, verify the canonical owner docs for the feature area. Do not rely on abbreviated docs or summaries.

## Required reading
- `AGENTS.md`
- `docs/ARCHITECTURE.md`
- `docs/ai/runtime/AI-PIPELINE.md`
- `docs/operations/RUNTIME-OPERATIONS.md`
- `docs/TRADING-LIFECYCLE.md`
- `docs/EXECUTION-LIFECYCLE.md`
- `docs/DATABASE-SCHEMA.md`
- `docs/security/SECURITY-CONTRACTS.md`

## Working rule
If the behavior is not explicit in the owner docs, stop and ask for clarification rather than inventing implementation details.
