---
metadata_schema_version: 1.0
document_id: DOC-0449
title: AI Failure Policy
plane: Repository Operating Model
domain: Agent System
class: Policy
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-repository-docs/agent-system/ai-failure-policy.md
related_concepts:
  - CONCEPT-0001
  - CONCEPT-0449
dependencies:
  - DOC-0001
  - DOC-0016
  - DOC-0442
  - DOC-0070
  - DOC-0447
  - DOC-0448
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Owner
owned_domains:
  - Agent System
type: STANDARD
purpose: Defines deterministic failure handling behavior for every failure type an AI agent may encounter.
scope: All repository-facing AI agents.
---

# AI Failure Policy

## Purpose

This policy defines the exact, deterministic behavior for every failure type. No improvisation. No "try again differently." Every failure has a prescribed response.

---

## Core Principle

```
FAILURE → STOP → REPAIR → RE-VALIDATE → CONTINUE
```

**Never**: Commit with failures, push with failures, skip validators, create workarounds.

---

## Failure Type Matrix

| Failure Type | Detection | Immediate Action | Repair Action | Re-validation | Escalation |
| --- | --- | --- | --- | --- | --- |
| **Metadata Validation Fails** (VAL-002) | Pre-flight or Repair phase | STOP implementation | Fix frontmatter fields per schema | Run VAL-002 only | If schema unclear → Runtime Team |
| **Cross-Reference Broken** (VAL-001) | Pre-flight or Repair phase | STOP implementation | Fix link or create missing target | Run VAL-001 only | If target concept missing → Request Concept ID |
| **Registry Inconsistent** (VAL-004) | Repair phase | STOP implementation | Sync registry with filesystem | Run VAL-004 + VAL-003 | If conflict → Regenerate per Registry Governance |
| **Duplicate Concept Owner** (VAL-003) | Repair phase | STOP implementation | Resolve to single Owner per concept | Run VAL-003 + VAL-004 | If ambiguity → Runtime Team |
| **Traceability Broken** (VAL-008) | Repair phase | STOP implementation | Fix traceability IDs or relationships | Run VAL-008 | If chain broken → Check Concept Registry |
| **Orphan Document** (VAL-005) | Repair phase | STOP implementation | Add navigation/traceability or deprecate | Run VAL-005 | If truly orphaned → Deprecate per lifecycle |
| **Document Class Mismatch** (VAL-007) | Repair phase | STOP implementation | Correct class/plane assignment | Run VAL-007 | If plane boundary violated → Runtime Team |
| **Generated Artifact Detected** (VAL-006) | Repair phase | STOP implementation | Delete prohibited file | Run VAL-006 | If intentional → Request exception |
| **Merge Conflict (Registry)** | Git merge | STOP; do not auto-resolve | Regenerate from canonical sources | Full suite | Runtime Team if unresolvable |
| **Merge Conflict (Document)** | Git merge | STOP | Resolve preserving canonical meaning | Full suite | Runtime Team if semantic conflict |
| **Push Failure** | Git push | STOP | Diagnose (auth, remote, sync) | N/A (retry after fix) | Runtime Team if persistent |
| **Sync Failure (origin/main)** | Post-push verify | STOP | Fetch, rebase if needed, re-verify | N/A | Runtime Team if divergent |
| **Validator Timeout** | Validator execution | STOP | Check for infinite loops, large files | Re-run with timeout | Runtime Team if systemic |
| **Missing Concept ID** | Pre-flight | STOP | Request Runtime Team allocation | N/A (wait) | Runtime Team |
| **Workspace Not Clean** | Pre-commit or post-push | STOP | Remove temp files, reset unintended changes | Full suite | If persistent → Runtime Team |

---

## Detailed Failure Procedures

### 1. Metadata Validation Fails (VAL-002)
```
DETECT: VAL-002 reports errors
ACTION:
  1. Read error output (file, field, expected vs actual)
  2. Fix each field to match schema enum/format
  3. Common fixes:
     - status: use valid enum (Draft/Review/Active/Deprecated/Archived/Superseded/Experimental)
     - authority: use valid enum (Canonical/Derived/Reference/Historical/Generated)
     - class: use valid class from taxonomy
     - document_id: DOC-XXXX format
     - concept_id in related_concepts: CONCEPT-XXXX format
     - plane: exact "Repository Operating Model" or "Product Specification"
     - last_updated: ISO date (YYYY-MM-DD)
  4. Re-run VAL-002
  5. If pass → continue; if fail → repeat
ESCALATION: If schema ambiguous → Runtime Team
```

