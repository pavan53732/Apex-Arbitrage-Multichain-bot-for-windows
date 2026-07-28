---
type: CONTRACT
owner: Quality Team
status: Canonical
version: 1.0.0
purpose: Defines the complete testing strategy — unit testing, integration testing, contract testing, state-machine testing, chaos testing, load testing, performance testing, recovery testing, security testing, end-to-end testing, Windows-specific testing, and cross-subsystem integration. See TESTING-GUIDE.md for detailed implementation guidance.
scope: None
last_updated: 2026-07-29
canonical_source: docs/TESTING.md
---

# Testing

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.0 | **Status:** Canonical | **Last Updated:** 2026-07-27 | **Owner:** Quality Team

## Purpose
Defines the complete testing strategy — unit testing, integration testing, contract testing, state-machine testing, chaos testing, load testing, performance testing, recovery testing, security testing, end-to-end testing, Windows-specific testing, and cross-subsystem integration. See TESTING-GUIDE.md for detailed implementation guidance.

---

## 1. Test Pyramid

| Layer | Primary Tools | Purpose | Coverage Target | Frequency |
|------|---------------|---------|----------------|-----------|
| **Unit** | Vitest | Pure logic, schema validation, utility behavior | 80%+ on critical logic | Every PR |
| **Integration** | Vitest + test DB + mocked services | Service boundaries, repositories, IPC handlers | 60%+ on service boundaries | Every PR |
| **Contract** | Vitest + schema validators | API contracts, event schemas, IPC message contracts | 100% on published contracts | Every PR |
| **State Machine** | Vitest + state machine test harness | State transition validation, forbidden path checks | 100% on all state machines | Every PR |
| **E2E UI** | Playwright + Electron | Real user flows through packaged app | 100% on critical flows | Nightly |
| **Security** | Custom harness + OWASP tools | Auth, permission, trust boundary enforcement | 100% on security boundaries | Nightly |
| **Recovery** | Custom crash simulation | Crash resume, sleep/resume, network recovery | 100% on recovery paths | Weekly |
| **Chaos** | Custom failure injection | Random subsystem failure, network partition | Key failure scenarios | Weekly |
| **Load** | Custom load generator | Throughput, queue depth, resource exhaustion | Target SLO thresholds | Monthly |
| **Performance** | Custom benchmarking | Latency, throughput, resource usage benchmarks | Target SLO thresholds | Monthly |

---

## 2. Unit Testing

### 2.1 Required Test Areas

| Area | Examples | Minimum Tests |
|------|---------|---------------|
| **Config validators** | Schema validation, default values, type checks | Per config key |
| **Provider adapters** | Request mapping, response parsing, error handling | Per adapter |
| **Strategy profit calculations** | Net profit, gas deduction, fee calculation | Per strategy |
| **Risk scoring functions** | Score formula, threshold evaluation, reject reasons | Per risk check |
| **Repository mapping helpers** | Entity-to-row mapping, query builders | Per repository |
| **Cache eviction rules** | TTL-based, LRU, priority-based eviction | Per cache type |
| **Token budgeting** | Token allocation, pruning, compression logic | Per budget type |
| **Event schema validation** | Schema conform, invalid rejection, version compatibility | Per event type |

### 2.2 Unit Test Rules

- Unit tests must be deterministic (no randomness, no I/O, no network).
- Unit tests must complete within 5ms each.
- Unit tests must not depend on other unit tests.
- All new code must have unit tests before merge.

---

## 3. Integration Testing

### 3.1 Required Integration Test Areas

| Area | Examples | Minimum Tests |
|------|---------|---------------|
| **IPC handler + validation + repository write** | Full request→validate→persist→respond chain | Per IPC handler |
| **Provider adapter + response parser + cache** | Live mock response → parse → cache store | Per provider |
| **Strategy output + risk-engine approval** | Strategy proposal → risk check → approve/reject | Per strategy |
| **Settings save + encrypted storage** | Config change → persist → verify on reload | Per config section |
| **Event publish → bus → consumer delivery** | Producer → event bus → consumer receives | Per event type |
| **Wallet sign → execution submit → confirm** | Full trade execution chain (mock chain) | Per chain type |
| **Plugin load → init → capability grant → sandbox** | Plugin lifecycle integration | Per capability |

### 3.2 Integration Test Database Strategy

- Use in-memory SQLite for each test suite (fast, isolated).
- Run migrations before each suite.
- Clean all tables between tests.
- Seed deterministic fixture data.
- No production database dependency.

---

## 4. Contract Testing

### 4.1 Contract Test Types

| Contract Type | What to Test | Tool | Frequency |
|-------------|-------------|------|-----------|
| **API contracts** | Request/response schema, error codes, auth | Vitest + schema validator | Every PR |
| **Event contracts** | Event payload schema, producer/consumer mapping | Vitest + event.schema.json | Every PR |
| **IPC contracts** | IPC message schema, permission per message | Vitest + IPC schema validator | Every PR |
| **State machine contracts** | Valid transitions, forbidden paths, recovery paths | Vitest + state machine harness | Every PR |
| **Configuration contracts** | Config key types, defaults, bounds, required/optional | Vitest + config.schema.json | Every PR |

