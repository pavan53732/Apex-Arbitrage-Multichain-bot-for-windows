# AI Knowledge Index

## Purpose
Defines how AI searches the knowledge graph, indexes documents, ranks retrieval results, and applies embedding strategies if added later.

## State machine
```mermaid
stateDiagram-v2
  [*] --> INDEXING
  INDEXING --> SEARCHING
  SEARCHING --> RANKING
  RANKING --> RETRIEVING
  RETRIEVING --> INDEXING
```

## Cross-references
- `KNOWLEDGE-GRAPH.md`
- `AI-MEMORY-SYSTEM.md`
- `CONTEXT-BUILDER.md`
