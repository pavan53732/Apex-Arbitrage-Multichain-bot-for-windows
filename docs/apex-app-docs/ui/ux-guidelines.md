---
metadata_schema_version: 1.0
document_id: DOC-0393
title: UX Guidelines
plane: Product Specification
domain: UI
class: Guide
authority: Canonical
status: Active
owner: UI Team
version: 1.1.0
canonical_source: docs/apex-app-docs/ui/ux-guidelines.md
related_concepts:
  - CONCEPT-0393
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - UI
type: GUIDE
purpose: Ux Guidelines documentation.
scope: Reference documentation.
---

# UX Guidelines

## Document type
Document type: [CONTRACT]

## Purpose
Defines interaction and presentation guidelines for the desktop experience.

## Scope
This document covers spacing, motion, loading states, empty states, errors, and notifications.

## Guidelines
- Use consistent spacing and hierarchy.
- Keep loading states explicit.
- Show clear empty states.
- Surface errors with actionable recovery text.
- Keep notifications concise and contextual.

## Trading-density rules
- Trading screens use a dense layout with data prioritized over chrome.
- Critical data (exposure, PnL, risk state) is visually prioritized with consistent emphasis.
- Motion is subtle and never obscures data changes; a data change is visible even without motion.

## Accessibility
- Contrast meets the accessibility targets; interaction is keyboard-accessible.
- Color is never the only signal; icons and text accompany status colors.

## Feedback timing
- Feedback is immediate for user actions.
- A destructive action requires clear confirmation and reversible feedback.

## Motion
- Motion is subtle and never obscures a data change.
- A data change is visible even without motion.
- Motion respects the reduced-motion accessibility setting.

## Density
- Trading screens use a dense layout with data prioritized over chrome.
- Critical data (exposure, PnL, risk state) is visually prioritized with consistent emphasis.

## Consistency
- Patterns follow the design system; ad hoc interaction patterns are prohibited.
- Terminology follows the glossary; labels are unambiguous.
- States (loading, empty, error, live) render consistently across surfaces.
- Color is never the only signal; icons and text accompany status colors.

## Review
- UX changes are reviewed against these guidelines and the design system.

## Cross-references
- `../windows/windows-desktop.md`
- `./ui-component-spec.md`
- `./design-system.md`
- `./designer-protocols.md`
- `./user-flows.md`

## Governance Rules
Defines interaction principles, accessibility expectations, feedback timing, and consistency standards.

## Example
A destructive action requires clear confirmation and reversible feedback; critical risk data is emphasized over noncritical chrome.
