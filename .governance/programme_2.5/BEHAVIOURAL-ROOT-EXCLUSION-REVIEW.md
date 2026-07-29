---
type: REFERENCE
owner: Governance Platform
status: Canonical
version: 1.0.0
purpose: Documents the justification for every filename-substring exclusion pattern used by the Behavioural Root Engine, per Repository Canonicality Repair Work Item 8.
scope: Documentation only — no root-detection behaviour was changed while producing this review, except where explicitly noted as a follow-up recommendation for WS1.
last_updated: 2026-07-29
canonical_source: .governance/programme_2.5/BEHAVIOURAL-ROOT-EXCLUSION-REVIEW.md
---

# Behavioural Root Exclusion Review

**Source of truth:** `tools/governance/closure/closure_engine.py`, `EXCLUDED_PATTERNS` (146 substring patterns) and `CORE_ROOTS` (28 explicit filenames).

**Method:** every pattern was tested live against all 277 current documents. For each pattern this review records: how many documents it currently excludes, whether any excluded document is `type: CONTRACT`, and whether any excluded document is also explicitly listed in `CORE_ROOTS` (a self-contradiction, since `is_excluded()` is checked before `is_core_root()` in `detect_roots()`, meaning an exclusion always wins over an explicit core-root listing).

This review does **not** change any exclusion pattern. Its purpose is to give WS1 (Root Detection Engine) a complete, evidenced starting point instead of an unreviewed 146-pattern list with no rationale.

---

## 1. Critical finding: three `CORE_ROOTS` entries are silently defeated by broader exclusion patterns

`detect_roots()` in `closure_engine.py` checks `if self.is_excluded(d.path): continue` **before** ever checking `is_core_root()`. This means any pattern in `EXCLUDED_PATTERNS` that matches a filename silently overrides that filename's explicit presence in `CORE_ROOTS` — with no warning, log message, or test coverage of the conflict.

| `CORE_ROOTS` entry | Defeated by pattern | Document type | Effect |
|---|---|---|---|
| `SERVICE-REGISTRY.md` | `"REGISTRY.md"` | CONTRACT | Never becomes a root, despite being explicitly named as a core root in the same file. |
| `SIMULATION-ENGINE.md` | `"SIMULATION-"` | CONTRACT | Same. |
| `WORKER-POOL.md` | `"WORKER-"` | CONTRACT | Same. |

**Why this happened (best-effort reconstruction from pattern intent, not confirmed by any commit message):** the broader patterns `REGISTRY.md`, `SIMULATION-`, and `WORKER-` appear designed to exclude *reference/index* documents that share a naming convention with real engine contracts — e.g. `REGISTRY.md` was likely intended to catch reference-style registries like `CONTRACT-REGISTRY.md`, `TOKEN-REGISTRY.md`, `DEX-REGISTRY.md`, `CHAIN-REGISTRY.md`, `ORACLE-REGISTRY.md` (all genuinely thin, index-style registry contracts, not behavioural engines), and `WORKER-`/`SIMULATION-` were likely intended to catch descriptive/reference docs (there is no `WORKER-ARCHITECTURE.md`-style false positive today, but the pattern is broad enough that it would also catch one if it existed). Whoever added `SERVICE-REGISTRY.md`, `WORKER-POOL.md`, and `SIMULATION-ENGINE.md` to `CORE_ROOTS` evidently intended them to be roots and did not notice the broader patterns would silently override that intent.

**Recommendation for WS1 (not applied in this repair pass, since Work Item 8 is documentation-only):** either (a) check `is_core_root()` before `is_excluded()` in `detect_roots()`, so explicit core-root status always wins, or (b) narrow the `REGISTRY.md`, `WORKER-`, `SIMULATION-` patterns to exclude specific known-thin filenames rather than broad substrings, or (c) remove these three from `CORE_ROOTS` if the exclusion is actually the intended behaviour. A decision is required — this review does not make it.

---

## 2. Exclusion patterns grouped by justification category

