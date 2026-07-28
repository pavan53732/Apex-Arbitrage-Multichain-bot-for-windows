---
last_updated: 2026-07-29
type: OVERVIEW
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Readme Governance documentation.
scope: Reference documentation.
canonical_source: docs/README-GOVERNANCE.md
---

# Readme Governance

## Document type
[REFERENCE]

# Governance

## Purpose
Defines how this repository decides ownership, review, approval, and documentation change control.

## Roles
- Architecture docs define boundaries.
- Owner docs define behavior.
- Index docs point to the owner docs.

## Review rules
- Changes to behavior must cite the canonical owner doc.
- Ambiguous behavior must be escalated before implementation.
- New docs must declare their role and authority.

## Decision model
- Repository changes must reference a single authoritative owner doc.
- If ownership is unclear, the change is blocked until resolved.
