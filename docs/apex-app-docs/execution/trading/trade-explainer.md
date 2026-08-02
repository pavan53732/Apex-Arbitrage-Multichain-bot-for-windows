---
metadata_schema_version: 1.0
document_id: DOC-0297
title: Trade Explainer
plane: Product Specification
domain: Execution
class: Reference
authority: Canonical
status: Active
owner: AI Team
version: 1.0.0
canonical_source: docs/apex-app-docs/execution/trading/trade-explainer.md
related_concepts:
  - CONCEPT-0297
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Execution
type: REFERENCE
purpose: Trade Explainer documentation.
scope: Reference documentation.
---

# Trade Explainer

## Document type
Document type: [CONTRACT]

## Purpose
Provides human-readable explanations for why a trade was executed.

## Explanation content
- The trade's trigger: which opportunity, spread, and window.
- The inputs used: market snapshot, risk score, and gates passed.
- The decision path: what was approved, skipped, or delayed and why.
- The outcome: execution result and post-execution state.

## Rules
- Explanations are generated from the decision ledger and explainability traces, never ad hoc.
- The explanation must be traceable to a recorded decision with its rationale.
- Skipped or delayed opportunities are explained with their rejection reason.
- Explanations are deterministic: the same decision produces the same explanation.

## Explanation format
- Structured: trigger, inputs, gates, decision, and outcome.
- Deterministic: the same decision produces the same explanation.

## Sources
- Decision ledger records.
- Explainability traces.
- Execution lifecycle outcomes.

## Quality rules
- An explanation is written in operator language; jargon is defined on first use.
- An explanation states what was done, why, and what changed as a result.
- A skipped or failed action explains the reason and the recovery guidance.
- Explanations are available in the UI and in exports at the same fidelity.
- An explanation that cannot be traced to a record is marked provisional, never presented as fact.
- Explanations are bounded in length and structured for scanning.
- Explanations are auditable: the trace identifiers are included in the output.
- An operator can replay an explanation from the underlying records.

## Delivery
- Explanations are available in the UI and in exports.
- Governance-grade lineage is owned by the governance explainability contract.

## Cross-references
- `../../ai/explainability/explainability.md`
- `../../ai/explainability/governance-explainability.md`
- `../../data/state/decision-ledger.md`
- `../transactions/execution-lifecycle.md`

## Operational Contract

This document owns the human-readable explanation of trades. Decision records are owned by the decision ledger; explainability format is owned by the explainability contract. This document renders them for operators.

## Example
A trade explanation shows the spread, the risk gates that passed, and the execution result, all traceable to the ledger record.
