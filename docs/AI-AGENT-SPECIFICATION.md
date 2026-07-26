# Ai Agent Specification

## Document type
This document is an overview, reference, or index as noted below.

# AI Agent Specification

## Purpose
Defines message and tool schemas for AI agents.

## Support Doc
This document provides schemas for agent messages and tool calls. Lifecycle rules are defined in `AI-ORCHESTRATION.md`.

## Cross-references
- `AI-ORCHESTRATION.md`
- `AI-PIPELINE.md`

## Interface Contract
Each agent defines purpose, inputs, outputs, tools, memory access, metrics, and lifecycle expectations.

## Example
The planner agent decomposes goals, orders dependencies, and emits a structured execution plan.

## Agent rules
- Define agent identity, goals, tools, permissions, and output expectations.
- Define failure and handoff behavior.
