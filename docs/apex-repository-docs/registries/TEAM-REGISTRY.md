---
metadata_schema_version: 1.0
document_id: DOC-0440
title: Team Registry
plane: Repository Operating Model
domain: Registries
class: Registry
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-repository-docs/registries/TEAM-REGISTRY.md
related_concepts:
  - CONCEPT-0440
dependencies: []
consumers:
  - DOC-0007
validator_coverage:
  - VAL-002
  - VAL-004
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Registries
registry_version: 1.0.0
registry_schema_version: 1.0
registry_model: team-identity
last_regenerated: 2026-08-02
---

# Team Registry

Stable team identity registry. Standardizes the `owner` field across all documents and validators.

## Registry Metadata

| Field | Value |
| --- | --- |
| Registry version | 1.0.0 |
| Registry schema version | 1.0 |
| Registry model | Team identity with domain ownership |
| Last regenerated | 2026-08-02 |
| Registered teams | 15 |

## Usage

The `TEAM-ID` value in this registry is the canonical value for the `owner` metadata field in all documents and for the Owner column in the Document Registry.

## Teams

| TEAM-ID | Team Name | Primary Domain(s) | Responsibility |
| --- | --- | --- | --- |
| TEAM-RUNTIME | Runtime Team | Governance, Registries, Standards, Validation, Workflows, Documentation Lifecycle, Contribution, Agent System, Traceability, Runtime, Interfaces, Reference, Market, Execution, Operations, Performance, Configuration, Data, State Machines, Plugins, Deployment | Repository operating model ownership, cross-cutting infrastructure, runtime architecture |
| TEAM-AI | AI Team | AI, Execution (Trade Explainer), Market (Chain Intelligence) | AI orchestration, memory, providers, safety, tools, prompts, explainability, learning, knowledge |
| TEAM-TRADING | Trading Team | Execution, Market | Trading engine, execution engine, risk/policy, simulation, chain integration, DEX integration, routing, market registries |
| TEAM-UI | UI Team | Dashboard, UI, Architecture (NFRs), Runtime (Workflow Builder), Execution (Wallet), Market (Liquidity) | Dashboard, UI components, user experience, design system, user flows |
| TEAM-ARCHITECTURE | Architecture Team | Architecture, Documentation Lifecycle, State Machines (Index) | Architecture specifications, ADR governance, end-to-end wiring, domain model |
| TEAM-SECURITY | Security Team | Security, Data (Ownership) | Security contracts, permission model, trust boundaries, secret lifecycle, data ownership |
| TEAM-CONFIG | Config Team | Configuration | Configuration profiles, feature flags, feature gates, contracts |
| TEAM-DATA | Data Team | Data | Database schema, persistence |
| TEAM-OPS | Ops Team | Operations | Diagnostics, monitoring, error handling, timing specification, capacity planning |
| TEAM-QUALITY | Quality Team | Testing | Testing strategy, testing guide |
| TEAM-PLUGIN | Plugin Team | Plugins, State Machines (Plugin) | Plugin SDK, plugin sandbox, plugin lifecycle, app builder |
| TEAM-WINDOWS | Windows Team | Windows, Deployment (Windows) | Windows desktop, service integration, notification, security, deployment |
| TEAM-EXECUTION | Execution Team | State Machines (Execution) | Execution state machine |
| TEAM-DEVOPS | DevOps Team | Plugins (App Builder Workflow) | App builder workflow, build/release |
| TEAM-DASHBOARD | Dashboard Team | Dashboard | Dashboard layout specification |

## Governance

- New teams must be registered here before being used as `owner` values.
- Team renaming requires updating all documents and the Document Registry.
- Deprecated teams should be marked as status "Inactive" but retained for history.
- Every document must have an `owner` that matches a TEAM-ID in this registry.