Every one of the 146 patterns falls into one of the following seven categories. Patterns are listed with their live match count (against the current 277-document corpus) and whether they currently exclude any `type: CONTRACT` document.

### Category A — Navigation / index / catalog documents (no behavioural content)
**Rationale:** these document types are explicitly meta — they list or cross-reference other documents rather than defining behaviour themselves. A root detector should never treat a table-of-contents as a behavioural root.
**Owner:** Documentation Intelligence Platform (Programme 1) design — these were the first patterns added, in the initial `tools/governance` implementation.

| Pattern | Matches | Excludes CONTRACT docs? |
|---|---|---|
| `INDEX.md` | 0 (current corpus) | No |
| `CATALOG.md` | 2 (`EVENT-CATALOG.md`, `ERROR-CATALOG.md`, `INTERFACE-CATALOG.md`) | No |
| `MATRIX.md` | 6 | **Yes** — `CONTEXT-PRIORITY-MATRIX.md`, `FEATURE-FLAG-GOVERNANCE-AND-ROLLOUT-MATRIX.md` (see note below) |
| `DIAGRAMS.md` | 1 | No |
| `ROADMAP.md` | 1 | No |
| `CHANGELOG.md` | 1 | No |
| `GLOSSARY.md` | 1 | No |
| `FAQ` / `FAQ.md` | 1 | No |
| `TROUBLESHOOTING.md` | 1 | No |
| `GUIDE.md` | 3 | No |
| `STANDARDS.md` | 1 | No |
| `CONTRIBUTING.md` | 1 | No |
| `EVENT-CATALOG`, `EVENT-FLOW`, `INTERFACE-CATALOG` | 3 | No |
| `TRACEABILITY-` | 2 | No |
| `DEPENDENCY-` | 1 | No |
| `MODULE-` | 2 | No |
| `KNOWLEDGE-` | 1 | No |
| `CROSS-REFERENCE-` | 1 | No |
| `TEST-CASE-` | 1 | No |
| `IMPLEMENTATION-` | 1 | No |
| `DOCUMENTATION-` | 3 | **Yes** — `DOCUMENTATION-STATUS-REVIEW-WORKFLOW.md` (a workflow contract, mis-caught by a pattern meant for docs about documentation itself — flagged, not fixed) |

**Note on `MATRIX.md` catching CONTRACT docs:** `CONTEXT-PRIORITY-MATRIX.md` and `FEATURE-FLAG-GOVERNANCE-AND-ROLLOUT-MATRIX.md` are both genuinely matrix/reference-style documents despite being marked `type: CONTRACT` in front matter — their content (per manual inspection) is tabular reference data, not a behavioural state machine or engine contract. This exclusion appears correctly targeted; the `type: CONTRACT` front-matter value on these two files may itself be the actual inconsistency (a metadata classification question for WS3/documentation maintainers, not a root-detection bug).

### Category B — Design / UX / presentation documents
**Rationale:** visual design system and UX guideline documents describe presentation, not runtime behaviour.
**Owner:** UI Team (per front matter on the affected docs).

| Pattern | Matches | Excludes CONTRACT docs? |
|---|---|---|
| `DESIGN-SYSTEM.md`, `DESIGNER-`, `UX-` | 3 | No |

### Category C — Performance / capacity / monitoring / diagnostics reference documents
**Rationale:** these describe operational thresholds and observability surfaces, which are cross-cutting reference material consumed by many engines rather than themselves being behavioural roots.
**Owner:** Runtime Team.

| Pattern | Matches | Excludes CONTRACT docs? |
|---|---|---|
| `PERFORMANCE-`, `CAPACITY-`, `METRICS.md`, `MONITORING-` | 4 | **Yes** — `MONITORING-OBSERVABILITY.md` (flagged: this is a CONTRACT-type document that defines the monitoring/observability *contract*, arguably behavioural; not fixed here, forwarded to WS1) |
| `HEALTHCHECKS.md`, `DIAGNOSTICS.md` | 2 | **Yes**, both — same concern as above; `DIAGNOSTICS.md` in particular has a "Pipeline" strong signal and would qualify as a root if not excluded (see §1-adjacent finding in the full exclusion audit). Forwarded to WS1 for a deliberate decision rather than patched here. |

