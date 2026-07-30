---
last_updated: 2026-07-29
type: REFERENCE
owner: AI Team
status: Canonical
version: 1.0.0
purpose: Ai Capability Matrix documentation.
scope: Reference documentation.
canonical_source: docs/ai/reference/AI-CAPABILITY-MATRIX.md
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
- `ai/runtime/AI-PIPELINE.md`
- `CLOUD-AI-INTEGRATION.md`
- `ai/providers/AI-SETTINGS.md`
- `CONFIGURATION.md`

## Orchestration boundary
This document governs capability, memory, prompt, or cost definitions. For runtime orchestration and pipeline sequencing, see `ai/runtime/AI-PIPELINE.md`.

## Governance Rules
Defines detected AI capabilities, provider support mapping, and compatibility decisions.

## Example
A provider supports reasoning but not vision, so the gateway disables vision calls.

## Capability rules
- Define capability names, supported models, constraints, and fallback choices.
- Define how unsupported capabilities are rejected.
