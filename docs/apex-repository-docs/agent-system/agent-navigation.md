---
metadata_schema_version: 1.0
document_id: DOC-0046
title: Agent Navigation
plane: Repository Operating Model
domain: Agent System
class: Reference
authority: Derived
status: Active
owner: AI Team
version: 1.0.0
canonical_source: AGENTS.md
related_concepts:
  - CONCEPT-0001
dependencies:
  - DOC-0001
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Reference
owned_domains: []
type: REFERENCE
purpose: AI agent navigation overview.
scope: Agent reference.
---

# Agent Navigation


## AI Guard
Before creating or modifying ANY markdown file, verify it complies with the 5 Prime Directives.
- Lifecycle docs must explicitly define initial state, terminal state, allowed transitions, forbidden transitions, recovery transitions, and failure transitions.
- Interface docs must explicitly define producer, consumer, payload, schema, validation, versioning, and failure behavior.
- Owner docs must explicitly state what they own and do not own.
- Cross-cutting docs must defer to canonical owners.
- Short docs must explicitly declare whether they are an [INDEX], [OVERVIEW], or [REFERENCE].
If a file fails any directive, abort and fix it before proceeding.

## Purpose
Provides navigation to the authoritative documentation set.

## Cross-references
- `./skills.md`
- `../../apex-app-docs/ai/runtime/ai-pipeline.md`
- `../../apex-app-docs/ui/user-flows.md`


## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Ownership boundary
- This document is navigation only. It does not own AI execution, orchestration, or lifecycle behavior.
- Authority belongs to `../../apex-app-docs/ai/runtime/ai-pipeline.md`, `../../apex-app-docs/runtime/orchestrator.md`, and `../../apex-app-docs/ai/orchestration/ai-agent-specification.md`.
