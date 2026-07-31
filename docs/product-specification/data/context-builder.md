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
version: 1.0.0
canonical_source: docs/product-specification/data/context-builder.md
related_concepts:
  - CONCEPT-0270
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Data
type: REFERENCE
purpose: Context Builder documentation.
scope: Reference documentation.
---

# Context Builder

## Document type
This document is an overview, reference, or index as noted below.

# Context Builder

## Purpose
Defines the component that assembles structured context before every AI request.

## Pipeline
Memory -> Knowledge Graph -> Current Market -> User Settings -> Runtime State -> Decision History -> Prompt Builder -> AI Gateway.

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
- `../ai/runtime/ai-pipeline.md`
- `../ai/memory/ai-memory-system.md`
- `./knowledge-graph.md`
- `../ai/runtime/ai-gateway.md`

## Operational Contract
Defines how user, market, wallet, and runtime context are assembled for downstream reasoning.

## Example
A prompt includes live balances, active positions, and current chain state.

## Context sources
- Must define which runtime, market, wallet, and Windows signals feed model context.
