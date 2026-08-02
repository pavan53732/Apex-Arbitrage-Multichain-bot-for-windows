---
metadata_schema_version: 1.0
document_id: DOC-0370
title: Glossary
plane: Product Specification
domain: Reference
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/reference/glossary.md
related_concepts:
  - CONCEPT-0370
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Reference
type: REFERENCE
purpose: Glossary documentation.
scope: Reference documentation.
---

# Glossary

## Document type
Document type: [REFERENCE]

## Purpose
Defines the canonical terms used across the APEX documentation set.

## Terms
- **Arbitrage window** — the time-bounded validity of an opportunity; expired windows are invalidated.
- **Slippage** — the difference between expected and executed price; bounded by the slippage model.
- **MEV** — maximal extractable value; mitigated by the MEV protection rules.
- **MSIX** — the Windows packaging format used for installation.
- **Tray mode** — the Windows system-tray presence of the desktop app.
- **Opportunity** — a detected candidate for execution, with lifecycle states.
- **Leg** — a single route step in a multi-step arbitrage.
- **Regime** — a classified market condition influencing strategy selection.
- **Workspace** — a saved arrangement of layout, providers, strategies, and wallets.
- **Decision ledger** — the immutable record of decisions and outcomes.

## Usage rules
- Terms are defined here; behavioral contracts are owned by their canonical owners.
- A new canonical term is added here with its owner in the same change.
- A term is added only when it is canonical across the documentation set.
- Terms are case-sensitive canonical spellings; synonyms point to the canonical term.
- A renamed term records the rename and updates all consumers in the same change.
- Glossary entries never define behavior; they define vocabulary.
- A term without an owner is not added; ownership is resolved first.
- Definitions are stable once active; refinement is a reviewed change.
- The glossary is the single vocabulary surface; other docs reference it.
- Retired terms are marked retired, never deleted, for lineage.
- Searching a term resolves to this entry or its owner document.
- Acronyms are expanded on first use in every document that uses them.
- New entries are validated against duplicate and near-duplicate terms before merge.
- The glossary is reviewed with the terminology validator.

## Cross-references
- `../architecture/architecture.md`
- `../execution/trading/strategies.md`
- `../execution/risk-policy/risk-engine.md`

## Operational Contract

This document owns the glossary of canonical terms. Definitions here are the shared vocabulary; the behavior behind each term is owned by its canonical owner.

## Example
A reader looks up "arbitrage window" and is directed to the window lifecycle behavior in the trading contracts.