### 4.2 Contract Test Rules

- Every published API must have a contract test.
- Every event type must have a schema validation test.
- Every state machine must have a transition coverage test.
- Contract tests must verify both conforming and non-conforming inputs.
- Contract failures block merge (hard gate).

---

## 5. State Machine Testing

### 5.1 State Machine Test Harness

For each state machine document (ENGINE, EXECUTION, WORKER, PLUGIN, SERVICE, AI, DASHBOARD-WORKSPACE):

| Test | Description | Required |
|------|-------------|----------|
| **All valid transitions** | Every transition in the state diagram must be reachable | Yes |
| **Forbidden paths** | Every transition NOT in the state diagram must be rejected | Yes |
| **Recovery paths** | Every failure → recovery path must be tested | Yes |
| **Timeout paths** | Every timeout → fallback path must be tested | Yes |
| **Crash resume** | State can be reconstructed after crash at every state | Yes |
| **Side effects** | Each transition emits expected events/persists expected data | Yes |

### 5.2 State Machine Test Example

```
describe('Execution State Machine', () => {
  it('valid transition: PENDING → SIGNING → SUBMITTING → IN_MEMPOOL → CONFIRMING → CONFIRMED', ...);
  it('forbidden: CONFIRMED → PENDING (cannot restart confirmed TX)', ...);
  it('timeout: IN_MEMPOOL → STUCK (no confirmation after timeout)', ...);
  it('recovery: STUCK → SUBMITTING (nonce replacement)', ...);
  it('crash resume: reconstruct SUBMITTING state from persisted data', ...);
  it('side effect: SIGNING → emit execution.submitted event', ...);
});
```

---

## 6. Chaos Testing

### 6.1 Chaos Scenarios

| Scenario | Failure Type | Expected Outcome | Recovery Test |
|---------|-------------|-----------------|---------------|
| **AI provider crash** | Kill AI provider process | AI falls back to next provider | Recovery: provider restored after health check |
| **Event bus queue overflow** | Flood bus with 10× normal volume | Drop oldest non-critical, keep critical | Recovery: queue drains, normal operation |
| **Database lock contention** | Multiple concurrent writes to same table | WAL mode handles contention gracefully | Recovery: no data loss |
| **Worker pool exhaustion** | All workers busy, queue backlog | Scale out + reject non-critical tasks | Recovery: workers free, backlog cleared |
| **Network partition** | Drop all network connections | Trading paused, offline mode | Recovery: network restored, resume trading |
| **Plugin sandbox crash** | Kill plugin sandbox process | Plugin enters CRASHED state, auto-restart once | Recovery: plugin RUNNING after restart |
| **Memory pressure** | Allocate 80%+ of max memory | P4 widgets suspended, Worker Pool reduced | Recovery: memory freed, widgets restored |
| **Config hot-reload failure** | Invalid config pushed | Config rejected, previous config maintained | Recovery: valid config applied |

---

## 7. Security Testing

### 7.1 Security Test Areas

| Area | What to Test | Frequency |
|------|-------------|-----------|
| **IPC permission enforcement** | Every IPC message rejected for unauthorized role | Every PR |
| **Trust boundary enforcement** | Cross-domain messages validated per trust boundary rules | Nightly |
| **Plugin sandbox isolation** | Plugin cannot access network, file system, secrets | Nightly |
| **Secret zeroing on sleep** | Secrets zeroed before sleep, re-auth on wake | Nightly |
| **AI context secret masking** | No secrets in AI context injection | Nightly |
| **Code signature verification** | Unsigned binaries rejected, tampered binaries rejected | Weekly |
| **Update chain verification** | Invalid signature → update rejected | Weekly |
| **STRIDE threat scenarios** | Each STRIDE threat has a test validating mitigation | Weekly |

---

## 8. Recovery Testing

| Scenario | Test | Expected Outcome |
|---------|------|-----------------|
| **Platform crash mid-trade** | Kill backend process during EXECUTING_LEG_1 | Recovery scan: Leg 1 confirmed → resume Leg 2 |
| **Platform crash mid-AI** | Kill backend during AI request | Pending AI requests cancelled, provider states reloaded |
| **Windows sleep/resume** | Simulate WM_POWERBROADCAST suspend/resume | Secrets zeroed, re-auth, RPC reconnect |
| **Network disconnect/reconnect** | Drop network for 60s | Trading paused, reconnect → resume |
| **Database corruption** | Corrupt SQLite file | Integrity check → repair or fallback to backup |
| **Workspace corruption** | Corrupt workspace JSON | Default workspace loaded |
| **Config hot-reload crash** | Invalid config causes crash | Previous config restored |

---

## 9. Performance Testing

### 9.1 Performance Benchmarks

