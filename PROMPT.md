# APEX ARBITRAGE FEATURE MAPPING PROMPT

**Master Template for Converting Legacy Components to Windows-First Architecture**

---

## Purpose
Use this prompt to map any legacy component from your 6,165-file system into the new Windows-first, feature-driven architecture that lives inside the `features/` folder. The output will specify which MD file owns the feature, which files reference it, and how it's implemented on Windows.

## How to Use
1. Copy this entire prompt into a new request
2. Fill in the fields under "Your Input" 
3. Receive a complete, copy-paste specification for the relevant MD files

---

# FEATURE MAPPING REQUEST TEMPLATE

## Your Input (Fill These Fields)

### 1) Original Component Analysis
- **Component Name**: [Name of the legacy component or capability]
- **Component Type**: [Feature | Subsystem | Adapter | Service | UI Widget | Config | Documentation]
- **Original Purpose**: [Short description of what it did in the 6,165-file system]
- **Criticality**: [P0 | P1 | P2 | P3] (P0=must-have for MVP, P3=nice-to-have)

### 2) Feature Identification Request
Map this component to the NEW Windows Desktop MD file architecture.

**PRIMARY OWNER (choose exactly one):**
- [ ] install-dependencies.md
- [ ] config.md
- [ ] backend.md
- [ ] dashboard.md
- [ ] ai-modules.md
- [ ] docs.md
- [ ] contracts.md (if needed)
- [ ] security.md (if needed)
- [ ] testing.md (if needed)
- [ ] deployment.md (if needed)

**SECONDARY REFERENCES (choose any that apply):**
- [ ] install-dependencies.md
- [ ] config.md
- [ ] backend.md
- [ ] dashboard.md
- [ ] ai-modules.md
- [ ] docs.md
- [ ] contracts.md
- [ ] security.md
- [ ] testing.md
- [ ] deployment.md

### 3) Windows Implementation Constraints
- **Runtime**: [Node/Electron, Python if needed, Windows Services]
- **Data Storage**: [SQLite, file logs, cache, registry]
- **Services**: [Windows Service, System Tray app, Event Log integration]
- **File System**: [%AppData% usage, local folders, encryption requirements]
- **Performance Target**: [latency/throughput requirements]
- **Security Requirements**: [key handling, secrets management, permissions]

---

# OUTPUT FORMAT REQUIRED

## A) Primary MD File Specification
```markdown
### Feature Name: [Clear, descriptive name]
- **Purpose**: [What this feature accomplishes]
- **Scope**: 
  - **In**: [What's included in this feature]
  - **Out**: [What's explicitly not included]
- **Windows Implementation**: 
  - [How this works on Windows desktop]
  - [Technologies and approaches used]
- **Key Functions**:
  - [Function 1]: [Description]
  - [Function 2]: [Description]
  - [Function 3]: [Description]
- **Data Model** (if applicable):
  - [Database tables, file structures, etc.]
- **Error Handling**:
  - [How errors are caught and handled]
- **Performance Targets**:
  - [Speed/throughput requirements]
- **Telemetry & Observability**:
  - [Metrics, logging, monitoring]
- **Acceptance Criteria (Definition of Done)**:
  - [ ] [Criterion 1]
  - [ ] [Criterion 2]
  - [ ] [Criterion 3]
```

## B) Secondary MD File Integration Notes
For each referenced MD file, provide:

```markdown
### [filename].md — Integration Notes
- **What to Expose/Consume**: [APIs, events, data]
- **UI/UX Impact** (if dashboard.md): [Widget descriptions]
- **Configuration Keys** (if config.md): [Settings needed]
- **Tests to Add** (if testing.md): [Test scenarios]
- **Security Controls** (if security.md): [Security measures]
- **Deployment Impact** (if deployment.md): [Installation effects]
- **Documentation Needed** (if docs.md): [User guides, references]
```

## C) Dependencies & Interfaces
- **Upstream Dependencies**: [What this feature needs]
- **Downstream Consumers**: [What depends on this feature]
- **Interfaces/APIs/Events**: [How components communicate]
- **Failure Modes and Fallbacks**: [What happens when things break]

## D) Priority & Development Milestones
- **Priority**: [P0 | P1 | P2 | P3]
- **Milestone 1** (2-3 days): [Initial implementation]
- **Milestone 2** (2-3 days): [Integration and testing]
- **Milestone 3** (2-3 days): [Polish and documentation]
- **Rollout Plan**: [Feature flag | Internal testing | Beta | General availability]

## E) Risks & Mitigations
- **Risk 1**: [Potential issue]
  - **Mitigation**: [How to address it]
- **Risk 2**: [Potential issue]
  - **Mitigation**: [How to address it]

---

# FULLY WORKED EXAMPLE

## Your Input (Example: Batch Logging)

### 1) Original Component Analysis
- **Component Name**: Batch Logging & Execution Tracking
- **Component Type**: Feature
- **Original Purpose**: Track arbitrage execution batches, outcomes, and performance metrics from backend/engine/data/batch-logs/
- **Criticality**: P0

### 2) Feature Identification Request
**PRIMARY OWNER**: ✅ backend.md

**SECONDARY REFERENCES**: 
- ✅ dashboard.md
- ✅ config.md
- ✅ docs.md
- ✅ testing.md
- ✅ security.md

