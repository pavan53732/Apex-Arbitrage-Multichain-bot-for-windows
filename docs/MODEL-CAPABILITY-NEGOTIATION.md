---
last_updated: 2026-07-29
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Model Capability Negotiation documentation.
scope: Reference documentation.
canonical_source: docs/MODEL-CAPABILITY-NEGOTIATION.md
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
- `AI-PROVIDER-MANAGER.md`
- `AI-GATEWAY.md`
- `INTERFACE-PROVIDER-ADAPTER.md`

## Governance Rules
Defines how model requirements, tool support, limits, and fallback choices are negotiated.

## Example
A smaller model is selected when the task exceeds the preferred context budget.
