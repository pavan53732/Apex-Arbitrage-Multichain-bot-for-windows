# Database Schema

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.1.0 | **Status:** Canonical | **Last Updated:** 2026-07-27 | **Owner:** Data Team

## Purpose
Defines table-level DDL detail, indexes, access patterns, retention policies, migration strategy, and Windows-specific storage behavior for all persistent entities in the Apex platform.

---

## 1. Storage Architecture

| Backend | Purpose | Location | Max Size | Windows Path |
|---------|---------|----------|----------|--------------|
| **SQLite (primary)** | Local persistent store | `%APPDATA%/Apex/data/apex.db` | 10 GB | User app data directory |
| **SQLite (event store)** | Event history | `%APPDATA%/Apex/data/events.db` | 5 GB | User app data directory |
| **SQLite (audit store)** | Audit and security logs | `%APPDATA%/Apex/data/audit.db` | 2 GB | User app data directory |
| **File storage** | Workspace, AI archives, diagnostics | `%APPDATA%/Apex/files/` | 500 MB | User app data directory |
| **In-memory (transient)** | Runtime state, event buffers, caches | Process heap | `resource.memory_limit_mb` | Not persisted |

---

## 2. Table Definitions

### 2.1 Trading Tables

#### `trades`

```sql
CREATE TABLE trades (
  trade_id        TEXT PRIMARY KEY,        -- UUID
  strategy_id     TEXT NOT NULL,           -- FK → strategies
  wallet_id       TEXT NOT NULL,           -- FK → wallets
  chain_a_id      TEXT NOT NULL,           -- FK → chains
  chain_b_id      TEXT NOT NULL,           -- FK → chains
  pair_a          TEXT NOT NULL,           -- e.g., "WETH/USDC"
  pair_b          TEXT NOT NULL,           -- e.g., "WETH/USDT"
  spread_bps      INTEGER NOT NULL,        -- Detected spread
  estimated_profit_usd REAL NOT NULL,      -- Pre-execution estimate
  actual_profit_usd    REAL,               -- Post-execution actual (nullable until settled)
  gas_total_usd   REAL,                    -- Total gas cost
  state           TEXT NOT NULL,           -- ENUM: opportunity, approved, executing, completed, aborted, failed
  risk_result     TEXT NOT NULL,           -- APPROVED/REJECTED + reason codes
  created_at      TEXT NOT NULL,           -- ISO-8601
  updated_at      TEXT NOT NULL,           -- ISO-8601
  completed_at    TEXT,                    -- ISO-8601 (nullable until settled)
  correlation_id  TEXT NOT NULL,           -- Cross-table correlation
  version         INTEGER NOT NULL DEFAULT 1
);

CREATE INDEX idx_trades_state ON trades(state);
CREATE INDEX idx_trades_created ON trades(created_at);
CREATE INDEX idx_trades_correlation ON trades(correlation_id);
CREATE INDEX idx_trades_strategy_wallet ON trades(strategy_id, wallet_id);
```

#### `execution_legs`

```sql
CREATE TABLE execution_legs (
  leg_id          TEXT PRIMARY KEY,        -- UUID
  trade_id        TEXT NOT NULL,           -- FK → trades
  leg_number      INTEGER NOT NULL,        -- 1 or 2
  chain_id        TEXT NOT NULL,           -- FK → chains
  direction       TEXT NOT NULL,           -- buy/sell
  tx_hash         TEXT,                    -- On-chain TX hash (nullable until submitted)
  nonce           INTEGER,                 -- Wallet nonce
  gas_used        INTEGER,                 -- Gas consumed
  gas_price_gwei  REAL,                    -- Gas price at execution
  block_number    INTEGER,                 -- Confirmation block
  state           TEXT NOT NULL,           -- ENUM: pending, signing, broadcasting, in_mempool, confirming, finalized, reverted, failed, stuck, aborted
  retry_count     INTEGER DEFAULT 0,
  created_at      TEXT NOT NULL,
  updated_at      TEXT NOT NULL,
  correlation_id  TEXT NOT NULL,
  version         INTEGER NOT NULL DEFAULT 1,
  FOREIGN KEY (trade_id) REFERENCES trades(trade_id)
);

CREATE INDEX idx_exec_legs_trade ON execution_legs(trade_id);
CREATE INDEX idx_exec_legs_state ON execution_legs(state);
CREATE INDEX idx_exec_legs_tx_hash ON execution_legs(tx_hash);
CREATE INDEX idx_exec_legs_chain_state ON execution_legs(chain_id, state);
```

### 2.2 Wallet Tables

#### `wallets`

