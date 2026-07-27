# Event Bus

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-27 | **Owner:** Runtime Team

## Purpose
Defines the central pub/sub backbone for asynchronous communication — producer/consumer contract, message schema, delivery guarantees, ordering, priority, retry, deduplication, timeout, persistence, replay, dead-letter handling, consumer groups, partitioning, and cross-subsystem integration.

---

## 1. Event Bus Architecture

### 1.1 Bus Components

| Component | Responsibility | Thread | Priority |
|-----------|---------------|--------|----------|
| **Publisher API** | Accept events from producers | Main (Service) | High |
| **Router** | Match events to consumer subscriptions | Event Bus thread | High |
| **Partition Manager** | Distribute events across partitions | Event Bus thread | High |
| **Consumer Dispatcher** | Deliver events to registered consumers | Event Bus thread | Normal |
| **DLQ Manager** | Handle failed deliveries, retry, purge | Event Bus thread | Low |
| **Persistence Store** | Store events for replay | Database thread | Normal |
| **Health Monitor** | Track bus throughput, consumer lag | Health Check thread | Low |

---

## 2. Producer Contract

### 2.1 Producer Registration

Every producer must register before publishing:

```json
{
  "producer_id": "trading-engine",
  "producer_domain": "T1",
  "topics": ["trade.*", "execution.*"],
  "max_publish_rate": 100,
  "delivery_guarantee": "exactly-once",
  "priority_range": ["CRITICAL", "HIGH"]
}
```

### 2.2 Producer Rules

- Producer must not publish events outside declared topics.
- Producer must not exceed `max_publish_rate` (enforced by rate limiter).
- Producer must include idempotency key on exactly-once events.
- Producer must set correct priority based on event severity.
- Producer must set `correlation_id` for events that are part of a request-response chain.
- Producer must set `ordering_key` for events requiring FIFO delivery.

---

## 3. Consumer Contract

### 3.1 Consumer Registration

Every consumer must register before subscribing:

```json
{
  "consumer_id": "risk-engine",
  "consumer_domain": "T1",
  "subscriptions": ["trade.opportunity.detected", "trade.leg.failed"],
  "consumer_group": "risk-checkers",
  "max_consume_rate": 50,
  "ack_timeout_ms": 5000,
  "retry_policy": {"max_retries": 3, "backoff_ms": [1000, 3000, 5000]}
}
```

### 3.2 Consumer Rules

- Consumer must acknowledge events within `ack_timeout_ms` (default 5000ms).
- Unacknowledged events are retried per retry policy.
- Consumer must handle idempotent events safely (same event may arrive twice for at-least-once delivery).
- Consumer must handle out-of-order events (check sequence numbers).
- Consumer must not consume events outside declared subscriptions.
- Consumer in a group: only one consumer in the group receives each event (load distribution).

### 3.3 Consumer Groups

| Group | Consumers | Distribution | Singleton? |
|-------|-----------|-------------|------------|
| `risk-checkers` | 1-3 Risk Engine instances | Round-robin | No |
| `trading-engine` | 1 Trading Engine | Competing (only 1 active) | Yes |
| `dashboard-updaters` | Dashboard Runtime (single) | All events to single consumer | Yes |
| `notification-senders` | 1-3 Notification instances | Round-robin | No |
| `health-monitors` | 1 Health Checker | All health events | Yes |
| `audit-loggers` | 1 Audit Logger | All events (fan-out) | No (receives copy) |

---

## 4. Message Envelope Schema

```json
{
  "id": "uuid-v4",
  "idempotency_key": "trade-abc123-leg1-confirm",
  "correlation_id": "trade-abc123",
  "ordering_key": "trade-abc123",
  "sequence_number": 42,
  "timestamp": "2026-07-27T12:34:56.789Z",
  "source": "trading-engine",
  "source_domain": "T1",
  "topic": "trade.leg.confirmed",
  "payload_type": "TradeLegConfirmed",
  "payload": { ... },
  "metadata": {
    "priority": "CRITICAL",
    "delivery_guarantee": "exactly-once",
    "retention_days": 90,
    "schema_version": "1.0"
  }
}
```

