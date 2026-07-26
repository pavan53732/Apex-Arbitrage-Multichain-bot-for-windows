# APEX Strategy Framework

> **Version:** 1.0.0 | **Last Updated:** July 25, 2026 | **Scope:** Strategy Interfaces, Lifecycle, Built-ins, Custom Extensions

---

## 1. Overview

Strategies are the profit-generation modules of APEX. They define how the system identifies, scores, validates, and forwards potential opportunities into the simulation, risk, and execution pipeline.

A strategy is not allowed to execute trades directly. It produces candidate opportunities that must pass shared validation, simulation, and risk controls.

---

## 2. Design Goals

- pluggable and independently enabled/disabled
- consistent lifecycle across all strategy types
- shared contract for observability and testing
- separation between detection logic and execution authority
- compatibility with AI-assisted ranking without depending on AI correctness

---

## 3. Strategy Lifecycle

```text
idle
  -> scheduled
  -> scanning
  -> opportunity_found
  -> validation
  -> simulation
  -> risk_review
  -> approved | rejected
  -> queued_for_execution | archived
  -> idle
```

### 3.1 Lifecycle Rules

- scanning must be repeatable and time-bounded
- validation must be deterministic where possible
- rejection reasons must be typed and logged
- approved opportunities expire after a TTL if not executed

---

## 4. Core Interface

```ts
export interface IStrategy {
  id: string;
  name: string;
  kind: 'intra-chain' | 'cross-chain' | 'triangular' | 'flash-loan' | 'stablecoin' | 'oracle-divergence' | 'custom';
  version: string;
  enabled: boolean;
  supportedChains(): number[];
  requiredAdapters(): string[];
  defaultConfig(): StrategyConfig;
  validateConfig(config: StrategyConfig): ValidationResult;
  scan(ctx: StrategyContext): Promise<Opportunity[]>;
  score?(ctx: StrategyContext, opportunities: Opportunity[]): Promise<Opportunity[]>;
  explain?(opportunity: Opportunity): StrategyExplanation;
}
```

### 4.1 Supporting Types

```ts
export interface StrategyConfig {
  minProfitUsd: number;
  maxPositionUsd: number;
  maxSlippageBps: number;
  enabledDexes: string[];
  enabledChains: number[];
  cooldownMs?: number;
  custom?: Record<string, unknown>;
}

export interface Opportunity {
  id: string;
  strategyId: string;
  chainPath: number[];
  tokenPath: string[];
  venuePath: string[];
  grossProfitUsd: number;
  estimatedGasUsd: number;
  estimatedFeesUsd: number;
  netProfitUsd: number;
  confidence?: number;
  expiresAt: number;
  metadata: Record<string, unknown>;
}
```

---

## 5. Shared Validation Pipeline

Every strategy output enters the same system pipeline:

1. schema validation
2. freshness/TTL validation
3. adapter availability check
4. profitability floor check
5. slippage and liquidity sanity check
6. simulation
7. risk-engine review
8. execution queue or rejection

This shared pipeline ensures all strategies meet the same minimum safety bar.

---

## 6. Built-In Strategy Types

### 6.1 Intra-Chain Arbitrage

Searches for price discrepancies between venues on the same chain.

Typical inputs:

- pool reserves
- fees
- token decimals
- gas estimate
- route depth constraints

Strengths:

- lower operational complexity than cross-chain flows
- no bridge latency
- easier deterministic simulation

Primary risks:

- stale reserves
- gas spikes
- route contention and MEV

### 6.2 Cross-Chain Arbitrage

Searches for profitable price differences across chains, including bridge costs and time assumptions.

Additional requirements:

- bridge adapters
- bridge fee estimation
- latency and settlement modelling
- higher confidence thresholds than same-chain flows

### 6.3 Triangular Arbitrage

Looks for profitable cycles such as `A -> B -> C -> A` on one chain across one or more DEXes.

Best suited when:

- liquidity is deep enough across all hops
- execution cost remains low relative to route edge
- reserve changes are frequent but measurable

