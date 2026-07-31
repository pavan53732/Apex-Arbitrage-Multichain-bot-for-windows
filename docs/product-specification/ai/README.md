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

Product AI specifications and references that describe behavior inside the application.

## What does not belong here

Repository AI agent operating rules, market/execution product behavior, plugin SDK behavior, and UI/dashboard behavior unless the document is explicitly about product AI integration.

## Canonical owner map

| Subdomain | Concept ID | Canonical owner | README |
| --- | --- | --- | --- |
| orchestration | CONCEPT-0102 | [AI Orchestration](./orchestration/ai-orchestration.md) | [AI Orchestration README](./orchestration/README.md) |
| runtime | CONCEPT-0103 | [AI Pipeline](./runtime/ai-pipeline.md) | [AI Runtime README](./runtime/README.md) |
| providers | CONCEPT-0104 | [AI Provider Manager](./providers/ai-provider-manager.md) | [AI Providers README](./providers/README.md) |
| memory | CONCEPT-0120 | [AI Memory System](./memory/ai-memory-system.md) | [AI Memory README](./memory/README.md) |
| tools | CONCEPT-0107 | [AI Tool Invocation Contract](./tools/ai-tool-invocation-contract.md) | [AI Tools README](./tools/README.md) |
| safety | CONCEPT-0105 | [AI Safety Boundary](./safety/ai-safety-boundary.md) | [AI Safety README](./safety/README.md) |
| prompts | CONCEPT-0109 | [Prompt Engineering](./prompts/prompt-engineering.md) | [AI Prompts README](./prompts/README.md) |
| knowledge | CONCEPT-0111 | [AI Knowledge Index](./knowledge/ai-knowledge-index.md) | [AI Knowledge README](./knowledge/README.md) |
| learning | CONCEPT-0128 | [Learning Pipeline](./learning/learning-pipeline.md) | [AI Learning README](./learning/README.md) |
| explainability | CONCEPT-0126 | [Explainability](./explainability/explainability.md) | [AI Explainability README](./explainability/README.md) |

## Document classes expected

- Index
- Specification
- Reference
- Policy where AI behavior constraints are owned

## Relationship to adjacent domains

AI consumes configuration, data, interfaces, operations, execution, and security documents but must not redefine those domain owners. Repository-agent guidance belongs under Repository Operating Model / Agent System.

## Subdomain navigation

### orchestration

- Concept: `CONCEPT-0102`
- Canonical owner: [AI Orchestration](./orchestration/ai-orchestration.md)
- Folder README: [AI Orchestration README](./orchestration/README.md)

Documents:

- [AI Agent Specification](./orchestration/ai-agent-specification.md) — Specification
- [AI Consensus](./orchestration/ai-consensus.md) — Reference
- [AI Orchestration](./orchestration/ai-orchestration.md) — Specification
- [AI Planner](./orchestration/ai-planner.md) — Reference
- [AI Reflection](./orchestration/ai-reflection.md) — Reference

### runtime

- Concept: `CONCEPT-0103`
- Canonical owner: [AI Pipeline](./runtime/ai-pipeline.md)
- Folder README: [AI Runtime README](./runtime/README.md)

Documents:

- [AI Context Window Management](./runtime/ai-context-window-management.md) — Reference
- [AI Gateway](./runtime/ai-gateway.md) — Reference
- [AI Pipeline](./runtime/ai-pipeline.md) — Specification

### providers

- Concept: `CONCEPT-0104`
- Canonical owner: [AI Provider Manager](./providers/ai-provider-manager.md)
- Folder README: [AI Providers README](./providers/README.md)

Documents:

- [AI Capability Matrix](./providers/ai-capability-matrix.md) — Reference
- [AI Cost Management](./providers/ai-cost-management.md) — Reference
- [AI Provider Manager](./providers/ai-provider-manager.md) — Specification
- [AI Settings](./providers/ai-settings.md) — Reference
- [Cloud AI Integration](./providers/cloud-ai-integration.md) — Reference
- [Model Capability Negotiation](./providers/model-capability-negotiation.md) — Reference

### memory

- Concept: `CONCEPT-0120`
- Canonical owner: [AI Memory System](./memory/ai-memory-system.md)
- Folder README: [AI Memory README](./memory/README.md)

Documents:

- [AI Memory System](./memory/ai-memory-system.md) — Reference
- [Context Priority Matrix](./memory/context-priority-matrix.md) — Specification
- [Memory Lifecycle](./memory/memory-lifecycle.md) — Reference

### tools

- Concept: `CONCEPT-0107`
- Canonical owner: [AI Tool Invocation Contract](./tools/ai-tool-invocation-contract.md)
- Folder README: [AI Tools README](./tools/README.md)

Documents:

- [AI Tool Invocation Contract](./tools/ai-tool-invocation-contract.md) — Specification
- [AI Tools](./tools/ai-tools.md) — Reference

### safety

- Concept: `CONCEPT-0105`
- Canonical owner: [AI Safety Boundary](./safety/ai-safety-boundary.md)
- Folder README: [AI Safety README](./safety/README.md)

Documents:

- [AI Reasoning Policy](./safety/ai-reasoning-policy.md) — Policy
- [AI Safety Boundary](./safety/ai-safety-boundary.md) — Specification

### prompts

- Concept: `CONCEPT-0109`
- Canonical owner: [Prompt Engineering](./prompts/prompt-engineering.md)
- Folder README: [AI Prompts README](./prompts/README.md)

Documents:

- [Prompt Engineering](./prompts/prompt-engineering.md) — Specification
- [Prompt Lifecycle](./prompts/prompt-lifecycle.md) — Reference

### knowledge

- Concept: `CONCEPT-0111`
- Canonical owner: [AI Knowledge Index](./knowledge/ai-knowledge-index.md)
- Folder README: [AI Knowledge README](./knowledge/README.md)

Documents:

- [AI Knowledge Index](./knowledge/ai-knowledge-index.md) — Index

### learning

- Concept: `CONCEPT-0128`
- Canonical owner: [Learning Pipeline](./learning/learning-pipeline.md)
- Folder README: [AI Learning README](./learning/README.md)

Documents:

- [Learning Pipeline](./learning/learning-pipeline.md) — Reference

### explainability

- Concept: `CONCEPT-0126`
- Canonical owner: [Explainability](./explainability/explainability.md)
- Folder README: [AI Explainability README](./explainability/README.md)

Documents:

- [Explainability](./explainability/explainability.md) — Reference
- [Governance Explainability](./explainability/governance-explainability.md) — Specification

## Before adding a document here

- Identify the active Concept ID in the Concept Registry before creating a new document.
- Update an existing canonical owner instead of creating a duplicate specification when the concept already exists.
- Place the document in the narrowest matching subdomain folder.
- Assign a stable Document ID only if the document is new permanent repository knowledge.
- Add or update metadata, registries, README navigation, and cross-references in the same change.
- Run local metadata, registry, traceability, link, stale-path, empty-folder, and repository hygiene validation before committing.
- Do not add generated documentation, CI/CD files, GitHub Actions, temporary reports, or repository automation.
