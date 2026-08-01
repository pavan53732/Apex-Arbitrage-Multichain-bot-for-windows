---
metadata_schema_version: 1.0
document_id: DOC-0130
title: Model Capability Negotiation
plane: Product Specification
domain: AI
class: Reference
authority: Reference
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/ai/providers/ai-provider-manager.md
related_concepts:
  - CONCEPT-0104
dependencies:
  - DOC-0104
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Reference
owned_domains: []
type: REFERENCE
purpose: Model Capability Negotiation documentation.
scope: Reference documentation.
---

# Model Capability Negotiation

## Document type
This document is an overview, reference, or index as noted below.

# Model Capability Negotiation

## Purpose
Defines automatic capability detection and configuration for chosen AI providers.

## Capabilities
Streaming, Reasoning, Vision, Tool Calling, JSON, Embeddings, Long Context.

## State machine
```mermaid
stateDiagram-v2
  [*] --> DETECTING
  DETECTING --> MATCHING
  MATCHING --> CONFIGURING
  CONFIGURING --> VERIFIED
  VERIFIED --> ACTIVE
```

## Failure modes
Capability mismatch, false positive, provider regression.

## Recovery
Downgrade features, switch providers, or reject unsupported capability use.

## Cross-references
- `./ai-provider-manager.md`
- `../runtime/ai-gateway.md`
- `../../interfaces/adapters/interface-provider-adapter.md`

## Governance Rules
Defines how model requirements, tool support, limits, and fallback choices are negotiated.

## Example
A smaller model is selected when the task exceeds the preferred context budget.
