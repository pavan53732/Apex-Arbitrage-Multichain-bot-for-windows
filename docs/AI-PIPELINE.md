# AI Pipeline

## Purpose
This document is the authoritative specification for AI decision lifecycle, prompt lifecycle, provider routing, confidence scoring, explainability, and learning behavior.

## Ownership
- Owns AI request orchestration, provider routing, prompt lifecycle, and structured response validation.
- Does not own execution authorization, which remains with risk and execution owners.

## Decision contract
## Provider policy
- Production AI must use approved cloud providers with paid API keys only.
- Local LLM inference is not supported in production and must not be used as an implicit fallback.
- Cloud fallback models are allowed only when explicitly configured and approved.
- Cost ceilings, provider routing, and model fallback order are governed by configuration and governance policy.

AI may rank, explain, or recommend, but it cannot bypass risk, security, wallet, or execution policy checks.

## Decision lifecycle
Ingest context -> retrieve memory -> assemble prompt -> select model -> generate candidate -> score confidence -> score opportunity -> score risk -> validate -> approve or reject -> execute or hold -> record outcome -> learn.

### Transition rules
- Ingest context only after all required state snapshots are available.
- Retrieve memory only from approved namespaces and freshness windows.
- Assemble prompt only from policy-approved fields.
- Select model only from pre-authorized routing tables.
- Generate candidate only when token and timeout budgets are available.
- Score and validate every response before downstream use.
- Record outcome only after the authoritative consumer has accepted or rejected the output.
- Learn only from persisted outcomes and only when learning is enabled by policy.

## Prompt lifecycle
Prompts are versioned artifacts. Each prompt has a template id, version, effective date, model compatibility, risk mode, and rollback path. A prompt version may not be promoted unless validation passes.

### Transition rules
- Draft -> Validated -> Promoted -> Active -> Deprecated -> Retired.
- A prompt cannot become Active until compatibility and safety tests pass.
- Deprecated prompts may serve only for rollback or compatibility windows.

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

## Persistence
- Persist prompt versions, routing decisions, model ids, tokens used, confidence scores, validation results, and final consumer decisions.
- Persist memory references and freshness labels, not raw secrets or unauthorized context fields.
- Persist learning outcomes only when offline learning is enabled.

## Cross-references
- `STRATEGIES.md`
- `SIMULATION-ENGINE.md`
- `MONITORING-OBSERVABILITY.md`
- `RISK-ENGINE.md`
- `CONFIGURATION.md`
