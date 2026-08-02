---
metadata_schema_version: 1.0
document_id: DOC-0394
title: Design System
plane: Product Specification
domain: UI
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/ui/design-system.md
related_concepts:
  - CONCEPT-0394
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - UI
type: REFERENCE
purpose: Design System documentation.
scope: Reference documentation.
---

# Design System

## Document type
Document type: [CONTRACT]

## Purpose
Defines visual tokens, spacing, component consistency, and shared interaction patterns for the APEX desktop UI.

## Visual tokens
- Color semantics: success, warning, danger, neutral, and accent for trading data.
- Spacing scale: consistent 4px-based spacing for density control.
- Typography: fixed type scale for data, headings, and body.
- States: default, hover, active, disabled, loading, empty, and error.

## Theme
- Dark and light themes are supported; both preserve data-legibility contrast.
- Theme tokens are the only source of color in components; hard-coded colors are prohibited.
- Trading-critical colors (danger, success) are theme-independent to avoid misreading.

## Consistency rules
- A primary button uses the same spacing and color semantics across screens.
- Components are built from the component spec and never restyle tokens ad hoc.
- Density follows the UX guidelines for trading screens.

## Accessibility
- Contrast ratios meet the accessibility targets in the UX guidelines.
- Focus states are explicit; interaction is keyboard-accessible.

## Token governance
- Tokens are defined once in the token set; components consume tokens, never hard-coded values.
- A token change is a reviewed change; consumers are updated in the same change.
- Trading-critical colors are theme-independent to avoid misreading.
- New tokens are added here before first use in any component.

## Component consistency
- Reusable components come from the component spec; ad hoc restyling is prohibited.
- Spacing, type, and state semantics come from this system's tokens.
- Density follows the UX guidelines for trading screens.
- Motion is subtle and never obscures data changes.

## Review
- UI changes are reviewed against the token set and the UX guidelines.
- A component that cannot meet contrast targets is flagged, not shipped.
- Design tokens are versioned with the UI contract.

## Cross-references
- `./designer-protocols.md`
- `./ui-component-spec.md`
- `./ux-guidelines.md`
- `../windows/windows-desktop.md`

## Governance Rules
Defines visual tokens, spacing, component consistency, and shared interaction patterns.

## Example
A primary button uses the same spacing and color semantics across screens because both come from the token set.
