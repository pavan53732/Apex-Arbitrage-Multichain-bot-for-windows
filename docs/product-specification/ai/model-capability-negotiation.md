---
metadata_schema_version: 1.0
document_id: DOC-0130
title: Model Capability Negotiation
plane: Product Specification
domain: AI
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/ai/model-capability-negotiation.md
related_concepts:
  - CONCEPT-0130
dependencies:
  - DOC-0104
  - DOC-0119
  - DOC-0262
consumers:
  - DOC-0024
  - DOC-0028
  - DOC-0049
  - DOC-0114
  - DOC-0119
  - DOC-0123
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
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
- `./ai-gateway.md`
- `../interfaces/interface-provider-adapter.md`

## Governance Rules
Defines how model requirements, tool support, limits, and fallback choices are negotiated.

## Example
A smaller model is selected when the task exceeds the preferred context budget.
