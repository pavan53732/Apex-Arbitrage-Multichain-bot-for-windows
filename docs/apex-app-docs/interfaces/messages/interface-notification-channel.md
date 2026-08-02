---
metadata_schema_version: 1.0
document_id: DOC-0261
title: Interface Notification Channel
plane: Product Specification
domain: Interfaces
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/interfaces/messages/interface-notification-channel.md
related_concepts:
  - CONCEPT-0261
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Interfaces
type: REFERENCE
purpose: Interface Notification Channel documentation.
scope: Reference documentation.
---

# Interface: Notification Channel

## Document type
Document type: [CONTRACT]

## Purpose
Defines outbound notification channel contracts.

## Methods
- Send(severity, title, body, metadata).
- Acknowledge(id).

## Validation
- `severity`, `title`, `body`, and `metadata` are required.
- `id` is required for acknowledgements.
- `metadata` must include channel, source, and timestamp.

## Delivery semantics
- Severity determines routing and priority: critical alerts use toast/operator channels; noncritical updates use in-app notices.
- Delivery guarantees are per channel; a channel that cannot deliver must return a delivery error rather than silently dropping.
- Retry policy is bounded and channel-aware; escalation raises severity after repeated failures.
- Notifications persist after restart per the notification-center contract.

## Interface model
- Producer: defined by the owning system.
- Consumer: defined by the owning system.
- Payload: defined by the owning system.
- Schema: defined by the owning system.
- Validation: defined by the owning system.
- Versioning: defined by the owning system.
- Failure behavior: defined by the owning system.

## Severity levels
- Critical, warning, and info severities are defined by the notification center.
- Critical alerts route to toast and operator channels; noncritical updates use in-app notices.

## Acknowledgement
- Acknowledged notifications are marked and re-escalated on timeout.
- Delivery receipts are returned per channel.
- An unacknowledged critical alert is re-escalated until acknowledged or resolved.
- Delivery failures record the channel error and route to the notification center for retry policy.
- Channel capabilities (rate limits, size limits) are declared per channel and enforced.
- Payloads conform to the notification channel schema; a malformed payload is rejected before send.
- Severity mapping follows the notification-center contract, never per-call ad hoc mapping.

## Cross-references
- `../../operations/notifications/notification-center.md`
- `../../operations/reliability/runtime-operations.md`

## Interface Contract
Defines channels, severities, delivery guarantees, retry policy, and escalation semantics for notifications.

## Example
A high-severity execution failure is routed to the notification center and operator channel; a noncritical update uses an in-app notice.
