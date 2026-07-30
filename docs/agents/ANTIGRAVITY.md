---
last_updated: 2026-07-29
type: REFERENCE
owner: AI Team
status: Canonical
version: 1.0.0
purpose: ANTIGRAVITY AI tool documentation.
scope: ANTIGRAVITY reference.
canonical_source: ANTIGRAVITY.md
---

# Antigravity


## AI Guard
Before creating or modifying ANY markdown file, verify it complies with the 5 Prime Directives.
- Lifecycle docs must explicitly define initial state, terminal state, allowed transitions, forbidden transitions, recovery transitions, and failure transitions.
- Interface docs must explicitly define producer, consumer, payload, schema, validation, versioning, and failure behavior.
- Owner docs must explicitly state what they own and do not own.
- Cross-cutting docs must defer to canonical owners.
- Short docs must explicitly declare whether they are an [INDEX], [OVERVIEW], or [REFERENCE].
If a file fails any directive, abort and fix it before proceeding.

## Purpose
Guidance for Antigravity-based coding agents contributing to this repository.

## Gates
- Read the canonical docs for the subsystem you are changing.
- Never infer unlisted payloads, lifecycle states, or ownership boundaries.
- Confirm the implementation target before editing.

## Required reading
- `AGENTS.md`
- `docs/ARCHITECTURE.md`
- `docs/ai/runtime/AI-PIPELINE.md`
- `docs/operations/RUNTIME-OPERATIONS.md`
- `docs/TRADING-LIFECYCLE.md`
- `docs/EXECUTION-LIFECYCLE.md`
- `docs/DATABASE-SCHEMA.md`

## Working rule
If the owner doc is missing, the change is blocked until the contract exists.