```sql
CREATE TABLE wallets (
  wallet_id       TEXT PRIMARY KEY,        -- UUID
  address         TEXT NOT NULL UNIQUE,     -- Checksummed address
  chain_id        TEXT NOT NULL,           -- FK → chains
  network         TEXT NOT NULL,           -- Mainnet/Testnet
  enabled         INTEGER NOT NULL DEFAULT 1, -- Boolean
  max_gas_price_gwei REAL NOT NULL DEFAULT 500,
  created_at      TEXT NOT NULL,
  updated_at      TEXT NOT NULL,
  version         INTEGER NOT NULL DEFAULT 1
);

CREATE INDEX idx_wallets_chain ON wallets(chain_id);
CREATE INDEX idx_wallets_enabled ON wallets(enabled);
```

#### `wallet_transactions`

```sql
CREATE TABLE wallet_transactions (
  tx_id           TEXT PRIMARY KEY,        -- UUID
  wallet_id       TEXT NOT NULL,           -- FK → wallets
  chain_id        TEXT NOT NULL,           -- FK → chains
  tx_hash         TEXT NOT NULL UNIQUE,    -- On-chain hash
  direction       TEXT NOT NULL,           -- incoming/outgoing
  amount_crypto   REAL NOT NULL,
  amount_usd      REAL NOT NULL,
  gas_used        INTEGER,
  gas_price_gwei  REAL,
  block_number    INTEGER,
  state           TEXT NOT NULL,           -- ENUM: pending, confirmed, failed
  created_at      TEXT NOT NULL,
  confirmed_at    TEXT,
  correlation_id  TEXT NOT NULL,
  FOREIGN KEY (wallet_id) REFERENCES wallets(wallet_id)
);

CREATE INDEX idx_wallet_txs_wallet ON wallet_transactions(wallet_id);
CREATE INDEX idx_wallet_txs_hash ON wallet_transactions(tx_hash);
CREATE INDEX idx_wallet_txs_state ON wallet_transactions(state);
```

### 2.3 AI Tables

#### `ai_tasks`

```sql
CREATE TABLE ai_tasks (
  task_id         TEXT PRIMARY KEY,        -- UUID
  session_id      TEXT NOT NULL,
  requestor       TEXT NOT NULL,           -- subsystem that initiated
  intent          TEXT NOT NULL,           -- ENUM: trade_signal, risk_assessment, strategy_suggestion, general
  model           TEXT NOT NULL,           -- e.g., "gpt-4o"
  provider        TEXT NOT NULL,           -- e.g., "openai"
  prompt_version  TEXT NOT NULL,           -- FK → ai_prompt_versions
  context_hash    TEXT NOT NULL,           -- Hash of assembled context
  tokens_in       INTEGER,                -- Input tokens
  tokens_out      INTEGER,                -- Output tokens
  cost_usd        REAL,                   -- Cost of this call
  confidence      REAL,                   -- 0.0–1.0
  result          TEXT,                   -- JSON response
  state           TEXT NOT NULL,           -- ENUM: draft, ready, running, completed, failed, cancelled
  duration_ms     INTEGER,
  created_at      TEXT NOT NULL,
  completed_at    TEXT,
  correlation_id  TEXT NOT NULL,
  version         INTEGER NOT NULL DEFAULT 1
);

CREATE INDEX idx_ai_tasks_state ON ai_tasks(state);
CREATE INDEX idx_ai_tasks_provider_model ON ai_tasks(provider, model);
CREATE INDEX idx_ai_tasks_session ON ai_tasks(session_id);
CREATE INDEX idx_ai_tasks_created ON ai_tasks(created_at);
```

#### `ai_memory_entries`

```sql
CREATE TABLE ai_memory_entries (
  memory_id       TEXT PRIMARY KEY,        -- UUID
  session_id      TEXT,                    -- Originating session
  category        TEXT NOT NULL,           -- ENUM: fact, insight, pattern, decision, trade_result
  content         TEXT NOT NULL,           -- The actual memory content
  content_hash    TEXT NOT NULL,           -- Hash for dedup
  relevance_score REAL NOT NULL DEFAULT 0.5, -- 0.0–1.0
  recency_score   REAL NOT NULL DEFAULT 1.0, -- 0.0–1.0 (decays over time)
  ttl_days        INTEGER NOT NULL DEFAULT 30,
  expires_at      TEXT NOT NULL,           -- ISO-8601
  created_at      TEXT NOT NULL,
  updated_at      TEXT NOT NULL,
  version         INTEGER NOT NULL DEFAULT 1
);

CREATE INDEX idx_ai_memory_category ON ai_memory_entries(category);
CREATE INDEX idx_ai_memory_score ON ai_memory_entries(relevance_score, recency_score);
CREATE INDEX idx_ai_memory_expires ON ai_memory_entries(expires_at);
CREATE INDEX idx_ai_memory_hash ON ai_memory_entries(content_hash);
```

### 2.4 Event Tables

#### `events`

