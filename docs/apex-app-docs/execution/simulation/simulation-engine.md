---
metadata_schema_version: 1.0
document_id: DOC-0283
title: Simulation Engine
plane: Product Specification
domain: Execution
class: Specification
authority: Canonical
status: Active
owner: Trading Team
version: 2.0.0
canonical_source: docs/apex-app-docs/execution/simulation/simulation-engine.md
related_concepts:
  - CONCEPT-0283
dependencies: []
consumers:
  - DOC-0236
  - DOC-0418
  - DOC-0284
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-01
concept_role: Owner
owned_domains:
  - Execution
type: CONTRACT
purpose: "Defines paper trading, replay, stress testing, and synthetic failure simulation with explicit MVP Phase 1 primacy."
scope: "Backtesting, paper trading, and simulation for all MVP phases. **Phase 1 (current): simulation-only operation. Phase 2: real-time validation layer. Phase 3: pre-execution gate.**"
---

# Simulation Engine

## Document type
Document type: [CONTRACT]

## Version
**Version:** 2.0.0 | **Status:** Canonical | **Last Updated:** 2026-08-01 | **Owner:** Trading Team

## Purpose
Defines paper trading, replay, stress testing, and synthetic failure simulation — the authoritative execution validation layer for all MVP phases.

**CRITICAL: In Phase 1 (current), simulation engine is the PRIMARY execution mode. No live trades occur without simulation validation in any phase.**

---

## 0. MVP Phase Roles

### Phase 1 — Simulation-Only (CURRENT)
**Simulation Mode:** PAPER_TRADING | **Live Execution:** BLOCKED

**Simulation Engine Responsibilities:**
- Execute all detected opportunities in paper-trading mode
- Record hypothetical PNL with realistic slippage and gas
- Track execution latency and failure modes
- Generate performance reports for Phase 2 eligibility
- **Block all live execution via hard gating**

**Execution Boundaries:**
- ✅ Detect opportunities
- ✅ Score and rank
- ✅ Simulate execution
- ✅ Record PNL
- ❌ Sign transactions
- ❌ Broadcast to chain
- ❌ Move real funds

### Phase 2 — Operator-Approved
**Simulation Mode:** REALTIME_VALIDATION | **Live Execution:** REQUIRES_APPROVAL

**Simulation Engine Responsibilities:**
- Real-time simulation of every opportunity
- Pre-approval validation for operator review
- Confidence scoring based on historical simulation accuracy
- Post-execution reconciliation (simulated vs. actual)

### Phase 3 — Autonomous
**Simulation Mode:** PRE_EXECUTION_GATE | **Live Execution:** ENABLED

**Simulation Engine Responsibilities:**
- Mandatory pre-execution gate (must pass before auto-execution)
- Sub-100ms simulation latency requirement
- Confidence threshold for auto-approval
- Continuous learning from live execution outcomes

---

## 1. Simulation Modes

### 1.1 Paper Trading (Phase 1 Primary)
**Purpose:** Simulate all trading logic without live execution

**Inputs:**
- Real-time market data (prices, liquidity, gas)
- Strategy signals
- Risk engine scores

**Execution Flow:**
```
1. Receive opportunity from trading engine
2. Validate market data freshness (<5s old)
3. Execute simulated route:
   - Calculate input amount
   - Apply slippage model
   - Calculate output amount
   - Subtract gas costs
   - Compute net PNL
4. Record simulation result
5. Return to trading engine
```

**Outputs:**
- Simulated PNL: `simulated_pnl_usd`
- Execution latency: `latency_ms`
- Failure mode (if any): `failure_code`
- Confidence score: `confidence_0_to_1`

### 1.2 Historical Replay
**Purpose:** Backtest strategies on historical data

**Inputs:**
- Historical market snapshots
- Strategy configuration
- Initial capital

**Execution Flow:**
```
1. Load historical data (e.g., 30 days)
2. Replay tick-by-tick or bar-by-bar
3. Execute strategy logic at each step
4. Track cumulative PNL
5. Calculate performance metrics
```

**Outputs:**
- Cumulative PNL curve
- Win rate, loss rate
- Max drawdown
- Sharpe ratio, Sortino ratio

### 1.3 Stress Testing
**Purpose:** Validate system behavior under adverse conditions

**Stress Scenarios:**
- Market crash (-50% in 1 hour)
- Liquidity drought (pools dry up)
- Gas spike (10x normal)
- RPC failures (multiple providers down)
- DEX contract failures
- Oracle manipulation

**Outputs:**
- System behavior under stress
- Failure modes and recovery
- Capital preservation metrics

---

## 2. Determinism Rules

### 2.1 Reproducibility
**All Phases:** Mandatory

- Same inputs + same seed = same outcome
- Record: market snapshot, strategy config, code version, simulation seed
- Enable replay of any simulated trade

