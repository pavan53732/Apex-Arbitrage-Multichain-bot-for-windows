---
metadata_schema_version: 1.0
document_id: DOC-0030
title: Google Code Assistant Agent Profile
plane: Repository Operating Model
domain: Agent System
class: Reference
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/repository-operating-model/agent-system/agent-profiles/google-code-assistant.md
related_concepts:
  - CONCEPT-0030
dependencies:
  - DOC-0001
  - DOC-0079
  - DOC-0103
  - DOC-0227
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
purpose: GOOGLE-CODE-ASSISTANT documentation.
scope: Reference documentation.
---

# GOOGLE CODE ASSISTANT


## AI Guard
Before creating or modifying ANY markdown file, verify it complies with the 5 Prime Directives.
- Lifecycle docs must explicitly define initial state, terminal state, allowed transitions, forbidden transitions, recovery transitions, and failure transitions.
- Interface docs must explicitly define producer, consumer, payload, schema, validation, versioning, and failure behavior.
- Owner docs must explicitly state what they own and do not own.
- Cross-cutting docs must defer to canonical owners.
- Short docs must explicitly declare whether they are an [INDEX], [OVERVIEW], or [REFERENCE].
If a file fails any directive, abort and fix it before proceeding.

## Purpose
Guidance for GOOGLE CODE ASSISTANT coding agents contributing to this repository.

## Gates
- Read the canonical owner docs before making changes.
- Do not infer behavior that is not explicitly written in the authoritative docs.
- Treat navigation docs as support only.
- Stop when ownership, payloads, transitions, or recovery are ambiguous.

## Required reading
- `../../../../AGENTS.md`
- `../../../product-specification/architecture/architecture.md`
- `../../../product-specification/ai/ai-pipeline.md`
- `../../../product-specification/operations/runtime-operations.md`
- `../../../product-specification/execution/trading-lifecycle.md`
- `../../../product-specification/execution/execution-lifecycle.md`
- `../../../product-specification/data/database-schema.md`
- `../../../product-specification/security/security-contracts.md`

## Working rule
If the repository does not define the behavior, do not guess.