```sql
CREATE TABLE events (
  event_id        TEXT PRIMARY KEY,        -- UUID
  event_type      TEXT NOT NULL,           -- e.g., "trade.opportunity.detected"
  event_version   TEXT NOT NULL DEFAULT "1.0",
  ordering_key    TEXT,                    -- Key for FIFO ordering
  payload         TEXT NOT NULL,           -- JSON payload
  producer        TEXT NOT NULL,           -- Subsystem that produced
  severity        TEXT NOT NULL DEFAULT "medium", -- ENUM: critical, high, medium, low
  delivery_guarantee TEXT NOT NULL,        -- ENUM: exactly_once, at_least_once, at_most_once
  created_at      TEXT NOT NULL,           -- ISO-8601
  consumed_at     TEXT,                    -- ISO-8601 (when fully consumed)
  correlation_id  TEXT NOT NULL,
  version         INTEGER NOT NULL DEFAULT 1
);

CREATE INDEX idx_events_type ON events(event_type);
CREATE INDEX idx_events_created ON events(created_at);
CREATE INDEX idx_events_ordering ON events(ordering_key, created_at);
CREATE INDEX idx_events_severity ON events(severity);
```

#### `dead_letter_queue`

```sql
CREATE TABLE dead_letter_queue (
  dlq_id          TEXT PRIMARY KEY,        -- UUID
  original_event_id TEXT NOT NULL,         -- FK → events
  retry_count     INTEGER NOT NULL DEFAULT 0,
  max_retries     INTEGER NOT NULL DEFAULT 3,
  last_error      TEXT,                    -- Error description
  created_at      TEXT NOT NULL,
  resolved_at     TEXT,                    -- When replayed successfully
  FOREIGN KEY (original_event_id) REFERENCES events(event_id)
);

CREATE INDEX idx_dlq_resolved ON dead_letter_queue(resolved_at);
```

### 2.5 System Tables

#### `audit_log`

```sql
CREATE TABLE audit_log (
  audit_id        TEXT PRIMARY KEY,
  subsystem       TEXT NOT NULL,
  action          TEXT NOT NULL,
  actor_role      TEXT NOT NULL,           -- ENUM: operator, trader, viewer, plugin, service
  actor_id        TEXT NOT NULL,           -- User ID or plugin ID
  target          TEXT,                    -- What was acted upon
  result          TEXT NOT NULL,           -- success/failure
  details         TEXT,                    -- JSON details (secrets redacted)
  severity        TEXT NOT NULL DEFAULT "info",
  created_at      TEXT NOT NULL,
  correlation_id  TEXT NOT NULL
);

CREATE INDEX idx_audit_subsystem ON audit_log(subsystem);
CREATE INDEX idx_audit_actor ON audit_log(actor_role, actor_id);
CREATE INDEX idx_audit_created ON audit_log(created_at);
CREATE INDEX idx_audit_severity ON audit_log(severity);
```

#### `config_history`

```sql
CREATE TABLE config_history (
  change_id       TEXT PRIMARY KEY,
  config_hash     TEXT NOT NULL,           -- Hash of full config at change time
  key_path        TEXT NOT NULL,           -- Which key was changed
  old_value       TEXT,                    -- Previous value (redacted for secrets)
  new_value       TEXT,                    -- New value (redacted for secrets)
  change_type     TEXT NOT NULL,           -- ENUM: hot_reload, restart_required, startup, profile_switch
  actor           TEXT NOT NULL,
  created_at      TEXT NOT NULL
);

CREATE INDEX idx_config_history_key ON config_history(key_path);
CREATE INDEX idx_config_history_created ON config_history(created_at);
```

#### `recovery_records`

```sql
CREATE TABLE recovery_records (
  recovery_id     TEXT PRIMARY KEY,
  subsystem       TEXT NOT NULL,
  failure_type    TEXT NOT NULL,
  severity        TEXT NOT NULL,
  phase           TEXT NOT NULL,           -- ENUM: detected, classified, contained, restored, reconciled, released
  duration_ms     INTEGER,
  details         TEXT,                    -- JSON
  operator_action TEXT,                    -- Manual intervention description
  created_at      TEXT NOT NULL,
  completed_at    TEXT,
  correlation_id  TEXT NOT NULL
);

CREATE INDEX idx_recovery_subsystem ON recovery_records(subsystem);
CREATE INDEX idx_recovery_phase ON recovery_records(phase);
CREATE INDEX idx_recovery_created ON recovery_records(created_at);
```

---

## 3. Access Patterns

