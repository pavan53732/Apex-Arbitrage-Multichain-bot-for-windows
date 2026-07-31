---
metadata_schema_version: 1.0
document_id: DOC-0059
title: Documentation Map
plane: Repository Operating Model
domain: Documentation Lifecycle
class: Index
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/repository-operating-model/documentation-lifecycle/documentation-map.md
related_concepts:
  - CONCEPT-0059
dependencies: []
consumers:
  - DOC-0058
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Documentation Lifecycle
type: INDEX
purpose: Documentation Map documentation.
scope: Reference documentation.
---

# Documentation Map

This map is regenerated from current document metadata and concept-centric registry ownership. Stable identity is controlled by the registries, not by folder paths.

## Registry Summary

| Field | Value |
| --- | --- |
| Documents | 327 |
| Active semantic concepts | 220 |
| Superseded concept aliases retained | 176 |
| Traceability relationships | 620 |

## Domain Map

| Plane | Domain | Documents | Active Concept Owners |
| --- | --- | --- | --- |
| Product Specification | AI | 40 | [AI State Machine](../../product-specification/ai/ai-state-machine.md), [Explainability](../../product-specification/ai/explainability/explainability.md), [Governance Explainability](../../product-specification/ai/explainability/governance-explainability.md), [AI Knowledge Index](../../product-specification/ai/knowledge/ai-knowledge-index.md), [Learning Pipeline](../../product-specification/ai/learning/learning-pipeline.md), [AI Memory System](../../product-specification/ai/memory/ai-memory-system.md) |
| Product Specification | Architecture | 21 | [ADR 0001 Provider Abstraction](../../adr/0001-provider-abstraction.md), [ADR 0002 Event Driven Kernel](../../adr/0002-event-driven-kernel.md), [ADR 0003 Plugin First Architecture](../../adr/0003-plugin-first-architecture.md), [ADR 0004 Polygon First](../../adr/0004-polygon-first.md), [ADR 0005 AI Memory](../../adr/0005-ai-memory.md), [ADR 0006 Runtime Governance](../../adr/0006-runtime-governance.md) |
| Product Specification | Configuration | 10 | [Configuration](../../product-specification/configuration/configuration.md), [Contract Management](../../product-specification/configuration/contract-management.md), [Contract Registry](../../product-specification/configuration/contract-registry.md), [Feature Flag Governance And Rollout Matrix](../../product-specification/configuration/feature-flag-governance-and-rollout-matrix.md), [Feature Flags](../../product-specification/configuration/feature-flags.md), [System Capability Registry](../../product-specification/configuration/system-capability-registry.md) |
| Product Specification | Dashboard | 6 | [Dashboard Layout](../../product-specification/dashboard/dashboard-layout.md), [Dashboard Runtime](../../product-specification/dashboard/dashboard-runtime.md), [Dashboard Widgets](../../product-specification/dashboard/dashboard-widgets.md), [Dashboard Workspaces](../../product-specification/dashboard/dashboard-workspaces.md), [UI Dashboard Spec](../../product-specification/dashboard/ui-dashboard-spec.md) |
| Product Specification | Data | 13 | [Cache Manager](../../product-specification/data/cache-manager.md), [Context Builder](../../product-specification/data/context-builder.md), [Data Flow](../../product-specification/data/data-flow.md), [Data Governance](../../product-specification/data/data-governance.md), [Data Ownership](../../product-specification/data/data-ownership.md), [Database Schema](../../product-specification/data/database-schema.md) |
| Product Specification | Deployment | 7 | [App Builder Deployment Guide](../../product-specification/deployment/app-builder-deployment-guide.md), [Build Release](../../product-specification/deployment/build-release.md), [Code Signing](../../product-specification/deployment/code-signing.md), [Deployment](../../product-specification/deployment/deployment.md), [Versioning](../../product-specification/deployment/versioning.md), [Windows Deployment](../../product-specification/deployment/windows-deployment.md) |
| Product Specification | Execution | 24 | [Arbitrage Window Manager](../../product-specification/execution/arbitrage-window-manager.md), [Asset Management](../../product-specification/execution/asset-management.md), [Cross Exchange Arbitrage](../../product-specification/execution/cross-exchange-arbitrage.md), [Decision Engine](../../product-specification/execution/decision-engine.md), [Decision Log](../../product-specification/execution/decision-log.md), [Execution Engine](../../product-specification/execution/execution-engine.md) |
| Product Specification | Interfaces | 16 | [API Contracts](../../product-specification/interfaces/api-contracts.md), [Domain Model](../../product-specification/interfaces/domain-model.md), [Event Bus](../../product-specification/interfaces/event-bus.md), [Interface Agent Message](../../product-specification/interfaces/interface-agent-message.md), [Interface Catalog](../../product-specification/interfaces/interface-catalog.md), [Interface Notification Channel](../../product-specification/interfaces/interface-notification-channel.md) |
| Product Specification | Market | 31 | [Chain Command Center](../../product-specification/market/chain-command-center.md), [Chain Integration](../../product-specification/market/chain-integration.md), [Chain Intelligence](../../product-specification/market/chain-intelligence.md), [Chain Registry](../../product-specification/market/chain-registry.md), [Chain Rotation](../../product-specification/market/chain-rotation.md), [DEX Integration](../../product-specification/market/dex-integration.md) |
| Product Specification | Operations | 24 | [Arbitrage Monitoring](../../product-specification/operations/arbitrage-monitoring.md), [Troubleshooting](../../product-specification/operations/diagnostics/troubleshooting.md), [Diagnostics](../../product-specification/operations/diagnostics.md), [Enterprise Operations](../../product-specification/operations/enterprise-operations.md), [Error Catalog](../../product-specification/operations/error-catalog.md), [Error Handling and Logging](../../product-specification/operations/error-handling-and-logging.md) |
| Product Specification | Performance | 7 | [Capacity Planning](../../product-specification/performance/capacity-planning.md), [Performance SLOs](../../product-specification/performance/performance-slos.md), [Resource Budget Specification](../../product-specification/performance/resource-budget-specification.md), [Threading Model](../../product-specification/performance/threading-model.md), [Timing Specification](../../product-specification/performance/timing-specification.md) |
| Product Specification | Plugins | 7 | [App Builder Plugin System](../../product-specification/plugins/app-builder-plugin-system.md), [App Builder Workflow](../../product-specification/plugins/app-builder-workflow.md), [Plugin Lifecycle](../../product-specification/plugins/plugin-lifecycle.md), [Plugin Marketplace](../../product-specification/plugins/plugin-marketplace.md), [Plugin Sandbox Contract](../../product-specification/plugins/plugin-sandbox-contract.md), [Plugin SDK](../../product-specification/plugins/plugin-sdk.md) |
| Product Specification | Reference | 10 | [Changelog](../../product-specification/reference/changelog.md), [Enhancement Roadmap](../../product-specification/reference/enhancement-roadmap.md), [FAQ](../../product-specification/reference/faq.md), [Feature Matrix](../../product-specification/reference/feature-matrix.md), [Glossary](../../product-specification/reference/glossary.md), [Implementation Roadmap](../../product-specification/reference/implementation-roadmap.md) |
| Product Specification | Runtime | 15 | [Bootstrap Sequence](../../product-specification/runtime/bootstrap-sequence.md), [Concurrency Model](../../product-specification/runtime/concurrency-model.md), [Orchestrator](../../product-specification/runtime/orchestrator.md), [Resource Manager](../../product-specification/runtime/resource-manager.md), [Runtime Flow Lifecycle](../../product-specification/runtime/runtime-flow-lifecycle.md), [Service Lifecycle](../../product-specification/runtime/service-lifecycle.md) |
| Product Specification | Security | 6 | [Permission Model](../../product-specification/security/permission-model.md), [Secret Lifecycle](../../product-specification/security/secret-lifecycle.md), [Security Contracts](../../product-specification/security/security-contracts.md), [Security](../../product-specification/security/security.md), [Trust Boundaries](../../product-specification/security/trust-boundaries.md) |
| Product Specification | State Machines | 7 | [Engine State Machine](../../product-specification/state-machines/engine-state-machine.md), [Execution State Machine](../../product-specification/state-machines/execution-state-machine.md), [Plugin State Machine](../../product-specification/state-machines/plugin-state-machine.md), [Service State Machine](../../product-specification/state-machines/service-state-machine.md), [System Wide State Machine Index](../../product-specification/state-machines/state-machine-index.md), [Worker State Machine](../../product-specification/state-machines/worker-state-machine.md) |
| Product Specification | Testing | 5 | [Testing](../../product-specification/testing/testing.md) |
| Product Specification | UI | 7 | [Design System](../../product-specification/ui/design-system.md), [Designer Protocols](../../product-specification/ui/designer-protocols.md), [UI Component Spec](../../product-specification/ui/ui-component-spec.md), [User Flows](../../product-specification/ui/user-flows.md), [User Guide](../../product-specification/ui/user-guide.md), [UX Guidelines](../../product-specification/ui/ux-guidelines.md) |
| Product Specification | Windows | 7 | [Windows App Architecture](../../product-specification/windows/windows-app-architecture.md), [Windows Desktop](../../product-specification/windows/windows-desktop.md), [Windows Network Resilience](../../product-specification/windows/windows-network-resilience.md), [Windows Notification Integration](../../product-specification/windows/windows-notification-integration.md), [Windows Security Integration](../../product-specification/windows/windows-security-integration.md), [Windows Service Integration](../../product-specification/windows/windows-service-integration.md) |
| Repository Operating Model | Agent System | 33 | [AGENTS](../../../AGENTS.md), [Agent Rules](../../../AGENTS_RULES.md), [Agent Profiles README](../agent-system/agent-profiles/README.md) |
| Repository Operating Model | Contribution | 2 | [Contributing](../contribution/contributing.md) |
| Repository Operating Model | Documentation Lifecycle | 5 | [Documentation Lifecycle](./documentation-lifecycle.md), [Documentation Map](./documentation-map.md), [Documentation Status Review Workflow](./documentation-status-review-workflow.md) |
| Repository Operating Model | Governance | 10 | [Repository README](../../../README.md), [REBUILD-SYSTEM-SPECIFICATION](../../../REBUILD-SYSTEM-SPECIFICATION.md), [REPOSITORY-EXECUTION-MODEL](../../../REPOSITORY-EXECUTION-MODEL.md), [Governance Overview](../governance/governance-overview.md) |
| Repository Operating Model | Registries | 4 | [Concept Registry](../registries/CONCEPT-REGISTRY.md), [Document Registry](../registries/DOCUMENT-REGISTRY.md), [Traceability Registry](../registries/TRACEABILITY-REGISTRY.md) |
| Repository Operating Model | Standards | 4 | [Canonical Source Rules](../standards/canonical-source-rules.md), [Coding Standards](../standards/coding-standards.md), [Dependency Authority Rules](../standards/dependency-authority-rules.md) |
| Repository Operating Model | Traceability | 4 | [Cross Reference Index](../traceability/cross-reference-index.md), [Module Ownership Matrix](../traceability/module-ownership-matrix.md) |
| Repository Operating Model | Validation | 1 |  |
| Repository Operating Model | Workflows | 1 |  |

## Registry Control

- [Concept Registry](../registries/CONCEPT-REGISTRY.md) owns concept identity and aliases.
- [Document Registry](../registries/DOCUMENT-REGISTRY.md) owns document identity and concept roles.
- [Traceability Registry](../registries/TRACEABILITY-REGISTRY.md) owns semantic relationships.
