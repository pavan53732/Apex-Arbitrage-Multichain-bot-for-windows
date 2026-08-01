---
metadata_schema_version: 1.0
document_id: DOC-0023
title: Claude Agent Profile
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
purpose: CLAUDE AI tool documentation.
scope: CLAUDE reference.
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
- `../../../../AGENTS.md`
- `../../../apex-app-docs/architecture/architecture.md`
- `../../../apex-app-docs/ai/runtime/ai-pipeline.md`
- `../../../apex-app-docs/operations/reliability/runtime-operations.md`
- `../../../apex-app-docs/execution/trading/trading-lifecycle.md`
- `../../../apex-app-docs/execution/transactions/execution-lifecycle.md`
- `../../../apex-app-docs/data/persistence/database-schema.md`
- `../../../apex-app-docs/security/security-contracts.md`

## Working rule
If the behavior is not explicit in the owner docs, stop and ask for clarification rather than inventing implementation details.
