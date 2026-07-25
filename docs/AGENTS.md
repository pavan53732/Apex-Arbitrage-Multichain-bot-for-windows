# APEX AI Agents - Definitions, Roles, and Communication Protocols

> **Version:** 2.0.0 | **Last Updated:** July 25, 2026

---

## 1. Agent System Overview

APEX uses a modular AI agent architecture. Each agent is a specialized unit
that handles a specific aspect of the arbitrage workflow. Agents are
prompt-engineered personas executing via cloud AI API calls.

### Agent Lifecycle
1. **Registration:** Registered in Agent Registry with metadata
2. **Activation:** Activated when relevant task arrives
3. **Execution:** Receives structured prompt via AI Pipeline
4. **Response:** Returns structured output (JSON schema enforced)
5. **Deactivation:** Releases context after completion
6. **Logging:** Interaction logged (no API keys)

---

## 2. Agent Registry Schema

- agent_id, name, role, system_prompt
- input_schema, output_schema (JSON)
- provider_preference (openai, anthropic, any)
- model_preference (gpt-4o, claude-sonnet-4-20250514, etc.)
- temperature (0.0-1.0), max_tokens, priority, enabled

---

## 3. Core Agents

### 3.1 Market Analyst (market-analyst)
- **Role:** Analyzes real-time market data across DEXs and chains
- **Inputs:** Token pair, chain list, prices, order book depth, volume
- **Outputs:** Market score (0-100), trend, volatility, liquidity assessment
- **Temperature:** 0.2

### 3.2 Opportunity Scanner (opportunity-scanner)
- **Role:** Identifies and ranks arbitrage opportunities
- **Inputs:** Price feeds, gas prices, bridge fees, slippage estimates
- **Outputs:** Ranked opportunities with profit, risk score, execution path
- **Temperature:** 0.1

### 3.3 Risk Assessor (risk-assessor)
- **Role:** Evaluates risk for each opportunity
- **Inputs:** Opportunity details, portfolio state, historical loss data
- **Outputs:** Risk score (0-100), position size, stop-loss, go/no-go
- **Temperature:** 0.1

### 3.4 Execution Planner (execution-planner)
- **Role:** Plans optimal execution strategy
- **Inputs:** Approved opportunity, liquidity, gas, MEV risk
- **Outputs:** Execution steps, tx ordering, gas strategy, timing
- **Temperature:** 0.2

### 3.5 Sentiment Analyst (sentiment-analyst)
- **Role:** Analyzes market sentiment from news, social, on-chain data
- **Inputs:** News, social signals, whale movements, funding rates
- **Outputs:** Sentiment score (-100 to +100), key events, confidence
- **Temperature:** 0.4

### 3.6 Portfolio Optimizer (portfolio-optimizer)
- **Role:** Optimizes allocation across chains and strategies
- **Inputs:** Portfolio, performance history, risk tolerance, capital
- **Outputs:** Allocation, rebalancing actions, chain distribution
- **Temperature:** 0.3

### 3.7 Anomaly Detector (anomaly-detector)
- **Role:** Detects unusual conditions, exploits, system errors
- **Inputs:** Price feeds, tx patterns, contract events, health metrics
- **Outputs:** Anomaly flag, severity, description, action
- **Temperature:** 0.1

### 3.8 Learning Agent (learning-agent)
- **Role:** Reviews past trades, extracts lessons
- **Inputs:** Trade history, P&L, market conditions, outcomes
- **Outputs:** Pattern insights, strategy adjustments, calibration
- **Temperature:** 0.5

---

## 4. Communication Protocol

### Message Envelope
- envelope_version, message_id (UUID), timestamp (ISO 8601)
- source_agent, target_agent, message_type, priority (1-5)
- payload (structured), correlation_id

### Orchestration Patterns
- **Sequential:** Market Analyst -> Opportunity Scanner -> Risk Assessor -> Execution Planner
- **Parallel Fan-Out:** Orchestrator -> [Market Analyst, Sentiment Analyst, Anomaly Detector] -> Orchestrator
- **Conditional:** Risk Assessor -> (score < 30) -> Execute; (score >= 30) -> Reduce size
- **Feedback Loop:** Learning Agent -> Strategy Engine -> next cycle

### Error Handling
- Timeout (30s): retry once, then skip
- Malformed: validate schema, retry with correction
- Provider failure: AI Pipeline handles failover
- Circuit breaker: 3 consecutive failures -> disable 5 min

---

## 5. User Configuration

- Enable/disable agents, adjust temperature, set max tokens
- Choose preferred provider per agent
- View interaction logs, reset to defaults

---

## 6. Adding New Agents

1. Define metadata (ID, name, role, schemas)
2. Write system prompt with output format
3. Register in Agent Registry
4. Add to orchestration workflow
5. Add UI toggle in AI Settings
6. Document here, test with samples

---

*Agents are the intelligence layer. Each must be focused and produce structured output.*
