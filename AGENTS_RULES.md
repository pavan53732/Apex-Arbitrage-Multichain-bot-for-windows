# Agent Rules

## Repository Rules

| Rule | Description |
|------|-------------|
| **Output Format** | All reports, analysis, and summaries must be presented in table format. No plain text narratives for structured data. |
| **No CI/CD Workflows** | The repository must not contain any GitHub Actions workflows, CI/CD pipelines, or automation workflows. No `.github/workflows/` directory or `*.yml`/`.yaml` pipeline files. |
| **Branch Strategy** | Work is done on session branches. Merge to `main` via explicit merge commits with detailed messages. |
| **Governance Platform** | The Apex Governance Platform (`tools/governance/`) is the single canonical runtime. All governance computation originates here. WS0 is a verification layer only. |

## Execution Model

| Rule | Description |
|------|-------------|
| **Repository Execution Model** | All validation, documentation generation, repository analysis, and quality checks are executed locally by contributors or AI agents. |
| **No CI/CD** | No GitHub Actions, Azure Pipelines, GitLab CI, CircleCI, Jenkins pipelines, Buildkite, Travis CI, or similar automation. |
| **No Repository Automation** | Do not introduce automated workflow engines that execute repository tasks remotely. |
| **Local First** | Validators, documentation tools, and helper utilities execute locally. |

See `REPOSITORY-EXECUTION-MODEL.md` for the canonical policy.

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
