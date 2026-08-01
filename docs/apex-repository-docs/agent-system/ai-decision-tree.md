---
metadata_schema_version: 1.0
document_id: DOC-0071
title: AI Decision Tree
plane: Repository Operating Model
domain: Agent System
class: Policy
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-repository-docs/agent-system/ai-decision-tree.md
related_concepts:
  - CONCEPT-0001
  - CONCEPT-0071
dependencies:
  - DOC-0001
  - DOC-0016
  - DOC-0065
  - DOC-0070
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Owner
owned_domains:
  - Agent System
type: STANDARD
purpose: Single deterministic decision tree that every AI agent must follow for any repository change.
scope: All repository-facing AI agents.
---

# AI Decision Tree

## Purpose

This decision tree provides a single, deterministic flow for every AI agent when considering any action in the repository. No deviations. No improvisation. Every agent follows this exact logic.

---

## Decision Tree: Need to Change Documentation?

```
START: Need to change documentation?
│
├─► NO ──► Reply only in chat. Do not create files. END.
│
└─► YES ──► Does a canonical document already own this concept?
              │
              ├─► YES ──► Edit the canonical document.
              │              │
              │              ├─► Update metadata (version, last_updated)
              │              ├─► Update registries if concept role changes
              │              ├─► Update cross-references if needed
              │              ├─► Run full validator suite (VAL-001 through VAL-008)
              │              │
              │              ├─► ALL PASS ──► Commit → Push → Verify → END
              │              │
              │              └─► ANY FAIL ──► Repair → Re-validate → (loop)
              │
              └─► NO ──► Is this permanent repository knowledge?
                        │
                        ├─► NO ──► Reply only in chat. Do not create files. END.
                        │
                        └─► YES ──► Is there an active Concept ID for this?
                                      │
                                      ├─► YES ──► Use existing Concept ID
                                      │              │
                                      │              ├─► Create new document with that Concept ID
                                      │              ├─► Place in narrowest matching subdomain
                                      │              ├─► Set concept_role: Owner (or Reference/Index)
                                      │              ├─► Update parent domain README navigation
                                      │              ├─► Update registries in same commit
                                      │              ├─► Run full validator suite
                                      │              │
                                      │              ├─► ALL PASS ──► Commit → Push → Verify → END
                                      │              │
                                      │              └─► ANY FAIL ──► Repair → Re-validate → (loop)
                                      │
                                      └─► NO ──► Request Runtime Team for new Concept ID
                                                     │
                                                     ├─► WAIT for allocation
                                                     │
                                                     └─► Then: Create document with new Concept ID
                                                              (same steps as above)
```

---

## Decision Tree: Need to Modify Code/Implementation?

```
START: Need to modify implementation code?
│
├─► NO ──► Not applicable. END.
│
└─► YES ──► Does this change product behavior?
              │
              ├─► NO (repository tooling only) ──► Follow documentation tree above
              │
              └─► YES ──► Is there a canonical specification for this behavior?
                          │
                          ├─► YES ──► Update specification first (documentation tree)
                          │              │
                          │              └─► Then implement to match specification
                          │                       │
                          │                       ├─► Run tests if applicable
                          │                       ├─► Run validators
                          │                       │
                          │                       ├─► ALL PASS ──► Commit → Push → Verify → END
                          │                       │
                          │                       └─► ANY FAIL ──► Repair → Re-validate → (loop)
                          │
                          └─► NO ──► Does this require new architecture?
                                        │
                                        ├─► YES ──► STOP. Create ADR first (doc tree).
                                        │              │
                                        │              └─► Wait for approval.
                                        │
                                        └─► NO ──► Implement with minimal scope
                                                      │
                                                      ├─► Run tests
                                                      ├─► Run validators
                                                      │
                                                      ├─► ALL PASS ──► Commit → Push → Verify → END
                                                      │
                                                      └─► ANY FAIL ──► Repair → Re-validate → (loop)
```

---

## Decision Tree: Need to Reorganize/Move Files?

