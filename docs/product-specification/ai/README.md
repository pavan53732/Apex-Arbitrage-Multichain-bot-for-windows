---
metadata_schema_version: 1.0
document_id: DOC-0114
title: AI README
plane: Product Specification
domain: AI
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/ai/runtime/ai-pipeline.md
related_concepts:
  - CONCEPT-0103
dependencies:
  - DOC-0103
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# AI

## Purpose and scope

Product AI runtime, orchestration, providers, memory, tools, safety, prompts, knowledge, learning, and explainability documentation.

## What belongs here

AI product specifications and references. Repository AI and coding-agent instructions belong under Repository Operating Model / Agent System.

## What does not belong here

Repository agent governance, product execution engines, market data, dashboard behavior, or plugin SDK behavior unless the document is explicitly about AI integration.

## Subdomains

| Subdomain | README | Canonical owner |
| --- | --- | --- |
| explainability | [AI Explainability README](explainability/README.md) | [Explainability](./explainability/explainability.md) |
| knowledge | [AI Knowledge README](knowledge/README.md) | [Ai Knowledge Index](./knowledge/ai-knowledge-index.md) |
| learning | [AI Learning README](learning/README.md) | [Learning Pipeline](./learning/learning-pipeline.md) |
| memory | [AI Memory README](memory/README.md) | [Ai Memory System](./memory/ai-memory-system.md) |
| orchestration | [AI Orchestration README](orchestration/README.md) | [Ai Orchestration](./orchestration/ai-orchestration.md) |
| prompts | [AI Prompts README](prompts/README.md) | [Prompt Engineering](./prompts/prompt-engineering.md) |
| providers | [AI Providers README](providers/README.md) | [Ai Provider Manager](./providers/ai-provider-manager.md) |
| runtime | [AI Runtime README](runtime/README.md) | [Ai Pipeline](./runtime/ai-pipeline.md) |
| safety | [AI Safety README](safety/README.md) | [Ai Safety Boundary](./safety/ai-safety-boundary.md) |
| tools | [AI Tools README](tools/README.md) | [Ai Tool Invocation Contract](./tools/ai-tool-invocation-contract.md) |
| state-machine | [AI State Machine](./ai-state-machine.md) | AI State Machine |

## Document creation rule

Before adding an AI document, identify the active concept owner in the Concept Registry and place the document in the matching subdomain. Do not create duplicate AI ownership documents.
