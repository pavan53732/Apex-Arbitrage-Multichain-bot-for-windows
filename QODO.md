# QODO


## AI Guard
Before creating or modifying ANY markdown file, verify it complies with the 5 Prime Directives.
- Lifecycle docs must explicitly define initial state, terminal state, allowed transitions, forbidden transitions, recovery transitions, and failure transitions.
- Interface docs must explicitly define producer, consumer, payload, schema, validation, versioning, and failure behavior.
- Owner docs must explicitly state what they own and do not own.
- Cross-cutting docs must defer to canonical owners.
- Short docs must explicitly declare whether they are an [INDEX], [OVERVIEW], or [REFERENCE].
If a file fails any directive, abort and fix it before proceeding.

## Purpose
Guidance for QODO-based coding agents contributing to this repository.

## Gates
- Read the canonical owner docs before making changes.
- Do not infer behavior that is not explicitly written in the authoritative docs.
- Treat navigation docs as support only.
- Stop when ownership, payloads, transitions, or recovery are ambiguous.

## Required reading
- `AGENTS.md`
- `ARCHITECTURE.md`
- `AI-PIPELINE.md`
- `RUNTIME-OPERATIONS.md`
- `TRADING-LIFECYCLE.md`
- `EXECUTION-LIFECYCLE.md`
- `DATABASE-SCHEMA.md`
- `SECURITY-CONTRACTS.md`

## Working rule
If the repository does not define the behavior, do not guess.
