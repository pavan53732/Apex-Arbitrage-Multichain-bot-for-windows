---
type: REFERENCE
owner: Governance Platform
status: Canonical
version: 1.0.0
purpose: Reports the fixes implemented against the 6-item Governance Correctness Remediation Programme.
scope: Implementation report. Every claim below is backed by a live, reproduced command shown in the accompanying evidence.
last_updated: 2026-07-29
canonical_source: .governance/programme_2.5/REMEDIATION-PROGRAMME-REPORT.md
---

# Governance Correctness Remediation Programme — Report

This report responds to the 6-item remediation programme specified after
review of `.governance/programme_2.5/EVIDENCE-FIRST-VERIFICATION-REPORT.md`.
Each item was implemented, verified with live-executed evidence, and
covered by new regression tests. **A new, previously-undiscovered defect
was found and fixed while verifying Item 1** (see §1).

---

## Item 1 — Identifier normalization

**Root cause (confirmed):** `RepoIndexer` indexes documents by their
actual relative path (`docs/DOCUMENTATION-MAP.md`, or a root-level gate
file with no `docs/` prefix). `ReferenceParser` previously stripped any
`docs/` prefix unconditionally from every extracted reference, with no
corresponding normalization applied to the indexer's own output. A
reference to `docs/DOCUMENTATION-MAP.md` therefore became the bare string
`DOCUMENTATION-MAP.md`, which never matched the indexed key.

**Fix:** new module `tools/governance/references/path_resolver.py`
(`DocumentIdentityResolver`) resolves every extracted reference against
the full canonically-indexed document set, using the same
directory-relative resolution strategy already proven correct by
`architecture-tests/validate_cross_references.py` (0 broken references).
Resolution order: exact match -> relative to the referencing document's
own directory -> explicit `docs/` prefix -> unambiguous basename fallback
(declines to guess when a basename is genuinely ambiguous, e.g. `AGENTS.md`
exists as two distinct real documents). `ReferenceParser` no longer
blindly strips `docs/`; `MetadataParser` now accepts a `known_paths` list
and builds a resolver from it; `cli/main.py`'s 5 call sites and
`reporting/document_inventory.py` were all updated to pass
`known_paths = [item["path"] for item in inventory]`.

**Verified impact (live, reproduced):**
| Metric | Before | After |
|---|---:|---:|
| `validation_findings` | 2,065 | 22 |
| `BROKEN_REFERENCE` findings | 2,054 | 8 |
| Dependency graph nodes | 415 | 234 (no phantom duplicates) |
| Phantom duplicate nodes (bare name shadowing a real `docs/`-prefixed document) | 178 | 0 |

The remaining 8 `BROKEN_REFERENCE` findings are genuine: `SIGNING-POLICY.md`,
`RELEASE-PROCESS.md`, `LOCK-ORDER.md`, `EVENT-SCHEMA-REGISTRY.md` (each
referenced twice) do not exist anywhere in the repository. All four are
now explicitly marked `(future)` in their referencing documents
(`docs/APP-BUILDER-WORKFLOW.md`, `docs/CODE-SIGNING.md`,
`docs/CONCURRENCY-MODEL.md`, `docs/EVENT-CATALOG.md`), completing
Remediation Item 6.

