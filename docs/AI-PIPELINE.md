# AI Pipeline

## Purpose
This document is the authoritative implementation specification for AI decisioning, prompt handling, retrieval, validation, execution gating, and learning feedback.

## Shared AI contract
Every AI decision must define decision lifecycle, prompt lifecycle, context assembly, retrieval pipeline, memory usage, model routing, confidence scoring, opportunity scoring, risk scoring, validation pipeline, human approval workflow, autonomous execution rules, retry behavior, fallback models, explainability, prompt versioning, feedback loop, learning lifecycle, performance metrics, failure handling, and recovery behavior.

## Decision lifecycle
Ingest input -> assemble context -> retrieve memory -> build prompt -> route model -> score output -> validate -> approve or hold -> execute or reject -> persist feedback.

## Context assembly
Context combines market data, strategy state, portfolio state, risk state, wallet/chain health, recent executions, and user settings. Context must be freshness-checked and size-limited.

## Retrieval pipeline
The retrieval pipeline pulls relevant historical decisions, strategy templates, and operational memory relevant to the current opportunity. Retrieval results must be ranked and deduplicated before prompt assembly.

## Memory usage
Memory is advisory only. It may improve ranking or explainability but cannot replace live market data or hard safety checks.

## Model routing
Model selection is based on task type, confidence requirements, latency budget, and configured provider availability. Routing must fall back deterministically when a primary provider fails.

## Confidence scoring
Confidence is a bounded score derived from model output quality, retrieval quality, market freshness, and validation strength.

## Opportunity scoring
Opportunity score combines AI estimate, deterministic strategy score, and route quality. AI score never overrides hard risk gates.

## Risk scoring
Risk score summarizes exposure, volatility, liquidity, and execution risk. High risk can suppress autonomous execution regardless of AI confidence.

## Validation pipeline
Validate prompt completeness, response schema, safety rules, route legitimacy, and risk policy before any execution handoff.

## Human approval workflow
If the configured policy requires approval, the AI may recommend but must wait for operator acceptance before execution.

## Autonomous execution rules
Autonomous execution is allowed only when the configured policy, risk rules, wallet policy, and confidence thresholds all pass.

## Retry behavior
Transient provider errors may be retried with bounded backoff and capped attempts. Prompt reconstruction is allowed if context freshness remains valid.

## Fallback models
A lower-tier or alternate provider may be used if the primary model is unavailable, but fallback cannot weaken safety policy.

## Explainability
Each decision must preserve a human-readable rationale, key factors, and the validation outcome that led to execution or rejection.

## Prompt versioning
Prompt templates are versioned. A decision record must reference the prompt version used.

## Feedback loop
Each executed or rejected decision produces feedback on outcome, confidence calibration, and error patterns.

## Learning lifecycle
Learning is offline and governed by versioned feedback artifacts. It can tune ranking weights or prompts, but not override hard safety rules.

## Performance metrics
Latency, success rate, validation pass rate, confidence calibration, fallback rate, and operator override rate.

## Failure handling
Model timeout, bad schema, unsafe suggestion, stale context, retrieval failure, or provider outage must fail closed.

## Recovery behavior
On failure, recompute context, switch provider, or hold the opportunity. No unsafe execution may proceed during recovery.

## Cross-references
- Strategy behavior: `STRATEGIES.md`
- Simulation behavior: `SIMULATION-ENGINE.md`
- Monitoring: `MONITORING-OBSERVABILITY.md`
- Risk rules: `RISK-ENGINE.md`
