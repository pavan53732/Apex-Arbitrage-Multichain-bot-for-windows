---
last_updated: 2026-07-29
type: CONTRACT
owner: Trading Team
status: Canonical
version: 1.0.1
purpose: Defines policy engine.
scope: Policy enforcement.
canonical_source: docs/POLICY-ENGINE.md
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
- `configuration/CONFIGURATION.md`
- `security/SECURITY-CONTRACTS.md`
- `RISK-ENGINE.md`
- `AI-COST-MANAGEMENT.md`

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
