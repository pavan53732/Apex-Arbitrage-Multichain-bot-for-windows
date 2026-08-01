---
metadata_schema_version: 1.0
document_id: DOC-0028
title: Gemini Agent Profile
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
purpose: GEMINI AI tool documentation.
scope: GEMINI reference.
---

# Gemini


## AI Guard
Before creating or modifying ANY markdown file, verify it complies with the 5 Prime Directives.
- Lifecycle docs must explicitly define initial state, terminal state, allowed transitions, forbidden transitions, recovery transitions, and failure transitions.
- Interface docs must explicitly define producer, consumer, payload, schema, validation, versioning, and failure behavior.
- Owner docs must explicitly state what they own and do not own.
- Cross-cutting docs must defer to canonical owners.
- Short docs must explicitly declare whether they are an [INDEX], [OVERVIEW], or [REFERENCE].
If a file fails any directive, abort and fix it before proceeding.

## Purpose
Guidance for Gemini-based coding agents contributing to this repository.

## Gates
- Use the authoritative docs as the source of truth.
- Treat navigation docs as support only.
- Do not synthesize missing behavior from assumptions.

## Required reading
- `../../../../AGENTS.md`
- `../../../apex-app-docs/architecture/architecture.md`
- `../../../apex-app-docs/ai/runtime/ai-pipeline.md`
- `../../../apex-app-docs/ai/providers/ai-provider-manager.md`
- `../../../apex-app-docs/ai/providers/model-capability-negotiation.md`
- `../../../apex-app-docs/execution/trading/trading-lifecycle.md`
- `../../../apex-app-docs/execution/transactions/execution-lifecycle.md`
- `../../../apex-app-docs/operations/reliability/runtime-operations.md`

## Working rule
If a contract, payload, or lifecycle transition is not written down, do not infer it.
