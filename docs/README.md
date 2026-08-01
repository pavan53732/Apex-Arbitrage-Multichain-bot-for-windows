---
metadata_schema_version: 1.0
document_id: DOC-0058
title: Documentation Index
plane: Repository Operating Model
domain: Documentation Lifecycle
class: Index
authority: Derived
status: Active
owner: Runtime Team
version: 1.1.0
canonical_source: docs/apex-repository-docs/documentation-lifecycle/documentation-map.md
related_concepts:
  - CONCEPT-0059
dependencies:
  - DOC-0059
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-01
concept_role: Index
owned_domains: []
type: OVERVIEW
purpose: Readme documentation.
scope: Reference documentation.
---

# Documentation Index

This index is the stable navigation surface for the repository knowledge system. Identity is controlled by the registries, not by folder paths.

`docs/` contains exactly two permanent documentation roots: `docs/apex-app-docs/` (the APEX application specification) and `docs/apex-repository-docs/` (repository governance and operating documentation). No third permanent documentation root is permitted.

| Folder | Purpose |
| --- | --- |
| [docs/apex-app-docs](./apex-app-docs/README.md) | Software-system specification for the Apex Windows arbitrage application. |
| [docs/apex-repository-docs](./apex-repository-docs/README.md) | How humans and AI agents govern and maintain repository knowledge. |
| [docs/apex-app-docs/ai](./apex-app-docs/ai/README.md) | Product AI runtime, memory, planning, providers, tools, reasoning, safety, and cost behavior. |
| [docs/apex-app-docs/architecture](./apex-app-docs/architecture/README.md) | System boundaries, kernel, structure, and cross-system architecture. |
| [docs/apex-app-docs/configuration](./apex-app-docs/configuration/README.md) | Configuration profiles, feature flags, capability registries, and config reference behavior. |
| [docs/apex-app-docs/dashboard](./apex-app-docs/dashboard/README.md) | Dashboard runtime, layout, widgets, and workspace behavior. |
| [docs/apex-app-docs/data](./apex-app-docs/data/README.md) | Database, state, storage, cache, data governance, and knowledge graph behavior. |
| [docs/apex-app-docs/deployment](./apex-app-docs/deployment/README.md) | Windows app deployment, packaging, signing, versioning, install/update behavior. |
| [docs/apex-app-docs/execution](./apex-app-docs/execution/README.md) | Trading, execution, risk, orders, wallets, portfolios, and strategy behavior. |
| [docs/apex-app-docs/interfaces](./apex-app-docs/interfaces/README.md) | APIs, IPC, events, provider adapters, message catalogs, and contracts. |
| [docs/apex-app-docs/market](./apex-app-docs/market/README.md) | Market data, chain/DEX/token/oracle registries, routing, liquidity, gas, MEV, opportunities. |
| [docs/apex-app-docs/operations](./apex-app-docs/operations/README.md) | Runtime operations, monitoring, diagnostics, recovery, failures, health, and troubleshooting. |
| [docs/apex-app-docs/performance](./apex-app-docs/performance/README.md) | Performance budgets, SLOs, capacity, threading, timing, and resource targets. |
| [docs/apex-app-docs/plugins](./apex-app-docs/plugins/README.md) | Plugin SDK, lifecycle, sandbox, marketplace, and app-builder plugin behavior. |
| [docs/apex-app-docs/reference](./apex-app-docs/reference/README.md) | Product reference material, roadmaps, changelog, glossary, and limitations. |
| [docs/apex-app-docs/runtime](./apex-app-docs/runtime/README.md) | Runtime lifecycle, orchestration, services, workers, scheduling, and platform internals. |
| [docs/apex-app-docs/security](./apex-app-docs/security/README.md) | Security contracts, permissions, secrets, trust boundaries, and signing/security behavior. |
| [docs/apex-app-docs/state-machines](./apex-app-docs/state-machines/README.md) | Product state machines and state-machine indexes. |
| [docs/apex-app-docs/testing](./apex-app-docs/testing/README.md) | Product testing strategy, test registries, backtesting, and local validation behavior. |
| [docs/apex-app-docs/ui](./apex-app-docs/ui/README.md) | Design system, UX guidelines, user flows, user guide, and UI components. |
| [docs/apex-app-docs/windows](./apex-app-docs/windows/README.md) | Windows desktop, service, network, notification, security integration, and platform behavior. |
| [docs/apex-repository-docs/agent-system](./apex-repository-docs/agent-system/README.md) | Rules and guidance for repository-facing coding and documentation agents. |
| [docs/apex-repository-docs/agent-system/agent-profiles](./apex-repository-docs/agent-system/agent-profiles/README.md) | Agent-specific guidance derived from the root agent contract. |
| [docs/apex-repository-docs/contribution](./apex-repository-docs/contribution/README.md) | Contributor-facing repository guidance. |
| [docs/apex-repository-docs/documentation-lifecycle](./apex-repository-docs/documentation-lifecycle/README.md) | Lifecycle, index, and review workflow for durable documentation. |
| [docs/apex-repository-docs/governance](./apex-repository-docs/governance/README.md) | Repository-level governance and source-of-truth conventions. |
| [docs/apex-repository-docs/registries](./apex-repository-docs/registries/README.md) | Canonical repository knowledge registries. |
| [docs/apex-repository-docs/standards](./apex-repository-docs/standards/README.md) | Repository standards for canonical sources, dependencies, and contributions. |
| [docs/apex-repository-docs/traceability](./apex-repository-docs/traceability/README.md) | Document relationships, cross-reference indexes, and ownership matrices. |
| [docs/apex-repository-docs/validation](./apex-repository-docs/validation/README.md) | Local-first validation expectations and quality gates. |
| [docs/apex-repository-docs/workflows](./apex-repository-docs/workflows/README.md) | Durable repository workflows executed locally by contributors or agents. |
