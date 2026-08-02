---
metadata_schema_version: 1.0
document_id: DOC-0111
title: AI Knowledge Index
plane: Product Specification
domain: AI
class: Index
authority: Canonical
status: Active
owner: AI Team
version: 1.0.0
canonical_source: docs/apex-app-docs/ai/knowledge/ai-knowledge-index.md
related_concepts:
  - CONCEPT-0111
dependencies: []
consumers:
  - DOC-0401
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - AI
type: INDEX
purpose: Ai Knowledge Index documentation.
scope: Reference documentation.
---

# AI Knowledge Index

## Document type
Document type: [CONTRACT]

## Purpose
Defines how AI searches the knowledge graph, indexes documents, ranks retrieval results, and applies embedding strategies if added later.

## Indexing rules
- Canonical knowledge sources are indexed with priority: canonical specs, registries, and owner documents rank above navigation and reference material.
- Documents are indexed with their document ID, path, domain, class, and authority so retrieval can honor canonical-source discipline.
- De-duplication is enforced by document ID; a moved or renamed document is re-indexed under its stable ID.

## Retrieval and ranking
- Retrieval ranks results by relevance, freshness, and canonical priority.
- Stale results are demoted; a result older than the freshness window is flagged.
- Retrieval never invents sources: a result must resolve to a real indexed document.

## State machine
```mermaid
stateDiagram-v2
  [*] --> INDEXING
  INDEXING --> SEARCHING
  SEARCHING --> RANKING
  RANKING --> RETRIEVING
  RETRIEVING --> INDEXING
```

## Lifecycle model
- Initial state: `INDEXING` — sources are enumerated and indexed.
- Terminal state: none — the index continuously refreshes.
- Allowed transitions: as shown in the state machine.
- Forbidden transitions: retrieving without ranking; searching an empty or stale index.
- Recovery: a failed retrieval returns to `INDEXING` and refreshes the affected source.
- Failure: a stale or missing index is surfaced rather than silently served.

## Embedding strategy
- Embedding strategies may be added later; the hooks are defined but the strategy is pluggable.
- An embedding index must preserve the document-ID mapping used by the keyword index.

## Freshness rules
- Index freshness is tracked per source; a stale index entry is flagged, never served as current.
- De-duplication is enforced by document ID; a rename re-indexes without creating a duplicate.
- Retrieval demotes stale results and never fabricates a source that is not in the index.

## Cross-references
- `../../data/knowledge/knowledge-graph.md`
- `../memory/ai-memory-system.md`
- `../../data/knowledge/context-builder.md`

## Interface Contract
Defines indexing, ranking, retrieval, embedding strategy hooks, and document search semantics.

## Example
A planner prompt retrieves strategy docs, market notes, and memory summaries ranked by relevance and canonical priority.
