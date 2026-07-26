# AI Pipeline

## Purpose
This document is the authoritative specification for AI decision lifecycle, prompt lifecycle, provider routing, confidence scoring, explainability, and learning behavior.

## Decision contract
AI may rank, explain, or recommend, but it cannot bypass risk, security, wallet, or execution policy checks.

## Decision lifecycle
Ingest context -> retrieve memory -> assemble prompt -> select model -> generate candidate -> score confidence -> score opportunity -> score risk -> validate -> approve or reject -> execute or hold -> record outcome -> learn.

## Prompt lifecycle
Prompts are versioned artifacts. Each prompt has a template id, version, effective date, model compatibility, risk mode, and rollback path. A prompt version may not be promoted unless validation passes.

## Context assembly
Context includes market data, strategy state, portfolio state, wallet state, prior decisions, and system configuration. Only policy-approved fields may be included.

## Retrieval pipeline
Retrieval first checks local memory, then approved knowledge sources, then current market state. Retrieval must be deterministic for the same inputs.

## Memory usage
Memory is advisory and must be labeled by freshness and source trust. Stale or low-trust memory may not override live data.

## Model routing
Model selection depends on task type, cost ceiling, latency budget, and risk mode. Fallback models are pre-authorized and ordered.

## Confidence scoring
Confidence is a bounded score derived from model output quality, retrieval support, and data freshness.

## Opportunity scoring
AI may rank opportunities, but final ranking must be bounded by deterministic market, liquidity, and risk rules.

## Risk scoring
Risk score combines drawdown, liquidity, volatility, slippage, execution, and chain-health features.

## Validation pipeline
Validate structure, policy compliance, safety constraints, and consistency with live market inputs.

## Human approval workflow
Human approval is required when policy mode, risk level, or operator settings demand review. Human rejection always wins.

## Autonomous execution rules
Autonomous execution is allowed only when confidence, opportunity, and risk thresholds pass and no approval gate is required.

## Retry behaviour
Transient provider failures may retry with bounded attempts and backoff. Prompt failures do not bypass validation.

## Fallback models
Fallback models are used in priority order when the primary provider fails or becomes unavailable.

## Explainability
Every actionable AI output must include rationale, supporting inputs, confidence, and the reasons for any rejection.

## Prompt versioning
Prompt versions are tracked with content hash, owner, release channel, and rollback target.

## Feedback loop
Execution outcomes feed back into evaluation metadata. Negative outcomes may reduce confidence or trigger model review.

## Learning lifecycle
Learning is offline-by-default unless explicitly enabled by configuration and governance policy.

## Performance metrics
Track confidence calibration, approval rate, precision, latency, fallback rate, and outcome quality.

## Failure handling
Handle provider timeout, empty response, malformed output, stale context, and model drift as explicit failure states.

## Recovery behaviour
Recover by falling back to a lower-priority model, human review, or no-trade according to policy.

## Cross-references
- Strategy rules: `STRATEGIES.md`
- Simulation: `SIMULATION-ENGINE.md`
- Monitoring: `MONITORING-OBSERVABILITY.md`
- Risk: `RISK-ENGINE.md`
- Configuration: `CONFIGURATION.md`

