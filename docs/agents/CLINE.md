---
last_updated: 2026-07-29
type: REFERENCE
owner: AI Team
status: Canonical
version: 1.0.0
purpose: CLINE AI tool documentation.
scope: CLINE reference.
canonical_source: CLINE.md
---

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
- `docs/ARCHITECTURE.md`
- `docs/ai/runtime/AI-PIPELINE.md`
- `docs/ai/providers/AI-PROVIDER-MANAGER.md`
- `docs/MODEL-CAPABILITY-NEGOTIATION.md`
- `docs/RUNTIME-OPERATIONS.md`
- `docs/security/SECURITY-CONTRACTS.md`

## Working rule
Only implement what the authoritative docs already define.