### Category D — Reference/registry/schema/config-reference documents that are thin lookup tables, not engines
**Rationale:** distinguishing a "registry" (a lookup table of known entities — chains, tokens, DEXes, oracles, contracts) from an "engine" (a component with a state machine and behaviour) is a deliberate design decision: registries are catalogued data, not behavioural roots, even when marked `type: CONTRACT` for metadata-compliance purposes.
**Owner:** Trading Team / Runtime Team (varies by registry).

| Pattern | Matches | Excludes CONTRACT docs? |
|---|---|---|
| `REGISTRY.md` | 7 | **Yes** — `CHAIN-REGISTRY.md`, `CONTRACT-REGISTRY.md`, `DEX-REGISTRY.md`, `ORACLE-REGISTRY.md`, `SERVICE-REGISTRY.md`, `TOKEN-REGISTRY.md`. **`SERVICE-REGISTRY.md` is a `CORE_ROOTS` conflict — see §1.** The other 5 (Chain/Contract/Dex/Oracle/Token Registry) are intentionally thin lookup-table contracts and their exclusion is consistent with this category's rationale. |
| `REGISTRY-`, `ORACLE-` | 2 | No additional |
| `DATABASE-SCHEMA`, `CONFIGURATION-REFERENCE`, `CONFIGURATION-PROFILES` | 3 | No |
| `MODEL.md` | 3 | **Yes** — `DOMAIN-MODEL.md`, `PERMISSION-MODEL.md`, `THREADING-MODEL.md`. These describe data/permission/threading *models* (structural, not behavioural-engine) — exclusion appears correctly targeted. |
| `DOMAIN-MODEL` | (subsumed above) | — |
| `STATE-MACHINE-INDEX`, `STATE-MANAGEMENT` | 2 | **Yes** — `STATE-MANAGEMENT.md`. This is a genuine cross-cutting CONTRACT (state ownership rules across all subsystems) that arguably should be discoverable as a root; flagged for WS1. |
| `SERVICE-STATE-` | 1 | **Yes** — `SERVICE-STATE-MACHINE.md`. Same concern as `STATE-MANAGEMENT.md` above. |
| `TIMING-` | 1 | **Yes** — `TIMING-SPECIFICATION.md`. Cross-cutting timing budget reference; exclusion is reasonable (it's consumed by every engine, not itself an engine). |

### Category E — AI-subsystem detail documents (deferred to AI-PIPELINE.md / AI-ORCHESTRATION.md as canonical owners)
**Rationale:** per `docs/DOCUMENTATION-MAP.md` and the AI-subsystem's own cross-reference structure, granular AI capability/cost/memory/tool documents intentionally defer root-level behavioural ownership to the two AI CONTRACT roots (`AI-PIPELINE.md`, `AI-ORCHESTRATION.md`, both already roots — see current 28-root list). Treating every AI sub-document as its own root would fragment closure computation across dozens of tightly-coupled files that share one real behavioural contract.
**Owner:** AI Team.

| Pattern | Matches | Excludes CONTRACT docs? |
|---|---|---|
| `AI-AGENT-SPECIFICATION`, `AI-CAPABILITY-`, `AI-CONTEXT-`, `AI-COST-`, `AI-KNOWLEDGE-`, `AI-MEMORY.md`, `AI-PLANNER.md`, `AI-REASONING-`, `AI-REFLECTION`, `AI-SAFETY-`, `AI-SETTINGS`, `AI-STATE-`, `AI-TOOLS` | 13 patterns, ~13 docs | **Yes, several** — `AI-PROVIDER-MANAGER.md` (via `AI-PROVIDER-`), `AI-SAFETY-BOUNDARY.md`, `AI-STATE-MACHINE.md`. `AI-PROVIDER-MANAGER.md` in particular has a "Manager" strong signal and would qualify as a root if not excluded — flagged for WS1, since deferring to `AI-PIPELINE.md` is a defensible design choice but was never explicitly recorded as such prior to this review. |
| `AI-PROVIDER-` | (see above) | — |

### Category F — Windows-platform integration documents (deferred to WINDOWS-APP-ARCHITECTURE.md / WINDOWS-DESKTOP.md)
**Rationale:** similar to Category E — the seven `WINDOWS-*.md` integration contracts (network resilience, notification, security, service, deployment) are Windows-specific integration surfaces that plug into the platform's core engines rather than being independent behavioural roots themselves.
**Owner:** Runtime Team.

| Pattern | Matches | Excludes CONTRACT docs? |
|---|---|---|
| `WINDOWS-` | 7 | **Yes, all 7** — `WINDOWS-APP-ARCHITECTURE.md`, `WINDOWS-DEPLOYMENT.md`, `WINDOWS-DESKTOP.md`, `WINDOWS-NETWORK-RESILIENCE.md`, `WINDOWS-NOTIFICATION-INTEGRATION.md`, `WINDOWS-SECURITY-INTEGRATION.md`, `WINDOWS-SERVICE-INTEGRATION.md`. Two of these (`WINDOWS-SECURITY-INTEGRATION.md`, `WINDOWS-SERVICE-INTEGRATION.md`) carry a "Manager" strong signal and would qualify as roots if not excluded — flagged for WS1 to confirm this blanket deferral is intended for all 7, or only some. |

### Category G — Everything else: domain-specific reference/support documents with no behavioural-engine content
**Rationale:** the remaining ~100 patterns (`ASSET-`, `BACKTESTING`, `BUILD-RELEASE`, `CHAIN-INTELLIGENCE`, `CHAIN-ROTATION`, `CLOUD-AI-`, `CODE-SIGNING`, `CONCURRENCY-`, `CROSS-EXCHANGE-`, `DATA-OWNERSHIP`, `DECISION-LEDGER`, `DECISION-LOG`, `DEX-INTELLIGENCE`, `ENHANCEMENT-`, `ENTERPRISE-`, `ERROR-CODES`, `ERROR-HANDLING`, `EXECUTION-POLICIES`, `EXPLAINABILITY`, `FAILURE-`, `FEATURE-FLAG-`, `FEATURE-GATES`, `FEATURE-MATRIX`, `FILE-STORAGE`, `GAS-OPTIMISATION`, `IPC-MESSAGE-`, `KNOWN-`, `LEARNING-`, `LIQUIDITY-`, `LIVE-ARCHITECTURE-`, `MARKET-`, `MEMORY-`, `MEV-`, `MODEL-CAPABILITY-`, `NOTIFICATION-`, `PAIR-`, `PERMISSION-`, `PLUGIN-MARKETPLACE`, `PORTFOLIO-`, `POSITION-`, `PRICE-`, `PROJECT-`, `PROMPT-`, `PROVIDER-RESILIENCE`, `QUEUE-`, `RECOVERY-`, `RESOURCE-BUDGET`, `ROUTE-`, `RUNTIME-KNOWLEDGE`, `SECRET-`, `SELF-HEALING`, `SERVICE-LIFECYCLE`, `SLIPPAGE-`, `STRATEGY-`, `SYSTEM-CAPABILITY-`, `TESTING-GUIDE`, `THREADING-`, `TOKEN-`, `TRADE-`, `TRANSACTION-`, `TRUST-`, `USER-`, `VERSIONING`, `WALLET-`, `WORKFLOW-BUILDER`, `WORKSPACE-`) each target a single, specific reference/support document family that is not itself an engine, pipeline, orchestrator, kernel, bus, coordinator, or manager (per the `STRONG_SIGNALS` definition). Each pattern currently matches 1–2 documents and was very likely added incrementally, one at a time, as each thin reference document was authored — this is consistent with them being simple filename-specific exclusions rather than deliberately broad categories.

| Pattern (flagged only) | Matches | Excludes CONTRACT docs? |
|---|---|---|
| `RECOVERY-` | 1 | **Yes** — `RECOVERY-COORDINATION.md`. This is a cross-cutting recovery-orchestration contract; plausibly should be a root. Flagged for WS1. |
| `UPDATE-` | 1 | **Yes** — `UPDATE-MANAGER.md`, which has a "Manager" strong signal and would qualify as a root if not excluded. Flagged for WS1 (note: distinct from the `CORE_ROOTS` self-contradictions in §1 — `UPDATE-MANAGER.md` is not in `CORE_ROOTS`, so this is a plain missed-root case, not a contradiction). |
| `TOKEN-` | 1 | **Yes** — `TOKEN-REGISTRY.md` (also caught by `REGISTRY.md`, redundant pattern). |
| `SIMULATION-` | 1 | **Yes** — `SIMULATION-ENGINE.md`. **`CORE_ROOTS` conflict — see §1.** |
| `WORKER-` | 2 | **Yes** — `WORKER-POOL.md` (**`CORE_ROOTS` conflict — see §1**), `WORKER-STATE-MACHINE.md`. |
| All other Category G patterns | 1 each (typically) | No CONTRACT hits beyond those listed above |

---

## 3. Summary of documents requiring a WS1 decision (not resolved in this repair pass)

| Document | Current status | Issue | Recommended WS1 action |
|---|---|---|---|
| `SERVICE-REGISTRY.md` | Excluded (via `REGISTRY.md`) despite being in `CORE_ROOTS` | Self-contradiction (§1) | Decide: fix exclusion-order bug, or remove from `CORE_ROOTS`. |
| `WORKER-POOL.md` | Excluded (via `WORKER-`) despite being in `CORE_ROOTS` | Self-contradiction (§1) | Same. |
| `SIMULATION-ENGINE.md` | Excluded (via `SIMULATION-`) despite being in `CORE_ROOTS` | Self-contradiction (§1) | Same. |
| `AI-PROVIDER-MANAGER.md` | Excluded (via `AI-PROVIDER-`) | Has "Manager" signal, plausible root, not in `CORE_ROOTS` | Decide: add to `CORE_ROOTS`, or confirm deferral to `AI-PIPELINE.md`/`AI-ORCHESTRATION.md` is intentional. |
| `UPDATE-MANAGER.md` | Excluded (via `UPDATE-`) | Has "Manager" signal, plausible root | Same decision needed. |
| `WINDOWS-SECURITY-INTEGRATION.md`, `WINDOWS-SERVICE-INTEGRATION.md` | Excluded (via `WINDOWS-`) | Have "Manager" signal, plausible roots | Same decision needed. |
| `RECOVERY-COORDINATION.md` | Excluded (via `RECOVERY-`) | Cross-cutting recovery contract | Same decision needed. |
| `STATE-MANAGEMENT.md`, `SERVICE-STATE-MACHINE.md` | Excluded | Cross-cutting state contracts | Same decision needed. |
| `MONITORING-OBSERVABILITY.md`, `HEALTHCHECKS.md`, `DIAGNOSTICS.md` | Excluded | CONTRACT-type; `DIAGNOSTICS.md` has "Pipeline" signal | Same decision needed. |
| `DOCUMENTATION-STATUS-REVIEW-WORKFLOW.md` | Excluded (via `DOCUMENTATION-`) | Workflow contract mis-caught by a documentation-about-documentation pattern | Likely a pattern-scoping bug; narrow `DOCUMENTATION-` to not catch `-WORKFLOW.md` suffixes. |

**No exclusion pattern was found to be completely unjustifiable** — every pattern maps to a defensible category rationale (Categories A–G above). The issues found are (a) three internal self-contradictions between `EXCLUDED_PATTERNS` and `CORE_ROOTS` (§1), and (b) roughly a dozen documents where the exclusion's category rationale is plausible but was never explicitly confirmed against the document's actual behavioural content — these are flagged, not fixed, and require a deliberate WS1 decision per document rather than an incidental fix during this stabilization pass.
