# Readme

## Document type
This document is an overview, reference, or index as noted below.

# README

## Purpose
Navigation-only document pointing to the authoritative owner(s).

## Cross-references
- `DOCUMENTATION-MAP.md`
- `APEX-ARCHITECTURE.md`
- `ARCHITECTURE.md`


## Cross-references
- `docs/ORCHESTRATOR.md`


## System Contracts
- `AI-ORCHESTRATION.md` — authoritative system contract.
- `AI-CONSENSUS.md` — authoritative system contract.
- `PLUGIN-SDK.md` — authoritative system contract.
- `DOMAIN-MODEL.md` — authoritative system contract.
- `METRICS.md` — authoritative system contract.
- `HEALTHCHECKS.md` — authoritative system contract.

- [TRADING-LIFECYCLE.md](./TRADING-LIFECYCLE.md) – Defines the complete state machine for trade discovery, risk, execution, and settlement.
- [EXECUTION-LIFECYCLE.md](./EXECUTION-LIFECYCLE.md) – Specifies the order submission, signing, broadcasting, and confirmation state transitions.
- [SECURITY-CONTRACTS.md](./SECURITY-CONTRACTS.md) – Codifies secret handling, wallet signing, plugin sandboxing, emergency stop, and audit logging.
- [PERFORMANCE-SLOS.md](./PERFORMANCE-SLOS.md) – Declares numeric latency, throughput, and budget SLOs for all major subsystems.
- [STRATEGY-ROTATION.md](./STRATEGY-ROTATION.md) – Defines strategy scoring, rotation, fallback, and monitoring.
- [CHAIN-ROTATION.md](./CHAIN-ROTATION.md) – Defines chain prioritization, allocation, and demotion rules.
- [TOKEN-INTELLIGENCE.md](./TOKEN-INTELLIGENCE.md) – Defines token metadata scoring, ranking, caching, and refresh.
- [ROUTE-OPTIMIZATION.md](./ROUTE-OPTIMIZATION.md) – Defines route simulation, scoring, and fallback selection.
- [CONTRACT-MANAGEMENT.md](./CONTRACT-MANAGEMENT.md) – Defines contract registry, ABI versioning, and governance approval.
- [PROVIDER-RESILIENCE.md](./PROVIDER-RESILIENCE.md) – Defines provider health checks, failover, and reinstatement.