### 2. Cross-Reference Broken (VAL-001)
```
DETECT: VAL-001 reports unresolved references
ACTION:
  1. Read error output (file, line, reference target)
  2. For each broken reference:
     - If target file moved → update path
     - If target file renamed → update reference
     - If target file deleted → restore or remove reference
     - If target DOC-ID not in registry → add to registry
     - If target CONCEPT-ID not in registry → request Concept ID
     - If anchor link broken → fix anchor or remove
  3. Re-run VAL-001
  4. If pass → continue; if fail → repeat
ESCALATION: If target concept missing → Request Concept ID from Runtime Team
```

### 3. Registry Inconsistent (VAL-004)
```
DETECT: VAL-004 reports mismatches
ACTION:
  1. Read error output (registry vs filesystem)
  2. For each mismatch:
     - File in registry but not on disk → remove from registry OR restore file
     - File on disk but not in registry → add to registry with correct metadata
     - Path mismatch → update registry path
     - Concept role mismatch → correct role
  3. Follow Registry Governance Standard update order:
     Concept Registry → Document Registry → Traceability Registry
  4. Re-run VAL-004 + VAL-003
  5. If pass → continue; if fail → repeat
ESCALATION: If irreconcilable → Regenerate registries per Registry Governance Standard
```

### 4. Duplicate Concept Owner (VAL-003)
```
DETECT: VAL-003 reports multiple Owners for same concept
ACTION:
  1. Identify the concept and competing Owner documents
  2. Determine correct Owner (Domain Ownership Matrix)
  3. For incorrect Owner:
     - Change concept_role from Owner to Reference
     - Add supersedes/superseded_by links
  4. Update Traceability Registry: Superseded By Concept
  5. Re-run VAL-003 + VAL-004 + VAL-008
  6. If pass → continue; if fail → repeat
ESCALATION: If ambiguity → Runtime Team decides canonical owner
```

### 5. Traceability Broken (VAL-008)
```
DETECT: VAL-008 reports invalid relationships
ACTION:
  1. Read error output (TRACE-ID, source, target, relationship)
  2. For each broken trace:
     - If source/target ID not in registry → add or fix ID
     - If relationship type invalid → correct to allowed set
     - If circular DependsOn → break cycle
     - If untraced requirement → add trace or suppress warning
  2. Re-run VAL-008
  3. If pass → continue; if fail → repeat
ESCALATION: If chain fundamentally broken → Runtime Team
```

### 6. Orphan Document (VAL-005)
```
DETECT: VAL-005 reports orphaned canonical document or concept
ACTION:
  1. Identify orphaned item
  2. Add to parent domain README navigation
  3. Add traceability relationship (Indexes or References)
  4. If truly no longer needed → Deprecate per Document Lifecycle Policy
  5. Re-run VAL-005
  6. If pass → continue; if fail → repeat
ESCALATION: If architectural orphan → Runtime Team
```

### 7. Document Class Mismatch (VAL-007)
```
DETECT: VAL-007 reports class/plane mismatch
ACTION:
  1. Read error output (file, current class, expected class)
  2. Correct class to match document function
  3. If plane boundary violated (ROM doc in PS or vice versa):
     - Move to correct plane/domain
     - Update all references
  4. Re-run VAL-007
  5. If pass → continue; if fail → repeat
ESCALATION: If classification unclear → Runtime Team
```

### 8. Generated Artifact Detected (VAL-006)
```
DETECT: VAL-006 reports prohibited file
ACTION:
  1. Identify prohibited file
  2. If temporary (AUDIT, REVIEW, SUMMARY, REPORT, NOTES, PLAN, TODO, MIGRATION, LOG, STATUS, RESULT, *.tmp, *.bak, *.old) → DELETE
  3. If CI/CD (.github/workflows/, .gitlab-ci.yml, jenkins*, .circleci/) → DELETE
  4. If generated doc not in generated/ → MOVE to generated/ or DELETE
  5. Re-run VAL-006
  6. If pass → continue; if fail → repeat
ESCALATION: If file claimed as permanent → Runtime Team review
```

