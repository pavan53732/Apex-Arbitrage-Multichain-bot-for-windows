# Event Bus

## Purpose
Defines the central pub/sub backbone for asynchronous communication between agents, workers, and UI.

## Topics
- market.data.
- ai.decision.
- execution.order.
- execution.settlement.
- system.alert.
- system.metric.
- learning.feedback.

## Message schema
- id.
- timestamp.
- source.
- correlation_id.
- topic.
- payload_type.
- payload.
- priority (HIGH/MEDIUM/LOW).

## Guarantees
At-least-once delivery with idempotency keys. No FIFO guarantee unless a partition key is used.

## DLQ
Failed messages after 3 retries go to a DLQ with a 24-hour TTL.

## Consumer groups
Workers in the same group compete for load. Orchestrator is a singleton consumer.

## Configuration
- MAX_RETRIES.
- DLQ_TTL_SECONDS.
- PARTITION_COUNT.
- CONSUMER_TIMEOUT_MS.

## Cross-references
- `ORCHESTRATOR.md`
- `AI-ORCHESTRATION.md`
- `RUNTIME-OPERATIONS.md`

## Interface Contract
Defines topics, message envelope, delivery guarantees, retry policy, partitioning, consumer groups, and dead-letter behavior.

## Example
A trade event is published with correlation id, priority, and payload type.
