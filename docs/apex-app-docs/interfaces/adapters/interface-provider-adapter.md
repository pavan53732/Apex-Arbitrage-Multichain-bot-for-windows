---
metadata_schema_version: 1.0
document_id: DOC-0262
title: Interface Provider Adapter
plane: Product Specification
domain: Interfaces
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/interfaces/adapters/interface-provider-adapter.md
related_concepts:
  - CONCEPT-0262
dependencies: []
consumers:
  - DOC-0425
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Interfaces
type: REFERENCE
purpose: Interface Provider Adapter documentation.
scope: Reference documentation.
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
- `../../ai/providers/ai-provider-manager.md`
- `../../ai/runtime/ai-gateway.md`
- `../../ai/runtime/ai-pipeline.md`

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
