---
type: REFERENCE
owner: Governance Platform
status: Archived
version: 1.0.0
purpose: Records why these artefacts were archived during Repository Canonicality Repair (Work Item 2 and Work Item 3).
scope: Historical record only. Nothing in this directory is consumed by any live code path.
last_updated: 2026-07-29
canonical_source: .governance/archive/pre-consolidation-2026-07-29/ARCHIVE-MANIFEST.md
---

# Archive: Pre-Consolidation Stray Governance Artefacts

This directory preserves (rather than silently deletes) governance artefacts
identified as duplicates/orphans by the Repository Canonicality Audit
(`.governance/programme_2.5/REPOSITORY-CANONICALITY-AUDIT.md`, §4 and §5a)
and removed from their original locations as part of Repository
Canonicality Repair, Work Items 2 (Database Consolidation) and 3 (Graph
Consolidation).

**Nothing in this archive is read by any live code path.** `git grep` for
each archived path from `HEAD` before this change confirmed zero
references outside of the files themselves.

## 1. `programme3.db`

- **Original path:** `.governance/db/programme3.db`
- **Creator:** commit `a8c178920` ("Pre-Programme 3 cleanup: Remove GitHub
  Actions CI/CD") — added as an unrelated binary blob in a commit whose
  message does not mention it at all.
- **Schema:** 11 tables (`closures`, `dimensions`, `documents`, `sections`,
  `tasks`, `findings`, `validators`, `freeze_records`,
  `regression_history`, `metrics`, `evidence`) — a schema design that does
  not match the current canonical `SqliteStore` (`documents` table only,
  see `tools/governance/storage/sqlite_store.py`).
- **Owner:** none — no ADR, manifest, or config entry claims ownership.
- **Consumer:** none — `git log --all -p -- '*.py' | grep "programme3.db"`
  returns zero hits across the entire repository history. No script,
  CLI command, or test ever opened this file.
- **Producer:** unknown — the schema does not correspond to any producer
  code present in the repository today, at any point in its history.
- **Current usage at time of archival:** none. Confirmed orphaned.
- **Disposition:** archived, not deleted, in case a future Programme 3
  effort intended to build against this schema and the code was simply
  never committed. If WS5 (Database Consolidation) or a future Programme 3
  restart confirms this schema is unwanted, it can be deleted outright.

## 2. `tools-governance-stray-artifacts/` (formerly `tools/governance/.governance/`)

Contains: `governance.db`, `GOVERNANCE-PROGRESS.json`,
`exports/documents.json`, and 8 `graphs/*.graphml` files.

- **Creator:** commit `cd84312cc` ("governance(platform): fix CLI import,
  config globs, add GOVERNANCE-PROGRESS.json, Programme 1 execution
  output"). The commit's own diff shows it added **both** the correct
  `.governance/GOVERNANCE-PROGRESS.json` at the repo root **and** a
  duplicate `tools/governance/.governance/GOVERNANCE-PROGRESS.json` +
  `governance.db` + `exports/documents.json` in the same commit.
- **Root cause:** at the time, `tools/governance/cli/main.py`'s `run()`
  command resolved `repo_root` from `governance.yaml`'s `repo_root: "."`
  relative to the *current working directory* of the process invoking it.
  When the CLI was invoked with `cwd=tools/governance/` (as it would be if
  run directly rather than via the installed `apex-gov` console script
  from the repository root), every output path resolved one level too
  deep, writing a full second copy of the database, progress file,
  document export, and all 8 graphs under `tools/governance/.governance/`
  instead of the intended `.governance/`.
- **Schema/content:** identical `documents` table schema to the canonical
  `.governance/governance.db`, but with stale, tiny content (12,288 bytes
  vs. 106,496 bytes canonical; `document_graph.graphml` had 1 node vs. 277
  canonical; all other graphs had 0 nodes/0 edges) — confirming it was
  captured once, early, and never updated again.
- **Owner:** none.
- **Consumer:** none. `governance.yaml`'s `storage.db_path` has always
  pointed at `.governance/governance.db` (the canonical path) — this stray
  copy was never the one actually read by any command.
- **Producer:** the same `apex-gov run` / `tools.governance.cli.main:run`
  code that produces the canonical artefacts, but invoked once from the
  wrong working directory.
- **Current usage at time of archival:** none.
- **Fix applied (see repository canonicality repair commit):**
  `tools/governance/cli/main.py`'s `run()` command already contained
  defensive fallback logic (added in an earlier session) that searches
  parent directories of the config file for one containing a `docs/`
  folder, specifically to prevent `repo_root` from resolving incorrectly
  again. This was verified in this repair pass by running `apex-gov run`
  from three different working directories
  (`/home/user/Apex-Arbitrage-Multichain-bot-for-windows`, and two
  unrelated temp directories) and confirming identical output in all
  three — see the Repository Canonicality Repair log.
- **Disposition:** archived, not deleted, since it demonstrates the exact
  failure mode the fallback logic now guards against; useful as a
  regression fixture if WS0/WS1 ever want a "wrong working directory"
  test case.

## Configuration verification after archival

`tools/governance/config/governance.yaml` was checked after this
archival — its `storage.db_path`, `storage.export_dir`, and
`storage.graphs_dir` keys were **already** pointing only at
`.governance/governance.db`, `.governance/exports`, and `.governance/graphs`
respectively, before this archival. No configuration change was required;
only the stray duplicate *data* files needed to be removed from their
incorrect location.

## 3. Competing document/root inventories (`.governance/exports/`)

Archived: `complete_repository_inventory.json`, `file_inventory.json`,
`programme3_execution_plan.json`, `behavioural_root_registry.json`.

- **Creators:** `7d73d4071` (Phase 0.5), `c2ab4b89e` and `f584abb26`
  (Programme 3, pre-2.5) — three separate one-off exports from tooling
  that no longer exists in the repository.
- **Producer code:** none. `grep -rln "file_inventory|complete_repository_inventory|
  behavioural_root_registry|programme3_execution_plan" --include="*.py" .`
  returns zero hits. Nothing in `tools/governance/` or anywhere else can
  regenerate these files.
- **Consumer:** none found (only self-references between the files, and
  the audit report that documents them).
- **Why this matters (Repository Canonicality Audit §1/§2):** these files
  contained document/root counts (360 documents, 22 roots, 34 roots) that
  disagreed with the canonical runtime's live output (277 documents, 28
  roots) and were the direct source of the "inconsistent counts across
  reports" finding. `.governance/freeze/freeze_WS0.json` had also copied
  the stale 360/22 figures from `complete_repository_inventory.json` and
  `behavioural_root_registry.json` respectively — see Work Item 4 (Freeze
  Framework) for the fix to that freeze record.
- **Disposition:** archived rather than deleted, since
  `behavioural_root_registry.json` in particular records a genuinely
  different (34-root, Tier A/B) root-classification scheme that may be
  worth revisiting during WS1 (Root Detection Engine) rather than being
  lost outright.
- **Result:** `.governance/exports/` now contains exactly one file —
  `documents.json` — which is the only export actually produced by the
  canonical runtime (`tools/governance/storage/json_export.py`,
  `export_documents_json()`, invoked from `apex-gov run`). This resolves
  the "no competing inventories" requirement (Work Item 9) for the
  `.governance/exports/` directory specifically. `GOVERNANCE-PROGRESS.json`
  at the repository root remains as the canonical progress tracker
  (produced by `tools/governance/progress/progress_tracker.py`) and was
  not touched.

