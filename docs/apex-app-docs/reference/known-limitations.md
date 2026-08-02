---
metadata_schema_version: 1.0
document_id: DOC-0372
title: Known Limitations
plane: Product Specification
domain: Reference
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.1.0
canonical_source: docs/apex-app-docs/reference/known-limitations.md
related_concepts:
  - CONCEPT-0372
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
purpose: Known Limitations documentation.
scope: Reference documentation.
---

# Known Limitations

## Document type
Document type: [REFERENCE]

## Purpose
Lists the explicit, accepted limitations of the APEX platform.

## Windows limitations
- Configuration mutations under `%PROGRAMDATA%` require admin elevation.
- Windows notification delivery is subject to OS notification service state.
- Signed installers are required for distribution; unsigned builds are developer-only.

## Performance limitations
- Large-model AI inference is bounded by the 2000ms p95 SLO; cost caps apply per call.
- Deep multi-leg routes are subject to the latency budget of the arbitrage window.
- Dashboard density is bounded by the refresh SLO and the render budget.

## Network limitations
- Provider availability is not guaranteed; the platform degrades gracefully but cannot execute without a reachable provider.
- No exact fee, latency, liquidity, or provider guarantees are made (ADR 0004).

## Arbitrage limitations
- Phase 1 is simulation-only; live execution is phased and operator-approved.
- Polygon is the first intended live network; other chains follow the same safety controls.

## Known limitations
- Live trading scope is Polygon-first; other chains are phased per the roadmap.
- Autonomous execution is not available; execution is operator-approved.
- Headless signing is forbidden by the security contracts.
- Cross-chain atomicity is best effort; partial fills are reconciled after execution.
- AI cannot own final financial calculations; risk and execution logic is deterministic.
- Plugin activation requires signature and trust checks; unsigned plugins are developer-mode only.
- Notifications require an operator-configured destination for opt-in channels.
- Update and rollback behavior is bounded by the update channel integrity checks.
- Workspace restore falls back to the last good snapshot on corruption.
- The documentation set is governed by the repository validators; temporary artifacts are prohibited.
- Simulated execution is the default mode for Phase 1.
- Cache and memory are acceleration surfaces; persistence is the source of truth.
- Windows service mode requires elevated configuration under `%PROGRAMDATA%`.
- Known limitations are reviewed on the roadmap cadence.

## Cross-references
- `../deployment/deployment.md`
- `../security/security.md`
- `../windows/windows-desktop.md`

## Operational Contract

This document owns the known-limitations list. A limitation removed by a change is deleted here in the same change.

## Example
An operator planning live trading on a non-Polygon chain is told the current network scope and the phased plan.
