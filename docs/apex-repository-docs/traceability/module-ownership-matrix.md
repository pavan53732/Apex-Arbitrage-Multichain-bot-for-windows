---
metadata_schema_version: 1.0
document_id: DOC-0050
title: Domain Ownership Matrix
plane: Repository Operating Model
domain: Traceability
class: Index
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-repository-docs/traceability/module-ownership-matrix.md
related_concepts:
  - CONCEPT-0050
dependencies:
  - DOC-0003
  - DOC-0059
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Owner
owned_domains:
  - Traceability
type: INDEX
purpose: Defines exactly which domain owns every major concept in the repository. This is the definitive answer whenever an AI agent asks where a document belongs.
scope: All domains in both Repository Operating Model and Product Specification planes.
---

# Domain Ownership Matrix

## Purpose

This document is the authoritative source for which domain owns every major concept. It eliminates ambiguity about where new documents belong and prevents cross-domain specification overlap.

**Rule**: Every concept must have exactly one owning domain. If overlap is suspected, consult this matrix.

## Repository Operating Model Domains

| Domain | Owns | Does NOT Own | Concept ID |
| --- | --- | --- | --- |
| Agent System | Repository AI agent rules, profiles, skills, navigation | Product AI runtime behavior | CONCEPT-0001 |
| Governance | Repository governance policies, source-of-truth rules | Product feature governance | CONCEPT-0003 |
| Registries | Concept, Document, and Traceability Registries | Product data registries | CONCEPT-0006, CONCEPT-0007, CONCEPT-0008 |
| Standards | Documentation standards, coding standards, validation policy | Product configuration standards | CONCEPT-0052, CONCEPT-0053, CONCEPT-0054, CONCEPT-0065, CONCEPT-0066, CONCEPT-0067 |
| Documentation Lifecycle | Documentation map, lifecycle policies, review workflows | Product feature lifecycles | CONCEPT-0056, CONCEPT-0057, CONCEPT-0059 |
| Contribution | Contributing guides and collaboration expectations | Product user guides | CONCEPT-0062 |
| Traceability | Cross-reference index, ownership matrices | Product dependency graphs | CONCEPT-0008, CONCEPT-0049, CONCEPT-0050 |
| Validation | Local validation policy, quality gates | Product testing specs | CONCEPT-0004 |
| Workflows | Repository workflow descriptions | Remote automation, CI/CD | CONCEPT-0004 |

## Product Specification Domains

| Domain | Owns | Does NOT Own | Concept ID |
| --- | --- | --- | --- |
| AI | AI orchestration, pipeline, providers, memory, tools, safety, prompts, knowledge, learning, explainability | Runtime services, market data, execution policies | CONCEPT-0101, CONCEPT-0102, CONCEPT-0103, CONCEPT-0104, CONCEPT-0105, CONCEPT-0106, CONCEPT-0107, CONCEPT-0108, CONCEPT-0109, CONCEPT-0110, CONCEPT-0111, CONCEPT-0112, CONCEPT-0120, CONCEPT-0124, CONCEPT-0125, CONCEPT-0126, CONCEPT-0127, CONCEPT-0128, CONCEPT-0131 |
| Architecture | System architecture, component diagrams, dependency graph, project structure, ADRs | Runtime implementation details | CONCEPT-0078, CONCEPT-0079, CONCEPT-0080, CONCEPT-0081, CONCEPT-0082, CONCEPT-0083, CONCEPT-0084, CONCEPT-0085 |
| Runtime | Bootstrap sequence, orchestrator, resource manager, task scheduler, worker pool, service registry, concurrency model, service lifecycle, shutdown lifecycle, worker architecture, workspace manager | Product AI reasoning, market logic | CONCEPT-0086, CONCEPT-0087, CONCEPT-0088, CONCEPT-0089, CONCEPT-0090, CONCEPT-0091, CONCEPT-0092, CONCEPT-0093, CONCEPT-0095, CONCEPT-0096, CONCEPT-0097, CONCEPT-0098, CONCEPT-0099, CONCEPT-0100 |
| Execution | Trading engine, execution engine, risk engine, simulation engine, wallet management | Market discovery, operations monitoring | CONCEPT-0280, CONCEPT-0282, CONCEPT-0283, CONCEPT-0284, CONCEPT-0301 |
| Market | Market data, chain integration, DEX integration, routing, tokens, connectivity, opportunities | Execution, wallet management | CONCEPT-0302, CONCEPT-0303, CONCEPT-0304, CONCEPT-0305, CONCEPT-0309, CONCEPT-0317, CONCEPT-0323 |
| Operations | Monitoring, diagnostics, recovery, reliability, notifications | Execution engines, market logic | CONCEPT-0333, CONCEPT-0336, CONCEPT-0337, CONCEPT-0338, CONCEPT-0345 |
| Interfaces | APIs, IPC, events, adapters, message catalogs | Runtime internals, UI behavior | CONCEPT-0251, CONCEPT-0253, CONCEPT-0254, CONCEPT-0255, CONCEPT-0262 |
| Data | State management, persistence, registries, knowledge | Configuration, runtime services | CONCEPT-0278, CONCEPT-0279, CONCEPT-0287, CONCEPT-0288, CONCEPT-0289, CONCEPT-0350, CONCEPT-0351 |
| Configuration | Feature flags, core configuration, registries configuration | Product data schemas | CONCEPT-0352, CONCEPT-0353, CONCEPT-0354, CONCEPT-0355 |
| Dashboard | Dashboard layout, runtime, widgets, workspaces | UI component behavior, plugin UI | CONCEPT-0213, CONCEPT-0214, CONCEPT-0215, CONCEPT-0216, CONCEPT-0217 |
| Deployment | Windows deployment, build/release, code signing, versioning, app builder guides | Security secrets, configuration features | CONCEPT-0219, CONCEPT-0221, CONCEPT-0222, CONCEPT-0223, CONCEPT-0224, CONCEPT-0225 |
| Security | Permission model, security contracts, secret lifecycle, trust boundaries | Execution policy, AI reasoning | CONCEPT-0226, CONCEPT-0227, CONCEPT-0228, CONCEPT-0230, CONCEPT-0231 |
| Testing | Testing framework, test case registry, testing guide, backtesting | Product execution testing | CONCEPT-0232 |
| Plugins | Plugin system, lifecycle, sandbox contract, SDK, marketplace | Product AI plugin orchestration | CONCEPT-0244, CONCEPT-0245, CONCEPT-0246, CONCEPT-0247, CONCEPT-0249, CONCEPT-0250 |
| Windows | Windows app architecture, desktop, network resilience, notification integration, security integration, service integration | Deployment packaging, UI behavior | CONCEPT-0237, CONCEPT-0238, CONCEPT-0239, CONCEPT-0240, CONCEPT-0241, CONCEPT-0242 |

## How to Use This Matrix

1. **Before creating a document**: Find the concept in this matrix. The Owns column tells you where it belongs.
2. **When in doubt**: If a concept spans domains, it belongs to the domain listed as owning the primary concept. Cross-domain references are allowed via traceability.
3. **Conflict resolution**: If two domains claim ownership, escalate to REBUILD-SYSTEM-SPECIFICATION.md for canonical resolution.

## Related Documents
- [Concept Registry](../registries/CONCEPT-REGISTRY.md)
- [Document Registry](../registries/DOCUMENT-REGISTRY.md)
- [REBUILD-SYSTEM-SPECIFICATION.md](../../../REBUILD-SYSTEM-SPECIFICATION.md)
