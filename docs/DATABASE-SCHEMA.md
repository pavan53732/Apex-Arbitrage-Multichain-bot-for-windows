# APEX Database Schema

> **Version:** 1.0.0 | **Last Updated:** July 25, 2026 | **Database:** SQLite (`better-sqlite3`)

---

## 1. Overview

APEX uses a local embedded SQLite database as the durable system of record for settings, providers, wallets, opportunities, trades, cache, memory, and operational logs. The schema is intentionally local-first and should remain readable, migratable, and resilient under desktop deployment constraints.

---

## 2. Design Goals

- simple local durability
- explicit schema versioning
- predictable migrations
- good read performance for operator dashboards
- safe separation between sensitive and nonsensitive data

---

## 3. Global Conventions

- timestamps stored as Unix epoch milliseconds unless noted otherwise
- IDs stored as text UUIDs unless chain-native identifiers are required
- booleans stored as integers `0`/`1`
- JSON payloads stored as `TEXT` only where normalisation is not worth the complexity
- foreign keys enabled at connection startup

```sql
PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;
PRAGMA temp_store = MEMORY;
```

---

## 4. Core Tables

### 4.1 `settings`

```sql
CREATE TABLE settings (
  key         TEXT PRIMARY KEY,
  value_json  TEXT NOT NULL,
  updated_at  INTEGER NOT NULL
);
```

Purpose: small application-wide settings not requiring a bespoke table.

### 4.2 `ai_providers`

```sql
CREATE TABLE ai_providers (
  id                 TEXT PRIMARY KEY,
  name               TEXT NOT NULL,
  provider_type      TEXT NOT NULL,
  base_url           TEXT NOT NULL,
  key_blob           BLOB,
  model              TEXT NOT NULL,
  temperature_default REAL,
  timeout_ms         INTEGER,
  enabled            INTEGER NOT NULL DEFAULT 1,
  priority           INTEGER NOT NULL DEFAULT 100,
  created_at         INTEGER NOT NULL,
  updated_at         INTEGER NOT NULL
);
```

### 4.3 `wallets`

```sql
CREATE TABLE wallets (
  id                 TEXT PRIMARY KEY,
  name               TEXT NOT NULL,
  address            TEXT NOT NULL,
  chain_ids_json     TEXT NOT NULL,
  outer_blob         BLOB NOT NULL,
  created_at         INTEGER NOT NULL,
  updated_at         INTEGER NOT NULL
);
```

### 4.4 `skills`

```sql
CREATE TABLE skills (
  id                 TEXT PRIMARY KEY,
  name               TEXT NOT NULL UNIQUE,
  category           TEXT NOT NULL,
  enabled            INTEGER NOT NULL DEFAULT 1,
  config_json        TEXT,
  created_at         INTEGER NOT NULL,
  updated_at         INTEGER NOT NULL
);
```

### 4.5 `agents`

```sql
CREATE TABLE agents (
  id                 TEXT PRIMARY KEY,
  name               TEXT NOT NULL UNIQUE,
  role               TEXT NOT NULL,
  enabled            INTEGER NOT NULL DEFAULT 1,
  provider_id        TEXT,
  config_json        TEXT,
  created_at         INTEGER NOT NULL,
  updated_at         INTEGER NOT NULL,
  FOREIGN KEY (provider_id) REFERENCES ai_providers(id) ON DELETE SET NULL
);
```

### 4.6 `opportunities`

```sql
CREATE TABLE opportunities (
  id                 TEXT PRIMARY KEY,
  strategy_id        TEXT NOT NULL,
  status             TEXT NOT NULL,
  chain_path_json    TEXT NOT NULL,
  token_path_json    TEXT NOT NULL,
  venue_path_json    TEXT NOT NULL,
  gross_profit_usd   REAL NOT NULL,
  estimated_gas_usd  REAL NOT NULL,
  estimated_fees_usd REAL NOT NULL,
  net_profit_usd     REAL NOT NULL,
  confidence         REAL,
  expires_at         INTEGER NOT NULL,
  metadata_json      TEXT,
  created_at         INTEGER NOT NULL
);
```

