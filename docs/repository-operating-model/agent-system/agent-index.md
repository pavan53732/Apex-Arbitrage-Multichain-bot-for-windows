---
metadata_schema_version: 1.0
document_id: DOC-0017
title: Agent Index
plane: Repository Operating Model
domain: Agent System
class: Index
authority: Derived
status: Active
owner: Trading Team
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
last_updated: 2026-07-30
concept_role: Index
owned_domains: []
type: INDEX
purpose: Agent Index documentation.
scope: Reference documentation.
---

# Agent Index


## AI Guard
Before creating or modifying ANY markdown file, verify it complies with the 5 Prime Directives.
- Lifecycle docs must explicitly define initial state, terminal state, allowed transitions, forbidden transitions, recovery transitions, and failure transitions.
- Interface docs must explicitly define producer, consumer, payload, schema, validation, versioning, and failure behavior.
- Owner docs must explicitly state what they own and do not own.
- Cross-cutting docs must defer to canonical owners.
- Short docs must explicitly declare whether they are an [INDEX], [OVERVIEW], or [REFERENCE].
If a file fails any directive, abort and fix it before proceeding.

## Document type
This document is an overview, reference, or index as noted below.

# Agent Index

Agent-specific configuration files have been consolidated into [AGENTS.md](../../../AGENTS.md) (canonical) and [agent-profiles/](./agent-profiles/README.md) for agent-specific overrides.

## Rule
Use [AGENTS.md](../../../AGENTS.md) as the first stop for assistant-specific behavior. Use the canonical owner docs for actual implementation contracts.
