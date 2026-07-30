---
last_updated: 2026-07-29
type: REFERENCE
owner: UI Team
status: Canonical
version: 1.0.0
purpose: Context Builder documentation.
scope: Reference documentation.
canonical_source: docs/CONTEXT-BUILDER.md
---

# Context Builder

## Document type
This document is an overview, reference, or index as noted below.

# Context Builder

## Purpose
Defines the component that assembles structured context before every AI request.

## Pipeline
Memory -> Knowledge Graph -> Current Market -> User Settings -> Runtime State -> Decision History -> Prompt Builder -> AI Gateway.

## State machine
```mermaid
stateDiagram-v2
  [*] --> COLLECTING
  COLLECTING --> MERGING
  MERGING --> TRIMMING
  TRIMMING --> VALIDATING
  VALIDATING --> DISPATCHING
  DISPATCHING --> [*]
```

## Failure modes
Missing memory, oversize context, invalid source, stale runtime state.

## Recovery
Compress context, fall back to curated memory, or refuse dispatch if policy fails.

## Cross-references
- `ai/runtime/AI-PIPELINE.md`
- `ai/memory/AI-MEMORY-SYSTEM.md`
- `KNOWLEDGE-GRAPH.md`
- `ai/runtime/AI-GATEWAY.md`

## Operational Contract
Defines how user, market, wallet, and runtime context are assembled for downstream reasoning.

## Example
A prompt includes live balances, active positions, and current chain state.

## Context sources
- Must define which runtime, market, wallet, and Windows signals feed model context.