### 9. Merge Conflict (Registry)
```
DETECT: Git reports conflict in registry files
ACTION:
  1. DO NOT AUTO-RESOLVE
  2. Abort merge
  3. Regenerate registries from canonical sources per Registry Governance Standard
  4. Or manually resolve using Registry Governance Standard rules
  5. Run FULL validator suite (VAL-001 through VAL-008)
  6. If all pass → continue merge
ESCALATION: Runtime Team if regeneration fails
```

### 10. Merge Conflict (Document)
```
DETECT: Git reports conflict in document files
ACTION:
  1. Resolve preserving canonical meaning
  2. Prefer canonical source content
  3. Update metadata (version, last_updated)
  4. Run FULL validator suite
  5. If all pass → continue merge
ESCALATION: Runtime Team if semantic conflict
```

### 11. Push Failure
```
DETECT: Git push fails
ACTION:
  1. Read error (authentication, remote rejected, non-fast-forward, etc.)
  2. If auth → Check credentials/token
  3. If non-fast-forward → Fetch, rebase, re-validate, re-push
  4. If remote rejected (hooks) → Check remote policies
  5. Retry push
  6. If persistent → Runtime Team
ESCALATION: Runtime Team after 3 failed retries
```

### 12. Sync Failure (origin/main)
```
DETECT: Post-push verify shows divergence
ACTION:
  1. git fetch origin
  2. Compare local HEAD vs origin/main
  3. If local behind → Fast-forward merge, re-validate, re-push
  4. If local ahead → Push again
  5. If diverged → Rebase, re-validate, force-push (with Runtime Team approval)
  6. Verify sync
ESCALATION: Runtime Team for force-push decisions
```

### 13. Validator Timeout
```
DETECT: Validator exceeds 30-second limit
ACTION:
  1. Check for infinite loops in validator code
  2. Check for extremely large files
  3. Run validator on subset to isolate
  4. Fix validator or exclude pathological case
  5. Re-run
ESCALATION: Runtime Team if systemic
```

### 14. Missing Concept ID
```
DETECT: Need Concept ID but none exists
ACTION:
  1. STOP implementation
  2. Request Runtime Team allocation via chat
  3. WAIT for allocation
  4. Use allocated ID
  5. Continue
ESCALATION: Runtime Team (only they allocate)
```

### 15. Workspace Not Clean
```
DETECT: git status shows untracked/modified files not in plan
ACTION:
  1. Identify unexpected files
  2. If temp files (AUDIT.md, *.tmp, etc.) → DELETE
  3. If unintended modifications → git checkout -- <file>
  4. If intentional new documents → include in commit
  5. Re-run full validator suite
  6. If clean → continue
ESCALATION: Runtime Team if persistent unexplained changes
```

---

## Failure State Machine

```
┌─────────┐     FAILURE      ┌─────────┐     REPAIR      ┌─────────────┐
│ WORKING ├─────────────────►│ STOPPED ├────────────────►│ RE-VALIDATE │
└─────────┘                  └─────────┘                 └──────┬──────┘
      ▲                                                           │
      │                        PASS                               │ FAIL
      │                           │                               │
      └───────────────────────────┴───────────────────────────────┘
```

**Never** transition from STOPPED to WORKING without RE-VALIDATE passing.

---

## Escalation Protocol

| Level | Trigger | Action |
| --- | --- | --- |
| **Level 1** | Single failure, clear repair | Agent repairs, re-validates |
| **Level 2** | Repeated same failure (3x) | Agent requests Runtime Team guidance |
| **Level 3** | Cross-cutting failure (multiple validators) | Agent stops, Runtime Team intervenes |
| **Level 4** | Architectural ambiguity | Runtime Team decides, documents decision |

---

## Related Documents
- [AI Capability Matrix](ai-capability-matrix.md)
- [AI Decision Tree](ai-decision-tree.md)
- [AI Execution Contract](ai-execution-contract.md)
- [AI Change Classification Matrix](ai-change-classification-matrix.md)
- [AI Commit Policy](ai-commit-policy.md)
- [AI Push Policy](ai-push-policy.md)
- [AI Workspace Policy](ai-workspace-policy.md)
- [Validation Specification](../validation/validation-specification.md)
- [Registry Governance Standard](../registries/registry-governance-standard.md)