### 3) Windows Implementation Constraints
- **Runtime**: Electron desktop app + backend Node service
- **Data Storage**: SQLite for structured events + rolling file logs
- **Services**: Optional Windows Service for continuous backend operation
- **File System**: %AppData%/ApexArbitrage/logs (rotating), %AppData%/ApexArbitrage/db (SQLite)
- **Performance Target**: Append logs <= 2ms per event; queries < 50ms for last 10k events
- **Security Requirements**: Log redaction for secrets; role-based access to export

## Expected Output

### A) backend.md — Primary Specification
```markdown
### Feature Name: Execution Batch Logging
- **Purpose**: Provide durable, queryable, real-time visibility into trade batches, decisions, and outcomes for operations, analytics, compliance, and incident response.
- **Scope**:
  - **In**: Structured event capture, rotating file logs, SQLite aggregates, event streaming to dashboard
  - **Out**: Strategy analytics, PnL attribution (covered by separate features)
- **Windows Implementation**:
  - Event capture in-process with async non-blocking writers
  - Dual-write: SQLite (primary analytics) + rolling file logs (forensic/backup)
  - Optional Windows Service for headless operation
- **Key Functions**:
  - `recordBatchStart()`: Initialize new batch tracking
  - `recordTradeAttempt()`: Log trade execution attempts
  - `recordBatchEnd()`: Complete batch with final status
  - `queryRecentBatches(limit)`: Retrieve recent batch data
  - `periodicCompaction()`: Manage log rotation and cleanup
- **Data Model**:
  - Tables: `batches(id, ts_start, ts_end, status, chain, strategy, pnl)`
  - Tables: `events(id, batch_id, ts, severity, kind, payload_json)`
- **Error Handling**:
  - Circuit-breaker on DB errors with file-only fallback
  - Backpressure handling when disk space low
  - Automatic redaction of sensitive data in logs
- **Performance Targets**:
  - Sustained 2k events/sec on standard hardware
  - <50ms p95 query time for recent aggregates
- **Telemetry & Observability**:
  - Metrics: events/sec, errors/sec, write latency, queue depth
  - Health endpoint for dashboard monitoring
- **Acceptance Criteria**:
  - [ ] 95%+ test coverage on core writers
  - [ ] 24h soak test without data loss
  - [ ] Log rotation verified under load
  - [ ] Export produces valid CSV/JSON output
```

### B) Secondary MD File Integration Notes

#### dashboard.md — Integration Notes
- **What to Expose/Consume**: Real-time event stream via WebSocket, batch metrics API
- **UI/UX Impact**: 
  - "Batch Stream" widget with severity/chain/strategy filters
  - Metrics cards: batches/hour, success rate, error rate, p95 latency
  - Export button for CSV/JSON download
  - Alert banners on error rate spikes

#### config.md — Integration Notes
- **Configuration Keys**:
  - `logging.level` (debug|info|warn|error)
  - `logging.retentionDays` (default: 30)
  - `logging.dbPath` (default: %AppData%/ApexArbitrage/logs.db)
  - `logging.maxFileMB` (default: 100)
  - `logging.service.enabled` (default: false)

#### docs.md — Integration Notes
- **Documentation Needed**:
  - Troubleshooting guide: where to find logs, export procedures
  - Operator runbook for incident response and log analysis
  - Performance tuning guide for high-frequency scenarios

#### testing.md — Integration Notes
- **Tests to Add**:
  - Unit tests: writer fallbacks, data redaction, rotation logic
  - Integration tests: 2k events/sec soak test, database lock contention
  - Performance tests: p95 latency validation, large aggregate queries

#### security.md — Integration Notes
- **Security Controls**:
  - Automatic redaction of secrets and private keys in log payloads
  - Optional AES encryption at rest for SQLite and log files
  - Role-based access control for export and deletion operations

### C) Dependencies & Interfaces
- **Upstream Dependencies**: Backend execution engine, strategy modules, order routing system
- **Downstream Consumers**: Dashboard widgets, analytics jobs, operator alert system
- **Interfaces**: WebSocket event stream to dashboard; REST API for queries and exports
- **Failure Modes**: DB unavailable → file-only mode; disk full → backpressure + operator alert

### D) Priority & Development Milestones
- **Priority**: P0 (Critical for MVP)
- **Milestone 1**: Database schema + basic writers + log rotation (3 days)
- **Milestone 2**: Dashboard integration + query API + metrics (3 days)
- **Milestone 3**: Testing suite + soak testing + export + documentation (3 days)
- **Rollout Plan**: Feature flag → internal testing → default enabled

### E) Risks & Mitigations
- **Risk 1**: High event volume causing UI lag and performance issues
  - **Mitigation**: Implement ring buffer + sampling for UI; decouple display from storage
- **Risk 2**: Uncontrolled disk growth from logging data
  - **Mitigation**: Strict rotation policy + retention limits + disk usage monitoring + operator warnings

---

# PRIORITY SCALE REFERENCE

- **P0**: Required for MVP stability and basic operability
- **P1**: High business value, implement in near-term roadmap  
- **P2**: Important functionality, can be implemented after core features
- **P3**: Nice-to-have enhancements, implement when resources allow

# RESPONSE CONTRACT

**What you'll receive every time:**
- One complete "Primary MD File Spec" ready to copy-paste into the target MD file
- Short "Integration Notes" sections for every referenced secondary MD file
- Clear Windows-specific implementation details and technical requirements
- Complete dependencies, risks, milestones, and rollout planning
- Acceptance criteria that define when the feature is complete and ready

---

**Ready to use! Copy this prompt, fill in your component details, and receive complete Windows desktop feature specifications.**