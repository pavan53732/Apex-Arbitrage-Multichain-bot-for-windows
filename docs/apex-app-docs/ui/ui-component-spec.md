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
version: 1.0.0
canonical_source: docs/apex-app-docs/ui/ui-component-spec.md
related_concepts:
  - CONCEPT-0390
dependencies: []
consumers:
  - DOC-0391
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - UI
type: SPECIFICATION
purpose: Ui Component Spec documentation.
scope: Reference documentation.
---

# Ui Component Spec

## Document type
This document is an overview, reference, or index as noted below.

# UI Component Spec

## Purpose
Defines reusable UI components for the desktop trading app.

## Ownership
- Owns component props, states, and interaction behavior.
- Does not own business logic or runtime orchestration.

## Required components
- Status badge.
- Spread panel.
- P&L panel.
- Health panel.
- Notification area.

## Cross-references
- `../dashboard/ui-dashboard-spec.md`
- `../dashboard/dashboard-widgets.md`
- `./ux-guidelines.md`
- `../windows/windows-desktop.md`

## Core components
- Status banner, spread panel, P&L panel, health panel, and notification drawer.
- Each component must define loading, empty, error, and live states.
