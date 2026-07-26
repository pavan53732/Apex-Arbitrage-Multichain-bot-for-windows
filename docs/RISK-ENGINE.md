# APEX Risk Engine

> **Version:** 1.0.0 | **Last Updated:** July 25, 2026 | **Scope:** Pre-Trade Risk, Exposure Controls, Circuit Breakers, Drawdown Management

---

## 1. Overview

The Risk Engine is the gating layer between opportunity detection and execution. Its responsibility is to prevent otherwise profitable-looking opportunities from being executed when the downside profile is unacceptable.

The Risk Engine must remain authoritative even when AI scoring is used elsewhere. AI may assist explanation and enrichment, but deterministic controls decide whether execution is allowed.

---

## 2. Placement in the Pipeline

```text
market data
  -> strategy scan
  -> opportunity candidate
  -> simulation
  -> risk engine
  -> approved / rejected
  -> execution queue
```

Depending on implementation details, some lightweight risk checks may also run before full simulation to reduce wasted compute.

---

## 3. Risk Objectives

- cap downside per trade
- cap aggregate exposure across chains and strategies
- reject low-confidence or low-liquidity opportunities
- halt execution during abnormal market or system states
- produce auditable reasons for every rejection

---

## 4. Risk Dimensions

Recommended base dimensions:

| Dimension | Description |
|----------|-------------|
| Liquidity risk | Depth insufficient for expected size or likely slippage |
| Contract risk | Smart-contract counterparty or integration hazard |
| MEV risk | Front-running, sandwiching, or route contention likelihood |
| Oracle/reference risk | Reference price uncertainty or divergence |
| Bridge risk | Settlement and custody risk in cross-chain flows |
| Network risk | Congestion, reorg probability, RPC instability, gas volatility |

---

## 5. Scoring Model

A practical v1 approach is a weighted additive score with hard-stop overrides.

```text
total_risk_score =
  liquidity_weight * liquidity_score +
  contract_weight  * contract_score +
  mev_weight       * mev_score +
  oracle_weight    * oracle_score +
  bridge_weight    * bridge_score +
  network_weight   * network_score
```

### 5.1 Interpretation

| Score Range | Meaning | Default Action |
|------------|---------|----------------|
| 0.00 - 0.29 | Low risk | eligible |
| 0.30 - 0.59 | Moderate risk | eligible only if profit/confidence exceed configured thresholds |
| 0.60 - 0.79 | High risk | reject unless explicitly allowed by specialized config |
| 0.80 - 1.00 | Extreme risk | hard reject |

### 5.2 Hard Stops

Regardless of aggregate score, reject if any of the following is true:

- estimated net profit below threshold
- slippage exceeds configured maximum
- simulation fails
- bridge or flash-loan dependency unavailable
- circuit breaker is open
- wallet exposure limit would be exceeded

---

## 6. Position Sizing

### 6.1 Goals

Position sizing controls how much capital is committed even when an opportunity is approved.

### 6.2 Inputs

- current wallet balance
- strategy-specific max position
- current drawdown state
- chain-specific exposure cap
- confidence-adjusted expected value

### 6.3 Policy Options

| Policy | Use |
|-------|-----|
| Fixed cap | simple, safe default |
| Percent-of-portfolio | scales automatically with capital |
| Kelly-inspired | advanced, requires reliable edge estimate |
| Volatility-adjusted | reduce size when conditions become unstable |

Recommended v1: fixed cap plus percent-of-portfolio ceiling.

---

## 7. Exposure Limits

Representative controls:

| Limit | Purpose |
|------|---------|
| Max single trade USD | prevent concentrated loss |
| Max per-chain exposure | reduce chain-specific event risk |
| Max per-strategy exposure | avoid one strategy dominating capital |
| Max open positions | cap operational complexity |
| Max bridge in-flight capital | control cross-chain settlement exposure |

These limits should be user-configurable with safe defaults.

---

## 8. Drawdown Controls

### 8.1 Required Controls

- daily loss limit
- rolling drawdown limit
- strategy-specific drawdown limit
- forced cooldown after repeated failed executions

### 8.2 Example Behaviour

- daily drawdown breached -> halt new execution until next reset window
- strategy drawdown breached -> disable affected strategy only
- repeated execution failure burst -> open execution circuit breaker

---

## 9. Stop-Loss and Take-Profit Logic

For atomic arbitrage, pre-trade controls matter more than discretionary exits. Still, post-trade controls can matter for inventory-bearing or non-atomic flows.

Applicable cases:

- partially hedged positions
- bridge settlement windows
- market-making or future strategy families

Required features when applicable:

- explicit stop-loss trigger model
- explicit take-profit rules
- timeout exits for stale open state

---

## 10. Volatility Management

Volatility directly changes slippage, gas competitiveness, and execution uncertainty.

Recommended responses to elevated volatility:

- raise required net profit threshold
- reduce position size
- shorten opportunity TTL
- increase simulation strictness
- temporarily disable fragile strategy classes

---

## 11. Circuit Breakers

### 11.1 Levels

| Level | Scope |
|------|-------|
| Provider breaker | one AI provider or RPC provider |
| Strategy breaker | one strategy family |
| Execution breaker | all trade submission |
| Global breaker | full system halt except monitoring |

### 11.2 Trigger Examples

- repeated simulation failures above threshold
- sudden gas spike above configured band
- consecutive failed submissions
- abnormal oracle divergence
- major provider outage in critical dependency path

### 11.3 Reset Rules

- automatic cooldown expiry for some local failures
- manual operator reset for severe or unclear incidents
- health-check-based half-open retry for provider-specific breakers

---

## 12. Emergency Shutdown

A global emergency halt should:

- stop new trade execution
- optionally stop scanning or keep scanning read-only
- preserve logs and current state
- surface a clear operator message and reason code

Triggers may include:

- suspicious wallet behaviour
- critical dependency compromise
- extreme drawdown
- operator-issued manual halt

---

## 13. Monitoring and Metrics

Required risk metrics for the dashboard:

- current portfolio exposure
- per-chain exposure
- open opportunities awaiting approval
- current drawdown
- recent rejection reasons
- circuit breaker states
- consecutive failure counts

These metrics should be observable without reading logs directly.

---

## 14. AI-Assisted Risk Review

AI can contribute in advisory roles such as:

- textual explanation of why a route appears risky
- anomaly pattern detection across historical failures
- confidence calibration support

AI must not override deterministic hard stops.

---

## 15. Rejection Reason Taxonomy

Representative reasons:

- `RISK_SCORE_TOO_HIGH`
- `MAX_POSITION_EXCEEDED`
- `CHAIN_EXPOSURE_EXCEEDED`
- `DAILY_DRAWDOWN_LIMIT`
- `SIMULATION_FAILED`
- `VOLATILITY_TOO_HIGH`
- `CIRCUIT_BREAKER_OPEN`
- `MEV_RISK_UNACCEPTABLE`

Typed rejection reasons are essential for tuning and observability.

---

## 16. Testing Requirements

The Risk Engine should be tested with scenarios covering:

- profitable but high-risk opportunities
- low-liquidity edge cases
- repeated failure bursts opening breakers
- drawdown threshold transitions
- per-chain and per-strategy exposure saturation

---

## 17. Future Evolution

Potential future additions:

- historical risk model calibration
- adaptive thresholds by market regime
- strategy covariance modelling
- anomaly detection from execution traces
- hardware-wallet-aware operational policies

---

The Risk Engine is the project’s safety governor. It is valuable only if it can reject apparently attractive opportunities consistently, explain why, and remain authoritative under pressure.
