---
metadata_schema_version: 1.0
document_id: DOC-0369
title: Feature Matrix
plane: Product Specification
domain: Reference
class: Reference
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-app-docs/reference/feature-matrix.md
related_concepts:
  - CONCEPT-0369
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
purpose: Feature Matrix documentation.
scope: Reference documentation.
---

# Feature Matrix

## Document type
Document type: [REFERENCE]

## Purpose
Lists supported strategies, platforms, and app modes for the APEX platform.

## Strategies
| Strategy | Owner | Status |
| --- | --- | --- |
| Cross-exchange arbitrage | `cross-exchange-arbitrage.md` | Active |
| Triangular arbitrage | strategies | Planned |
| Flash-loan arbitrage | strategies | Planned |
| Route-scored execution | routing engine | Active |

## Platforms
| Platform | Mode | Notes |
| --- | --- | --- |
| Windows desktop | App + tray | Primary target |
| Windows service | Headless service mode | Managed via SCM |
| Simulation | Paper trading | Phase 1 default |

## App modes
- Simulation (paper trading).
- Operator-approved execution.
- Autonomous execution (phased).

## Feature status legend
- Active — implemented and governed by a canonical owner.
- Planned — on the roadmap; not yet implemented.
- Deprecated — scheduled for removal.
- In development — partially implemented; not yet governed.
- Maintenance — implemented and stable; changes limited to fixes.
- The matrix is updated in the same change as the feature's status change.
- A status change updates the roadmap and the enhancement roadmap together.
- Rows reference their canonical owner; a row without an owner is a documentation gap.
- The matrix is the single status surface; other docs reference it.
- Platform rows reflect the deployment contracts' current modes.

## Cross-references
- `./implementation-roadmap.md`
- `./enhancement-roadmap.md`
- `../execution/trading/strategies.md`

## Operational Contract

This document owns the feature matrix: strategies, platforms, and app modes with status. Behavior for each feature is owned by its canonical owner; this matrix is the status table.

## Example
A user checks the matrix to confirm that simulation mode is the current default for Phase 1.
