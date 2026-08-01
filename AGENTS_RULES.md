---
metadata_schema_version: 1.0
governance_version: 2.0.0
document_id: DOC-0002
title: Repository Operating Rules
plane: Repository Operating Model
domain: Agent System
class: Policy
authority: Canonical
status: Active
owner: Runtime Team
version: 1.1.0
canonical_source: AGENTS_RULES.md
related_concepts:
  - CONCEPT-0002
dependencies: []
consumers:
  - DOC-0044
validator_coverage: []
supersedes:
  - DOC-0044
superseded_by: []
last_updated: 2026-08-01
concept_role: Owner
owned_domains:
  - Agent System
---

# Agent Rules

## Repository Rules

| Rule | Description |
|------|-------------|
| **Output Format** | All reports, analysis, and summaries must be presented in table format. No plain text narratives for structured data. |
| **No CI/CD Workflows** | The repository must not contain any GitHub Actions workflows, CI/CD pipelines, or automation workflows. No `.github/workflows/` directory or `*.yml`/`.yaml` pipeline files. |
| **Branch Strategy** | Work directly on `main`. Commit after successful validation. Push immediately after commit. Verify remote synchronization. No unfinished local commits. No abandoned branches unless explicitly requested. |
| **Governance Platform** | Repository governance is defined by the canonical root governance documents (README.md, AGENTS.md, AGENTS_RULES.md, REPOSITORY-EXECUTION-MODEL.md, REBUILD-SYSTEM-SPECIFICATION.md) and enforced by the local validator suite (`validators/`). All governance computation is local-first and originates from these documents. |
| **Two Documentation Roots** | `docs/` shall contain exactly two permanent documentation roots: `docs/apex-repository-docs/` and `docs/apex-app-docs/`. No third permanent documentation root may be created without an explicit governance revision. |

## Execution Model

| Rule | Description |
|------|-------------|
| **Repository Execution Model** | All validation, documentation generation, repository analysis, and quality checks are executed locally by contributors or AI agents. |
| **No CI/CD** | No GitHub Actions, Azure Pipelines, GitLab CI, CircleCI, Jenkins pipelines, Buildkite, Travis CI, or similar automation. |
| **No Repository Automation** | Do not introduce automated workflow engines that execute repository tasks remotely. |
| **Local First** | Validators, documentation tools, and helper utilities execute locally. |

See `./REPOSITORY-EXECUTION-MODEL.md` for the canonical policy.

## AI Output Rules

| Rule | Description |
|------|-------------|
| **Chat-First Output** | Reviews, audits, reports, plans, summaries, findings, and analysis must be returned directly in the conversation unless the user explicitly requests a repository document. |
| **No Temporary Markdown** | Do not create temporary .md files for execution output. |
| **No Temporary JSON** | Do not create temporary JSON reports. |
| **No Temporary HTML** | Do not create HTML reports. |
| **No Temporary PDFs** | Do not create PDF reports. |
| **No Temporary CSV** | Do not create CSV reports. |
| **No Workspace Artifacts** | Do not generate temporary execution artifacts anywhere in the workspace. |
| **Repository Contains Durable Knowledge Only** | The repository stores long-lived engineering knowledge only. |

## Git Rules

| Rule | Description |
|------|-------------|
| **Work on Main** | Work directly on `main` unless explicitly instructed otherwise. |
| **Commit After Validation** | Commit only after validators pass and quality checks complete. |
| **Push Immediately** | Push to `main` immediately after commit. |
| **Verify Synchronization** | Confirm remote is synchronized before declaring completion. |
| **No Unfinished Commits** | No unfinished local commits. |
| **No Abandoned Branches** | No abandoned branches unless explicitly requested. |
| **Detailed Messages** | Use detailed commit messages explaining what changed and why. |



See `./REPOSITORY-EXECUTION-MODEL.md` for the canonical policy.


## Development Rules

| Rule | Description |
|------|-------------|
| **Determinism** | All governance operations must be deterministic and reproducible on fresh clones. |
| **Evidence-Based** | Every claim must be backed by repository evidence (files, commits, command output). |
| **No Fabrication** | Never assume, infer, or fabricate state. Verify directly from repository contents. |
| **Read-Only Investigation** | Initial audits/reconstructions are read-only. No modifications until explicitly approved. |

## Implementation Rules

| Rule | Description |
|------|-------------|
| **Specification Drift** | If implementation diverges from frozen Phase-0 spec, propose ADR (Option B) rather than silently certifying against outdated spec. |
| **Fresh-Clone Verification** | Certification requires independent `git clone` + clean environment re-verification. |
| **Zero Phantom Data** | Dependency graphs must have zero phantom nodes. Path normalization must be consistent. |
| **Validator Exit Codes** | `apex-gov validate` must return non-zero exit code when findings exceed threshold. |

## Quality Gates

| Gate | Requirement |
|------|-------------|
| **Integrity** | `apex-gov integrity` → 14/14 PASS |
| **Tests** | Governance test suite → 238/238 PASS |
| **Architecture** | All 5 architecture test scripts → PASS |
| **Certification** | Programme 2.5 certified before Programme 3 begins |

---

*Last updated: 2026-07-31*
*Source: Session agreements between user and agent*
