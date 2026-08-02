---
metadata_schema_version: 1.0
document_id: DOC-0390
title: UI Component Spec
plane: Product Specification
domain: UI
class: Specification
authority: Canonical
status: Active
owner: UI Team
version: 1.1.0
canonical_source: docs/apex-app-docs/ui/ui-component-spec.md
related_concepts:
  - CONCEPT-0390
dependencies: []
consumers:
  - DOC-0391
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - UI
type: SPECIFICATION
purpose: Ui Component Spec documentation.
scope: Reference documentation.
---

# UI Component Spec

## Document type
Document type: [CONTRACT]

## Purpose
Defines reusable UI components for the desktop trading app.

## Ownership
- Owns component props, states, and interaction behavior.
- Does not own business logic or runtime orchestration.

## Core components
- Status banner.
- Spread panel.
- P&L panel.
- Health panel.
- Notification drawer.
- Data table and chart primitives.

## Component contract
- Every component defines loading, empty, error, and live states.
- Props are typed and bound to the domain model; components never fetch runtime state directly.
- Components are theme-driven and consume design-system tokens only.
- Interaction behavior follows the UX guidelines; destructive actions require confirmation.

## State semantics
- Loading: explicit and non-blocking where possible.
- Empty: informative, with a recovery action where one exists.
- Error: actionable recovery text, never a raw stack trace.
- Live: reflects current domain state and refreshes per the dashboard contract.
- A component never blocks the shell while waiting for data.
- Data binding flows through the domain model; components never read runtime state directly.
- Destructive actions require confirmation per the UX guidelines.
- Component names and props follow the design-system conventions.
- New components are added here before first use in a screen.
- Accessibility states (focus, keyboard) are part of every component contract.

## Cross-references
- `../dashboard/ui-dashboard-spec.md`
- `../dashboard/dashboard-widgets.md`
- `./design-system.md`
- `./ux-guidelines.md`
- `../windows/windows-desktop.md`

## Operational Contract

This document owns reusable UI component definitions. Business logic and runtime state are owned by their canonical owners; components render the domain model through the dashboard and API contracts.

## Example
The health panel renders loading while health is unknown, shows an error with retry when health checks fail, and shows live status otherwise.
