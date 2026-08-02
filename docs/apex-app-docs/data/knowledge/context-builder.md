---
metadata_schema_version: 1.0
document_id: DOC-0270
title: Context Builder
plane: Product Specification
domain: Data
class: Reference
authority: Canonical
status: Active
owner: UI Team
version: 1.1.0
canonical_source: docs/apex-app-docs/data/knowledge/context-builder.md
related_concepts:
  - CONCEPT-0270
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Data
type: REFERENCE
purpose: Context Builder documentation.
scope: Reference documentation.
---

# Context Builder

## Document type
Document type: [CONTRACT]

## Purpose
Defines the component that assembles structured context before every AI request.

## Pipeline
Memory -> Knowledge Graph -> Current Market -> User Settings -> Runtime State -> Decision History -> Prompt Builder -> AI Gateway.

## Context sources
- **Memory** — curated memory scopes relevant to the task.
- **Knowledge graph** — canonical knowledge and registries.
- **Current market** — live prices, pools, and chain state.
- **User settings** — profile and preferences.
- **Runtime state** — health, workers, providers, and balances.
- **Decision history** — recent decisions and outcomes.
- **Windows signals** — tray, service, and notification state where relevant.

## Assembly rules
- Sources are collected in pipeline order and merged into a single structured context.
- Context is trimmed to fit the model window; oversize context is compressed, not silently truncated.
- Context is validated before dispatch; a request with invalid or stale runtime state is refused.
- Only context required for the task is injected; sensitive data is redacted per policy.

## State machine
```mermaid
stateDiagram-v2
  [*] --> COLLECTING
  COLLECTING --> MERGING
  MERGING --> TRIMMING
  TRIMMING --> VALIDATING
  VALIDATING --> DISPATCHING
  DISPATCHING --> [*]
```

## Failure modes
Missing memory, oversize context, invalid source, stale runtime state.

## Recovery
Compress context, fall back to curated memory, or refuse dispatch if policy fails.

## Cross-references
- `../../ai/runtime/ai-pipeline.md`
- `../../ai/memory/ai-memory-system.md`
- `./knowledge-graph.md`
- `../../ai/runtime/ai-gateway.md`

## Operational Contract

Defines how user, market, wallet, and runtime context are assembled for downstream reasoning. The context builder composes sources; each source remains owned by its canonical owner.

## Example
A prompt includes live balances, active positions, and current chain state, trimmed to the model window before dispatch.
