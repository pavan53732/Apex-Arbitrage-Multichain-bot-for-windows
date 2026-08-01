---
metadata_schema_version: 1.0
document_id: DOC-0070
title: AI Capability Matrix
plane: Repository Operating Model
domain: Agent System
class: Policy
authority: Canonical
status: Active
owner: Runtime Team
version: 1.0.0
canonical_source: docs/apex-repository-docs/agent-system/ai-capability-matrix.md
related_concepts:
  - CONCEPT-0001
  - CONCEPT-0070
dependencies:
  - DOC-0001
  - DOC-0016
  - DOC-0065
consumers: []
validator_coverage: []
supersedes: []
superseded_by: []
last_updated: 2026-07-31
concept_role: Owner
owned_domains:
  - Agent System
type: STANDARD
purpose: Defines explicit capabilities and prohibitions for every supported AI agent operating on this repository.
scope: All repository-facing AI agents (Kilo Code, Cursor, Claude Code, GitHub Copilot, etc.)
---

# AI Capability Matrix

## Purpose

This matrix defines exactly what each AI agent may and may not do when operating on this repository. It eliminates ambiguity and prevents agents from taking actions outside their authorized scope.

## Universal Prohibitions (Apply to ALL Agents)

| Prohibited Action | Rationale |
| --- | --- |
| Create duplicate canonical documents | Violates canonical edit-first rule (AGENTS.md) |
| Invent Concept IDs (CONCEPT-XXXX) | Only Runtime Team allocates |
| Invent Document IDs (DOC-XXXX) | Only Runtime Team allocates |
| Create temporary report files (AUDIT.md, REVIEW.md, SUMMARY.md, etc.) | Temporary Execution Output Policy (AGENTS.md) |
| Create CI/CD pipelines or GitHub Actions | Repository excludes remote automation (REPOSITORY-EXECUTION-MODEL.md) |
| Ignore validator failures | All validators must pass before commit |
| Bypass registry updates | Registry changes required in same commit |
| Commit with broken cross-references | VAL-001 must pass |
| Create files in repository root without approval | Root-level discipline (AGENTS.md) |

## Per-Agent Capabilities

### Kilo Code

| Category | Allowed | Prohibited |
| --- | --- | --- |
| **Read** | Full repository read access | — |
| **Modify Canonical Docs** | Yes (with canonical edit-first rule) | Modify without checking existing canonical |
| **Update Registries** | Yes (in same commit as doc changes) | Update in isolation |
| **Rename Documents** | Yes (with registry + cross-ref updates) | Rename without updating all references |
| **Move Documents** | Yes (with registry + README updates) | Move without updating navigation |
| **Validate** | Yes (run all validators) | Skip validators |
| **Commit** | Yes (after full validation pass) | Commit with failures |
| **Push to Main** | Yes (after commit + verify sync) | Push without verification |
| **Create New Documents** | Yes (only permanent knowledge, with Concept ID) | Create temporary/generated docs |
| **Delete Documents** | No (only supersede via lifecycle) | Delete directly |
| **Modify REBUILD-SYSTEM-SPECIFICATION.md** | No (high-caution, requires human) | — |
| **Modify AGENTS.md** | No (high-caution, requires human) | — |

### Cursor

| Category | Allowed | Prohibited |
| --- | --- | --- |
| **Read** | Full repository read access | — |
| **Modify Canonical Docs** | Yes (with canonical edit-first rule) | Modify without checking existing canonical |
| **Update Registries** | Yes (in same commit as doc changes) | Update in isolation |
| **Rename Documents** | Yes (with registry + cross-ref updates) | Rename without updating all references |
| **Move Documents** | Yes (with registry + README updates) | Move without updating navigation |
| **Validate** | Yes (run all validators) | Skip validators |
| **Commit** | Yes (after full validation pass) | Commit with failures |
| **Push to Main** | Yes (after commit + verify sync) | Push without verification |
| **Create New Documents** | Yes (only permanent knowledge, with Concept ID) | Create temporary/generated docs |
| **Delete Documents** | No (only supersede via lifecycle) | Delete directly |
| **Modify REBUILD-SYSTEM-SPECIFICATION.md** | No (high-caution, requires human) | — |
| **Modify AGENTS.md** | No (high-caution, requires human) | — |

### Claude Code

| Category | Allowed | Prohibited |
| --- | --- | --- |
| **Read** | Full repository read access | — |
| **Modify Canonical Docs** | Yes (with canonical edit-first rule) | Modify without checking existing canonical |
| **Update Registries** | Yes (in same commit as doc changes) | Update in isolation |
| **Rename Documents** | Yes (with registry + cross-ref updates) | Rename without updating all references |
| **Move Documents** | Yes (with registry + README updates) | Move without updating navigation |
| **Validate** | Yes (run all validators) | Skip validators |
| **Commit** | Yes (after full validation pass) | Commit with failures |
| **Push to Main** | Yes (after commit + verify sync) | Push without verification |
| **Create New Documents** | Yes (only permanent knowledge, with Concept ID) | Create temporary/generated docs |
| **Delete Documents** | No (only supersede via lifecycle) | Delete directly |
| **Modify REBUILD-SYSTEM-SPECIFICATION.md** | No (high-caution, requires human) | — |
| **Modify AGENTS.md** | No (high-caution, requires human) | — |

