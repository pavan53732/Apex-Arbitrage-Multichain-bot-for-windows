---
metadata_schema_version: 1.0
document_id: DOC-0275
title: Knowledge Graph
plane: Product Specification
domain: Data
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/data/knowledge/knowledge-graph.md
related_concepts:
  - CONCEPT-0275
dependencies: []
consumers:
  - DOC-0432
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Data
type: REFERENCE
purpose: Knowledge Graph documentation.
scope: Reference documentation.
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
- `../../ai/memory/ai-memory-system.md`
- `../../market/chains/chain-intelligence.md`
- `../../market/core/market-intelligence.md`
- `../../interfaces/api/domain-model.md`

For data governance, see `./data-governance.md`.
## Governance Rules
Defines node types, edges, indexing, update propagation, and retrieval semantics for the knowledge graph.

## Example
A strategy node links to market regime, risk policy, and execution history.
