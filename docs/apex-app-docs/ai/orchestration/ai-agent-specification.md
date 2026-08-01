---
metadata_schema_version: 1.0
document_id: DOC-0101
title: AI Agent Specification
plane: Product Specification
domain: AI
class: Specification
authority: Canonical
status: Active
owner: AI Team
version: 1.0.0
canonical_source: docs/apex-app-docs/ai/orchestration/ai-agent-specification.md
related_concepts:
  - CONCEPT-0101
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - AI
type: SPECIFICATION
purpose: Ai Agent Specification documentation.
scope: Reference documentation.
---

# Ai Agent Specification


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

# AI Agent Specification

## Purpose
Defines message and tool schemas for AI agents.

## Support Doc
This document provides schemas for agent messages and tool calls. Lifecycle rules are defined in `./ai-orchestration.md`.

## Cross-references
- `./ai-orchestration.md`
- `../runtime/ai-pipeline.md`

## Interface Contract
Each agent defines purpose, inputs, outputs, tools, memory access, metrics, and lifecycle expectations.

## Example
The planner agent decomposes goals, orders dependencies, and emits a structured execution plan.

## Agent rules
- Define agent identity, goals, tools, permissions, and output expectations.
- Define failure and handoff behavior.