### 4.1 Required Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | UUID | Always | Unique event identifier |
| `timestamp` | ISO8601 | Always | Event creation time |
| `source` | string | Always | Producer ID |
| `topic` | string | Always | Event topic (e.g., `trade.leg.confirmed`) |
| `payload_type` | string | Always | Payload schema name |
| `payload` | object | Always | Event payload data |
| `metadata.priority` | enum | Always | `CRITICAL`, `HIGH`, `MEDIUM`, `LOW` |
| `metadata.delivery_guarantee` | enum | Always | `exactly-once`, `at-least-once`, `best-effort` |

### 4.2 Optional Fields

| Field | Type | When Required | Description |
|-------|------|-------------|-------------|
| `idempotency_key` | string | Exactly-once delivery | Duplicate detection key |
| `correlation_id` | string | Request-response chains | Links related events |
| `ordering_key` | string | FIFO ordering required | Partition key for ordering |
| `sequence_number` | int | Ordered event streams | Monotonic per producer per topic |
| `source_domain` | string | Cross-domain events | Trust domain (T0-T5) |
| `metadata.retention_days` | int | Override default retention | Category-specific retention |
| `metadata.schema_version` | string | All events | Payload schema version |

---

## 5. Delivery Guarantees

| Guarantee | Mechanism | Producer Action | Consumer Action |
|-----------|-----------|----------------|-----------------|
| **Exactly-once** | Producer stores → consumer acks + commits → producer deletes | Must include `idempotency_key` | Must deduplicate by key; must ack after commit |
| **At-least-once** | Consumer acks after processing | No idempotency required | Must handle duplicates (idempotent processing) |
| **Best-effort** | Fire-and-forget | No persistence required | No ack required; may be lost |

### 5.1 Exactly-Once Implementation

```
1. Producer writes event to persistent store (status: PENDING).
2. Producer publishes event to bus.
3. Consumer receives event → processes → commits locally.
4. Consumer sends ACK to bus.
5. Bus forwards ACK to producer.
6. Producer updates event status: DELIVERED.
7. If no ACK within ack_timeout_ms → bus retries delivery.
8. If retries exhausted → event goes to DLQ.
```

---

## 6. Ordering

### 6.1 Ordering Rules

| Ordering Type | Mechanism | Guarantees | Limitations |
|--------------|-----------|------------|-------------|
| **FIFO per key** | Same `ordering_key` → same partition → FIFO | Events with same key arrive in order | No cross-key ordering |
| **Unordered** | No `ordering_key` → distributed across partitions | Best throughput | No ordering guarantee |
| **Best-effort FIFO** | `ordering_key` + at-least-once | Mostly ordered | Retries may cause duplicate delivery |

### 6.2 Partition Assignment

```
partition_index = hash(ordering_key) % PARTITION_COUNT

If no ordering_key:
  partition_index = round_robin(counter++ % PARTITION_COUNT)

PARTITION_COUNT: event.bus.partition_count (default 8)
```

---

## 7. Priority

| Priority | Delivery Behavior | Queue Position | Retry Budget | Examples |
|----------|-------------------|---------------|-------------|----------|
| **CRITICAL** | Immediate delivery, no queue delay | Head of queue | 5 retries | `trade.*`, `security.*`, `risk.circuit_breaker.*` |
| **HIGH** | Fast delivery, minimal queue delay | Near head | 3 retries | `execution.*`, `risk.check.*`, `secret.*` |
| **MEDIUM** | Normal delivery | Middle | 3 retries | `ai.*`, `plugin.*`, `config.*` |
| **LOW** | Background delivery | Tail of queue | 1 retry | `health.*`, `dashboard.*`, `metrics.*` |