**New defect found while verifying this fix (disclosed, not hidden):**
eliminating the phantom nodes reconnected a genuine 165-document
strongly-connected component in the dependency graph (real, heavy mutual
cross-referencing among interconnected documentation). The existing
`_check_cycles()` implementation used `nx.simple_cycles()`, which
enumerates every individual simple cycle — combinatorially infeasible at
this scale. This caused `apex-gov validate` to hang indefinitely (verified:
did not return within 25 seconds). Fixed by switching to
`nx.strongly_connected_components()` (Tarjan's algorithm, O(V+E)), which
detects cycle *existence* without enumeration. See Item 3 for the
associated severity correction.

**Tests added:** `tools/governance/tests/test_identifier_normalization.py`
(6 tests, including a live end-to-end phantom-node regression check
against the real corpus).

---

## Item 2 — Regenerate graphs/closures, verify phantom-node count is zero

Done as part of Item 1's verification. Live-reproduced: `apex-gov run`'s
`graph_nodes` output field dropped from 415 to 277 (the canonical
document-graph node count now exactly matches the indexed document
count — `document_graph.graphml` adds one node per document
unconditionally, unlike `dependency_graph.graphml` which only contains
nodes participating in at least one edge). The dedicated regression test
`test_live_corpus_has_zero_phantom_graph_nodes` asserts zero phantom
nodes and that the dependency graph never has more nodes than indexed
documents.

---

## Item 3 — Validator exit semantics

**Fix, part A (`apex-gov validate`):** `GovernanceValidator` now defines
`FAILURE_THRESHOLD = Severity.HIGH` and a `has_failing_findings()`
classmethod. `cli/main.py`'s `validate()` command now prints an explicit
`RESULT: PASS` / `RESULT: FAIL (...)` line and calls `raise typer.Exit(code=1)`
when any finding meets or exceeds the threshold. Previously this command
never set a non-zero exit code under any circumstance (confirmed: 2,065
findings including 11 HIGH, exit code 0).

**Fix, part B (severity redesign — a second real defect found and fixed,
not merely wrapped in a threshold):** simply adding an exit-code check on
top of the pre-existing severities would have made `apex-gov validate`
FAIL permanently and incorrectly, because two of the four in-engine rules
were themselves false-positive generators at HIGH/CRITICAL severity:

- `UNIQUE_OWNER` (now renamed `TEAM_OWNERSHIP_CONCENTRATION`, downgraded
  HIGH -> INFO): the `owner:` front-matter field is a TEAM assignment
  (e.g. "AI Team"); many documents legitimately sharing one owning team
  is expected, not a defect. Genuine subsystem-authority conflicts (two
  documents claiming to own the same subsystem) are a different concept,
  already correctly detected by `architecture-tests/validate_ownership.py`
  and `architecture-tests/audit_duplicates.py`, which were not touched.
- `NO_CYCLES` (downgraded CRITICAL -> INFO for all cases, not just large
  ones): verified by direct corpus inspection (`grep -n "## Depends On" docs/*.md`
  returns **zero** matches across all 277 documents) that this
  repository has no document using an explicit "Depends On" section —
  every `depends_on` value is populated from `## Cross-references`
  (`MetadataParser`'s own documented fallback). The "dependency graph" is
  therefore, in its current form, indistinguishable from a documentation
  cross-reference graph, and two documents mutually cross-referencing
  each other is normal practice, not a circular-dependency defect. This
  was verified empirically for all 3 SCCs found (165, 2, and 2 documents)
  before deciding severity — a naive "small cycles are more likely real"
  heuristic was considered and disproven by direct inspection of the two
  small cycles (`ENHANCEMENT-ROADMAP.md`<->`FEATURE-MATRIX.md`,
  `TROUBLESHOOTING.md`<->`USER-GUIDE.md` — both benign
  `## Cross-references`).

**Live-verified result:** `apex-gov validate` now exits 0 (PASS) with 22
findings, none at or above HIGH. Verified stable across 10 runs with
randomized `PYTHONHASHSEED`.

**Fix, part C (`apex-gov integrity`):** `IntegrityEngine.check_validators()`'s
message now explicitly states "all N validator executions completed AND
reported zero findings at or above the failure threshold" rather than the
previous "all N registered validators pass" (which, given `apex-gov validate`'s
prior always-zero exit code, only ever meant "did not crash"). The
underlying PASS/FAIL logic is unchanged (`returncode == 0`), but it is now
backed by a real check rather than a vacuous one, because `apex-gov validate`
itself was fixed.

**Tests added:** `tools/governance/tests/test_validator_exit_semantics.py`
(6 tests) and `tools/governance/tests/test_cycle_detection.py` (updated
severity assertions, 4 tests total, including a performance regression
test with a synthetic 200-node densely-connected graph that reproduces
the exact failure mode and must complete in under 5 seconds).

---

## Item 4 — Real Freeze Framework producer

**Confirmed gap (before fix):** no code anywhere in the repository
produced `.governance/freeze/freeze_WS0.json`. Two candidates were
directly inspected and ruled out: `FreezeManager`
(`tools/governance/freeze/manager.py`) has zero call sites anywhere and
uses an unrelated SQL schema (`freeze_records`/`dimensions`/`closures`
tables) that does not exist in `governance.db`;
`ClosureOrchestrator.freeze_dimension()`/`freeze_closure()`
(`tools/governance/closure/orchestrator.py`) are same-named but unrelated
empty no-op stubs, and `ClosureOrchestrator` itself is never imported
anywhere. Every historical regeneration of `freeze_WS0.json` was
performed via ad hoc, uncommitted interactive Python.

**Fix:** new module `tools/governance/freeze/freeze_engine.py`
(`FreezeEngine`), wired to a new CLI command `apex-gov freeze`. It
composes a freeze record ENTIRELY from live canonical outputs (no
re-derivation of governance state): the canonical `apex-gov run`
output via the Evidence Engine, live Validator Registry results, live
graph/database/config file hashes, and git's own commit/tree hash. Every
field required by the remediation directive is present: version, commit,
repository hash, validator results, evidence hashes, metrics, graphs,
database hash, timestamp, integrity checksum. This is a repository-level
(WS0-granularity) freeze, matching `freeze_WS0.json`'s existing schema —
it deliberately does NOT reimplement `FreezeManager`'s distinct
per-dimension/per-closure freezing model, which is a larger, separate
Programme 3 concept requiring its own schema design, not an incidental
fix to fold into this remediation.

Also fixed as a related, smaller defect: `tools/governance/freeze/`,
`tools/governance/scheduler/`, and `tools/governance/standardiser/` were
missing `__init__.py` (not proper importable packages).

**Tests added:** `tools/governance/tests/test_freeze_engine.py` (4 tests,
including a live check that the produced `commit_hash` matches the actual
current `git rev-parse HEAD`).

---

## Item 5 — Reverse closure

**Confirmed gap (before fix):** `ClosureEngine` had no reverse-closure
method (`hasattr` check confirmed absence).

**Fix:** `ClosureEngine.compute_reverse_closure()` uses `nx.ancestors()`
(everything with a path TO the root, i.e. everything that depends on the
root, directly or transitively) as the correct complement to the existing
`compute_closure()`'s `nx.descendants()` (forward closure — everything
the root depends on). `validate_closure()` now returns both
`closure_docs`/`closure_size` and `reverse_closure_docs`/`reverse_closure_size`.
`apex-gov closure <path>` now prints both. `document_inventory.py` now
includes `reverse_closure_size` per document.
`IntegrityEngine.check_closures()` now additionally verifies, in-process
against the live corpus, that reverse closure is actually computable for
every one of the 28 behavioural roots (not merely that the method exists).

**Tests added:** `tools/governance/tests/test_reverse_closure.py` (6
tests, including a live determinism check against the real corpus).

---

## Item 6 — Resolve genuine broken references, document intentional exceptions

Completed as part of Item 1's verification. All 4 genuinely-missing
referenced documents (`SIGNING-POLICY.md`, `RELEASE-PROCESS.md`,
`LOCK-ORDER.md`, `EVENT-SCHEMA-REGISTRY.md`) are now consistently marked
`(future)` at every reference site, with an explanatory note pointing at
this remediation. `LOCK-ORDER.md` already carried a `(future)` marker
before this remediation; the other three did not and were updated for
consistency. These are intentionally-deferred documents, not resolved by
authoring new stub files (which would be scope creep beyond identifier
normalization — authoring `SIGNING-POLICY.md` etc. is a documentation
task, not a governance-runtime fix).

---

## Full verification summary (all commands re-executed live for this report)

| Check | Result |
|---|---|
| `tools/governance/tests/` | **46/46 passed** (was 21; added 25 new tests across 5 new test files) |
| `architecture-tests/*.py` (5 scripts) | 5/5 exit 0 (unchanged) |
| `apex-gov run` | `documents_indexed: 277, behavioural_roots: 28, validation_findings: 22 (was 2065), closures_computed: 28, graph_nodes: 277, graph_edges: 878` |
| `apex-gov validate` | exit 0, `RESULT: PASS` (previously always exit 0 regardless of findings — now a real signal) |
| `apex-gov integrity` | **13/13 PASS** |
| Determinism (50 runs, randomized `PYTHONHASHSEED`, combined artefact hash of `documents.json` + `governance.db` + all 8 graphs) | **50/50 identical** |
| `apex-gov validate` exit-code determinism (10 runs, randomized seeds) | 10/10 exit code 0 |

## Files changed

**New modules:**
- `tools/governance/references/path_resolver.py` (`DocumentIdentityResolver`)
- `tools/governance/freeze/freeze_engine.py` (`FreezeEngine`)
- `tools/governance/freeze/__init__.py`, `tools/governance/scheduler/__init__.py`, `tools/governance/standardiser/__init__.py` (missing package markers)

**Modified modules:**
- `tools/governance/references/reference_parser.py` — resolver integration, no more blind `docs/` stripping
- `tools/governance/metadata/metadata_parser.py` — accepts `known_paths`, builds resolver
- `tools/governance/cli/main.py` — 5 call sites updated to pass `known_paths`; `validate()` now has real exit semantics; new `freeze` command
- `tools/governance/reporting/document_inventory.py` — `known_paths` fix; added `reverse_closure_size` field
- `tools/governance/validator/governance_validator.py` — `FAILURE_THRESHOLD`/`has_failing_findings()`; `_check_cycles()` rewritten for both performance and severity correctness; `_check_duplicate_owners()` renamed/downgraded
- `tools/governance/closure/closure_engine.py` — `compute_reverse_closure()` added
- `tools/governance/integrity/integrity_engine.py` — `check_validators()` message corrected; `check_closures()` now verifies reverse closure too

**Documentation (intentional-exception markers):**
- `docs/APP-BUILDER-WORKFLOW.md`, `docs/CODE-SIGNING.md`, `docs/EVENT-CATALOG.md` — `(future)` markers added to genuinely-missing referenced documents

**New tests (5 files, 25 tests):**
- `tools/governance/tests/test_identifier_normalization.py`
- `tools/governance/tests/test_cycle_detection.py`
- `tools/governance/tests/test_validator_exit_semantics.py`
- `tools/governance/tests/test_freeze_engine.py`
- `tools/governance/tests/test_reverse_closure.py`

## Remaining known limitations (disclosed, not fixed in this pass)

1. `apex-gov validate`'s `FAILURE_THRESHOLD` is set at HIGH; the 8 genuine
   `BROKEN_REFERENCE` findings are MEDIUM severity and therefore do not
   currently fail validation. This is a deliberate, disclosed design
   choice (documented forward-references are non-blocking), not an
   oversight — but it means a future genuinely-broken reference at MEDIUM
   severity also would not fail CI/validation. If stricter enforcement is
   wanted, `BROKEN_REFERENCE`'s severity or `FAILURE_THRESHOLD` itself
   should be revisited as a separate, explicit decision.
2. `FreezeManager`'s per-dimension/per-closure freezing model
   (Programme 3-oriented) remains unimplemented; only the repository-level
   (WS0-granularity) `FreezeEngine` was built. This was a deliberate
   scoping decision (see Item 4), not an oversight.
3. The 3 `CORE_ROOTS`/`EXCLUDED_PATTERNS` self-contradictions and ~10
   plausibly-missed behavioural roots documented in
   `.governance/programme_2.5/BEHAVIOURAL-ROOT-EXCLUSION-REVIEW.md`
   (from the prior Repository Canonicality Repair) remain unresolved,
   reserved for a deliberate WS1 decision as previously stated.