### 2.2 External Dependencies
**Phase 1:** External live dependencies DISABLED

- No live RPC calls during simulation
- Use cached or historical market data
- Gas estimates from historical averages
- Slippage from historical pool behavior

**Phase 2:** External dependencies ENABLED for validation

- Real-time RPC queries for validation
- Live gas estimates
- Real-time pool state

**Phase 3:** External dependencies MANDATORY

- Pre-execution validation with live data
- Sub-100ms latency requirement

---

## 3. Scenario Lifecycle

### 3.1 Scenario Definition
**Owner:** Simulation Engine

```yaml
scenario:
  id: "SCENARIO-001"
  type: "PAPER_TRADING"  # | HISTORICAL_REPLAY | STRESS_TEST
  market_snapshot:
    timestamp: "2026-08-01T06:00:00Z"
    chains: ["BSC", "Polygon"]
    dexes: ["PancakeSwap", "Uniswap"]
  strategy_config:
    min_profit_usd: 5.0
    max_slippage_pct: 0.5
  execution_config:
    simulated_gas_price_gwei: 3
    simulated_slippage_model: "HISTORICAL_P95"
```

### 3.2 Scenario Materialization
**Process:**
1. Load market data
2. Initialize strategy
3. Configure execution parameters
4. Set random seed for determinism
5. Begin simulation loop

### 3.3 Scenario Execution
**Phase 1:** Continuous loop
- Scan for opportunities
- Simulate each opportunity
- Record outcomes
- Update PNL

**Phase 2:** Real-time validation
- Validate opportunities before operator approval
- Compare simulated vs. actual post-execution

**Phase 3:** Pre-execution gate
- Must complete in <100ms
- Confidence threshold: >0.8 for auto-approval

### 3.4 Scenario Scoring
**Metrics:**
- Win rate: `wins / total_trades`
- Avg PNL per trade: `total_pnl / total_trades`
- Sharpe ratio: `avg_return / std_dev(returns)`
- Max drawdown: `max_peak_to_trough_decline`
- Simulation accuracy: `|simulated_pnl - actual_pnl| / actual_pnl`

### 3.5 Scenario Storage
**Persisted Data:**
- All simulated trades
- PNL curve
- Performance metrics
- Failure logs
- Market snapshots

### 3.6 Scenario Release
**Eligibility Criteria:**
- Phase 1 → Phase 2: 100+ trades, positive PNL, <1% failure
- Phase 2 → Phase 3: 500+ trades, positive PNL, <0.5% failure

---

## 4. Accuracy Metrics

### 4.1 Simulation vs. Actual
**Target (Phase 2+):**
- PNL accuracy: >95%
- Slippage accuracy: >90%
- Gas estimate accuracy: >85%

**Calculation:**
```
pnl_accuracy = 1 - |simulated_pnl - actual_pnl| / |actual_pnl|
slippage_accuracy = 1 - |simulated_slippage - actual_slippage| / actual_slippage
```

### 4.2 Phase 1 Validation
**No live execution, so accuracy measured against:**
- Historical execution data
- DEX aggregator quotes
- Third-party backtesting tools

---

## 5. Failure Modes

### 5.1 Data Failures
- **Stale market data:** Reject opportunity, log warning
- **Missing pool data:** Skip route, continue scanning
- **RPC timeout:** Retry once, then failover to backup

### 5.2 Execution Failures
- **Simulation timeout:** Reject opportunity (<100ms budget)
- **Calculation error:** Log anomaly, continue simulation
- **State inconsistency:** Pause simulation, alert operator

### 5.3 System Failures
- **Memory overflow:** Trigger garbage collection, reduce history window
- **Disk full:** Pause logging, alert operator
- **Corrupted state:** Restore from last checkpoint

---

## 6. Cross-Subsystem Contracts

### 6.1 Trading Engine
**Contract:**
- Trading engine sends opportunities to simulation
- Simulation returns within 100ms (Phase 3) or 500ms (Phase 2)
- Trading engine respects simulation results (no execution on failed simulation)

### 6.2 Risk Engine
**Contract:**
- Simulation provides inputs to risk engine
- Risk engine can veto simulation results
- Risk engine receives all simulation outcomes for learning

### 6.3 Execution Engine
**Phase 1:** Execution engine receives simulation-only payloads
**Phase 2:** Execution engine compares simulated vs. actual
**Phase 3:** Execution engine requires simulation pass before auto-execution

---

## Cross-references
- `../trading/trading-engine.md` — trading lifecycle and opportunity flow
- `../risk-policy/risk-engine.md` — risk validation gates
- `../transactions/execution-engine.md` — execution lifecycle
- `../../interfaces/api/domain-model.md` — simulation data schemas
- `../../operations/monitoring/metrics.md` — accuracy metrics
