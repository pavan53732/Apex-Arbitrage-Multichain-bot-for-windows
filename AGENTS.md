# Agents


## AI Guard
Before creating or modifying ANY markdown file, verify it complies with the 5 Prime Directives.
- Lifecycle docs must explicitly define initial state, terminal state, allowed transitions, forbidden transitions, recovery transitions, and failure transitions.
- Interface docs must explicitly define producer, consumer, payload, schema, validation, versioning, and failure behavior.
- Owner docs must explicitly state what they own and do not own.
- Cross-cutting docs must defer to canonical owners.
- Short docs must explicitly declare whether they are an [INDEX], [OVERVIEW], or [REFERENCE].
If a file fails any directive, abort and fix it before proceeding.

## Purpose
Navigation entry point for autonomous coding agents working in this repository.

## Authority
This document is navigation only. It does not own product behavior, runtime behavior, trading behavior, or interface contracts. Those remain with the canonical owner documents.

## How to use this repo
- Read the authoritative owner docs before changing code.
- Prefer lifecycle, interface, registry, schema, and architecture boundary docs over summaries.
- Do not infer behavior from short references or roadmaps.
- Run `scripts/validate_markdown_refs.sh` after documentation edits to catch broken local references before commit.
- If a behavior is not explicit in an owner doc, treat it as ambiguous and stop.

## Canonical starting points
- [docs/ARCHITECTURE.md](./docs/ARCHITECTURE.md) for system boundaries.
- [docs/AI-PIPELINE.md](./docs/AI-PIPELINE.md) for AI decision behavior.
- [docs/RUNTIME-OPERATIONS.md](./docs/RUNTIME-OPERATIONS.md) for runtime control.
- [docs/TRADING-LIFECYCLE.md](./docs/TRADING-LIFECYCLE.md) and [docs/EXECUTION-LIFECYCLE.md](./docs/EXECUTION-LIFECYCLE.md) for trade and execution flow.
- [docs/DATABASE-SCHEMA.md](./docs/DATABASE-SCHEMA.md) for persistence structure.
- [docs/SECURITY-CONTRACTS.md](./docs/SECURITY-CONTRACTS.md) for security rules.
