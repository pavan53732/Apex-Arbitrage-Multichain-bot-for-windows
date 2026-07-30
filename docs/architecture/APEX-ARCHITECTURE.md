---
last_updated: 2026-07-29
type: OVERVIEW
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Apex architecture overview.
scope: Architecture reference.
canonical_source: APEX-ARCHITECTURE.md
---

# APEX Architecture


## AI Guard
Before creating or modifying ANY markdown file, verify it complies with the 5 Prime Directives.
- Lifecycle docs must explicitly define initial state, terminal state, allowed transitions, forbidden transitions, recovery transitions, and failure transitions.
- Interface docs must explicitly define producer, consumer, payload, schema, validation, versioning, and failure behavior.
- Owner docs must explicitly state what they own and do not own.
- Cross-cutting docs must defer to canonical owners.
- Short docs must explicitly declare whether they are an [INDEX], [OVERVIEW], or [REFERENCE].
If a file fails any directive, abort and fix it before proceeding.

## Purpose
Top-level index for the implementation specification set.

## Ownership
- `docs/DOCUMENTATION-MAP.md` owns documentation authority rules.
- `docs/ARCHITECTURE.md` owns system architecture and subsystem boundaries.
- `docs/PROJECT-STRUCTURE.md` owns repository layout and package boundaries.

## Cross-references
- `docs/DOCUMENTATION-MAP.md`
- `docs/ARCHITECTURE.md`
- `docs/PROJECT-STRUCTURE.md`
- `docs/TRADING-ENGINE.md`
- `docs/EXECUTION-ENGINE.md`


## Cross-references
- `docs/ORCHESTRATOR.md`


## System Contracts
- `docs/DOMAIN-MODEL.md` — authoritative system contract.
