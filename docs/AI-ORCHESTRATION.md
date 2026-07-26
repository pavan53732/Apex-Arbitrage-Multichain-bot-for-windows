# Ai Orchestration

## Document type
This document is an overview, reference, or index as noted below.

# AI Orchestration

## Purpose
Defines lifecycle and coordination rules for the AI agent set.

## Agents
- Market Agent.
- Risk Agent.
- Planner Agent.
- Execution Agent.
- Learning Agent.
- Documentation Agent.
- Operations Agent.

## Coordination
Agent lifecycle, inputs, outputs, permissions, tools, and health checks are defined here.

## Cross-references
- `ORCHESTRATOR.md`
- `AI-PIPELINE.md`
- `AI-AGENT-SPECIFICATION.md`

For decision authority, see `DECISION-ENGINE.md`.
For policy governance, see `POLICY-ENGINE.md`.
For explainability, see `EXPLAINABILITY.md`.
For AI planning, see `AI-PLANNER.md`.
For AI reflection, see `AI-REFLECTION.md`.
For AI knowledge index, see `AI-KNOWLEDGE-INDEX.md`.
## Operational Contract
Defines the coordination of agents, tool calls, memory, consensus, and decision handoff.

## Example
Market analysis, risk review, and planning converge before the Decision Engine receives a recommendation.

## Orchestration rules
- Define routing, sequencing, fallback, and coordination across AI agents.
- Define how orchestration degrades under failure.
