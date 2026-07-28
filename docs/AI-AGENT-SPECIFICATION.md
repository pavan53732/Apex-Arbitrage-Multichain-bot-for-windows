---
last_updated: 2026-07-29
type: SPECIFICATION
owner: AI Team
status: Canonical
version: 1.0.0
purpose: Ai Agent Specification documentation.
scope: Reference documentation.
canonical_source: docs/AI-AGENT-SPECIFICATION.md
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
This document provides schemas for agent messages and tool calls. Lifecycle rules are defined in `AI-ORCHESTRATION.md`.

## Cross-references
- `AI-ORCHESTRATION.md`
- `AI-PIPELINE.md`

## Interface Contract
Each agent defines purpose, inputs, outputs, tools, memory access, metrics, and lifecycle expectations.

## Example
The planner agent decomposes goals, orders dependencies, and emits a structured execution plan.

## Agent rules
- Define agent identity, goals, tools, permissions, and output expectations.
- Define failure and handoff behavior.
