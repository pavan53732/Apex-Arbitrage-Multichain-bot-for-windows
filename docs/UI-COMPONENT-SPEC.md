---
last_updated: 2026-07-29
type: SPECIFICATION
owner: UI Team
status: Canonical
version: 1.0.0
purpose: Ui Component Spec documentation.
scope: Reference documentation.
canonical_source: docs/UI-COMPONENT-SPEC.md
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
- `UI-DASHBOARD-SPEC.md`
- `DASHBOARD-WIDGETS.md`
- `UX-GUIDELINES.md`
- `WINDOWS-DESKTOP.md`

## Core components
- Status banner, spread panel, P&L panel, health panel, and notification drawer.
- Each component must define loading, empty, error, and live states.
