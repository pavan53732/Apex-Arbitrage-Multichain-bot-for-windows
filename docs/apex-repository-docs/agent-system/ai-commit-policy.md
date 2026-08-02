---
metadata_schema_version: 1.0
document_id: DOC-0451
title: AI Commit Policy
plane: Repository Operating Model
domain: Agent System
class: Policy
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-repository-docs/agent-system/ai-commit-policy.md
related_concepts:
  - CONCEPT-0001
  - CONCEPT-0451
dependencies:
  - DOC-0001
  - DOC-0016
  - DOC-0442
  - DOC-0070
  - DOC-0447
  - DOC-0448
  - DOC-0449
  - DOC-0450
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Owner
owned_domains:
  - Agent System
type: STANDARD
purpose: Defines exactly when an AI agent is allowed to create a commit, including preconditions, commit message requirements, prohibitions, and post-commit verification.
scope: All repository-facing AI agents.
---

# AI Commit Policy

## Purpose

This policy answers one question: **When is an AI allowed to create a commit?** It defines mandatory preconditions, commit message format, prohibited scenarios, and post-commit verification.

---

## Preconditions (ALL Must Be True)

Before any commit, the AI agent MUST verify:

### 1. All Requested Work Completed
- [ ] Every task in the execution plan is done
- [ ] No partial implementations
- [ ] No "TODO" comments left in committed files

### 2. Required Validators Passed (0 Errors)
- [ ] VAL-006: Generated Artifact Guard — PASS
- [ ] VAL-002: Metadata Validator — PASS
- [ ] VAL-001: Cross-Reference Validator — PASS
- [ ] VAL-004: Registry Consistency Validator — PASS
- [ ] VAL-003: Concept Uniqueness Validator — PASS
- [ ] VAL-008: Traceability Validator — PASS
- [ ] VAL-005: Orphan Detector — PASS
- [ ] VAL-007: Documentation-Class Validator — PASS

### 3. Registry Consistency Verified
- [ ] Concept Registry matches canonical documents
- [ ] Document Registry matches filesystem
- [ ] Traceability Registry IDs resolve
- [ ] Registry version metadata current

### 4. Metadata Valid
- [ ] All frontmatter fields present and valid enums
- [ ] Document IDs correct format (DOC-XXXX)
- [ ] Concept IDs correct format (CONCEPT-XXXX)
- [ ] Status values valid
- [ ] Authority values valid
- [ ] Class values valid
- [ ] Plane values exact match

### 5. Cross-References Repaired
- [ ] No broken internal links
- [ ] No broken DOC-ID references
- [ ] No broken CONCEPT-ID references
- [ ] No broken anchor links

### 6. No Temporary Artifacts
- [ ] No AUDIT.md, REVIEW.md, REPORT.md, SUMMARY.md
- [ ] No ANALYSIS.md, FINDINGS.md, NOTES.md, PLAN.md
- [ ] No TODO.md, MIGRATION.md, IMPLEMENTATION-REPORT.md
- [ ] No COMPLETION-REPORT.md, STATUS.md, LOG.md, RESULT.md
- [ ] No *.tmp, *.bak, *.old files
- [ ] No CI/CD files (.github/workflows/, .gitlab-ci.yml, etc.)

### 7. Working Tree Contains Only Intentional Changes
- [ ] `git status` shows only files part of the planned change
- [ ] No untracked files except new permanent documents
- [ ] No unintended modifications to unrelated files

---

## Commit Message Requirements

### Format (Conventional + Registry)
```
<type>(<scope>): <action> <identifier> - <summary>

[optional body]

Registry-Version: X.Y.Z (if registry changed)
Validator-Pass: VAL-XXX,VAL-YYY,...
```

### Type Must Match Change Classification Matrix
| Class | Type |
| --- | --- |
| DOC-CANON | docs(canon) |
| DOC-DERIVED | docs(derived) |
| DOC-POLICY | docs(policy) |
| DOC-ARCH | docs(arch) |
| DOC-HIST | docs(hist) |
| REG-CONCEPT | registry(concept) |
| REG-DOCUMENT | registry(doc) |
| REG-TRACE | registry(trace) |
| REG-GOV | registry(gov) |
| META-FIX | meta |
| REF-REPAIR | ref |
| NAV-UPDATE | nav |
| FOLDER-SPLIT | structure(split) |
| FOLDER-MOVE | structure(move) |
| VALID-SPEC | validator(spec) |
| VALID-IMPL | validator(impl) |
| AI-GOV | ai(gov) |
| LIFECYCLE | lifecycle |
| CONCEPT-LIFECYCLE | concept(lifecycle) |
| REFACTOR | refactor |
| FEATURE | feat |
| CONFIG | config |
| SCRIPT | script |

### Prohibited Message Patterns
```
❌ "fix stuff"
❌ "updates"
❌ "misc changes"
❌ "WIP"
❌ "cleanup"
❌ "minor fixes"
❌ "" (empty)
```

### One Logical Change Per Commit
- Split multi-class changes into separate commits
- Each commit has exactly one class from Change Classification Matrix
- Registry updates bundled with their document changes

---

## When Commits Are PROHIBITED

| Condition | Action |
| --- | --- |
| Any validator failing | STOP → Repair → Re-validate |
| Partial implementation | STOP → Complete work |
| Unresolved merge conflict | STOP → Resolve per Failure Policy |
| Dirty workspace (unintentional changes) | STOP → Clean workspace |
| Broken registry consistency | STOP → Sync registries |
| Missing Concept ID allocation | STOP → Request Runtime Team |
| Temporary artifacts present | STOP → Delete artifacts |
| No change classification identified | STOP → Classify first |

---

## Post-Commit Verification (Mandatory)

After `git commit`, the AI MUST verify:

```
1. git status → clean (only staged changes committed)
2. git log --oneline -1 → shows new commit with correct message
3. Commit SHA recorded for push verification
4. All validators still pass on committed state
```

**Only after ALL verify → proceed to Push Policy.**

---

## Quick Checklist (Pre-Commit)

```
□ All work complete
□ VAL-006 PASS
□ VAL-002 PASS
□ VAL-001 PASS
□ VAL-004 PASS
□ VAL-003 PASS
□ VAL-008 PASS
□ VAL-005 PASS
□ VAL-007 PASS
□ Registries consistent
□ Metadata valid
□ Cross-references repaired
□ No temp artifacts
□ Clean working tree
□ Change class identified
□ Commit message formatted
□ Post-commit verify ready
```

---

## Related Documents
- [AI Change Classification Matrix](ai-change-classification-matrix.md)
- [AI Push Policy](ai-push-policy.md)
- [AI Failure Policy](ai-failure-policy.md)
- [AI Execution Contract](ai-execution-contract.md)
- [Validation Specification](../validation/validation-specification.md)
- [Registry Governance Standard](../registries/registry-governance-standard.md)