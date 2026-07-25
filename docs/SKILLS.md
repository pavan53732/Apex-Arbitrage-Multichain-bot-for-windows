# APEX Bot Skills - Registry, Capabilities, and Lifecycle

> **Version:** 2.0.0 | **Last Updated:** July 25, 2026

---

## 1. Overview

A Skill is a discrete, composable capability. Skills orchestrate multiple AI
agent calls, data transformations, and optional on-chain actions. Registered
in Skill Registry with metadata, user-toggleable, versioned.

**Skill vs Agent:** Agent is a single AI persona. Skill is a higher-level capability using multiple agents.

---

## 2. Skill Metadata Schema

- skill_id, name, version, description, category
- required_agents[], inputs (JSON schema), outputs (JSON schema)
- chains[] (e.g., [1, 56, 137, 42161]), enabled, priority
- cooldown_ms, max_concurrent, created_at, updated_at, author

---

## 3. Core Skills

### Arbitrage Skills
- **intra-chain-arb:** Scans DEXs on single chain. Agents: market-analyst, opportunity-scanner
- **cross-chain-arb:** Cross-chain via bridges. Agents: market-analyst, opportunity-scanner, risk-assessor
- **triangular-arb:** A to B to C to A paths. Agents: opportunity-scanner
- **flash-loan-arb:** Zero-capital flash loan trades. Agents: opportunity-scanner, execution-planner, risk-assessor

### Analysis Skills
- **market-sentiment:** News/social/on-chain sentiment. Agents: sentiment-analyst, market-analyst
- **liquidity-depth:** Pool depth and max tradeable size. Agents: market-analyst
- **gas-optimization:** Gas timing and pricing. Agents: market-analyst

### Risk Skills
- **pre-trade-risk:** Pre-trade evaluation. Agents: risk-assessor, anomaly-detector
- **portfolio-risk-monitor:** Continuous monitoring. Agents: risk-assessor, portfolio-optimizer
- **anomaly-circuit-breaker:** Anomaly detection plus circuit breaker. Agents: anomaly-detector

### Execution Skills
- **smart-order-routing:** Optimal DEX routing. Agents: execution-planner
- **mev-protection:** Flashbots/private mempools. Agents: execution-planner, anomaly-detector
- **bridge-execution:** Cross-chain bridge transfers. Agents: execution-planner, risk-assessor

### Learning Skills
- **trade-review:** Performance insights. Agents: learning-agent
- **strategy-calibration:** Parameter adjustment. Agents: learning-agent, portfolio-optimizer

---

## 4. Skill Lifecycle

1. **Registration:** Metadata defined, agents verified, schemas validated
2. **Activation:** Trigger met, cooldown elapsed, concurrency available
3. **Execution:** Inputs validated, agents orchestrated, outputs validated
4. **Completion:** Logged, cooldown started, metrics updated
5. **Error:** Retry per circuit breaker, timeout 60s default, partial results with flags

---

## 5. User Management

- View skills by category, enable/disable, view metadata
- Execution history and success rates
- Configure parameters (thresholds, cooldowns)
- Create custom skills (advanced), export/import configs

---

*Skills are actionable capabilities. Well-defined, testable, composable.*
