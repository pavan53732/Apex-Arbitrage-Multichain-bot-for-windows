---
metadata_schema_version: 1.0
document_id: DOC-0115
title: AI Capability Matrix
plane: Product Specification
domain: AI
class: Reference
authority: Canonical
status: Active
owner: AI Team
version: 1.0.0
canonical_source: docs/product-specification/ai/ai-capability-matrix.md
related_concepts:
  - CONCEPT-0115
dependencies:
  - DOC-0103
  - DOC-0123
  - DOC-0125
  - DOC-0381
consumers:
  - DOC-0049
  - DOC-0059
  - DOC-0114
  - DOC-0123
  - DOC-0125
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: Ai Capability Matrix documentation.
scope: Reference documentation.
---

# Ai Capability Matrix

## Document type
This document is an overview, reference, or index as noted below.

# AI Capability Matrix

## Purpose
Defines which AI providers and models support which capabilities.

## Scope
This matrix is descriptive and used by AI routing, provider selection, and configuration.

## Matrix
| Capability | OpenAI | Anthropic | Gemini | OpenRouter | Custom |
|---|---|---|---|---|---|
| Streaming | Supported | Supported | Supported | Provider-dependent | Provider-dependent |
| Reasoning | Supported | Supported | Supported | Provider-dependent | Provider-dependent |
| Vision | Supported | Supported | Supported | Provider-dependent | Provider-dependent |
| JSON mode | Supported | Supported | Supported | Provider-dependent | Provider-dependent |
| Tool calling | Supported | Supported | Supported | Provider-dependent | Provider-dependent |
| Embeddings | Supported | Supported | Supported | Provider-dependent | Provider-dependent |
| Speech | Supported | Limited | Limited | Provider-dependent | Provider-dependent |

## Cross-references
- `./ai-pipeline.md`
- `./cloud-ai-integration.md`
- `./ai-settings.md`
- `../configuration/configuration.md`

## Orchestration boundary
This document governs capability, memory, prompt, or cost definitions. For runtime orchestration and pipeline sequencing, see `./ai-pipeline.md`.

## Governance Rules
Defines detected AI capabilities, provider support mapping, and compatibility decisions.

## Example
A provider supports reasoning but not vision, so the gateway disables vision calls.

## Capability rules
- Define capability names, supported models, constraints, and fallback choices.
- Define how unsupported capabilities are rejected.