| Metric | Target | Test Method | Frequency |
|--------|--------|------------|-----------|
| **Trade detection latency** | < 100ms from price update to opportunity | Unit benchmark | Monthly |
| **Risk check latency** | < 50ms per check | Unit benchmark | Monthly |
| **AI request latency** | < 10s end-to-end (with context assembly) | Integration benchmark | Monthly |
| **Event bus throughput** | > 5000 msg/s sustained | Load test | Monthly |
| **Dashboard render latency** | < 16ms per frame (P0 widgets) | Playwright benchmark | Monthly |
| **Database write latency** | < 5ms per insert | Integration benchmark | Monthly |
| **IPC round-trip** | < 5ms Main → Backend → Main | Integration benchmark | Monthly |
| **Startup time** | < 3s for P0-P2 widgets visible | E2E measurement | Monthly |

---

## 10. Windows-Specific Testing

| Test | Description | Expected | Frequency |
|------|-------------|----------|-----------|
| **Packaged Windows build launches** | MSIX installer → app starts | App visible, tray icon active | Every release |
| **DB migrations on upgrade** | Upgrade from v1 → v2 | All migrations succeed, data preserved | Every release |
| **Tray icon lifecycle** | Minimize → tray → restore | Tray icon visible, window restores | Nightly |
| **Sleep/resume** | Simulate Windows suspend/resume | Secrets zeroed, re-auth, state restored | Nightly |
| **Multi-monitor** | Move window to second monitor | Layout persists, DPI re-scales | Weekly |
| **DPI scaling** | Change monitor DPI from 100% → 150% | Layout adjusts, fonts re-scale | Weekly |
| **Portable mode** | Run from USB drive with portable marker | All paths relative, no registry writes | Weekly |
| **Auto-start** | Enable auto-start, restart Windows | App starts on login | Every release |
| **Windows service** | Install service, start via SCM | Service starts, backend accessible | Every release |
| **Crash dump** | Force crash, verify dump file created | Dump file at expected path | Weekly |
| **SmartScreen** | Verify signed installer bypasses SmartScreen | No warning on signed installer | Every release |
| **Windows Defender** | Verify app registered in exclusion list | Defender not blocking app | Every release |

---

## 11. Cross-Subsystem Integration

### 11.1 Test Responsibility Matrix

| Subsystem | Unit Tests | Integration Tests | Contract Tests | E2E Tests |
|-----------|-----------|-------------------|---------------|-----------|
| **Trading Engine** | Strategy, scoring | Trade flow chain | State machine, API | Critical operator flows |
| **Execution Engine** | TX preparation, retry logic | TX submit → confirm chain | State machine, API | Trade execution flow |
| **AI Pipeline** | Context assembly, pruning | AI request → response chain | API, event schema | Provider setup flow |
| **Event Bus** | Routing, dedup | Publish → subscribe chain | Message schema | Event stream display |
| **Dashboard** | Widget lifecycle, data binding | IPC → render chain | Widget contract | Critical UI flows |
| **Plugin System** | Capability check, sandbox | Plugin load → run chain | Manifest schema | Plugin install/uninstall |
| **Security** | Permission check, masking | IPC auth chain | Trust boundary | Auth, secret management |
| **Database** | Repository mapping | Persist → query chain | Schema integrity | Migration, backup |
| **Windows** | Tray, power handling | Process lifecycle | Service lifecycle | Install/uninstall |

### 11.2 Test Coverage Monitoring

| Metric | Target | Tool | Reporting |
|--------|--------|------|-----------|
| **Unit coverage (critical logic)** | 80%+ | Vitest coverage | CI report |
| **Integration coverage (boundaries)** | 60%+ | Vitest coverage | CI report |
| **Contract coverage (published APIs)** | 100% | Custom contract validator | CI gate |
| **E2E coverage (critical flows)** | 100% | Playwright coverage | Nightly report |
| **State machine coverage** | 100% | Custom harness | CI gate |

---

## Cross-References

- **TESTING-GUIDE.md** — Detailed implementation guidance, Vitest examples, Playwright setup.
- **TEST-CASE-REGISTRY.md** — Registered test case inventory.
- **SIMULATION-ENGINE.md** — Backtesting and simulation.
- **BACKTESTING.md** — Strategy backtesting methodology.
- **STRATEGIES.md** — Strategy definitions (test targets).
- **AI-PIPELINE.md** — AI test targets.
- **RUNTIME-OPERATIONS.md** — Runtime test targets.
- **MONITORING-OBSERVABILITY.md** — Test monitoring.
- **PERFORMANCE-SLOS.md** — Performance SLO targets.
- **SECURITY.md** — Security test targets.
- **THREADING-MODEL.md** — Threading test targets.
- **CONFIGURATION-REFERENCE.md** — Test config keys.
- **END-TO-END-WIRING-CONTRACT.md** — Cross-subsystem test wiring.
- **TRACEABILITY-MATRIX.md** — REQ-TEST-001.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-07-27 | Production-grade testing contract: 10-layer test pyramid, unit testing (8 areas + rules), integration testing (7 areas + DB strategy), contract testing (5 types + rules), state machine testing (6 test types + example), chaos testing (8 scenarios), security testing (8 areas), recovery testing (7 scenarios), performance testing (8 benchmarks), Windows-specific testing (12 tests), cross-subsystem integration (test responsibility matrix + coverage monitoring) | Quality Team |
| 0.1.0 | 2026-07-27 | Initial stub | Quality Team |
