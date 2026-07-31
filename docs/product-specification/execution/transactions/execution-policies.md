---
metadata_schema_version: 1.0
document_id: DOC-0290
title: Execution Policies
plane: Product Specification
domain: Execution
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/product-specification/execution/transactions/execution-policies.md
related_concepts:
  - CONCEPT-0290
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
purpose: Execution Policies documentation.
scope: Reference documentation.
---

# Execution Policies

## Document type
This document is an overview, reference, or index as noted below.

# Execution Policies

## Purpose
Defines the policy layer for gas, exposure, trading windows, profit thresholds, retry policy, emergency stop, and pause policy.

## State machine
```mermaid
stateDiagram-v2
  [*] --> EVALUATING
  EVALUATING --> APPROVED
  EVALUATING --> BLOCKED
  APPROVED --> ACTIVE
  ACTIVE --> PAUSED
  PAUSED --> ACTIVE
  ACTIVE --> EMERGENCY_STOPPED
```

## Failure modes
Threshold breach, policy conflict, emergency stop, invalid pause state.

## Recovery
Stop execution, notify operators, and require approval to resume.

## Cross-references
- `../risk-policy/risk-engine.md`
- `../risk-policy/policy-engine.md`
- `../trading/trading-lifecycle.md`
- `./execution-lifecycle.md`

## Governance Rules
Defines execution permissions, sequencing, retries, stop conditions, and exception handling.

## Example
A policy prevents execution when risk checks fail.

## Required details
- Define risk, slippage, timing, and proxy-related policy limits.
