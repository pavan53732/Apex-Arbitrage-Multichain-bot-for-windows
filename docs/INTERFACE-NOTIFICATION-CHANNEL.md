---
last_updated: 2026-07-29
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Interface Notification Channel documentation.
scope: Reference documentation.
canonical_source: docs/INTERFACE-NOTIFICATION-CHANNEL.md
---

# Interface Notification Channel

## Document type
This document is an overview, reference, or index as noted below.

# Interface: Notification Channel

## Purpose
Defines outbound notification channel contracts.

## Methods
- Send(severity, title, body, metadata).
- Acknowledge(id).

## Validation
- `severity`, `title`, `body`, and `metadata` are required.
- `id` is required for acknowledgements.
- `metadata` must include channel, source, and timestamp.

## Cross-references
- `NOTIFICATION-CENTER.md`
- `RUNTIME-OPERATIONS.md`

## Interface Contract
Defines channels, severities, delivery guarantees, retry policy, and escalation semantics for notifications.

## Example
A high-severity execution failure is routed to the notification center and operator channel.

## Required details
- Define toast persistence, delivery guarantees, and priority routing.

## Interface model
- Producer: defined by the owning system.
- Consumer: defined by the owning system.
- Payload: defined by the owning system.
- Schema: defined by the owning system.
- Validation: defined by the owning system.
- Versioning: defined by the owning system.
- Failure behavior: defined by the owning system.