### 4.7 `trades`

```sql
CREATE TABLE trades (
  id                    TEXT PRIMARY KEY,
  opportunity_id        TEXT,
  strategy_id           TEXT NOT NULL,
  status                TEXT NOT NULL,
  chain_id              INTEGER NOT NULL,
  wallet_id             TEXT,
  tx_hash               TEXT,
  gross_profit_usd      REAL,
  net_profit_usd        REAL,
  gas_used              INTEGER,
  gas_cost_usd          REAL,
  failure_code          TEXT,
  failure_detail        TEXT,
  submitted_at          INTEGER,
  confirmed_at          INTEGER,
  settled_at            INTEGER,
  created_at            INTEGER NOT NULL,
  updated_at            INTEGER NOT NULL,
  FOREIGN KEY (opportunity_id) REFERENCES opportunities(id) ON DELETE SET NULL,
  FOREIGN KEY (wallet_id) REFERENCES wallets(id) ON DELETE SET NULL
);
```

### 4.8 `agent_logs`

```sql
CREATE TABLE agent_logs (
  id                 INTEGER PRIMARY KEY AUTOINCREMENT,
  agent_id           TEXT NOT NULL,
  level              TEXT NOT NULL,
  event_type         TEXT NOT NULL,
  message            TEXT NOT NULL,
  context_json       TEXT,
  created_at         INTEGER NOT NULL,
  FOREIGN KEY (agent_id) REFERENCES agents(id) ON DELETE CASCADE
);
```

### 4.9 `cache_entries`

```sql
CREATE TABLE cache_entries (
  key                TEXT PRIMARY KEY,
  namespace          TEXT NOT NULL,
  value_json         TEXT NOT NULL,
  semantic_hash      TEXT,
  expires_at         INTEGER,
  created_at         INTEGER NOT NULL,
  last_accessed_at   INTEGER NOT NULL
);
```

### 4.10 `memory_entries`

```sql
CREATE TABLE memory_entries (
  id                 TEXT PRIMARY KEY,
  agent_id           TEXT,
  memory_type        TEXT NOT NULL,
  content_text       TEXT NOT NULL,
  importance         REAL NOT NULL DEFAULT 0.5,
  created_at         INTEGER NOT NULL,
  last_used_at       INTEGER,
  metadata_json      TEXT,
  FOREIGN KEY (agent_id) REFERENCES agents(id) ON DELETE SET NULL
);
```

### 4.11 `rag_documents`

```sql
CREATE TABLE rag_documents (
  id                 TEXT PRIMARY KEY,
  source_type        TEXT NOT NULL,
  source_ref         TEXT,
  title              TEXT,
  content_text       TEXT NOT NULL,
  chunk_count        INTEGER NOT NULL DEFAULT 1,
  created_at         INTEGER NOT NULL,
  updated_at         INTEGER NOT NULL
);
```

### 4.12 `rag_embeddings`

```sql
CREATE TABLE rag_embeddings (
  id                 TEXT PRIMARY KEY,
  document_id        TEXT NOT NULL,
  chunk_index        INTEGER NOT NULL,
  content_text       TEXT NOT NULL,
  embedding_blob     BLOB,
  created_at         INTEGER NOT NULL,
  FOREIGN KEY (document_id) REFERENCES rag_documents(id) ON DELETE CASCADE
);
```

### 4.13 `logs`

```sql
CREATE TABLE logs (
  id                 INTEGER PRIMARY KEY AUTOINCREMENT,
  level              TEXT NOT NULL,
  category           TEXT NOT NULL,
  event_code         TEXT,
  message            TEXT NOT NULL,
  context_json       TEXT,
  created_at         INTEGER NOT NULL
);
```

---

## 5. Indexes