```
START: Need to reorganize or move files?
│
├─► NO ──► Not applicable. END.
│
└─► YES ──► Is this a folder split (exceeding 25 docs)?
              │
              ├─► YES ──► Split by semantic subdomain (never alphabetical)
              │              │
              │              ├─► Create new subdomain Concept IDs
              │              ├─► Move documents to new subdomain folders
              │              ├─► Update parent README Canonical Owner Map
              │              ├─► Create new subdomain READMEs (full standard)
              │              ├─► Update registries
              │              ├─► Update traceability
              │              ├─► Run full validator suite
              │              │
              │              ├─► ALL PASS ──► Commit → Push → Verify → END
              │              │
              │              └─► ANY FAIL ──► Repair → Re-validate → (loop)
              │
              └─► NO (simple move/rename) ──► Update all references
                                                    │
                                                    ├─► Update registries
                                                    ├─► Update READMEs
                                                    ├─► Update cross-references
                                                    ├─► Run full validator suite
                                                    │
                                                    ├─► ALL PASS ──► Commit → Push → Verify → END
                                                    │
                                                    └─► ANY FAIL ──► Repair → Re-validate → (loop)
```

---

## Decision Tree: Validator Failure During Work

```
START: Validator failed?
│
├─► VAL-006 (Generated Artifact) ──► Delete prohibited file → Re-validate
│
├─► VAL-002 (Metadata) ──► Fix frontmatter → Re-validate
│
├─► VAL-001 (Cross-Reference) ──► Fix broken link or add missing target → Re-validate
│
├─► VAL-004 (Registry Consistency) ──► Sync registry with filesystem → Re-validate
│
├─► VAL-003 (Concept Uniqueness) ──► Resolve duplicate Owner → Re-validate
│
├─► VAL-008 (Traceability) ──► Fix broken traceability IDs → Re-validate
│
├─► VAL-005 (Orphan) ──► Add navigation/traceability or deprecate → Re-validate
│
├─► VAL-007 (Document Class) ──► Correct class/plane assignment → Re-validate
│
└─► MULTIPLE ──► Fix ALL before committing. Never commit with failures.
```

---

## Decision Tree: Merge Conflict

```
START: Merge conflict detected?
│
├─► NO ──► Continue.
│
└─► YES ──► Is it a registry conflict?
              │
              ├─► YES ──► STOP. Do not auto-resolve.
              │              │
              │              ├─► Regenerate registries from canonical sources
              │              ├─► Or manually resolve using Registry Governance Standard
              │              ├─► Run ALL validators
              │              │
              │              └─► ALL PASS ──► Continue
              │
              └─► NO (document conflict) ──► Resolve preserving canonical meaning
                                                │
                                                ├─► Run validators
                                                │
                                                └─► ALL PASS ──► Continue
```

---

## Mandatory Checkpoints (Never Skip)

| Checkpoint | When | Required |
| --- | --- | --- |
| Concept Registry check | Before any document creation | Yes |
| Canonical owner search | Before any document creation | Yes |
| Narrowest subdomain placement | Before any document creation | Yes |
| README navigation update | After any document add/move | Yes |
| Registry updates | Same commit as doc changes | Yes |
| Full validator suite | Before every commit | Yes |
| Push verification | After every push | Yes |

---

## Quick Reference Card

```
EVERY CHANGE:
1. Read → Understand → Locate Canonical
2. Plan → Validate → Implement
3. Repair → Review → Commit
4. Push → Verify → Return Results
5. Leave Workspace Clean

NEVER:
- Create temp files
- Invent IDs
- Skip validators
- Commit with failures
- Push without verify
- Leave audit/summary/report files
```

---

## Related Documents
- [AI Capability Matrix](ai-capability-matrix.md)
- [AI Execution Contract](ai-execution-contract.md)
- [AI Failure Policy](ai-failure-policy.md)
- [AI Change Classification Matrix](ai-change-classification-matrix.md)
- [AI Commit Policy](ai-commit-policy.md)
- [AI Push Policy](ai-push-policy.md)
- [AI Workspace Policy](ai-workspace-policy.md)