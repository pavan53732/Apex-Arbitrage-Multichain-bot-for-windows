# Gemini


## AI Guard
Before creating or modifying ANY markdown file, verify it complies with the 5 Prime Directives.
- Lifecycle docs must explicitly define initial state, terminal state, allowed transitions, forbidden transitions, recovery transitions, and failure transitions.
- Interface docs must explicitly define producer, consumer, payload, schema, validation, versioning, and failure behavior.
- Owner docs must explicitly state what they own and do not own.
- Cross-cutting docs must defer to canonical owners.
- Short docs must explicitly declare whether they are an [INDEX], [OVERVIEW], or [REFERENCE].
If a file fails any directive, abort and fix it before proceeding.

## Purpose
Guidance for Gemini-based coding agents contributing to this repository.

## Gates
- Use the authoritative docs as the source of truth.
- Treat navigation docs as support only.
- Do not synthesize missing behavior from assumptions.

## Required reading
- `AGENTS.md`
- `ARCHITECTURE.md`
- `AI-PIPELINE.md`
- `AI-PROVIDER-MANAGER.md`
- `MODEL-CAPABILITY-NEGOTIATION.md`
- `TRADING-LIFECYCLE.md`
- `EXECUTION-LIFECYCLE.md`
- `RUNTIME-OPERATIONS.md`

## Working rule
If a contract, payload, or lifecycle transition is not written down, do not infer it.
