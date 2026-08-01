---
metadata_schema_version: 1.0
document_id: DOC-0076
title: AI Push Policy
plane: Repository Operating Model
domain: Agent System
class: Policy
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-repository-docs/agent-system/ai-push-policy.md
related_concepts:
  - CONCEPT-0001
  - CONCEPT-0076
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
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Owner
owned_domains:
  - Agent System
type: STANDARD
purpose: Defines exactly when and how an AI agent synchronizes with the remote repository, including push targets, verification requirements, and failure behaviors.
scope: All repository-facing AI agents.
---

# AI Push Policy

## Purpose

This policy defines the deterministic push behavior for this repository. The repository uses **direct pushes to main** — no feature branches, no pull requests, no CI/CD gates. This document makes that workflow deterministic for every AI agent.

---

## Universal Push Rules

### Push Target
- **Target**: `main` branch only
- **Remote**: `origin`
- **No exceptions**: No feature branches, no PR branches, no release branches

### Push Only After Successful Commit
```
Precondition: AI Commit Policy post-commit verification PASSED
```
- Never push without a preceding successful commit
- Never push uncommitted changes
- Never push with validator failures

---

## Tier-Based Push Authorization

| Tier | Agents | Push Authority |
| --- | --- | --- |
| **Tier 1** | Kilo Code, Cursor, Claude Code, Gemini CLI | **Direct push to main** |
| **Tier 2** | GitHub Copilot, Copilot CLI, other agents without push capability | **Cannot push** — request human to push |

### Tier 1 Push Procedure
```
1. Verify Commit Policy post-commit checks passed
2. git push origin main
3. Verify synchronization (see below)
4. Return push result in chat
```

### Tier 2 Push Procedure
```
1. Verify Commit Policy post-commit checks passed
2. Output: "Commit ready. Push required by human."
3. Provide commit SHA and verification steps
4. Wait for human to push
5. Verify synchronization after human pushes
```

---

## Synchronization Verification (Mandatory After Every Push)

After `git push`, the AI MUST verify:

### Step 1: Local Status Clean
```bash
git status
```
**Expected**: `nothing to commit, working tree clean`

### Step 2: Local HEAD Matches Commit
```bash
git log --oneline -1
```
**Expected**: Shows the commit that was just pushed

### Step 3: Remote HEAD Matches Local
```bash
git fetch origin
git rev-parse HEAD
git rev-parse origin/main
```
**Expected**: Both SHAs identical

### Step 4: No Divergence
```bash
git status
```
**Expected**: `Your branch is up to date with 'origin/main'.`

---

## Failure Behaviors

### Push Failure: Authentication
```
DETECT: "Permission denied", "Authentication failed", "Invalid token"
ACTION:
  1. STOP
  2. Do NOT retry with same credentials
  3. Report: "Push failed: authentication error"
  4. Request Runtime Team to provide valid credentials
  5. Do NOT commit again until credentials resolved
```

### Push Failure: Non-Fast-Forward (Remote Ahead)
```
DETECT: "rejected] main -> main (non-fast-forward)"
ACTION:
  1. STOP
  2. git fetch origin
  3. git rebase origin/main
  4. Run FULL validator suite (VAL-001 through VAL-008)
  5. If all pass → git push origin main
  6. If validators fail → Repair → Re-validate → Push
  7. If rebase conflict → Follow AI Failure Policy (Merge Conflict)
```

### Push Failure: Remote Rejected (Hooks/Policies)
```
DETECT: "remote rejected" with policy message
ACTION:
  1. STOP
  2. Read remote rejection message
  3. If policy violation → Fix violation locally
  4. Re-validate
  5. Retry push
  6. If persistent → Runtime Team
```

### Push Failure: Network/Timeout
```
DETECT: Connection timeout, network unreachable
ACTION:
  1. Wait 30 seconds
  2. Retry once
  3. If fails again → Report: "Push failed: network error"
  4. Request Runtime Team
```

---

## Post-Push Verification Failure Behaviors

### Local Clean but Remote Divergent
```
DETECT: git status shows "Your branch and 'origin/main' have diverged"
ACTION:
  1. STOP
  2. git fetch origin
  3. Compare commits
  4. If local has extra → Force push WITH Runtime Team approval only
  5. If remote has extra → Rebase, validate, push
  6. Never force-push without explicit Runtime Team approval
```

### Sync Verification Timeout
```
DETECT: git fetch hangs or times out
ACTION:
  1. Wait 30 seconds
  2. Retry fetch once
  3. If fails → Report: "Sync verification failed: network"
  4. Request Runtime Team
```

---

## Prohibited Push Behaviors

| Behavior | Prohibition |
| --- | --- |
| Push without preceding commit | ❌ Never |
| Push with validator failures | ❌ Never |
| Push to any branch except main | ❌ Never |
| Push without sync verification | ❌ Never |
| Force push without Runtime Team approval | ❌ Never |
| Claim push success without verification | ❌ Never |
| Retry failed push without diagnosis | ❌ Never |

---

## Push Success Criteria

A push is only considered successful when ALL are true:
- [ ] `git push origin main` exits 0
- [ ] `git status` shows clean
- [ ] `git rev-parse HEAD` == `git rev-parse origin/main`
- [ ] `git status` shows "up to date with origin/main"
- [ ] No remote rejection messages

---

## Quick Push Checklist

```
□ Commit Policy verification passed
□ Tier authorization confirmed
□ git push origin main
□ Exit code 0
□ git status clean
□ Local HEAD == Remote HEAD
□ Branch up to date with origin/main
□ No remote rejections
□ Result returned in chat
```

---

## Related Documents
- [AI Commit Policy](ai-commit-policy.md)
- [AI Failure Policy](ai-failure-policy.md)
- [AI Execution Contract](ai-execution-contract.md)
- [AI Capability Matrix](ai-capability-matrix.md)
- [REPOSITORY-EXECUTION-MODEL.md](../../../REPOSITORY-EXECUTION-MODEL.md)