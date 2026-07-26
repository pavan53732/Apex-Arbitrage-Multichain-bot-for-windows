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
