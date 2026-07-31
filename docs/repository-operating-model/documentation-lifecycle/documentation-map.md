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
| Documents | 353 |
| Active semantic concepts | 220 |
| Superseded concept aliases retained | 176 |
| Traceability relationships | 672 |

## Domain Map

| Plane | Domain | Documents | Active Concept Owners |
| --- | --- | --- | --- |
| Product Specification | AI | 40 | [AI State Machine](../../product-specification/ai/ai-state-machine.md), [Explainability](../../product-specification/ai/explainability/explainability.md), [Governance Explainability](../../product-specification/ai/explainability/governance-explainability.md), [AI Knowledge Index](../../product-specification/ai/knowledge/ai-knowledge-index.md), [Learning Pipeline](../../product-specification/ai/learning/learning-pipeline.md), [AI Memory System](../../product-specification/ai/memory/ai-memory-system.md) |
| Product Specification | Architecture | 21 | [ADR 0001 Provider Abstraction](../../adr/0001-provider-abstraction.md), [ADR 0002 Event Driven Kernel](../../adr/0002-event-driven-kernel.md), [ADR 0003 Plugin First Architecture](../../adr/0003-plugin-first-architecture.md), [ADR 0004 Polygon First](../../adr/0004-polygon-first.md), [ADR 0005 AI Memory](../../adr/0005-ai-memory.md), [ADR 0006 Runtime Governance](../../adr/0006-runtime-governance.md) |
| Product Specification | Configuration | 13 | [Configuration](../../product-specification/configuration/core/configuration.md), [Feature Flag Governance And Rollout Matrix](../../product-specification/configuration/features/feature-flag-governance-and-rollout-matrix.md), [Feature Flags](../../product-specification/configuration/features/feature-flags.md), [Contract Management](../../product-specification/configuration/registries/contract-management.md), [Contract Registry](../../product-specification/configuration/registries/contract-registry.md), [System Capability Registry](../../product-specification/configuration/registries/system-capability-registry.md) |
| Product Specification | Dashboard | 6 | [Dashboard Layout](../../product-specification/dashboard/dashboard-layout.md), [Dashboard Runtime](../../product-specification/dashboard/dashboard-runtime.md), [Dashboard Widgets](../../product-specification/dashboard/dashboard-widgets.md), [Dashboard Workspaces](../../product-specification/dashboard/dashboard-workspaces.md), [UI Dashboard Spec](../../product-specification/dashboard/ui-dashboard-spec.md) |
| Product Specification | Data | 17 | [Context Builder](../../product-specification/data/knowledge/context-builder.md), [Data Flow](../../product-specification/data/knowledge/data-flow.md), [Data Governance](../../product-specification/data/knowledge/data-governance.md), [Data Ownership](../../product-specification/data/knowledge/data-ownership.md), [Knowledge Graph](../../product-specification/data/knowledge/knowledge-graph.md), [Database Schema](../../product-specification/data/persistence/database-schema.md) |
| Product Specification | Deployment | 7 | [App Builder Deployment Guide](../../product-specification/deployment/app-builder-deployment-guide.md), [Build Release](../../product-specification/deployment/build-release.md), [Code Signing](../../product-specification/deployment/code-signing.md), [Deployment](../../product-specification/deployment/deployment.md), [Versioning](../../product-specification/deployment/versioning.md), [Windows Deployment](../../product-specification/deployment/windows-deployment.md) |
| Product Specification | Execution | 29 | [Decision Log](../../product-specification/execution/decision-log.md), [Decision Engine](../../product-specification/execution/risk-policy/decision-engine.md), [Policy Engine](../../product-specification/execution/risk-policy/policy-engine.md), [Risk Engine](../../product-specification/execution/risk-policy/risk-engine.md), [Simulation Engine](../../product-specification/execution/simulation/simulation-engine.md), [Arbitrage Window Manager](../../product-specification/execution/trading/arbitrage-window-manager.md) |
| Product Specification | Interfaces | 20 | [Interface Provider Adapter](../../product-specification/interfaces/adapters/interface-provider-adapter.md), [API Contracts](../../product-specification/interfaces/api/api-contracts.md), [Domain Model](../../product-specification/interfaces/api/domain-model.md), [Event Bus](../../product-specification/interfaces/events/event-bus.md), [IPC Protocol](../../product-specification/interfaces/ipc/ipc-protocol.md), [Interface Agent Message](../../product-specification/interfaces/messages/interface-agent-message.md) |
| Product Specification | Market | 38 | [Chain Command Center](../../product-specification/market/chains/chain-command-center.md), [Chain Integration](../../product-specification/market/chains/chain-integration.md), [Chain Intelligence](../../product-specification/market/chains/chain-intelligence.md), [Chain Registry](../registries/chain-registry.md), [Chain Rotation](../../product-specification/market/chains/chain-rotation.md), [RPC Manager](../../product-specification/market/connectivity/rpc-manager.md) |
| Product Specification | Operations | 27 | [Diagnostics](../../product-specification/operations/diagnostics/diagnostics.md), [Error Catalog](../../product-specification/operations/diagnostics/error-catalog.md), [Error Handling and Logging](../../product-specification/operations/diagnostics/error-handling-and-logging.md), [Troubleshooting](../../product-specification/operations/diagnostics/troubleshooting.md), [Arbitrage Monitoring](../../product-specification/operations/monitoring/arbitrage-monitoring.md), [Health Checks](../../product-specification/operations/monitoring/health-checks.md) |
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


