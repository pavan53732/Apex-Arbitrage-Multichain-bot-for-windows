---
metadata_schema_version: 1.0
document_id: DOC-0322
title: MEV Protection
plane: Product Specification
domain: Market
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/market/routing/mev-protection.md
related_concepts:
  - CONCEPT-0322
dependencies: []
consumers:
  - DOC-0321
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Market
type: REFERENCE
purpose: Mev Protection documentation.
scope: Reference documentation.
---

# Mev Protection

## Document type
This document is an overview, reference, or index as noted below.

# MEV Protection

## Purpose
Defines MEV avoidance, mitigation, and execution safeguards.

## Ownership
- Owns MEV visibility assessment, protection mode selection, and blocking policy.
- Feeds routing and execution.

## Responsibilities
- Detect high-risk visibility conditions.
- Choose private or protected submission when policy permits.
- Apply sandwich, backrun, and replay safeguards.
- Block submissions when protection policy cannot be satisfied.

## Inputs
- Route fingerprint.
- Venue visibility.
- Mempool exposure.
- Chain conditions.
- Submission mode policy.

## Outputs
- MEV risk label.
- Protection mode.
- Reject reason.
- Submission recommendation.

## Validation
- Reject if policy demands protection and no safe protection path exists.
- Reject if a route cannot be protected under the current chain or venue.

## Persistence
- Persist MEV risk class, selected protection, reject reason, and route fingerprint.

## Monitoring
- Protected submission rate.
- MEV rejection count.
- Visibility risk count.

## Cross-references
- `../../execution/transactions/execution-engine.md`
- `./routing-engine.md`
- `../../execution/transactions/transaction-lifecycle.md`

## Operational Contract
Defines the responsibilities, invariants, and expected behavior for this component.

## Example
An input is validated before any state-changing action.

## Protection detail
- Must define private relay behavior and simulation checks.

## Required details
- Define private routing and sandbox protections.

## Protection rules
- Define private routing, sandwich mitigation, and simulation checks.
- Define fallback behavior when MEV protection fails.