```sql
CREATE INDEX idx_ai_providers_enabled_priority ON ai_providers(enabled, priority);
CREATE INDEX idx_agents_enabled ON agents(enabled);
CREATE INDEX idx_opportunities_strategy_status ON opportunities(strategy_id, status);
CREATE INDEX idx_opportunities_expires_at ON opportunities(expires_at);
CREATE INDEX idx_trades_status_created_at ON trades(status, created_at DESC);
CREATE INDEX idx_trades_strategy_id ON trades(strategy_id);
CREATE INDEX idx_trades_wallet_id ON trades(wallet_id);
CREATE INDEX idx_agent_logs_agent_created_at ON agent_logs(agent_id, created_at DESC);
CREATE INDEX idx_cache_namespace_expires_at ON cache_entries(namespace, expires_at);
CREATE INDEX idx_memory_agent_last_used ON memory_entries(agent_id, last_used_at DESC);
CREATE INDEX idx_rag_embeddings_document_chunk ON rag_embeddings(document_id, chunk_index);
CREATE INDEX idx_logs_category_created_at ON logs(category, created_at DESC);
```

### 5.1 Index Rationale

- provider selection depends on `enabled` + `priority`
- trade dashboards sort heavily by recency and status
- cache eviction depends on namespace and expiration
- agent and system logs are commonly queried by recent timestamp

---

## 6. Relationship Overview

```text
ai_providers 1---* agents
agents       1---* agent_logs
agents       1---* memory_entries
wallets      1---* trades
opportunities 1--* trades
rag_documents 1--* rag_embeddings
```

---

## 7. Constraints and Validation Rules

Recommended logical constraints beyond raw SQL types:

- `net_profit_usd = gross_profit_usd - estimated_gas_usd - estimated_fees_usd` at write time for opportunities
- `enabled` columns limited to `0` or `1`
- `status` values restricted by application enums
- `priority` lower number means higher routing preference
- `expires_at` for opportunities must be greater than `created_at`

Optional CHECK constraints can be added where they do not block future evolvability.

---

## 8. Migration Strategy

### 8.1 Version Tracking

Use SQLite `PRAGMA user_version` for global schema versioning.

```sql
PRAGMA user_version = 1;
```

### 8.2 Migration Runner Rules

- migrations execute in ascending order
- each migration runs in a transaction where possible
- migration history should also be recorded in an internal table for audit clarity

Recommended metadata table:

```sql
CREATE TABLE IF NOT EXISTS schema_migrations (
  version       INTEGER PRIMARY KEY,
  name          TEXT NOT NULL,
  applied_at    INTEGER NOT NULL
);
```

### 8.3 Change Patterns

- additive nullable columns are safest
- destructive changes require copy-table migrations
- indexes may be created post-copy for faster rebuilds

---

## 9. Data Lifecycle and Retention

| Table | Retention Guidance |
|------|--------------------|
| `settings` | persistent until changed |
| `ai_providers` | persistent until removed |
| `wallets` | persistent until removed |
| `opportunities` | prune expired/rejected records on rolling policy if needed |
| `trades` | retain long-term for audit and analytics |
| `agent_logs` | rolling retention window |
| `cache_entries` | TTL-based eviction |
| `memory_entries` | retention based on importance and usage |
| `rag_documents` | retained until source removed or rebuilt |
| `logs` | rolling retention, e.g. 7 days |

---

## 10. Backup and Recovery

Recommended practices:

- use WAL mode for desktop reliability
- support safe export while app is idle or via checkpoint flow
- provide manual backup command from settings
- on recovery, verify schema version before opening

Sensitive backups should be documented as still encrypted but machine/user-bound where DPAPI-wrapped blobs are involved.

---

## 11. Performance Considerations

- keep hot-path tables indexed narrowly
- avoid overusing JSON where relational queries are common
- prune expired cache rows in batches
- separate high-volume logs from frequently read operator tables

---

## 12. Future Schema Extensions

Likely future additions:

- `notifications`
- `provider_health_checks`
- `simulation_runs`
- `backtest_runs`
- `portfolio_snapshots`
- `plugin_registry`

These should be added through normal migrations rather than ad hoc table creation.

---

The database schema is the local backbone of APEX. Clear schema discipline is required because every desktop feature, audit path, and recovery flow depends on it.
