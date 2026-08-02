---
metadata_schema_version: 1.0
document_id: DOC-0217
title: UI Dashboard Spec
plane: Product Specification
domain: Dashboard
class: Specification
authority: Canonical
status: Active
owner: UI Team
version: 1.0.0
canonical_source: docs/apex-app-docs/dashboard/ui-dashboard-spec.md
related_concepts:
  - CONCEPT-0217
dependencies: []
consumers:
  - DOC-0218
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Dashboard
type: SPECIFICATION
purpose: Ui Dashboard Spec documentation.
scope: Reference documentation.
---

# UI Dashboard Specification

## Document type
Document type: [CONTRACT]

## Purpose
Defines the dashboard surface, panels, navigation, and data contracts for the professional trading UI.

## Coverage
Executive overview, live market intelligence, AI intelligence center, strategy control, execution monitor, portfolio analytics, chain command center, DEX intelligence, wallet command center, and notification center.

## Panel layout
- The dashboard is organized into panels bound to the domain model; each panel renders a defined widget set.
- Executive overview shows portfolio, health, and active-opportunity summary at a glance.
- Live trading status is represented explicitly: active, paused, emergency-stopped, and offline states are visually distinct.
- Navigation moves between the command centers without leaving the shell.

## Refresh behavior
- Panels refresh on a fixed cadence and on change events from the runtime.
- A chart widget refreshes after a new trade completes.
- Refresh latency must meet the dashboard SLO; a slow panel degrades visibly rather than blocking the shell.
- Error states are explicit: a panel that cannot render shows its error with recovery guidance.

## Data contracts
- Panels consume the domain model and metrics contracts; they never read runtime state directly.
- Interaction with the backend flows through the typed IPC and API contracts.

## Panel inventory
- Executive overview.
- Market intelligence.
- AI intelligence center.
- Strategy control.
- Execution monitor.
- Portfolio analytics.
- Chain and DEX command centers.
- Wallet command center.
- Notification center.
- Each panel declares the domain-model surface it consumes and the widget set it renders.
- Panels are added here in the same change that introduces their widget definition.

## Cross-references
- `../interfaces/api/domain-model.md`
- `../operations/monitoring/metrics.md`
- `../operations/monitoring/health-checks.md`
- `../ai/orchestration/ai-orchestration.md`
- `../ui/ui-component-spec.md`

## Operational Contract

Defines the dashboard UI contract, data binding, refresh behavior, and interaction expectations. The dashboard renders runtime state; the runtime remains the source of truth.

## Example
A chart widget refreshes after a new trade completes, and if the refresh fails the panel shows its error state with retry guidance.
