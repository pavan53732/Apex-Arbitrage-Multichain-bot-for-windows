---
metadata_schema_version: 1.0
document_id: DOC-0122
title: AI Reflection
plane: Product Specification
domain: AI
class: Reference
authority: Reference
status: Active
owner: AI Team
version: 1.0.0
canonical_source: docs/product-specification/ai/ai-orchestration.md
related_concepts:
  - CONCEPT-0102
dependencies:
  - DOC-0102
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Reference
owned_domains: []
type: REFERENCE
purpose: Ai Reflection documentation.
scope: Reference documentation.
---

# Ai Reflection

## Document type
This document is an overview, reference, or index as noted below.

# AI Reflection

## Purpose
Defines self-evaluation for response review, decision review, confidence assessment, error analysis, and prompt refinement.

## State machine
```mermaid
stateDiagram-v2
  [*] --> REVIEWING
  REVIEWING --> SCORING
  SCORING --> ANALYZING
  ANALYZING --> REFINING
  REFINING --> STORED
```

## Cross-references
- `./ai-orchestration.md`
- `./learning-pipeline.md`
- `./explainability.md`

## Operational Contract
Defines how responses, decisions, and prompts are reviewed for confidence, errors, and refinement.

## Example
A failed recommendation is analyzed and turned into a prompt refinement action.

## Required details
- Define reflection inputs and decision quality criteria.

## Reflection rules
- Define the inputs, scoring, and outcomes used for reflection.
- Tie reflections to trade quality and decision quality.

## Reflection rules
- Define inputs, scoring, and outputs for reflection on decisions.
- Tie reflection to trade and reasoning quality.
