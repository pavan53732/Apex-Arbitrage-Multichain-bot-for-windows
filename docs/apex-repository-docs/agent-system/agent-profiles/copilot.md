---
metadata_schema_version: 1.0
document_id: DOC-0026
title: Copilot Agent Profile
plane: Repository Operating Model
domain: Agent System
class: Reference
authority: Derived
status: Active
owner: AI Team
version: 1.0.0
canonical_source: docs/apex-repository-docs/agent-system/agent-profiles/README.md
related_concepts:
  - CONCEPT-0018
dependencies:
  - DOC-0018
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Reference
owned_domains: []
type: REFERENCE
purpose: COPILOT AI tool documentation.
scope: COPILOT reference.
---

# COPILOT


## AI Guard
Before creating or modifying ANY markdown file, verify it complies with the 5 Prime Directives.
- Lifecycle docs must explicitly define initial state, terminal state, allowed transitions, forbidden transitions, recovery transitions, and failure transitions.
- Interface docs must explicitly define producer, consumer, payload, schema, validation, versioning, and failure behavior.
- Owner docs must explicitly state what they own and do not own.
- Cross-cutting docs must defer to canonical owners.
- Short docs must explicitly declare whether they are an [INDEX], [OVERVIEW], or [REFERENCE].
If a file fails any directive, abort and fix it before proceeding.

## Purpose
Guidance for COPILOT-based coding agents contributing to this repository.

## Gates
- Read the canonical owner docs before making changes.
- Do not infer behavior that is not explicitly written in the authoritative docs.
- Treat navigation docs as support only.
- Stop when ownership, payloads, transitions, or recovery are ambiguous.

## Required reading
- `../../../../AGENTS.md`
- `../../../apex-app-docs/architecture/architecture.md`
- `../../../apex-app-docs/ai/runtime/ai-pipeline.md`
- `../../../apex-app-docs/operations/reliability/runtime-operations.md`
- `../../../apex-app-docs/execution/trading/trading-lifecycle.md`
- `../../../apex-app-docs/execution/transactions/execution-lifecycle.md`
- `../../../apex-app-docs/data/persistence/database-schema.md`
- `../../../apex-app-docs/security/security-contracts.md`

## Working rule
If the repository does not define the behavior, do not guess.