## Registered Document Reachability

All registered document identities are reachable through this canonical documentation map. Detailed path and ownership metadata remains in the [Document Registry](../registries/DOCUMENT-REGISTRY.md).

- `DOC-0001`
- `DOC-0002`
- `DOC-0003`
- `DOC-0004`
- `DOC-0005`
- `DOC-0006`
- `DOC-0007`
- `DOC-0008`
- `DOC-0009`
- `DOC-0010`
- `DOC-0011`
- `DOC-0012`
- `DOC-0013`
- `DOC-0014`
- `DOC-0015`
- `DOC-0016`
- `DOC-0017`
- `DOC-0018`
- `DOC-0019`
- `DOC-0020`
- `DOC-0021`
- `DOC-0022`
- `DOC-0023`
- `DOC-0024`
- `DOC-0025`
- `DOC-0026`
- `DOC-0027`
- `DOC-0028`
- `DOC-0029`
- `DOC-0030`
- `DOC-0031`
- `DOC-0032`
- `DOC-0033`
- `DOC-0034`
- `DOC-0035`
- `DOC-0036`
- `DOC-0037`
- `DOC-0038`
- `DOC-0039`
- `DOC-0040`
- `DOC-0041`
- `DOC-0042`
- `DOC-0043`
- `DOC-0044`
- `DOC-0045`
- `DOC-0046`
- `DOC-0047`
- `DOC-0048`
- `DOC-0049`
- `DOC-0050`
- `DOC-0051`
- `DOC-0052`
- `DOC-0053`
- `DOC-0054`
- `DOC-0055`
- `DOC-0056`
- `DOC-0057`
- `DOC-0058`
- `DOC-0059`
- `DOC-0060`
- `DOC-0061`
- `DOC-0062`
- `DOC-0063`
- `DOC-0064`
- `DOC-0065`
- `DOC-0066`
- `DOC-0067`
- `DOC-0068`
- `DOC-0069`
- `DOC-0070`
- `DOC-0071`
- `DOC-0072`
- `DOC-0073`
- `DOC-0074`
- `DOC-0075`
- `DOC-0076`
- `DOC-0077`
- `DOC-0078`
- `DOC-0079`
- `DOC-0080`
- `DOC-0081`
- `DOC-0082`
- `DOC-0083`
- `DOC-0084`
- `DOC-0085`
- `DOC-0086`
- `DOC-0087`
- `DOC-0088`
- `DOC-0089`
- `DOC-0090`
- `DOC-0091`
- `DOC-0092`
- `DOC-0093`
- `DOC-0094`
- `DOC-0095`
- `DOC-0096`
- `DOC-0097`
- `DOC-0098`
- `DOC-0099`
- `DOC-0100`
- `DOC-0101`
- `DOC-0102`
- `DOC-0103`
- `DOC-0104`
- `DOC-0105`
- `DOC-0106`
- `DOC-0107`
- `DOC-0108`
- `DOC-0109`
- `DOC-0110`
- `DOC-0111`
- `DOC-0114`
- `DOC-0115`
- `DOC-0116`
- `DOC-0117`
- `DOC-0118`
- `DOC-0119`
- `DOC-0120`
- `DOC-0121`
- `DOC-0122`
- `DOC-0123`
- `DOC-0124`
- `DOC-0125`
- `DOC-0126`
- `DOC-0127`
- `DOC-0128`
- `DOC-0129`
- `DOC-0130`
- `DOC-0131`
- `DOC-0132`
- `DOC-0213`
- `DOC-0214`
- `DOC-0215`
- `DOC-0216`
- `DOC-0217`
- `DOC-0218`
- `DOC-0219`
- `DOC-0220`
- `DOC-0221`
- `DOC-0222`
- `DOC-0223`
- `DOC-0224`
- `DOC-0225`
- `DOC-0226`
- `DOC-0227`
- `DOC-0228`
- `DOC-0229`
- `DOC-0230`
- `DOC-0231`
- `DOC-0232`
- `DOC-0233`
- `DOC-0234`
- `DOC-0235`
- `DOC-0236`
- `DOC-0237`
- `DOC-0238`
- `DOC-0239`
- `DOC-0240`
- `DOC-0241`
- `DOC-0242`
- `DOC-0243`
- `DOC-0244`
- `DOC-0245`
- `DOC-0246`
- `DOC-0247`
- `DOC-0248`
- `DOC-0249`
- `DOC-0250`
- `DOC-0251`
- `DOC-0252`
- `DOC-0253`
- `DOC-0254`
- `DOC-0255`
- `DOC-0256`
- `DOC-0257`
- `DOC-0258`
- `DOC-0259`
- `DOC-0260`
- `DOC-0261`
- `DOC-0262`
- `DOC-0263`
- `DOC-0264`
- `DOC-0265`
- `DOC-0266`
- `DOC-0267`
- `DOC-0268`
- `DOC-0269`
- `DOC-0270`
- `DOC-0271`
- `DOC-0272`
- `DOC-0273`
- `DOC-0274`
- `DOC-0275`
- `DOC-0276`
- `DOC-0277`
- `DOC-0278`
- `DOC-0279`
- `DOC-0280`
- `DOC-0281`
- `DOC-0282`
- `DOC-0283`
- `DOC-0284`
- `DOC-0285`
- `DOC-0286`
- `DOC-0287`
- `DOC-0288`
- `DOC-0289`
- `DOC-0290`
- `DOC-0291`
- `DOC-0292`
- `DOC-0293`
- `DOC-0294`
- `DOC-0295`
- `DOC-0296`
- `DOC-0297`
- `DOC-0298`
- `DOC-0299`
- `DOC-0300`
- `DOC-0301`
- `DOC-0302`
- `DOC-0303`
- `DOC-0304`
- `DOC-0305`
- `DOC-0306`
- `DOC-0307`
- `DOC-0308`
- `DOC-0309`
- `DOC-0310`
- `DOC-0311`
- `DOC-0312`
- `DOC-0313`
- `DOC-0314`
- `DOC-0315`
- `DOC-0316`
- `DOC-0317`
- `DOC-0318`
- `DOC-0319`
- `DOC-0320`
- `DOC-0321`
- `DOC-0322`
- `DOC-0323`
- `DOC-0324`
- `DOC-0325`
- `DOC-0326`
- `DOC-0327`
- `DOC-0328`
- `DOC-0329`
- `DOC-0330`
- `DOC-0331`
- `DOC-0332`
- `DOC-0333`
- `DOC-0334`
- `DOC-0335`
- `DOC-0336`
- `DOC-0337`
- `DOC-0338`
- `DOC-0339`
- `DOC-0340`
- `DOC-0341`
- `DOC-0342`
- `DOC-0343`
- `DOC-0344`
- `DOC-0345`
- `DOC-0346`
- `DOC-0347`
- `DOC-0348`
- `DOC-0349`
- `DOC-0350`
- `DOC-0351`
- `DOC-0352`
- `DOC-0353`
- `DOC-0354`
- `DOC-0355`
- `DOC-0356`
- `DOC-0357`
- `DOC-0358`
- `DOC-0359`
- `DOC-0360`
- `DOC-0361`
- `DOC-0362`
- `DOC-0363`
- `DOC-0364`
- `DOC-0365`
- `DOC-0366`
- `DOC-0367`
- `DOC-0368`
- `DOC-0369`
- `DOC-0370`
- `DOC-0371`
- `DOC-0372`
- `DOC-0373`
- `DOC-0374`
- `DOC-0375`
- `DOC-0376`
- `DOC-0377`
- `DOC-0378`
- `DOC-0379`
- `DOC-0380`
- `DOC-0381`
- `DOC-0382`
- `DOC-0383`
- `DOC-0384`
- `DOC-0385`
- `DOC-0386`
- `DOC-0387`
- `DOC-0388`
- `DOC-0389`
- `DOC-0390`
- `DOC-0391`
- `DOC-0392`
- `DOC-0393`
- `DOC-0394`
- `DOC-0395`
- `DOC-0396`
- `DOC-0397`
- `DOC-0398`
- `DOC-0399`
- `DOC-0400`
- `DOC-0401`
- `DOC-0402`
- `DOC-0403`
- `DOC-0404`
- `DOC-0405`
- `DOC-0406`
- `DOC-0407`
- `DOC-0408`
- `DOC-0409`
- `DOC-0410`
- `DOC-0411`
- `DOC-0412`
- `DOC-0413`
- `DOC-0414`
- `DOC-0415`
- `DOC-0416`
- `DOC-0417`
- `DOC-0418`
- `DOC-0419`
- `DOC-0420`
- `DOC-0421`
- `DOC-0422`
- `DOC-0423`
- `DOC-0424`
- `DOC-0425`
- `DOC-0426`
- `DOC-0427`
- `DOC-0428`
- `DOC-0429`
- `DOC-0430`
- `DOC-0431`
- `DOC-0432`
- `DOC-0433`
- `DOC-0434`
- `DOC-0435`
