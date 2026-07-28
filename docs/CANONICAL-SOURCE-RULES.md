---
last_updated: 2026-07-29
type: STANDARD
owner: Runtime Team
status: Canonical
version: 1.0.0
purpose: Canonical Source Rules documentation.
scope: Reference documentation.
canonical_source: docs/CANONICAL-SOURCE-RULES.md if filename.startswith('docs/') else CANONICAL-SOURCE-RULES.md
---

# Canonical Source Rules

## Document type
Document type: [REFERENCE]

## Purpose
Defines what wins when documents conflict.

## Rules
- Owner document wins over index or overview.
- Schema wins for field definitions.
- ADR wins for architecture decisions.