### GitHub Copilot / Copilot CLI

| Category | Allowed | Prohibited |
| --- | --- | --- |
| **Read** | Full repository read access | — |
| **Modify Canonical Docs** | Yes (with canonical edit-first rule) | Modify without checking existing canonical |
| **Update Registries** | Yes (in same commit as doc changes) | Update in isolation |
| **Rename Documents** | Yes (with registry + cross-ref updates) | Rename without updating all references |
| **Move Documents** | Yes (with registry + README updates) | Move without updating navigation |
| **Validate** | Yes (run all validators) | Skip validators |
| **Commit** | Yes (after full validation pass) | Commit with failures |
| **Push to Main** | No (Copilot cannot push) | Push directly |
| **Create New Documents** | Yes (only permanent knowledge, with Concept ID) | Create temporary/generated docs |
| **Delete Documents** | No (only supersede via lifecycle) | Delete directly |
| **Modify REBUILD-SYSTEM-SPECIFICATION.md** | No (high-caution, requires human) | — |
| **Modify AGENTS.md** | No (high-caution, requires human) | — |

### Gemini CLI / Google Code Assistant

| Category | Allowed | Prohibited |
| --- | --- | --- |
| **Read** | Full repository read access | — |
| **Modify Canonical Docs** | Yes (with canonical edit-first rule) | Modify without checking existing canonical |
| **Update Registries** | Yes (in same commit as doc changes) | Update in isolation |
| **Rename Documents** | Yes (with registry + cross-ref updates) | Rename without updating all references |
| **Move Documents** | Yes (with registry + README updates) | Move without updating navigation |
| **Validate** | Yes (run all validators) | Skip validators |
| **Commit** | Yes (after full validation pass) | Commit with failures |
| **Push to Main** | Yes (after commit + verify sync) | Push without verification |
| **Create New Documents** | Yes (only permanent knowledge, with Concept ID) | Create temporary/generated docs |
| **Delete Documents** | No (only supersede via lifecycle) | Delete directly |
| **Modify REBUILD-SYSTEM-SPECIFICATION.md** | No (high-caution, requires human) | — |
| **Modify AGENTS.md** | No (high-caution, requires human) | — |

### Other Agents (OpenCode, Qodo, Windsurf, Zed, etc.)

| Category | Allowed | Prohibited |
| --- | --- | --- |
| **Read** | Full repository read access | — |
| **Modify Canonical Docs** | Yes (with canonical edit-first rule) | Modify without checking existing canonical |
| **Update Registries** | Yes (in same commit as doc changes) | Update in isolation |
| **Rename Documents** | Yes (with registry + cross-ref updates) | Rename without updating all references |
| **Move Documents** | Yes (with registry + README updates) | Move without updating navigation |
| **Validate** | Yes (run all validators) | Skip validators |
| **Commit** | Yes (after full validation pass) | Commit with failures |
| **Push to Main** | If agent supports push (after verify) | Push without verification |
| **Create New Documents** | Yes (only permanent knowledge, with Concept ID) | Create temporary/generated docs |
| **Delete Documents** | No (only supersede via lifecycle) | Delete directly |
| **Modify REBUILD-SYSTEM-SPECIFICATION.md** | No (high-caution, requires human) | — |
| **Modify AGENTS.md** | No (high-caution, requires human) | — |

## Capability Tiers

| Tier | Agents | Push to Main |
| --- | --- | --- |
| **Tier 1 (Full)** | Kilo Code, Cursor, Claude Code, Gemini CLI | Yes |
| **Tier 2 (No Push)** | GitHub Copilot, Copilot CLI | No (human pushes) |
| **Tier 3 (Restricted)** | Future agents not yet evaluated | Requires explicit approval |

## Adding New Agents

To add a new AI agent to this matrix:
1. Evaluate against all capabilities in this matrix
2. Assign to appropriate tier
3. Update this document (requires Runtime Team approval)
4. Add agent profile in `docs/apex-repository-docs/agent-system/agent-profiles/`
5. Update Agent Index

## Compliance

- VAL-007 checks that agents don't perform prohibited actions
- VAL-006 catches temporary files created by agents
- Registry Governance Standard enforces update rules

## Related Documents
- [AI Decision Tree](ai-decision-tree.md)
- [AI Execution Contract](ai-execution-contract.md)
- [AI Failure Policy](ai-failure-policy.md)
- [AI Change Classification Matrix](ai-change-classification-matrix.md)
- [AI Commit Policy](ai-commit-policy.md)
- [AI Push Policy](ai-push-policy.md)
- [AI Workspace Policy](ai-workspace-policy.md)
- [AGENTS.md](../../../AGENTS.md)
- [REPOSITORY-EXECUTION-MODEL.md](../../../REPOSITORY-EXECUTION-MODEL.md)