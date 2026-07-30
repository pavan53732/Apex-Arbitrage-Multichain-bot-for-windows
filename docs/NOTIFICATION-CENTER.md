---
last_updated: 2026-07-29
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Notification Center documentation.
scope: Reference documentation.
canonical_source: docs/NOTIFICATION-CENTER.md
---

# Notification Center

## Document type
This document is an overview, reference, or index as noted below.

# Notification Center

## Purpose
Defines outbound notifications for desktop, Telegram, Discord, Slack, email, and webhooks.

## Cross-references
- `operations/HEALTHCHECKS.md`
- `operations/RUNTIME-OPERATIONS.md`

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
