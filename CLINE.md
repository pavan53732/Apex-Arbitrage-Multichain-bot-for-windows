# Cline


## AI Guard
Before creating or modifying ANY markdown file, verify it complies with the 5 Prime Directives.
- Lifecycle docs must explicitly define initial state, terminal state, allowed transitions, forbidden transitions, recovery transitions, and failure transitions.
- Interface docs must explicitly define producer, consumer, payload, schema, validation, versioning, and failure behavior.
- Owner docs must explicitly state what they own and do not own.
- Cross-cutting docs must defer to canonical owners.
- Short docs must explicitly declare whether they are an [INDEX], [OVERVIEW], or [REFERENCE].
If a file fails any directive, abort and fix it before proceeding.

## Purpose
Guidance for Cline-based coding agents contributing to this repository.

## Gates
- Start with the owner docs, not with summaries.
- Follow the documented authority boundaries exactly.
- Treat ambiguous behavior as unresolved.

## Required reading
- `AGENTS.md`
- `ARCHITECTURE.md`
- `AI-PIPELINE.md`
- `AI-PROVIDER-MANAGER.md`
- `MODEL-CAPABILITY-NEGOTIATION.md`
- `RUNTIME-OPERATIONS.md`
- `SECURITY-CONTRACTS.md`

## Working rule
Only implement what the authoritative docs already define.
