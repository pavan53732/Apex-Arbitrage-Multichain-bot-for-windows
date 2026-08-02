---
metadata_schema_version: 1.0
document_id: DOC-0371
title: Implementation Roadmap
plane: Product Specification
domain: Reference
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.1.0
canonical_source: docs/apex-app-docs/reference/implementation-roadmap.md
related_concepts:
  - CONCEPT-0371
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Reference
type: REFERENCE
purpose: Implementation Roadmap documentation.
scope: Reference documentation.
---

# Implementation Roadmap

## Document type
Document type: [REFERENCE]

## Purpose
Defines implementation sequencing so major subsystems are delivered in a safe dependency order.

## Ownership
- Sequence and dependency order only; behavior is owned by each subsystem's canonical owner.

## Sequence
1. Core kernel and registries.
2. Market data, chain, DEX, and token layers.
3. Risk and policy engines.
4. Opportunity detection, ranking, and simulation.
5. Trading and execution lifecycle.
6. AI pipeline and explainability.
7. Dashboard, UI, and Windows shell.
8. Deployment, packaging, and updates.

## Sequencing rules
- A subsystem lands only after its declared dependencies are implemented and validated.
- The sequence follows the dependency graph; an unblocked change may land early.
- Each stage ends with validators passing and the relevant contracts satisfied.

## Stage acceptance
- A stage is accepted when its contracts are validated and its tests pass.
- Acceptance is recorded with the release version it landed in.
- A stage that fails acceptance returns to the prior stage's queue with its findings.

## Dependencies
- Dependencies are declared explicitly per subsystem in this roadmap.
- An unlisted dependency is a documentation gap and is resolved before scheduling.
- Dependency changes update the roadmap and the dependency graph together.

## Status tracking
- Each item records its status: not started, in progress, blocked, complete, deferred.
- A blocked item records its blocker and unblocking condition.
- Deferred items are reviewed on the roadmap cadence before re-scheduling.

## Governance
- The roadmap is reviewed with the enhancement roadmap and the feature matrix.
- Sequencing never reorders a safety-critical dependency without review.
- Roadmap changes are validated and committed with the docs they affect.

## Cross-references
- `../architecture/architecture.md`
- `../architecture/project-structure.md`
- `../execution/trading/trading-engine.md`
- `./enhancement-roadmap.md`

## Operational Contract

This document owns implementation sequencing and dependency order. It does not own subsystem behavior; each subsystem's canonical owner does.

## Example
The AI pipeline is sequenced after market data and risk land, because it consumes both.
