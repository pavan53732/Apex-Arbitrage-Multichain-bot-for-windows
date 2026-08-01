---
metadata_schema_version: 1.0
document_id: DOC-0068
title: Document Lifecycle Policy
plane: Repository Operating Model
domain: Documentation Lifecycle
class: Policy
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-repository-docs/documentation-lifecycle/document-lifecycle-policy.md
related_concepts:
  - CONCEPT-0056
  - CONCEPT-0057
  - CONCEPT-0068
dependencies:
  - DOC-0056
  - DOC-0057
  - DOC-0059
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Owner
owned_domains:
  - Documentation Lifecycle
type: STANDARD
purpose: Defines the lifecycle states and transition rules for all repository documents.
scope: All documents in both Repository Operating Model and Product Specification planes.
---

# Document Lifecycle Policy

## Purpose

This policy defines the lifecycle states, promotion/demotion rules, and metadata requirements for every document in the repository. It ensures consistent document status management and prevents documents from stagnating in ambiguous states.

## Lifecycle States

```
Draft → Review → Active → Deprecated → Archived
```

### State Definitions

| State | Meaning | Typical Duration | Who Can Transition |
| --- | --- | --- | --- |
| **Draft** | Work in progress, not yet reviewed | Days to weeks | Author creates |
| **Review** | Submitted for review, under evaluation | Days | Author → Reviewer |
| **Active** | Approved, current, maintained | Months to years | Reviewer approves |
| **Deprecated** | Superseded, kept for reference only | Indefinite | Owner initiates |
| **Archived** | Historical, no longer relevant | Permanent | Owner initiates |

### Metadata Requirements per State

| Field | Draft | Review | Active | Deprecated | Archived |
| --- | --- | --- | --- | --- | --- |
| `status` | Draft | Review | Active | Deprecated | Archived |
| `version` | 0.x | 0.x | 1.0.0+ | Final version | Final version |
| `last_updated` | Current | Current | Current | Transition date | Transition date |
| `canonical_source` | Self | Self | Self | Self | Self |
| `supersedes` | Empty | Empty | May reference | May reference | References active |
| `superseded_by` | Empty | Empty | Empty | Active DOC-ID | Active DOC-ID |

## Promotion Rules

### Draft → Review
**Trigger**: Author considers document complete
**Requirements**:
- All metadata fields complete
- Canonical concept identified (or new concept proposed)
- Placed in correct domain/subdomain
- README navigation updated in parent domain
- Cross-references added to related documents
- Local validation passes (VAL-002, VAL-001)

**Approver**: Any team member with domain knowledge

### Review → Active
**Trigger**: Reviewer approves
**Requirements**:
- Reviewer validates canonical ownership
- No duplicate concept conflicts (VAL-003)
- Registry updates prepared (if new concept)
- Traceability relationships defined
- All validators pass (VAL-001 through VAL-008)

**Approver**: Domain owner (from Domain Ownership Matrix) or Runtime Team

### Active → Deprecated
**Trigger**: Concept superseded by new canonical document
**Requirements**:
- New canonical document exists with `status: Active`
- New document has `concept_role: Owner` for same concept
- Deprecated document gets `superseded_by` pointing to new
- New document gets `supersedes` pointing to old
- Traceability updated with `Superseded By Concept` relationship
- Registries updated in same commit

**Approver**: Domain owner

### Deprecated → Archived
**Trigger**: No longer needed for reference (after grace period)
**Requirements**:
- Minimum 6 months in Deprecated state
- No active documents reference it (traceability check)
- Moved to `docs/historical/` if not already there
- Status changed to `Archived`

**Approver**: Runtime Team

## Demotion Rules (Exceptional)

### Active → Review
**Trigger**: Critical error found requiring revision
**Requirements**: Runtime Team approval, issue documented

### Review → Draft
**Trigger**: Major revision needed before approval
**Requirements**: Reviewer returns with specific feedback

### Deprecated → Active
**Trigger**: Reversal of deprecation decision
**Requirements**: Runtime Team approval, both documents updated

## Special Cases

### Generated Documents
- Created with `status: Experimental` and `authority: Generated`
- Must not reach `Active` without explicit promotion
- Auto-archived after 30 days if not promoted

### Historical Documents
- Imported with `status: Historical` and `authority: Historical`
- Never transition to Active
- Permanent record

### ADR Documents
- Follow same lifecycle but with additional constraint:
- Once `Active`, never `Deprecated` — only `Superseded` by new ADR
- ADR status: `Proposed` → `Accepted` → `Superseded`

## Compliance

Validators check:
- VAL-002: Status field valid enum
- VAL-004: Registry reflects current status
- VAL-005: No orphaned Active documents
- VAL-008: Traceability chains complete for supersession

## Related Documents
- [Documentation Lifecycle](documentation-lifecycle.md)
- [Documentation Status Review Workflow](documentation-status-review-workflow.md)
- [Domain Ownership Matrix](../traceability/module-ownership-matrix.md)
- [Registry Governance Standard](../registries/registry-governance-standard.md)