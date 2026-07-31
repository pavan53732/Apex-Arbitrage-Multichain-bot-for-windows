---
metadata_schema_version: 1.0
document_id: DOC-0021
title: Antigravity Agent Profile
plane: Repository Operating Model
domain: Agent System
class: Reference
authority: Derived
status: Active
owner: AI Team
version: 1.0.0
canonical_source: docs/repository-operating-model/agent-system/agent-profiles/antigravity.md
related_concepts:
  - CONCEPT-0021
dependencies:
  - DOC-0001
  - DOC-0079
  - DOC-0103
  - DOC-0266
  - DOC-0289
  - DOC-0298
  - DOC-0338
consumers:
  - DOC-0018
  - DOC-0049
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: ANTIGRAVITY AI tool documentation.
scope: ANTIGRAVITY reference.
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
- `../../../../AGENTS.md`
- `../../../product-specification/architecture/architecture.md`
- `../../../product-specification/ai/ai-pipeline.md`
- `../../../product-specification/operations/runtime-operations.md`
- `../../../product-specification/execution/trading-lifecycle.md`
- `../../../product-specification/execution/execution-lifecycle.md`
- `../../../product-specification/data/database-schema.md`

## Working rule
If the owner doc is missing, the change is blocked until the contract exists.