### 6.4 Flash-Loan Arbitrage

Uses temporary borrowed capital inside one atomic transaction.

Additional requirements:

- flash-loan provider adapter
- repayment validation
- transaction atomicity support
- strict simulation before approval

### 6.5 Stablecoin Cycle Arbitrage

Targets smaller spread inefficiencies among stable assets and wrapped variants.

Characteristics:

- lower per-trade edge
- higher frequency potential
- stronger sensitivity to fees and slippage

### 6.6 Oracle Divergence Monitoring

Detects mismatches between market prices and reference/oracle signals that may imply a tradable dislocation or a safety warning.

This strategy can be profit-seeking or purely defensive depending on configuration.

---

## 7. Strategy Configuration

### 7.1 Required Baseline Fields

| Field | Purpose |
|------|---------|
| `minProfitUsd` | Global per-opportunity profit floor |
| `maxPositionUsd` | Capital cap for a single opportunity |
| `maxSlippageBps` | Execution tolerance |
| `enabledDexes` | Venue allowlist |
| `enabledChains` | Chain allowlist |
| `cooldownMs` | Minimum delay between repeated scans or executions |

### 7.2 Strategy-Specific Extensions

Each strategy may add additional fields under `custom`, but these must still be schema-validated and documented.

Examples:

- `maxBridgeMinutes`
- `maxHopCount`
- `flashLoanProviders`
- `oracleDeviationThresholdBps`

---

## 8. Strategy Registry

Strategies should be registered through a central registry rather than imported ad hoc.

```ts
class StrategyRegistry {
  register(strategy: IStrategy): void;
  list(): IStrategy[];
  get(id: string): IStrategy | undefined;
  enabled(): IStrategy[];
}
```

Benefits:

- consistent discovery
- UI integration for enable/disable and configuration
- simplified testing and dependency inspection

---

## 9. Interaction with Agents and Skills

Strategies may request AI assistance for ranking, explanation, or anomaly detection, but not for final execution authority.

Representative agent interactions:

| Agent | Role |
|------|------|
| Opportunity Scanner | enrich and rank detected candidates |
| Risk Assessor | provide advisory risk score and explanation |
| Gas Forecaster | improve execution cost estimate |
| Execution Supervisor | track post-approval lifecycle |

AI output remains advisory unless converted into typed intermediate data and approved by deterministic guards.

---

## 10. Custom Strategy Development

### 10.1 Development Steps

1. implement `IStrategy`
2. define config schema
3. declare required adapters
4. emit typed `Opportunity` records
5. add tests for scan logic and edge cases
6. register strategy with the registry
7. document UI configuration fields

### 10.2 Minimum Quality Bar

A custom strategy should not be accepted unless it has:

- clear profitability model
- deterministic validation steps
- test coverage for happy path and key failure paths
- observability fields for logs and dashboard display

---

## 11. Rejection Reason Taxonomy

Representative rejection codes:

- `PROFIT_BELOW_THRESHOLD`
- `LIQUIDITY_INSUFFICIENT`
- `SLIPPAGE_TOO_HIGH`
- `SIMULATION_FAILED`
- `RISK_SCORE_TOO_HIGH`
- `ADAPTER_UNAVAILABLE`
- `STALE_MARKET_DATA`
- `OPPORTUNITY_EXPIRED`

A typed rejection taxonomy is important for debugging strategy quality and tuning false positives.

---

## 12. Testing Expectations

Each strategy should have:

- unit tests for route construction and profitability maths
- integration tests with mocked chain and DEX adapters
- simulation tests for edge slippage and fee changes
- regression fixtures for previously false-positive opportunities

---

## 13. Future Extensions

Potential future strategy families:

- statistical arbitrage
- basis/funding arbitrage
- market-making assistance
- liquidity migration detection
- non-EVM strategy adapters

These should adopt the same registry and validation model rather than invent a second execution path.

---

The strategy framework is the main extensibility surface for profit generation. It must remain modular, typed, and subordinate to shared safety controls.