---

## 8. Retry Policy

### 8.1 Retry Algorithm

```
1. Event published → consumer receives.
2. Consumer processing timeout: ack_timeout_ms (default 5000ms).
3. If no ACK → retry with exponential backoff:
   backoff_ms = base_backoff × 2^(attempt-1) × jitter
   base_backoff: event.bus.retry.base_backoff_ms (default 1000ms)
   jitter: random ±event.bus.retry.jitter_pct (default 10%)
4. Max retries per priority:
   CRITICAL: 5
   HIGH: 3
   MEDIUM: 3
   LOW: 1
5. If retries exhausted → event goes to DLQ.
```

---

## 9. Deduplication

### 9.1 Deduplication Protocol

| Delivery Guarantee | Deduplication Method | Window | Storage |
|-------------------|---------------------|--------|---------|
| **Exactly-once** | `idempotency_key` lookup | 24h sliding window | SQLite `dedup_cache` table |
| **At-least-once** | No deduplication (consumer must be idempotent) | — | — |
| **Best-effort** | No deduplication | — | — |

### 9.2 Deduplication Rules

- Exactly-once events with the same `idempotency_key` within the 24h window are silently dropped (second occurrence logged as `dedup_duplicate`).
- Dedup cache is cleaned every hour (expired entries removed).
- If dedup cache exceeds `event.bus.dedup_cache_max_entries` (default 100000) → oldest entries evicted.

---

## 10. Timeout

| Timeout Type | Default | Config Key | Action |
|-------------|---------|------------|--------|
| **Consumer ACK timeout** | 5000ms | `event.bus.ack_timeout_ms` | Retry delivery |
| **Consumer processing timeout** | 10000ms | `event.bus.processing_timeout_ms` | Mark as stuck, retry |
| **Producer confirmation timeout** | 30000ms | `event.bus.confirmation_timeout_ms` | Mark as delivery_unknown |
| **Total delivery timeout** | 120000ms | `event.bus.total_delivery_timeout_ms` | Move to DLQ |

---

## 11. Persistence & Replay

### 11.1 Persistence Rules

| Category | Retention | Storage | Compression |
|----------|-----------|---------|-------------|
| Trading (`trade.*`) | 365 days | SQLite `events_trading` table | After 30 days |
| Execution (`execution.*`) | 90 days | SQLite `events_execution` table | After 30 days |
| Security (`security.*`) | 365 days | SQLite `events_security` table | None |
| System (`system.*`) | 30 days | SQLite `events_system` table | After 7 days |
| AI (`ai.*`) | 30 days | SQLite `events_ai` table | After 7 days |
| All other | 7-30 days (per category) | SQLite `events_general` table | After 7 days |

### 11.2 Replay Protocol

| Replay Type | Trigger | Method | Scope |
|-------------|---------|--------|-------|
| **Manual replay** | Operator request via dashboard or API | `POST /api/admin/events/replay?topic=X&from=Y&to=Z` | Specific topic + time range |
| **Recovery replay** | Startup recovery scan | Replay from last checkpoint | All critical events |
| **Consumer resubscribe** | Consumer reconnect after disconnect | Resume from last acked sequence | Per consumer subscription |
| **DLQ replay** | Operator manually clears DLQ entries | Replay individual DLQ entries | Per DLQ entry |

---

## 12. Dead-Letter Queue (DLQ)

### 12.1 DLQ Configuration

| Property | Value | Config Key |
|----------|-------|------------|
| Max retries before DLQ | Per priority (see §8) | — |
| DLQ storage | SQLite `dead_letter_queue` table | — |
| DLQ replay | Manual via operator dashboard or API | `POST /api/admin/events/replay` |
| Auto-purge | After 90 days | `event.bus.dlq_purge_days: 90` |
| DLQ alert | When DLQ exceeds 100 entries | `system.warning` event |
| DLQ max size | 1000 entries | `event.bus.dlq_max_entries: 1000` |

