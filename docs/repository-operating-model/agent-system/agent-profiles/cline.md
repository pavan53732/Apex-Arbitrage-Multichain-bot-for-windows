---
metadata_schema_version: 1.0
document_id: DOC-0024
title: Cline Agent Profile
plane: Repository Operating Model
domain: Agent System
class: Reference
authority: Derived
status: Active
owner: AI Team
version: 1.0.0
canonical_source: docs/repository-operating-model/agent-system/agent-profiles/README.md
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
purpose: CLINE AI tool documentation.
scope: CLINE reference.
---

# Cline


## AI Guard
Before creating or modifying ANY markdown file, verify it complies with the 5 Prime Directives.
- Lifecycle docs must explicitly define initial state, terminal state, allowed transitions, forbidden transitions, recovery transitions, and failure transitions.
- Interface docs must explicitly define producer, consumer, payload, schema, validation, versioning, and failure behavior.
- Owner docs must explicitly state what they own and do not own.
- Cross-cutting docs must defer to canonical owners.
- Short docs must explicitly declare whether they are an [INDEX], [OVERVIEW], or [REFERENCE].
If a file fails any directive, abort and fix it before proceeding.

## Purpose
Guidance for Cline-based coding agents contributing to this repository.

## Gates
- Start with the owner docs, not with summaries.
- Follow the documented authority boundaries exactly.
- Treat ambiguous behavior as unresolved.

## Required reading
- `../../../../AGENTS.md`
- `../../../product-specification/architecture/architecture.md`
- `../../../product-specification/ai/runtime/ai-pipeline.md`
- `../../../product-specification/ai/providers/ai-provider-manager.md`
- `../../../product-specification/ai/providers/model-capability-negotiation.md`
- `../../../product-specification/operations/reliability/runtime-operations.md`
- `../../../product-specification/security/security-contracts.md`

## Working rule
Only implement what the authoritative docs already define.
