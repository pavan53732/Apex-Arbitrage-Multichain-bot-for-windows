---
last_updated: 2026-07-29
type: REFERENCE
owner: AI Team
status: Canonical
version: 1.0.0
purpose: KILO-CODE AI tool documentation.
scope: KILO-CODE reference.
canonical_source: KILO-CODE.md
---

# Kilo Code


## AI Guard
Before creating or modifying ANY markdown file, verify it complies with the 5 Prime Directives.
- Lifecycle docs must explicitly define initial state, terminal state, allowed transitions, forbidden transitions, recovery transitions, and failure transitions.
- Interface docs must explicitly define producer, consumer, payload, schema, validation, versioning, and failure behavior.
- Owner docs must explicitly state what they own and do not own.
- Cross-cutting docs must defer to canonical owners.
- Short docs must explicitly declare whether they are an [INDEX], [OVERVIEW], or [REFERENCE].
If a file fails any directive, abort and fix it before proceeding.

## Purpose
Guidance for Kilo Code-based coding agents contributing to this repository.

## Gates
- Use only canonical owner docs to decide behavior.
- Verify state machines, recovery, and interfaces before implementation.
- Do not expand scope beyond the documented contract.

## Required reading
- `AGENTS.md`
- `docs/ARCHITECTURE.md`
- `docs/TRADING-LIFECYCLE.md`
- `docs/EXECUTION-LIFECYCLE.md`
- `docs/TRANSACTION-LIFECYCLE.md`
- `docs/ORDER-MANAGEMENT.md`
- `docs/RUNTIME-OPERATIONS.md`

## Working rule
If two docs appear to disagree, stop and resolve the canonical owner before coding.
