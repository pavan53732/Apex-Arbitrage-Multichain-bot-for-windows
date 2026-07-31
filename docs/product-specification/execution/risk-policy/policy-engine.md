---
metadata_schema_version: 1.0
document_id: DOC-0281
title: Policy Engine
plane: Product Specification
domain: Execution
class: Specification
authority: Canonical
status: Active
owner: Trading Team
version: 1.0.1
canonical_source: docs/product-specification/execution/risk-policy/policy-engine.md
related_concepts:
  - CONCEPT-0281
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-29
concept_role: Owner
owned_domains:
  - Execution
type: CONTRACT
purpose: Defines policy engine.
scope: Policy enforcement.
---

# Policy Engine

## Document type
Document type: [CONTRACT]

## Version
**Version:** 1.0.1 | **Status:** Canonical | **Last Updated:** 2026-07-29 | **Owner:** Trading Team

## Purpose
Defines the central source of truth for all user-configurable policies.

## Scope
Trading, AI, security, recovery, failover, and operational thresholds.

## Content
- Max daily loss.
- Position size.
- Budget caps.
- Model selection.
- Plugin permissions.
- Secret rotation.
- Retry limits.
- Failover behavior.

## Governance
Policies load from a central config file and can be hot-reloaded. Policy changes require approval and are versioned.

## Cross-references
- `../../configuration/core/configuration.md`
- `../../security/security-contracts.md`
- `./risk-engine.md`
- `../../ai/providers/ai-cost-management.md`

## Governance Rules
Defines policy evaluation, priority ordering, overrides, and final decision selection.

## Example
A routing policy blocks execution when cost exceeds target.

## Arbitrage policies
- Must define spread, latency, and loss-limit policies.

## Required details
- Define policy inputs, limits, and enforcement.

## Policy rules
- Define policy inputs, limits, enforcement, and override behavior.
- Define how policy failures block execution.

## Operational Contract
Defines the Policy Engine as the single, hot-reloadable source of truth for every user-configurable operational threshold (max daily loss, position size, budget caps, model selection, plugin permissions, secret rotation, retry limits, failover behavior). Consumers (Decision Engine, Risk Engine, AI Cost Management) must read policy values through the Policy Engine rather than caching or re-deriving thresholds locally; a policy failure (missing or invalid value) blocks the dependent execution path rather than falling back to an implicit default.

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.1 | 2026-07-29 | Added `## Operational Contract` section (state-machine-consistent authoritative contract body) to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`). All other content unchanged. | Trading Team |
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Trading Team |