- [EVENT-BUS.md](./EVENT-BUS.md) – Defines the pub/sub backbone for agents, workers, and UI.
- [WORKER-POOL.md](./WORKER-POOL.md) – Defines worker lifecycle, queue priority, and scaling policy.
- [REGISTRY-SYSTEM.md](./REGISTRY-SYSTEM.md) – Defines the unified registry interface and governance rules.
- [DASHBOARD-WORKSPACES.md](./DASHBOARD-WORKSPACES.md) – Defines workspace persistence, restore, and isolation.
- [LEARNING-PIPELINE.md](./LEARNING-PIPELINE.md) – Defines the retraining, evaluation, and promotion pipeline.
- [DECISION-ENGINE.md](./DECISION-ENGINE.md) – Defines the authoritative approval gate between recommendation and execution.
- [POLICY-ENGINE.md](./POLICY-ENGINE.md) – Defines the central source of truth for configurable governance policies.
- [APEX-KERNEL.md](./APEX-KERNEL.md) – Defines the runtime kernel for service registration, lifecycle, health, and plugin loading.
- [SERVICE-REGISTRY.md](./SERVICE-REGISTRY.md) – Defines the canonical service registration and lookup mechanism.
- [DEPENDENCY-GRAPH.md](./DEPENDENCY-GRAPH.md) – Defines the system-wide dependency graph for startup, upgrades, and debugging.
- [EXPLAINABILITY.md](./EXPLAINABILITY.md) – Defines the mandatory trace format for decisions and actions.
- [WORKFLOW-BUILDER.md](./WORKFLOW-BUILDER.md) – Defines event-driven user workflows and policy-checked automation.
- [KNOWLEDGE-GRAPH.md](./KNOWLEDGE-GRAPH.md) – Defines the structured graph of protocols, tokens, strategies, chains, DEXs, risks, and agents.
- [GOVERNANCE-EXPLAINABILITY.md](./GOVERNANCE-EXPLAINABILITY.md) – Centralizes audit lineage, rationale retention, and trace governance.
- [LIVE-ARCHITECTURE-VIEWER.md](./LIVE-ARCHITECTURE-VIEWER.md) – Centralizes live topology visualization and runtime graph rendering.
- [DATA-GOVERNANCE.md](./DATA-GOVERNANCE.md) – Centralizes normalization, validation, provenance, caching, and graph linking.
- [DECISION-LEDGER.md](./DECISION-LEDGER.md) – Defines the immutable record of autonomous decisions and outcomes.
- [CONTEXT-BUILDER.md](./CONTEXT-BUILDER.md) – Defines how structured context is assembled before AI requests.
- [RUNTIME-KNOWLEDGE.md](./RUNTIME-KNOWLEDGE.md) – Defines the system’s live self-knowledge at runtime.
- [SYSTEM-CAPABILITY-REGISTRY.md](./SYSTEM-CAPABILITY-REGISTRY.md) – Defines platform capability discovery independent of names.
- [FEATURE-FLAGS.md](./FEATURE-FLAGS.md) – Defines controlled rollout states for features.
- [CONFIGURATION-PROFILES.md](./CONFIGURATION-PROFILES.md) – Defines profile inheritance and overrides.
- [AI-REASONING-POLICY.md](./AI-REASONING-POLICY.md) – Defines when AI may advise versus when determinism is required.
- [AI-CONTEXT-WINDOW-MANAGEMENT.md](./AI-CONTEXT-WINDOW-MANAGEMENT.md) – Defines context compression and token budgeting.
- [MODEL-CAPABILITY-NEGOTIATION.md](./MODEL-CAPABILITY-NEGOTIATION.md) – Defines automatic AI capability detection and negotiation.
- [EXECUTION-POLICIES.md](./EXECUTION-POLICIES.md) – Defines execution guardrails and stop conditions.
- [ROUTE-SCORING-MODEL.md](./ROUTE-SCORING-MODEL.md) – Defines the mathematical route scoring model.
- [MARKET-REGIME-DETECTION.md](./MARKET-REGIME-DETECTION.md) – Defines market regime classification.
- [RESOURCE-MANAGER.md](./RESOURCE-MANAGER.md) – Defines lifecycle management for runtime resources.
- [TASK-SCHEDULER.md](./TASK-SCHEDULER.md) – Defines priority, fair, adaptive task scheduling.
- [SELF-HEALING.md](./SELF-HEALING.md) – Defines recovery actions for unhealthy components.
- [APEX-OS.md](./APEX-OS.md) – Defines the constitution, principles, roadmap, and evolution strategy of the platform.
- [SERVICE-LIFECYCLE.md](./SERVICE-LIFECYCLE.md) – Defines the canonical lifecycle for all services.
- [PLUGIN-LIFECYCLE.md](./PLUGIN-LIFECYCLE.md) – Defines the canonical lifecycle for all plugins.
- [WORKSPACE-MANAGER.md](./WORKSPACE-MANAGER.md) – Defines workspace ownership, layout, settings, and isolation.
- [AI-TOOLS.md](./AI-TOOLS.md) – Defines the tool surface available to AI agents.
- [AI-PLANNER.md](./AI-PLANNER.md) – Defines the planning agent for decomposition and sequencing.
- [AI-REFLECTION.md](./AI-REFLECTION.md) – Defines AI self-evaluation and refinement.
- [AI-KNOWLEDGE-INDEX.md](./AI-KNOWLEDGE-INDEX.md) – Defines retrieval and ranking over the knowledge graph.
- [TRADE-EXPLAINER.md](./TRADE-EXPLAINER.md) – Defines human-readable trade explanations.
- [MARKET-SESSION.md](./MARKET-SESSION.md) – Defines market condition labels for strategy selection.
- [OPPORTUNITY-LIFECYCLE.md](./OPPORTUNITY-LIFECYCLE.md) – Defines the lifecycle from detection to archival.
- [CONTRACT-REGISTRY.md](./CONTRACT-REGISTRY.md) – Defines the canonical registry of deployed contracts, versions, ABIs, and addresses.
- [RPC-MANAGER.md](./RPC-MANAGER.md) – Defines provider pools, health, rotation, latency, failover, and load balancing.
- [CACHE-MANAGER.md](./CACHE-MANAGER.md) – Defines cache ownership, invalidation, TTL, and compression policies.
- [UPDATE-MANAGER.md](./UPDATE-MANAGER.md) – Defines application, plugin, prompt, and model update lifecycle.
- [DIAGNOSTICS.md](./DIAGNOSTICS.md) – Defines support bundle generation and troubleshooting output.
- [BOOTSTRAP-SEQUENCE.md](./BOOTSTRAP-SEQUENCE.md) – Defines deterministic platform startup order.
- [EVENT-CATALOG.md](./EVENT-CATALOG.md) – Defines the canonical registry of platform events and payloads.
- [AI-GATEWAY.md](./AI-GATEWAY.md) – Defines provider-agnostic AI routing and capability normalization.
- [AI-CONSENSUS.md](./AI-CONSENSUS.md) – Defines multi-agent consensus and voting policy.
- [AI-MEMORY-SYSTEM.md](./AI-MEMORY-SYSTEM.md) – Defines the layered AI memory model and retention rules.
- [DECISION-LOG.md](./DECISION-LOG.md) – Defines the operational decision log and replay-friendly narratives.
## Overview rules
- Describe purpose, prerequisites, and quick start for Windows users.
- Describe what the bot does and does not do.

## Final rules
- Define quick start, prerequisites, and scope for Windows users.
- Define what the bot does and does not do.

## Canonical ownership
This document defers to the canonical owners for implementation, policy, and schema details.