| Query Pattern | Tables | Index Used | Frequency | Expected Latency |
|---------------|--------|------------|-----------|-----------------|
| Get active trades | `trades` WHERE state IN ('approved', 'executing') | `idx_trades_state` | 5 Hz | < 5ms |
| Get trade by correlation ID | `trades` + `execution_legs` | `idx_trades_correlation` | 1 Hz | < 10ms |
| Get wallet balance | `wallet_transactions` WHERE wallet_id + state='confirmed' | `idx_wallet_txs_wallet` | 2 Hz | < 5ms |
| Get recent events by type | `events` WHERE event_type + created_at > threshold | `idx_events_type, idx_events_created` | 10 Hz | < 10ms |
| Get DLQ entries | `dead_letter_queue` WHERE resolved_at IS NULL | `idx_dlq_resolved` | 0.1 Hz | < 5ms |
| Get AI tasks by session | `ai_tasks` WHERE session_id | `idx_ai_tasks_session` | 2 Hz | < 10ms |
| Get audit log by subsystem | `audit_log` WHERE subsystem + created_at range | `idx_audit_subsystem, idx_audit_created` | 0.5 Hz | < 20ms |
| Memory lookup by relevance | `ai_memory_entries` ORDER BY relevance+recency LIMIT K | `idx_ai_memory_score` | 2 Hz | < 10ms |
| Config change history | `config_history` WHERE key_path | `idx_config_history_key` | 0.1 Hz | < 5ms |

---

## 4. Retention Policies

| Table | Retention | Prune Method | Prune Schedule |
|-------|-----------|--------------|----------------|
| `trades` | 365 days | Archive completed/aborted trades > 365d to compressed file; delete from main | Daily at 03:00 UTC |
| `execution_legs` | 90 days (with trade) | Cascade delete with parent trade | Daily at 03:00 UTC |
| `wallet_transactions` | 90 days | Archive > 90d to compressed file | Daily at 03:00 UTC |
| `ai_tasks` | 30 days | Delete completed/failed/cancelled > 30d | Daily at 03:00 UTC |
| `ai_memory_entries` | TTL-based (30d default) | Delete expired entries on insert (lazy eviction) | Continuous |
| `events` | Per `event.retention_days` (7d default) | Delete consumed events > retention_days | Daily at 03:00 UTC |
| `dead_letter_queue` | 90 days | Delete resolved > 90d; unresolved > 365d trigger alert | Daily at 03:00 UTC |
| `audit_log` | 365 days | Archive > 365d to compressed cold storage | Monthly |
| `config_history` | 365 days | Archive > 365d | Monthly |
| `recovery_records` | 90 days | Delete released/reconciled > 90d | Daily at 03:00 UTC |

---

## 5. Migration Strategy

| Rule | Description |
|------|-------------|
| Migrations are versioned | Each migration has a unique version number (e.g., `V001__create_trades.sql`) |
| Migrations are idempotent | Running a migration twice must not produce errors |
| Migrations are reversible where possible | Each `Vxxx__name.sql` has a corresponding `Vxxx__name__rollback.sql` |
| Breaking changes require compatibility notes | Column removals, type changes, and constraint changes documented |
| Schema version tracked | `schema_version` table stores current migration version |
| Active histories preserved | Migrations must not delete data needed for in-flight trades or AI sessions |
| Hash integrity verified on restore | After backup restore, verify all `version` fields and `content_hash` consistency |

---

## 6. Windows Storage Behavior

| Aspect | Rule |
|--------|------|
| **File path** | `%APPDATA%/Apex/` (or custom path per config) |
| **Locking** | SQLite WAL mode for concurrent read/write; file-level lock on backup operations |
| **Backup** | Manual export as `.apex-backup` archive (encrypted with user master password); auto-backup weekly |
| **Migration on update** | Run pending migrations on app startup after update; rollback on migration failure |
| **Disk cleanup** | Prune operations run daily at 03:00 local time; respect Windows power state (skip during sleep) |
| **Integrity check** | `PRAGMA integrity_check` on startup; if corrupted → attempt repair → fallback to backup |
| **Defragmentation** | `PRAGMA optimize` weekly; `VACUUM` monthly or when DB size > 5 GB |
| **File permissions** | DB files readable only by current Windows user; service mode uses SYSTEM account |

---

## Cross-References

- **STATE-MANAGEMENT.md** — State ownership and persistence rules.
- **CACHE-MANAGER.md** — Cache eviction policies.
- **EVENT-CATALOG.md** — Event payload schemas.
- **CONFIGURATION-REFERENCE.md** — Storage config keys (`resource.disk_cache_max_mb`, `event.retention_days`).
- **TRACEABILITY-MATRIX.md** — Data persistence requirements.
- **SECURITY.md** — Secret storage and audit retention.
- **AI-MEMORY.md** — AI memory store governance.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.1.0 | 2026-07-27 | Full DDL for 10 tables, indexes, access patterns, retention policies, migration strategy, Windows storage | Data Team |
| 1.0.0 | 2025-01-15 | Initial stub (entity list only) | Data Team |
