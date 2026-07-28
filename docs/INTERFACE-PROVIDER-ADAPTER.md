---
last_updated: 2026-07-29
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Interface Provider Adapter documentation.
scope: Reference documentation.
canonical_source: docs/INTERFACE-PROVIDER-ADAPTER.md
---

# Interface Provider Adapter

## Document type
This document is an overview, reference, or index as noted below.

# Interface: Provider Adapter

## Purpose
Defines provider adapter request and response contracts.

## Methods
- ListModels().
- Infer(prompt, opts).
- HealthCheck().
- Capabilities().

## Validation
- `inference_timeout_ms` must be between 100 and 30000.
- `prompt` must be non-empty.
- `model_id` must be non-empty.
- `capabilities` must include streaming, tool_calling, embeddings, and vision flags.

## Cross-references
- `AI-PROVIDER-MANAGER.md`
- `AI-GATEWAY.md`
- `AI-PIPELINE.md`

## Interface Contract
Defines provider adapter inputs, outputs, capability declarations, errors, and compatibility rules.

## Example
An OpenAI-compatible adapter exposes streaming, JSON, embeddings, and tool-calling capabilities.

## Required details
- Define model request, response, error, and resource limits.

## Interface model
- Producer: defined by the owning system.
- Consumer: defined by the owning system.
- Payload: defined by the owning system.
- Schema: defined by the owning system.
- Validation: defined by the owning system.
- Versioning: defined by the owning system.
- Failure behavior: defined by the owning system.
