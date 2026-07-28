---
type: CONTRACT
owner: AI Team
status: Canonical
version: 1.0.0
purpose: AI orchestration event contract for Contract 15
scope: Defines event contracts for AI orchestration subsystem.
last_updated: 2026-07-28
canonical_source: docs/ai-orchestration/contract_15.md
---

# Contract 15

## Events

### Producer
- **Producer:** AI-ORCHESTRATION
- **Producer Type:** Behavioural root
- **Event Source:** Orchestration engine

### Consumer
- **Primary Consumer:** AI-PIPELINE
- **Secondary Consumers:** AI-TOOLS, AI-GATEWAY
- **Consumer Type:** Event subscribers

### Payload Schema
- **Event Type:** OrchestrationEvent
- **Schema Version:** 1.0.0
- **Fields:**
  - event_id: string (required)
  - event_type: string (required)
  - timestamp: ISO8601 (required)
  - payload: object (required)
  - correlation_id: string (optional)

### Ordering
- **Ordering Guarantee:** Per-correlation-id ordering
- **Delivery Order:** FIFO within correlation group
- **Parallelism:** Across different correlation groups

### Delivery Semantics
- **Delivery Mode:** At-least-once
- **Acknowledgement:** Required
- **Retry:** On failure

### Retry Policy
- **Max Retries:** 3
- **Backoff:** Exponential (1s, 2s, 4s)
- **Dead Letter:** After max retries exceeded

### Acknowledgement
- **Ack Type:** Explicit
- **Ack Timeout:** 30 seconds
- **Nack Handling:** Retry or dead-letter

### Failure Behaviour
- **Transient Failures:** Retry with backoff
- **Permanent Failures:** Dead-letter queue
- **Error Logging:** Structured logging

### Persistence
- **Event Store:** Event-sourced
- **Retention:** 90 days
- **Archival:** Cold storage after 30 days

### Replay
- **Replay Support:** Yes
- **Replay Scope:** From checkpoint or time range
- **Replay Idempotency:** Guaranteed

### Dead-Letter Handling
- **DLQ:** Enabled
- **DLQ Processing:** Manual review + automated retry
- **DLQ Retention:** 30 days

### Version Compatibility
- **Backward Compatible:** Yes
- **Forward Compatible:** Partial
- **Version Negotiation:** Schema registry

### Ownership
- **Event Owner:** AI Team
- **Schema Owner:** AI Team
- **Contract Owner:** AI-ORCHESTRATION

## Acceptance Criteria

- Producer defined ✓
- Consumer(s) defined ✓
- Payload schema defined ✓
- Ordering specified ✓
- Delivery semantics defined ✓
- Retry policy defined ✓
- Dead-letter handling defined ✓
- Version compatibility defined ✓
- Ownership documented ✓
