---
metadata_schema_version: 1.0
document_id: DOC-0034
title: Opencode Agent Profile
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
purpose: OPENCODE AI tool documentation.
scope: OPENCODE reference.
---

# OpenCode


## AI Guard
Before creating or modifying ANY markdown file, verify it complies with the 5 Prime Directives.
- Lifecycle docs must explicitly define initial state, terminal state, allowed transitions, forbidden transitions, recovery transitions, and failure transitions.
- Interface docs must explicitly define producer, consumer, payload, schema, validation, versioning, and failure behavior.
- Owner docs must explicitly state what they own and do not own.
- Cross-cutting docs must defer to canonical owners.
- Short docs must explicitly declare whether they are an [INDEX], [OVERVIEW], or [REFERENCE].
If a file fails any directive, abort and fix it before proceeding.

## Purpose
Guidance for OpenCode-based coding agents contributing to this repository.

## Gates
- Read the owner docs before making changes.
- Prefer explicit lifecycle and interface contracts over overview docs.
- Keep architecture, runtime, and trading boundaries separate.

## Required reading
- `../../../../AGENTS.md`
- `../../../apex-app-docs/architecture/architecture.md`
- `../../../apex-app-docs/operations/reliability/runtime-operations.md`
- `../../../apex-app-docs/ai/runtime/ai-pipeline.md`
- `../../../apex-app-docs/data/state/cache-manager.md`
- `../../../apex-app-docs/data/persistence/database-schema.md`
- `../../../apex-app-docs/security/security-contracts.md`

## Working rule
If the repo does not explicitly define the behavior, do not guess.
