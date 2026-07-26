# AI Pipeline

## Purpose
This document is the authoritative specification for AI decision lifecycle, prompt lifecycle, provider routing, confidence scoring, explainability, and learning behavior.

## Ownership
- Owns AI request routing, prompt lifecycle, and structured response validation. For multi-agent sequencing and consensus policy, see `AI-ORCHESTRATION.md` and `AI-CONSENSUS.md`.
- Does not own execution authorization, which remains with risk and execution owners.

## Provider policy
- Production AI must use approved cloud providers with paid API keys only.
- Local LLM inference is unsupported in production.
- Provider selection, fallback order, cost caps, and audit logging are governed by this pipeline.
- AI outputs must identify the provider and model used for each actionable decision.

## Decision contract
AI may rank, explain, or recommend, but it cannot bypass risk, security, wallet, or execution policy checks.

## For behavioral orchestration and multi-agent sequencing, see `ORCHESTRATOR.md` and `AI-ORCHESTRATION.md`.
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
Prompts are versioned artifacts with template id, version, effective date, model compatibility, risk mode, and rollback path.

### Transition rules
Draft -> Validated -> Promoted -> Active -> Deprecated -> Retired.

## Context assembly
Context includes market data, strategy state, portfolio state, wallet state, prior decisions, configuration, and operator policy. Only approved fields may be included.

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
Every actionable AI output must include rationale, supporting inputs, confidence, provider, model, and the reasons for any rejection.

## Prompt versioning
Prompt versions are tracked with content hash, owner, release channel, and rollback target.

## Feedback loop
Execution outcomes feed back into evaluation metadata. Negative outcomes may reduce confidence or trigger model review.

## Learning lifecycle
Learning is offline-by-default unless explicitly enabled by configuration and governance policy.

## Performance metrics
Track confidence calibration, approval rate, precision, latency, fallback rate, token cost, and outcome quality.

## Failure handling
Handle provider timeout, empty response, malformed output, stale context, and model drift as explicit failure states.

## Recovery behaviour
Recover by falling back to a lower-priority model, human review, or no-trade according to policy.

## Persistence
Persist prompt versions, routing decisions, model ids, tokens used, confidence scores, validation results, and final consumer decisions.

## Cross-references
- `STRATEGIES.md`
- `SIMULATION-ENGINE.md`
- `MONITORING-OBSERVABILITY.md`
- `RISK-ENGINE.md`
- `CONFIGURATION.md`
- `AI-CAPABILITY-MATRIX.md`
- `AI-MEMORY.md`
- `PROMPT-ENGINEERING.md`
- `AI-COST-MANAGEMENT.md`

## Orchestration authority
AI-PIPELINE.md is the single source for behavioural orchestration, provider routing, prompt lifecycle, and decision sequencing.

- `AI-CONSENSUS.md`

- `AI-AGENT-SPECIFICATION.md`


For provider abstraction and gateway routing, see `AI-PROVIDER-MANAGER.md` and `AI-GATEWAY.md`.


## Enterprise Contract – AI Pipeline
- Interfaces: `INTERFACE-PROVIDER-ADAPTER.md`, `INTERFACE-AGENT-MESSAGE.md`, `INTERFACE-TOOL-CALL.md`.
- State machine: `AI-ORCHESTRATION.md`, `AI-CONSENSUS.md`.
- Security boundaries: `SECURITY-CONTRACTS.md`.
- Performance SLOs: `PERFORMANCE-SLOS.md`.
- Failure modes: provider timeout, model rejection, consensus veto, memory miss; recover via fallback provider, no-op, or retry policy.

For AI orchestration, see `AI-ORCHESTRATION.md`.
For consensus, see `AI-CONSENSUS.md`.
For provider abstraction, see `AI-PROVIDER-MANAGER.md`.
For memory, see `AI-MEMORY-SYSTEM.md`.