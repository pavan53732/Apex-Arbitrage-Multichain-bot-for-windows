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
version: 1.1.0
canonical_source: docs/apex-app-docs/operations/notifications/notification-center.md
related_concepts:
  - CONCEPT-0345
dependencies: []
consumers:
  - DOC-0422
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Operations
type: REFERENCE
purpose: Notification Center documentation.
scope: Reference documentation.
---

# Notification Center

## Document type
Document type: [CONTRACT]

## Purpose
Defines outbound notifications for desktop, Telegram, Discord, Slack, email, and webhooks.

## Delivery behavior
- Toast notifications handle critical alerts.
- In-app notices handle noncritical updates.
- User preferences control quiet hours and persistence.
- Channel delivery failures return an error and escalate; a notification is never silently dropped.

## Windows delivery
- Which alerts become Windows toasts versus in-app banners follows the severity mapping.
- Notifications persist after restart; the notification history is queryable.
- Quiet hours suppress noncritical notifications per user preference.

## Severity mapping
- Critical alerts route to toast and operator channels.
- Warnings route to in-app notices and optional channels.
- Info updates route to in-app notices only.

## Routing rules
- Routing is derived from severity and operator preferences; a user preference never downgrades a critical alert.
- Channel delivery is validated: a channel that cannot deliver returns an error and escalates.
- Retry is bounded and channel-aware; repeated failure raises severity.
- Notifications are deduplicated by incident to prevent alert storms.
- Quiet hours suppress noncritical notifications only.
- Notification history is queryable and persists across restarts.
- Opt-in channels (Telegram, Discord, Slack, email, webhooks) require an operator-configured destination.
- Delivery receipts are recorded per channel.
- An undeliverable critical alert is retried until acknowledged or resolved.
- Notification configuration is validated before activation.
- The notification center never fabricates events; it routes events from owners.
- Every notification carries its source event identifier for traceability.
- Rate limits are enforced per channel per the channel capabilities.
- Notification center status is visible in the dashboard.

## Cross-references
- `../monitoring/health-checks.md`
- `../reliability/runtime-operations.md`
- `../../interfaces/messages/interface-notification-channel.md`

## Operational Contract

Defines outbound notifications across desktop, Telegram, Discord, Slack, email, and webhooks. The channel contract owns the message shape; this document owns the center's routing and delivery policy.

## Example
A critical execution failure routes to a Windows toast and the operator channel, and persists in the notification history after restart.
