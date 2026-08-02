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
version: 1.1.0
canonical_source: docs/apex-app-docs/execution/risk-policy/policy-engine.md
related_concepts:
  - CONCEPT-0281
dependencies: []
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-08-02
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
**Version:** 1.1.0 | **Status:** Canonical | **Last Updated:** 2026-08-02 | **Owner:** Trading Team

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

## Failure Handling

A policy failure blocks the dependent execution path. The Policy Engine never
substitutes an implicit default for a missing or invalid threshold, because a
silently defaulted limit is indistinguishable from an intentionally configured
one and would weaken every consumer that depends on it.

| Failure | Detection | Outcome |
| --- | --- | --- |
| Policy file missing or unreadable | Load fails at startup | Startup aborts; the engine does not begin serving policy values it cannot source |
| Policy file invalid | Schema or type validation fails on load | The load is rejected and the previous valid policy set is retained |
| Hot reload produces invalid policy | Validation fails during reload | The reload is discarded atomically; the running policy set is left unchanged and the failure is surfaced to the Windows UI |
| Requested policy value absent | Consumer requests an undefined key | The request fails explicitly; the dependent execution path blocks rather than proceeding on an assumed value |
| Policy value out of permitted range | Range check on read or load | The value is rejected and treated as absent |
| Conflicting policy sources | Priority ordering resolves to more than one candidate | Resolution fails closed; the conflict is reported rather than arbitrarily broken |

Because consumers such as the Decision Engine and Risk Engine read thresholds
through this engine rather than caching them, a retained or rejected policy set
takes effect consistently across all consumers at once.

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
| 1.1.0 | 2026-08-02 | Added Failure Handling section defining load, hot-reload, missing-value, range, and conflict failure behaviour. | Trading Team |
| 1.0.1 | 2026-07-29 | Added `## Operational Contract` section (state-machine-consistent authoritative contract body) to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`). All other content unchanged. | Trading Team |
| 1.0.0 | 2026-07-29 | Added formal Document type declaration, Version block, and Version History section to satisfy [CONTRACT] compliance (`architecture-tests/validate_contracts.py`, `architecture-tests/validate_ownership.py`). Substantive content unchanged. | Trading Team |
