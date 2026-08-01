---
metadata_schema_version: 1.0
document_id: DOC-0077
title: AI Workspace Policy
plane: Repository Operating Model
domain: Agent System
class: Policy
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-repository-docs/agent-system/ai-workspace-policy.md
related_concepts:
  - CONCEPT-0001
  - CONCEPT-0077
dependencies:
  - DOC-0001
  - DOC-0016
  - DOC-0065
  - DOC-0070
  - DOC-0071
  - DOC-0072
  - DOC-0073
  - DOC-0074
  - DOC-0075
  - DOC-0076
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Owner
owned_domains:
  - Agent System
type: STANDARD
purpose: Explicitly prohibits leaving behind temporary execution artifacts and requires clean workspace termination for all AI agents.
scope: All repository-facing AI agents.
---

# AI Workspace Policy

## Purpose

This policy prevents repository pollution by explicitly forbidding AI agents from leaving behind any temporary execution artifacts. The repository is not a workspace for temporary AI outputs.

---

## Explicitly Prohibited Artifacts

### Report/Documentation Artifacts (Never Create Unless Explicitly Requested)
```
AUDIT.md
REVIEW.md
REPORT.md
SUMMARY.md
ANALYSIS.md
FINDINGS.md
NOTES.md
PLAN.md
TODO.md
MIGRATION.md
IMPLEMENTATION-REPORT.md
COMPLETION-REPORT.md
STATUS.md
LOG.md
RESULT.md
```

### Temporary File Extensions (Never Create)
```
*.tmp
*.bak
*.old
*.temp
*.swp
*.swo
*~
```

### Generated Data Formats (Never Create Unless Permanent Knowledge)
```
*.json (unless canonical registry or config)
*.csv (unless canonical data registry)
*.yaml / *.yml (unless canonical config)
*.xml (unless canonical)
*.pdf (unless canonical reference)
```

### CI/CD and Automation (Never Create)
```
.github/workflows/
.gitlab-ci.yml
.github/actions/
jenkins*
.circleci/
.azure-pipelines/
.travis.yml
```

### Scratch/Working Directories (Never Create in Repository)
```
scratch/
temp/
tmp/
work/
working/
build/
dist/
out/
output/
*.log
```

---

## Mandatory Clean Workspace Requirements

### At Task Start
- `git status` must be clean
- No untracked files from previous runs
- No modified files from previous runs

### During Task
- No temporary files created in repository
- All working files in `/tmp/` or agent's designated scratch space
- No intermediate outputs written to repository paths

### At Task End (Mandatory)
```
BEFORE returning results:
1. git status → must show ONLY intentional changes
2. No untracked files except new permanent documents
3. No modified files except intended changes
4. No temporary artifacts anywhere in repository
5. No empty directories created
6. No orphan files
```

### Clean Workspace Verification
```bash
# Must pass all checks
git status --porcelain | grep -v "^??" | grep -v "^A " | wc -l  # = 0 (no unintended modifications)
git status --porcelain | grep "^??" | grep -v "docs/" | wc -l  # = 0 (no untracked outside docs)
find . -name "*.tmp" -o -name "*.bak" -o -name "*.old" -o -name "AUDIT.md" -o -name "REVIEW.md" -o -name "REPORT.md" -o -name "SUMMARY.md" -o -name "ANALYSIS.md" -o -name "FINDINGS.md" -o -name "NOTES.md" -o -name "PLAN.md" -o -name "TODO.md" -o -name "MIGRATION.md" -o -name "STATUS.md" -o -name "LOG.md" -o -name "RESULT.md" | wc -l  # = 0
```

---

## Results Return Policy

### Default: Return in Chat
All task results, analysis, findings, summaries, and reports MUST be returned **in the chat conversation**.

### Exception: Explicit User Request for Permanent Documentation
Only create a permanent repository document if:
1. User explicitly requests: "Create a permanent document for this"
2. The content represents permanent repository knowledge (not task execution output)
3. It follows Document Lifecycle Policy (Draft → Review → Active)
4. It gets a valid DOC-ID and Concept ID
5. It passes all validators

### Examples

| Output Type | Default | Exception |
| --- | --- | --- |
| Task completion summary | Chat only | User asks for permanent record |
| Error analysis | Chat only | User asks for permanent doc |
| Migration plan | Chat only | User asks for permanent doc |
| Code review findings | Chat only | User asks for permanent doc |
| Test results | Chat only | User asks for permanent doc |
| Architecture decision | ADR (permanent) | — |

---

## Scratch Space Usage

### Approved Scratch Locations
- `/tmp/agent_c29bde1a-ddd6-416e-ba05-aace3b75f6fb/` (pre-approved)
- System temp directory (`$TMPDIR`, `/tmp`)
- Agent's designated workspace outside repository

### Prohibited Scratch Locations
- Repository root
- Any `docs/` subdirectory
- Any domain folder
- `.git/`

---

## Enforcement

### Validator Checks
- **VAL-006 (Generated Artifact Guard)** catches prohibited files at commit time
- **AI Commit Policy** requires clean workspace pre-commit
- **AI Failure Policy** handles workspace violations

### Violation Consequences
| Violation | Detection | Consequence |
| --- | --- | --- |
| Prohibited file committed | VAL-006 | Commit blocked, file must be deleted |
| Temp file in workspace at commit | Commit Policy | Commit blocked, workspace must be cleaned |
| Results written to file instead of chat | Review | File deleted, results returned in chat |
| Scratch files in repository | VAL-006 / Review | Files deleted |

---

## Quick Reference: DO / DO NOT

### DO ✅
- Work in `/tmp/agent_c29bde1a-ddd6-416e-ba05-aace3b75f6fb/`
- Return all analysis, summaries, reports in chat
- Create permanent documents only when explicitly requested
- Verify `git status` clean at start and end
- Delete any accidental temp files immediately

### DO NOT ❌
- Create AUDIT.md, REVIEW.md, REPORT.md, SUMMARY.md, etc.
- Create *.tmp, *.bak, *.old files in repository
- Create CI/CD files (.github/workflows/, etc.)
- Write results to repository files instead of chat
- Leave empty directories
- Leave orphan files
- Use repository as scratch space

---

## Related Documents
- [AI Capability Matrix](ai-capability-matrix.md)
- [AI Decision Tree](ai-decision-tree.md)
- [AI Execution Contract](ai-execution-contract.md)
- [AI Failure Policy](ai-failure-policy.md)
- [AI Commit Policy](ai-commit-policy.md)
- [AI Push Policy](ai-push-policy.md)
- [Validation Specification](../validation/validation-specification.md)
- [Temporary Execution Output Policy (AGENTS.md)](../../../AGENTS.md)