### 12.2 DLQ Entry Schema

```json
{
  "dlq_id": "uuid",
  "original_event_id": "uuid",
  "topic": "trade.leg.confirmed",
  "failure_reason": "ack_timeout",
  "retry_count": 3,
  "consumer_id": "risk-engine",
  "original_timestamp": "ISO8601",
  "dlq_timestamp": "ISO8601",
  "payload": { ... }
}
```

---

## 13. Cross-Subsystem Integration

### 13.1 Who Calls Event Bus

| Caller | Purpose | Contract |
|--------|---------|----------|
| Trading Engine | Publish trade events | `bus.publish` API |
| Execution Engine | Publish execution events | `bus.publish` API |
| Risk Engine | Publish risk events | `bus.publish` API |
| Security Manager | Publish security events | `bus.publish` API |
| AI Pipeline | Publish AI events | `bus.publish` API |
| Plugin Manager | Publish plugin events | `bus.publish` API |
| Runtime Orchestrator | Publish system events | `bus.publish` API |
| All subsystems | Subscribe to events | `bus.subscribe` API |

### 13.2 Events Event Bus Emits (Meta-Events)

| Event | Payload | Consumer |
|-------|---------|----------|
| `event.bus.consumer.lag` | `{consumer_id, lag_count, lag_ms, topic}` | Health, Dashboard |
| `event.bus.dlq.threshold` | `{dlq_count, threshold, auto_purge_enabled}` | Dashboard, Operator |
| `event.bus.partition.rebalance` | `{old_count, new_count, reason}` | Health |
| `event.bus.throughput.exceeded` | `{msg_per_sec, limit, dropped_count}` | Health, Dashboard |

### 13.3 Configuration Event Bus Owns

| Config Key | Default | Description |
|-----------|---------|-------------|
| `event.bus.partition_count` | `8` | Number of partitions |
| `event.bus.ack_timeout_ms` | `5000` | Consumer ACK timeout |
| `event.bus.processing_timeout_ms` | `10000` | Consumer processing timeout |
| `event.bus.retry.base_backoff_ms` | `1000` | Retry base backoff |
| `event.bus.retry.jitter_pct` | `0.10` | Retry jitter |
| `event.bus.dead_letter_max_retries` | `3` | Default max retries before DLQ |
| `event.bus.dlq_purge_days` | `90` | DLQ auto-purge age |
| `event.bus.dlq_max_entries` | `1000` | DLQ maximum entries |
| `event.bus.dedup_cache_max_entries` | `100000` | Dedup cache maximum |
| `event.bus.max_throughput_msg_per_sec` | `10000` | Maximum bus throughput |

---

## Cross-References

- **EVENT-CATALOG.md** — Full event definitions, payload schemas, producer/consumer mapping.
- **EVENT-OWNERSHIP-MATRIX.md** — Event ownership, delivery guarantees, ordering, priority per event.
- **IPC-PROTOCOL.md** — Inter-process communication for cross-domain events.
- **ORCHESTRATOR.md** — Platform-level orchestration.
- **AI-ORCHESTRATION.md** — AI agent orchestration and events.
- **RUNTIME-OPERATIONS.md** — Runtime event handling.
- **RECOVERY-COORDINATION.md** — Event replay during recovery.
- **CONFIGURATION-REFERENCE.md** — Event bus config keys.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-27 | Production-grade event bus contract: producer/consumer registration schema with rules, message envelope (9 required + 7 optional fields), exactly-once implementation (7 steps), ordering (3 types + partition assignment), priority (4 levels with retry budgets), retry algorithm with exponential backoff, deduplication protocol, timeout (4 types), persistence & replay (4 types + retention per category), DLQ configuration with entry schema, consumer groups (6 groups), cross-subsystem integration | Runtime Team |
| 0.1.0 | 2026-07-27 | Initial stub | Runtime Team |
