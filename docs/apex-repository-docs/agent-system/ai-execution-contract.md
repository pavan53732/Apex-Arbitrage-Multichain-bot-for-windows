---
metadata_schema_version: 1.0
document_id: DOC-0448
title: AI Execution Contract
plane: Repository Operating Model
domain: Agent System
class: Policy
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-repository-docs/agent-system/ai-execution-contract.md
related_concepts:
  - CONCEPT-0001
  - CONCEPT-0448
dependencies:
  - DOC-0001
  - DOC-0016
  - DOC-0442
  - DOC-0070
  - DOC-0447
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Owner
owned_domains:
  - Agent System
type: STANDARD
purpose: Formalizes the mandatory execution contract that every AI agent must follow for every repository task.
scope: All repository-facing AI agents.
---

# AI Execution Contract

## Purpose

This contract defines the mandatory, non-negotiable execution sequence that every AI agent must follow for every task in this repository. It is the behavioral specification for repository AI agents.

---

## The Contract (12 Steps - Mandatory Order)

```
┌─────────────────────────────────────────────────────────────────────┐
│                    AI EXECUTION CONTRACT                            │
├─────────────────────────────────────────────────────────────────────┤
│  1. READ          → Read all relevant canonical documents           │
│  2. UNDERSTAND    → Confirm understanding of task and constraints   │
│  3. LOCATE        → Find canonical owner for every concept involved │
│  4. PLAN          → Create execution plan following decision tree   │
│  5. VALIDATE      → Run pre-flight validators (VAL-002, VAL-001)   │
│  6. IMPLEMENT     → Execute changes per plan                        │
│  7. REPAIR        → Fix all validator failures                      │
│  8. REVIEW        → Self-review against all policies                │
│  9. COMMIT        → Atomic commit with all related changes          │
│ 10. PUSH          → Push to main (if Tier 1 agent)                  │
│ 11. VERIFY        → Confirm origin/main sync                        │
│ 12. RETURN        → Return results in chat                          │
│ 13. CLEAN         → Leave workspace clean (no temp files)           │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Step-by-Step Specification

### Step 1: READ
**Action**: Read all relevant canonical documents before acting.
**Required Reads**:
- AGENTS.md (always)
- REBUILD-SYSTEM-SPECIFICATION.md (for structural changes)
- Domain README for target domain
- Canonical owner document for each concept
- Applicable standards (README Governance, Registry Governance, etc.)
**Output**: Confirmed understanding in chat.

### Step 2: UNDERSTAND
**Action**: Explicitly confirm task understanding.
**Required**:
- Identify which plane (Repository Operating Model vs Product Specification)
- Identify domain(s) affected
- Identify document class(es) involved
- Identify if new Concept ID needed
- Confirm no temporary files will be created
**Output**: "Understood: [task summary with plane/domain/class/Concept ID plan]"

### Step 3: LOCATE
**Action**: Find canonical owner for every concept.
**Required**:
- Query Concept Registry for each concept
- Identify document with `concept_role: Owner`
- Confirm document exists at registered path
- If no owner → request Runtime Team for Concept ID allocation
**Output**: List of canonical owners with DOC-IDs and paths.

### Step 4: PLAN
**Action**: Create execution plan following AI Decision Tree.
**Required**:
- Determine exact files to create/modify/move
- Determine registry updates needed
- Determine README navigation updates needed
- Identify validator sequence
- Identify commit message format
**Output**: Written plan (in chat or as todo list).

### Step 5: VALIDATE (Pre-flight)
**Action**: Run pre-flight validators before implementing.
**Required Validators**:
- VAL-002: Metadata Validator (on existing files to be modified)
- VAL-001: Cross-Reference Validator (on existing files)
**Pass Criteria**: 0 errors
**On Failure**: Repair before proceeding to Step 6.

### Step 6: IMPLEMENT
**Action**: Execute changes per plan.
**Rules**:
- Edit canonical documents first (edit-first rule)
- Create new documents only if permanent knowledge
- Update registries in same logical change
- Update README navigation in same logical change
- Follow naming conventions
- No temporary files
- No CI/CD files
**Output**: Modified/created files.

### Step 7: REPAIR
**Action**: Run full validator suite and fix ALL failures.
**Required Validators (in order)**:
1. VAL-006: Generated Artifact Guard
2. VAL-002: Metadata Validator
3. VAL-001: Cross-Reference Validator
4. VAL-004: Registry Consistency Validator
5. VAL-003: Concept Uniqueness Validator
6. VAL-008: Traceability Validator
7. VAL-005: Orphan Detector
8. VAL-007: Documentation-Class Validator
**Pass Criteria**: 0 errors across ALL validators
**On Failure**: Fix → Re-run → Repeat until all pass.

### Step 8: REVIEW
**Action**: Self-review against all policies.
**Checklist**:
- [ ] Canonical edit-first rule followed (no duplicates)
- [ ] Concept IDs valid and not invented
- [ ] Document IDs valid and not invented
- [ ] Registries updated in same commit
- [ ] README navigation updated
- [ ] Cross-references repaired
- [ ] Metadata complete and valid
- [ ] No temporary files created
- [ ] No CI/CD files created
- [ ] Change classification identified
- [ ] Commit message format correct
**On Failure**: Return to Step 6 or 7.

### Step 9: COMMIT
**Action**: Create atomic commit with all related changes.
**Rules**:
- Single commit for all related changes (docs + registries + READMEs)
- Commit message format per Registry Governance Standard / AI Commit Policy
- Include validator pass confirmation
- No partial commits
**Output**: Commit SHA.

### Step 10: PUSH
**Action**: Push to main branch.
**Tier 1 Agents (Kilo Code, Cursor, Claude Code, Gemini CLI)**:
- Push to `main` directly
**Tier 2 Agents (GitHub Copilot, Copilot CLI)**:
- Cannot push; request human to push
**Rules**:
- Only push after successful commit
- Only push if workspace clean
**Output**: Push confirmation.

### Step 11: VERIFY
**Action**: Verify synchronization with origin/main.
**Required**:
- `git status` shows clean
- `git log --oneline -1` matches local commit
- Remote HEAD matches local HEAD
**On Failure**: Report sync failure → AI Failure Policy.

### Step 12: RETURN
**Action**: Return results in chat.
**Format**:
```
✅ Task Complete
Commit: <sha>
Push: <verified/pending>
Validators: All passed
Files changed: <list>
```
**No additional files created**.

### Step 13: CLEAN
**Action**: Leave workspace clean.
**Required**:
- No temporary files (AUDIT.md, REVIEW.md, SUMMARY.md, etc.)
- No `.tmp`, `.bak`, `.old` files
- No generated reports
- No untracked files except intentional new documents
- `git status` clean (except intentional changes)

---

## Contract Enforcement

| Violation | Consequence |
| --- | --- |
| Skip Step 1 (Read) | Task rejected; must re-read |
| Skip Step 3 (Locate) | Task rejected; must locate canonical owners |
| Skip Step 5 (Pre-flight) | Task rejected; must validate first |
| Skip Step 7 (Repair) | Commit blocked; must fix all validators |
| Skip Step 9 (Atomic commit) | Commit rejected; must combine |
| Skip Step 11 (Verify) | Push rejected; must verify sync |
| Skip Step 13 (Clean) | Task incomplete; must clean workspace |
| Create temp files | VAL-006 failure; must delete |

---

## Emergency Override

**Only** Runtime Team may authorize deviation from this contract.
**Requirements**:
- Documented justification in commit message
- All validators still must pass
- Post-task audit required

---

## Quick Reference

```
READ → UNDERSTAND → LOCATE → PLAN → VALIDATE → IMPLEMENT → REPAIR → REVIEW → COMMIT → PUSH → VERIFY → RETURN → CLEAN

NEVER SKIP. NEVER REORDER. NEVER CREATE TEMP FILES.
```

---

## Related Documents
- [AI Capability Matrix](ai-capability-matrix.md)
- [AI Decision Tree](ai-decision-tree.md)
- [AI Failure Policy](ai-failure-policy.md)
- [AI Change Classification Matrix](ai-change-classification-matrix.md)
- [AI Commit Policy](ai-commit-policy.md)
- [AI Push Policy](ai-push-policy.md)
- [AI Workspace Policy](ai-workspace-policy.md)