---
metadata_schema_version: 1.0
document_id: DOC-0406
title: AI Providers README
plane: Product Specification
domain: AI
class: Index
authority: Derived
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
last_updated: 2026-07-31
concept_role: Index
owned_domains: []
---

# AI Providers

## Purpose and scope

AI provider management, model capability, cost, and cloud AI integration documentation.

## What belongs here

Provider manager, settings, capability, cost, and cloud integration documents.

## What does not belong here

Agent orchestration, prompt design, and tool invocation contracts.

## Expected document classes

- Index
- Specification
- Reference
- Policy where the subdomain owns AI behavioral constraints

## Canonical boundaries

This folder indexes AI documents in this subdomain and defers behavior to the canonical owner document identified by metadata and registry entries.

## Documents

| Document | Class |
| --- | --- |
| [AI Capability Matrix](ai-capability-matrix.md) | Reference |
| [AI Cost Management](ai-cost-management.md) | Reference |
| [AI Provider Manager](ai-provider-manager.md) | Specification |
| [AI Settings](ai-settings.md) | Reference |
| [Cloud AI Integration](cloud-ai-integration.md) | Reference |
| [Model Capability Negotiation](model-capability-negotiation.md) | Reference |

## Adjacent domains

Adjacent AI subdomains may reference these documents, but they must not redefine this folder's canonical ownership boundaries.
