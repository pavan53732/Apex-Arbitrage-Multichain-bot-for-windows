---
metadata_schema_version: 1.0
document_id: DOC-0123
title: AI Settings
plane: Product Specification
domain: AI
class: Reference
authority: Canonical
status: Active
owner: AI Team
version: 1.0.0
canonical_source: docs/product-specification/ai/ai-settings.md
related_concepts:
  - CONCEPT-0123
dependencies:
  - DOC-0103
  - DOC-0104
  - DOC-0109
  - DOC-0115
  - DOC-0118
  - DOC-0125
  - DOC-0130
  - DOC-0381
consumers:
  - DOC-0049
  - DOC-0109
  - DOC-0114
  - DOC-0115
  - DOC-0118
  - DOC-0125
  - DOC-0386
  - DOC-0395
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: Ai Settings documentation.
scope: Reference documentation.
---

# Ai Settings

## Document type
This document is an overview, reference, or index as noted below.

# AI Settings

## Purpose
Defines user-facing AI configuration, provider selection, fallback ordering, and cost controls.

## Policy
- Production AI uses cloud providers with paid API keys only.
- Local LLM inference is not supported in the production configuration.
- Provider enablement, ordering, and cost caps must match `./ai-pipeline.md` and `./cloud-ai-integration.md`.

## Cross-references
- `./ai-pipeline.md`
- `./cloud-ai-integration.md`
- `../configuration/configuration.md`
- `./ai-capability-matrix.md`
- `./prompt-engineering.md`
- `./ai-cost-management.md`

## Governance Rules
Defines AI provider selection, model preferences, temperature, max tokens, streaming, vision, reasoning, JSON, embeddings, and save/test actions.

## Example
A balanced profile uses reasoning with a smaller context window and JSON output enabled.

## Validation
- Validate provider enablement against `./ai-provider-manager.md`.
- Validate capability requirements against `./model-capability-negotiation.md`.
- Reject profiles that omit required provider, model, or cost settings.

## Lifecycle
- Settings are loaded at startup, validated before use, and revalidated on profile change.
- Provider lifecycle details remain owned by `./ai-provider-manager.md`.

## Windows AI settings
- Must define local model path and per-user profile isolation on Windows.

## Required details
- Define local inference and per-user isolation.

## Windows AI settings
- Define local model paths, GPU fallback, and per-user profile isolation.
- Define proxy-aware cloud model access.

## AI settings
- Define local inference, cloud fallback, proxy handling, and per-user profile isolation.
- Define how settings are validated before use.
