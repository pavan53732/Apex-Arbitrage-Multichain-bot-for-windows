---
metadata_schema_version: 1.0
document_id: DOC-0117
title: AI Context Window Management
plane: Product Specification
domain: AI
class: Reference
authority: Reference
status: Active
owner: AI Team
version: 1.0.0
canonical_source: docs/product-specification/ai/ai-pipeline.md
related_concepts:
  - CONCEPT-0103
dependencies:
  - DOC-0103
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Reference
owned_domains: []
type: REFERENCE
purpose: Ai Context Window Management documentation.
scope: Reference documentation.
---

# Ai Context Window Management

## Document type
This document is an overview, reference, or index as noted below.

# AI Context Window Management

## Purpose
Defines context compression, rolling summaries, token budgeting, memory retrieval, and chunk selection.

## State machine
```mermaid
stateDiagram-v2
  [*] --> COLLECTING
  COLLECTING --> SUMMARIZING
  SUMMARIZING --> BUDGETING
  BUDGETING --> CHUNKING
  CHUNKING --> DISPATCHING
```

## Failure modes
Context overflow, stale summary, missing retrieval, token budget breach.

## Recovery
Compress, trim, retrieve alternate memory, or refuse request.

## Cross-references
- `./ai-pipeline.md`
- `./ai-memory-system.md`
- `../data/context-builder.md`
- `../../historical/traceability-matrix.md`

## Governance Rules
Defines token budgeting, compression, rolling summaries, chunk selection, and retrieval prioritization.

## Example
Long market history is compressed before dispatching a prompt to the AI provider.

## Context rules
- Define what enters the AI context window, what is summarized, and what is excluded.
- Define token budget and retention behavior.
