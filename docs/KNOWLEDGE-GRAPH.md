---
last_updated: 2026-07-29
type: REFERENCE
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Knowledge Graph documentation.
scope: Reference documentation.
canonical_source: docs/KNOWLEDGE-GRAPH.md
---

# Knowledge Graph

## Document type
This document is an overview, reference, or index as noted below.

# Knowledge Graph

## Purpose
Defines the structured graph linking protocols, tokens, strategies, chains, DEXs, risks, and AI agents.

## State machine
```mermaid
stateDiagram-v2
  [*] --> INGESTING
  INGESTING --> LINKING
  LINKING --> VALIDATING
  VALIDATING --> SERVING
  SERVING --> REFRESHING
  REFRESHING --> INGESTING
```

## Failure modes
Stale node, broken edge, duplicate entity, invalid relation, version drift.

## Recovery
Refresh source nodes, revalidate relations, and isolate stale subgraphs.

## Cross-references
- `AI-MEMORY-SYSTEM.md`
- `CHAIN-INTELLIGENCE.md`
- `MARKET-INTELLIGENCE.md`
- `DOMAIN-MODEL.md`

For data governance, see `DATA-GOVERNANCE.md`.
## Governance Rules
Defines node types, edges, indexing, update propagation, and retrieval semantics for the knowledge graph.

## Example
A strategy node links to market regime, risk policy, and execution history.
