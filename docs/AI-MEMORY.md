# Ai Memory

## Document type
This document is an overview, reference, or index as noted below.

# AI Memory

## Purpose
Defines the memory model used by AI orchestration.

## Scope
This document covers short-term memory, long-term memory, retrieval, summarization, compression, and eviction.

## Memory model
- Context builder.
- Prompt builder.
- Session memory.
- Persistent memory.
- Conversation summaries.
- Knowledge retrieval.
- Compression and eviction.

## Cross-references
- `AI-PIPELINE.md`
- `STATE-MANAGEMENT.md`
- `DATABASE-SCHEMA.md`
- `CONFIGURATION.md`

## Orchestration boundary
This document governs capability, memory, prompt, or cost definitions. For runtime orchestration and pipeline sequencing, see `AI-PIPELINE.md`.

## Governance Rules
Defines the memory surface exposed to the rest of the platform, including session recall and persistence boundaries.

## Example
A user preference is recalled for prompt construction without exposing unrelated private data.
