# AI Reflection

## Purpose
Defines self-evaluation for response review, decision review, confidence assessment, error analysis, and prompt refinement.

## State machine
```mermaid
stateDiagram-v2
  [*] --> REVIEWING
  REVIEWING --> SCORING
  SCORING --> ANALYZING
  ANALYZING --> REFINING
  REFINING --> STORED
```

## Cross-references
- `AI-ORCHESTRATION.md`
- `LEARNING-PIPELINE.md`
- `EXPLAINABILITY.md`
