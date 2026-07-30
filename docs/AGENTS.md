---
last_updated: 2026-07-29
type: REFERENCE
owner: AI Team
status: Canonical
version: 1.0.0
purpose: AI agent documentation overview.
scope: Agent reference.
canonical_source: docs/AGENTS.md
---

# Agents


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
- `SKILLS.md`
- `ai/runtime/AI-PIPELINE.md`
- `USER-FLOWS.md`


## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Ownership boundary
- This document is navigation only. It does not own AI execution, orchestration, or lifecycle behavior.
- Authority belongs to `ai/runtime/AI-PIPELINE.md`, `ORCHESTRATOR.md`, and `ai/reference/AI-AGENT-SPECIFICATION.md`.
