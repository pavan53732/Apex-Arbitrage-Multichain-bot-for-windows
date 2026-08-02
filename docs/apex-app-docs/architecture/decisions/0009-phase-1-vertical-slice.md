---
metadata_schema_version: 1.0
document_id: DOC-0455
title: ADR 0009 Phase 1 Vertical Slice
plane: Product Specification
domain: Architecture
class: ADR
authority: Canonical
status: Active
owner: Architecture Team
version: 1.1.0
canonical_source: docs/apex-app-docs/architecture/decisions/0009-phase-1-vertical-slice.md
related_concepts:
  - CONCEPT-0455
dependencies:
  - DOC-0073
  - DOC-0281
consumers:
  - DOC-0067
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
concept_role: Owner
owned_domains:
  - Architecture
type: ADR
purpose: "Records the decision to authorise a src/ implementation root and build a Phase 1 simulation-only vertical slice that proves the specification is implementable."
scope: "The src/ root, the Phase 1 slice boundary, and the constraints under which implementation code may exist in this repository."
---

# ADR 0009 Phase 1 Vertical Slice

## Status

Accepted. Authorised by explicit maintainer instruction, which the root-layout
rule in `REBUILD-SYSTEM-SPECIFICATION.md` requires before a new permanent
root-level folder may be committed.

## Context

The repository held 372 specification documents, 18 validators, and twelve
immutable governance rules, and no implementation. Every consistency guarantee
was therefore internal: validators could confirm that documents agreed with each
other, but nothing could confirm that the specifications describe a system that
can actually be built.

This is a specific and unfalsifiable kind of risk. A specification can be
perfectly self-consistent and still under-determine behaviour, contradict itself
in ways no mechanical check detects, or omit a decision an implementer must make.
No amount of additional documentation governance detects that class of defect,
because the defect is only visible when something is built against the document.

Two constraints bound any implementation:

- `REBUILD-SYSTEM-SPECIFICATION.md` states that the root contains only
  repository entry documents and `validators/`, and that no other permanent
  root-level folder is part of the approved architecture.
- `docs/apex-app-docs/execution/risk-policy/risk-engine.md` §0 places the
  product in Phase 1, where live execution is `ALWAYS_REJECTED`.

## Decision

**Authorise a `src/` implementation root, and populate it with a Phase 1
simulation-only vertical slice rather than a full scaffold.**

### Scope of the slice

The slice implements one path end to end: configuration loading, an RPC provider
pool, a constant-product DEX adapter, opportunity detection, route construction
and ranking, and a simulated result. It covers `configuration.md`,
`rpc-manager.md`, `dex-integration.md`, `opportunity-detection.md`,
`opportunity-lifecycle.md`, `opportunity-ranking.md`, `routing-engine.md`,
`route-scoring-model.md`, and the Phase 1 clauses of `risk-engine.md` and
`decision-engine.md`.

A vertical slice is chosen over a horizontal scaffold because a scaffold of
empty modules mirroring 372 documents would restate the specification in a
second notation without testing whether any of it composes. One path built end
to end answers the question the documentation cannot.

The slice was widened in a second step, after the initial quote-only path
proved implementable. The widening added detection and routing — the stages
where the specification carries its most substantive claims, including two
lifecycle state machines, stable route fingerprints, idempotent ranking, and an
explicit tie-break order. Those claims are the ones most likely to be
under-determined, so exercising them is where the evidence is worth most.

### Phase 1 is enforced structurally, not by configuration

Live execution is impossible in this build rather than disabled in it:

- `load_config` refuses to start in any phase other than `simulation_only`.
- `Config.live_execution_permitted` returns `False` unconditionally.
- `SimulationPipeline.execute` raises `ExecutionBlocked` with the specification's
  `PHASE_1_EXECUTION_BLOCK` code for every input, and has no success path.
- No wallet, key handling, signing, or broadcast capability exists. A test
  asserts their absence by scanning the package source, so adding one fails the
  suite and forces the phase question to be answered deliberately.

### Constraints on code in this repository

- Financial arithmetic is integer-only and deterministic, per
  `coding-standards.md`. No floating point appears on a path that influences a
  quote.
- No network transport is implemented. The RPC pool is driven by an injected
  callable, keeping the slice offline and its tests reproducible.
- Generated build output is never committed, per the generated-artefact rule.

## Consequences

### Positive

- The specification is now falsifiable. The slice compiles, runs, and passes 101
  deterministic tests, which is direct evidence that these documents are
  implementable rather than merely self-consistent.
- Two lifecycle state machines transcribed directly from the specification —
  opportunity and route — hold as executable transition tables, so a forbidden
  transition named in prose is now a forbidden transition in code.
- Phase progression becomes an explicit, reviewable decision rather than a
  configuration value someone can flip.
- Validator behaviour is unchanged: the documentation plane and the
  implementation root are independent, and the full suite still passes.

### Negative

- The repository now has a fourth root-level entry, which the previous
  architecture prohibited. This ADR is the governance revision that permits it,
  and the permission is scoped to `src/` alone.
- The slice covers a small fraction of the specified system. Its passing tests
  demonstrate that this path is implementable, not that the whole specification
  is.

### Neutral

- Later phases require a further governance decision. This ADR authorises
  simulation only, and deliberately provides no mechanism to advance beyond it.

## Affected Components

- `src/apex/` — the Phase 1 slice: config, RPC pool, DEX adapter, opportunity
  detection, routing, and the simulation pipeline.
- `docs/apex-app-docs/execution/risk-policy/risk-engine.md` — supplies the phase
  invariant the slice enforces.
- `docs/apex-app-docs/market/connectivity/rpc-manager.md` and
  `docs/apex-app-docs/market/dex/dex-integration.md` — supply the provider and
  venue rules.
- `REBUILD-SYSTEM-SPECIFICATION.md` — root-layout rule revised by this decision.

## Cross-references

- `./0004-polygon-first.md`
- `../../market/opportunities/opportunity-detection.md`
- `../../market/opportunities/opportunity-lifecycle.md`
- `../../market/routing/routing-engine.md`
- `../../execution/risk-policy/risk-engine.md`
- `../../execution/risk-policy/policy-engine.md`
- `../../market/connectivity/rpc-manager.md`
- `../../market/dex/dex-integration.md`
- `../../../apex-repository-docs/standards/coding-standards.md`
