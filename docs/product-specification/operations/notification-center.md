---
metadata_schema_version: 1.0
document_id: DOC-0345
title: Notification Center
plane: Product Specification
domain: Operations
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/operations/notification-center.md
related_concepts:
  - CONCEPT-0345
dependencies:
  - DOC-0335
  - DOC-0338
consumers:
  - DOC-0049
  - DOC-0261
  - DOC-0296
  - DOC-0342
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
type: REFERENCE
purpose: Notification Center documentation.
scope: Reference documentation.
---

# Notification Center

## Document type
This document is an overview, reference, or index as noted below.

# Notification Center

## Purpose
Defines outbound notifications for desktop, Telegram, Discord, Slack, email, and webhooks.

## Cross-references
- `./healthchecks.md`
- `./runtime-operations.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Windows delivery
- Must define which alerts become Windows toasts versus in-app banners.
- Must define persistence after restart and user preference controls.

## Required details
- Define toast vs in-app routing, severity mapping, and restart persistence.

## Delivery behavior
- Toast notifications handle critical alerts.
- In-app notices handle noncritical updates.
- User preferences control quiet hours and persistence.
