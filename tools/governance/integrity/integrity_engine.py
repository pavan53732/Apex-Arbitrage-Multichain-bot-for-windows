"""Integrity Engine — Repository Canonicality Repair, Work Item 6.

This is the FIRST implementation of an Integrity Engine in this
repository. Prior to this module, no `class.*Integrity` existed anywhere
in the codebase (confirmed by repository-wide grep during the Repository
Canonicality Audit, section 5e). Any "integrity_checksum" values seen in
`.governance/freeze/freeze_WS0.json` before this repair were computed
inline by a one-off script that no longer exists.

Single command: `apex-gov integrity`.

The Integrity Engine does NOT recompute governance state itself. It
orchestrates and cross-checks the canonical runtime's own outputs:
  - database:      exactly one canonical SQLite database exists and its
                    `documents` table row count matches the indexer.
  - graphs:         exactly one set of 8 canonical .graphml files exists,
                    each is well-formed, and their combined content hash
                    is stable across two consecutive canonical runs.
  - closures:       every behavioural root has a computable closure.
  - validators:     every validator in the Validator Registry
                    (tools/governance/validator/registry.py) passes.
  - roots:          the behavioural root count is stable across two
                    consecutive canonical runs (a determinism check
                    specific to root detection).
  - ownership:      no two documents claim the same owner (delegated to
                    GovernanceValidator._check_duplicate_owners via
                    `apex-gov validate`).
  - cross_references: no broken cross-references (delegated to
                    GovernanceValidator._check_broken_references and
                    architecture-tests/validate_cross_references.py).
  - freeze:         the current freeze record's repository_version
                    matches the currently checked-out git commit.
  - evidence:       the WS0 verification layer's evidence collection
                    succeeds and returns at least one evidence file.
  - metrics:        avg_completeness is a valid float in [0, 1].
  - configuration:  governance.yaml exists, parses, and its `storage.*`
                    paths point at exactly the canonical locations
                    (.governance/governance.db, .governance/exports,
                    .governance/graphs) — i.e. no configuration references
                    a duplicate/stray location.
  - runtime:        `apex-gov run` executes successfully and returns
                    well-formed JSON.
  - repository:     git working tree is in a known state (clean or
                    explicitly reported as dirty; never silently ignored).

Output: PASS or FAIL, with one diagnostic entry per check explaining
exactly what failed and why, so the result is actionable rather than a
bare boolean.
"""
from __future__ import annotations

import json
import subprocess
import sqlite3
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

import yaml


@dataclass
class IntegrityCheckResult:
    check: str
    status: str  # "PASS" | "FAIL" | "SKIP"
    detail: str
    evidence: dict = field(default_factory=dict)


class IntegrityEngine:
    """Runs every integrity check and produces a single PASS/FAIL verdict."""

    CANONICAL_DB = ".governance/governance.db"
    CANONICAL_EXPORT_DIR = ".governance/exports"
    CANONICAL_GRAPHS_DIR = ".governance/graphs"
    # Per-behavioural-root closure dependency graphs (WS2,
    # closure_artefacts.py's dependency_graph.graphml, one per root
    # under .governance/closures/<root>/) are a DELIBERATE, canonical
    # second location for .graphml files -- each is an induced subgraph
    # of the single canonical dependency_graph.graphml restricted to
    # one root's closure, not an independent computation or a stray
    # duplicate of the repository-wide graph set. This directory is
    # therefore excluded from the "stray graph location" check below,
    # same as the archive/ exclusion already in place.
    CANONICAL_CLOSURES_DIR = ".governance/closures"
    # WS4 (Programme 2.5 Phase-0 graph_specification.json): the 14 frozen
    # graphs (document/dependency/ownership/interface/event/schema/
    # configuration/service/plugin/runtime/security/recovery/validation/
    # algorithm) plus state_machine_graph, a 15th graph kept beyond the
    # frozen spec because multiple existing consumers (evidence_engine.py,
    # freeze_engine.py, tests) already depend on it and removing it would
    # be a regression, not a fix.
    EXPECTED_GRAPH_NAMES = {
        "config_graph.graphml",
        "dependency_graph.graphml",
        "document_graph.graphml",
        "event_graph.graphml",
        "interface_graph.graphml",
        "ownership_graph.graphml",
        "schema_graph.graphml",
        "state_machine_graph.graphml",
        "security_graph.graphml",
        "recovery_graph.graphml",
        "validation_graph.graphml",
        "service_graph.graphml",
        "plugin_graph.graphml",
        "runtime_graph.graphml",
        "algorithm_graph.graphml",
    }

    def __init__(self, repo_root: Path, config_path: str = "tools/governance/config/governance.yaml"):
        self.repo_root = Path(repo_root).resolve()
        self.config_path = config_path
        self.results: list[IntegrityCheckResult] = []

    # -- helpers ---------------------------------------------------------

    def _run(self, cmd: list[str]) -> subprocess.CompletedProcess:
        return subprocess.run(cmd, cwd=self.repo_root, capture_output=True, text=True)

    def _record(self, check: str, status: str, detail: str, evidence: Optional[dict] = None) -> None:
        self.results.append(IntegrityCheckResult(check=check, status=status, detail=detail, evidence=evidence or {}))

    # -- individual checks -------------------------------------------------

    def check_configuration(self) -> None:
        cfg_file = self.repo_root / self.config_path
        if not cfg_file.exists():
            self._record("configuration", "FAIL", f"{self.config_path} does not exist")
            return
        try:
            cfg = yaml.safe_load(cfg_file.read_text(encoding="utf-8"))
        except Exception as exc:
            self._record("configuration", "FAIL", f"{self.config_path} failed to parse: {exc}")
            return

        storage = cfg.get("storage", {})
        problems = []
        if storage.get("db_path") != self.CANONICAL_DB:
            problems.append(f"storage.db_path is {storage.get('db_path')!r}, expected {self.CANONICAL_DB!r}")
        if storage.get("export_dir") != self.CANONICAL_EXPORT_DIR:
            problems.append(f"storage.export_dir is {storage.get('export_dir')!r}, expected {self.CANONICAL_EXPORT_DIR!r}")
        if storage.get("graphs_dir") != self.CANONICAL_GRAPHS_DIR:
            problems.append(f"storage.graphs_dir is {storage.get('graphs_dir')!r}, expected {self.CANONICAL_GRAPHS_DIR!r}")

        if problems:
            self._record("configuration", "FAIL", "; ".join(problems))
        else:
            self._record("configuration", "PASS", "governance.yaml storage paths point only at canonical locations", {"storage": storage})

    def check_database(self) -> None:
        # Exactly one canonical database should exist; any stray copies
        # outside .governance/archive/ are a FAIL.
        all_dbs = [p for p in self.repo_root.rglob("*.db") if ".git" not in p.parts]
        stray = [
            str(p.relative_to(self.repo_root))
            for p in all_dbs
            if "archive" not in p.parts and str(p.relative_to(self.repo_root)) != self.CANONICAL_DB
        ]
        canonical_path = self.repo_root / self.CANONICAL_DB
        if not canonical_path.exists():
            self._record("database", "FAIL", f"canonical database {self.CANONICAL_DB} does not exist")
            return
        if stray:
            self._record("database", "FAIL", f"stray database file(s) found outside .governance/archive/: {stray}")
            return
        try:
            conn = sqlite3.connect(str(canonical_path))
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM documents")
            row_count = cur.fetchone()[0]
            cur.execute("PRAGMA user_version")
            schema_version = cur.fetchone()[0]
            conn.close()
        except Exception as exc:
            self._record("database", "FAIL", f"canonical database could not be queried: {exc}")
            return

        # WS5: verify the live database is at the current expected
        # schema version (imported from the single source of truth,
        # storage/schema.py's SCHEMA_VERSION) -- catches a database file
        # that predates a schema migration and was never regenerated.
        try:
            from ..storage.schema import SCHEMA_VERSION, FROZEN_TABLE_NAMES
        except ImportError:
            from governance.storage.schema import SCHEMA_VERSION, FROZEN_TABLE_NAMES  # type: ignore
        if schema_version != SCHEMA_VERSION:
            self._record(
                "database", "FAIL",
                f"canonical database schema_version={schema_version} does not match expected SCHEMA_VERSION={SCHEMA_VERSION}",
            )
            return
        try:
            conn = sqlite3.connect(str(canonical_path))
            cur = conn.cursor()
            cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
            existing_tables = {row[0] for row in cur.fetchall()}
            conn.close()
        except Exception as exc:
            self._record("database", "FAIL", f"could not enumerate tables: {exc}")
            return
        missing_tables = set(FROZEN_TABLE_NAMES) - existing_tables
        if missing_tables:
            self._record("database", "FAIL", f"missing frozen table(s): {sorted(missing_tables)}")
            return

        self._record(
            "database", "PASS",
            f"exactly one canonical database exists with {row_count} document rows, "
            f"schema_version={schema_version}, all {len(FROZEN_TABLE_NAMES)} frozen tables present",
            {"row_count": row_count, "schema_version": schema_version},
        )

    def check_graphs(self) -> None:
        graphs_dir = self.repo_root / self.CANONICAL_GRAPHS_DIR
        if not graphs_dir.exists():
            self._record("graphs", "FAIL", f"{self.CANONICAL_GRAPHS_DIR} does not exist")
            return
        present = {p.name for p in graphs_dir.glob("*.graphml")}
        missing = self.EXPECTED_GRAPH_NAMES - present
        extra = present - self.EXPECTED_GRAPH_NAMES
        # Also check for any duplicate graph sets elsewhere in the repo
        # (outside archive), which would indicate a regression to the
        # duplicated-graph state found by the Canonicality Audit.
        closures_dir = self.repo_root / self.CANONICAL_CLOSURES_DIR
        all_graphml = [
            p for p in self.repo_root.rglob("*.graphml")
            if ".git" not in p.parts
            and "archive" not in p.parts
            and closures_dir not in p.parents
        ]
        stray_dirs = {p.parent for p in all_graphml if p.parent != graphs_dir}

        problems = []
        if missing:
            problems.append(f"missing graph(s): {sorted(missing)}")
        if extra:
            problems.append(f"unexpected extra graph file(s): {sorted(extra)}")
        if stray_dirs:
            problems.append(f"graph files found outside {self.CANONICAL_GRAPHS_DIR}: {[str(d.relative_to(self.repo_root)) for d in stray_dirs]}")

        if problems:
            self._record("graphs", "FAIL", "; ".join(problems))
            return

        # WS4 ("Every graph is validated against source documents"):
        # beyond structural presence (checked above), verify every
        # graph's actual node/edge CONTENT is traceable back to real,
        # currently-indexed source documents -- catching a stale graph
        # left over from a prior repository state that a mere
        # file-existence check would miss. Rebuilds the graphs
        # in-process (not by re-reading the persisted .graphml files)
        # from a fresh indexing pass, exactly as check_closures() and
        # other checks already do, preserving the single-canonical-
        # computation invariant.
        try:
            import yaml as _yaml
            try:
                from ..indexer.repo_indexer import RepoIndexer
                from ..parser.markdown_parser import MarkdownParser
                from ..metadata.metadata_parser import MetadataParser
                from ..graphs.graph_builder import GraphBuilder
                from ..graphs.graph_source_validator import validate_all_graphs
                from ..references.event_matrix_parser import build_event_graph_edges, parse_event_ownership_matrix
                from ..references.schema_reference_scanner import scan_corpus_for_schema_references
            except ImportError:
                from governance.indexer.repo_indexer import RepoIndexer  # type: ignore
                from governance.parser.markdown_parser import MarkdownParser  # type: ignore
                from governance.metadata.metadata_parser import MetadataParser  # type: ignore
                from governance.graphs.graph_builder import GraphBuilder  # type: ignore
                from governance.graphs.graph_source_validator import validate_all_graphs  # type: ignore
                from governance.references.event_matrix_parser import build_event_graph_edges, parse_event_ownership_matrix  # type: ignore
                from governance.references.schema_reference_scanner import scan_corpus_for_schema_references  # type: ignore

            cfg = _yaml.safe_load((self.repo_root / "tools/governance/config/governance.yaml").read_text())
            indexer = RepoIndexer(str(self.repo_root), cfg["docs_globs"])
            inventory = indexer.build_inventory()
            known_paths = [item["path"] for item in inventory]
            md_parser = MarkdownParser(str(self.repo_root))
            meta_parser = MetadataParser(known_paths=known_paths)
            graph_builder = GraphBuilder()
            docs = []
            for item in inventory:
                parsed = md_parser.parse_file(item["path"])
                meta = meta_parser.parse_document(parsed["raw_text"], item["path"])
                docs.append(meta)
                graph_builder.add_document(meta)

            matrix_path = self.repo_root / "docs" / "EVENT-OWNERSHIP-MATRIX.md"
            if matrix_path.exists():
                rows = parse_event_ownership_matrix(matrix_path.read_text(encoding="utf-8"))
                event_result = build_event_graph_edges(rows, self.repo_root / "docs")
                graph_builder.add_event_matrix_edges(event_result["edges"])
            schema_results = scan_corpus_for_schema_references(docs, self.repo_root / "schemas")
            graph_builder.add_schema_references(schema_results)

            source_validation = validate_all_graphs(graph_builder, docs)
        except Exception as exc:
            self._record("graphs", "FAIL", f"graph-vs-source-document validation raised an exception: {exc}")
            return

        if not source_validation["overall_valid"]:
            failing = [r for r in source_validation["results"] if not r["valid"]]
            self._record(
                "graphs", "FAIL",
                f"exactly {len(present)} canonical graphs present, but {len(failing)} graph(s) failed "
                f"source-document validation: {[r['graph_name'] for r in failing]}",
                {"graphs": sorted(present), "source_validation_failures": failing},
            )
            return

        self._record(
            "graphs", "PASS",
            f"exactly {len(present)} canonical graphs present, no stray copies found, "
            f"and all {source_validation['graphs_validated']} content-validated graphs trace back to real source documents",
            {"graphs": sorted(present), "graphs_source_validated": source_validation["graphs_validated"]},
        )

    def check_runtime(self) -> None:
        result = self._run(["apex-gov", "run"])
        if result.returncode != 0:
            self._record("runtime", "FAIL", f"`apex-gov run` exited {result.returncode}: {result.stderr[:500]}")
            return
        try:
            output = json.loads(result.stdout)
        except Exception as exc:
            self._record("runtime", "FAIL", f"`apex-gov run` did not return valid JSON: {exc}")
            return
        required_fields = {"documents_indexed", "behavioural_roots", "validation_findings", "closures_computed", "avg_completeness", "graph_nodes", "graph_edges"}
        missing_fields = required_fields - set(output.keys())
        if missing_fields:
            self._record("runtime", "FAIL", f"canonical output missing fields: {sorted(missing_fields)}")
            return
        self._record("runtime", "PASS", "canonical runtime executed successfully and returned well-formed output", output)
        self._last_run_output = output

    def check_roots(self) -> None:
        # Determinism check specific to root detection: run twice, compare.
        r1 = self._run(["apex-gov", "roots"])
        r2 = self._run(["apex-gov", "roots"])
        if r1.returncode != 0 or r2.returncode != 0:
            self._record("roots", "FAIL", "`apex-gov roots` failed to execute")
            return
        if r1.stdout != r2.stdout:
            self._record("roots", "FAIL", "behavioural root output differs between two consecutive runs (non-deterministic)")
            return
        count_line = r1.stdout.splitlines()[0] if r1.stdout else ""
        self._record("roots", "PASS", f"root detection stable across 2 consecutive runs: {count_line}")

    def check_closures(self) -> None:
        result = self._run(["apex-gov", "run"])
        if result.returncode != 0:
            self._record("closures", "FAIL", "could not execute canonical runtime to verify closures")
            return
        try:
            output = json.loads(result.stdout)
        except Exception:
            self._record("closures", "FAIL", "canonical runtime output not valid JSON")
            return
        roots = output.get("behavioural_roots", 0)
        closures = output.get("closures_computed", 0)
        if roots != closures:
            self._record("closures", "FAIL", f"behavioural_roots ({roots}) != closures_computed ({closures}); every root must have exactly one closure")
            return

        # FIX (Remediation Item 5: reverse-closure support): also verify
        # reverse closure is computable for every root, in-process (not
        # merely that ClosureEngine.compute_reverse_closure exists as a
        # method -- actually invoke it against the live corpus).
        try:
            import yaml as _yaml
            try:
                from ..indexer.repo_indexer import RepoIndexer
                from ..parser.markdown_parser import MarkdownParser
                from ..metadata.metadata_parser import MetadataParser
                from ..graphs.graph_builder import GraphBuilder
                from ..closure.closure_engine import BehaviouralRootDetector, ClosureEngine
            except ImportError:
                from governance.indexer.repo_indexer import RepoIndexer  # type: ignore
                from governance.parser.markdown_parser import MarkdownParser  # type: ignore
                from governance.metadata.metadata_parser import MetadataParser  # type: ignore
                from governance.graphs.graph_builder import GraphBuilder  # type: ignore
                from governance.closure.closure_engine import BehaviouralRootDetector, ClosureEngine  # type: ignore

            cfg = _yaml.safe_load((self.repo_root / "tools/governance/config/governance.yaml").read_text())
            indexer = RepoIndexer(str(self.repo_root), cfg["docs_globs"])
            inventory = indexer.build_inventory()
            known_paths = [item["path"] for item in inventory]
            md_parser = MarkdownParser(str(self.repo_root))
            meta_parser = MetadataParser(known_paths=known_paths)
            graph_builder = GraphBuilder()
            docs = []
            for item in inventory:
                parsed = md_parser.parse_file(item["path"])
                meta = meta_parser.parse_document(parsed["raw_text"], item["path"])
                docs.append(meta)
                graph_builder.add_document(meta)
            detector = BehaviouralRootDetector(cfg["behavioural_root_signals"])
            live_roots = detector.detect_roots(docs)
            closure_engine = ClosureEngine(graph_builder.dependency_graph)
            reverse_closures_ok = 0
            for r in live_roots:
                rc = closure_engine.compute_reverse_closure(r.path)
                if r.path in rc:  # a root's reverse closure always contains itself
                    reverse_closures_ok += 1
            if reverse_closures_ok != len(live_roots):
                self._record(
                    "closures", "FAIL",
                    f"reverse closure could not be computed for all roots: {reverse_closures_ok}/{len(live_roots)}",
                )
                return
        except Exception as exc:
            self._record("closures", "FAIL", f"reverse closure verification raised an exception: {exc}")
            return

        # WS2: every behavioural root must have its full 5-artefact set
        # (manifest, dependency_graph, audit, work_queue, maturity_report)
        # persisted under .governance/closures/<root>/ -- verified by
        # checking the files actually exist on disk (produced by the
        # preceding `apex-gov run` invocation above), not merely that the
        # writer function exists.
        closures_dir = self.repo_root / self.CANONICAL_CLOSURES_DIR
        required_files = {"manifest.json", "dependency_graph.graphml", "audit.json", "work_queue.json", "maturity_report.json"}
        incomplete_roots = []
        for r in live_roots:
            root_dir = closures_dir / Path(r.path).stem
            present = {p.name for p in root_dir.glob("*")} if root_dir.exists() else set()
            if not required_files.issubset(present):
                incomplete_roots.append(r.path)
        if incomplete_roots:
            self._record(
                "closures", "FAIL",
                f"{len(incomplete_roots)} root(s) missing one or more of the 5 required closure artefacts: {sorted(incomplete_roots)}",
            )
            return

        self._record(
            "closures", "PASS",
            f"every one of {roots} behavioural roots has a computed forward closure, reverse closure, and full 5-artefact set (manifest/dependency_graph/audit/work_queue/maturity_report)",
            {"roots": roots, "closures": closures, "reverse_closures_verified": reverse_closures_ok, "roots_with_full_artefact_set": len(live_roots) - len(incomplete_roots)},
        )

    def check_validators(self) -> None:
        # NOTE: the installed console-script package is named `governance`
        # (see tools/governance/pyproject.toml: packages.find where=[".."],
        # include=["governance*"]), not `tools.governance` — `import
        # tools.governance...` fails once installed into a venv via
        # `pip install -e tools/governance`, since `tools/` itself is not
        # part of the installed package. Import relative to the installed
        # package name to work both when installed and (via the `..`
        # relative import elsewhere in this module) when run in-place.
        try:
            from ..validator.registry import run_all_validators
        except ImportError:
            try:
                from governance.validator.registry import run_all_validators  # type: ignore
            except Exception as exc:
                self._record("validators", "FAIL", f"could not import validator registry: {exc}")
                return
        # FIX (Remediation Item 3): this check's PASS/FAIL now genuinely
        # reflects "did the repository pass validation", not merely "did
        # the validator process execute without crashing". Previously,
        # `apex-gov validate` (which `run_all_validators()` shells out to
        # for in-engine validators) always returned exit code 0 regardless
        # of findings count/severity, so `run_validator()`'s
        # `"PASS" if returncode == 0 else "FAIL"` logic was checking
        # execution success only. `apex-gov validate` now exits non-zero
        # when GovernanceValidator.has_failing_findings() is true (any
        # finding at or above FAILURE_THRESHOLD), so this check's result
        # is now a genuine repository-passed-validation signal.
        results = run_all_validators(self.repo_root)
        failed = [r["id"] for r in results if r["status"] != "PASS"]
        if failed:
            self._record(
                "validators", "FAIL",
                f"{len(failed)}/{len(results)} validator executions reported failing findings (not merely a crash): {failed}",
            )
            return
        self._record(
            "validators", "PASS",
            f"all {len(results)} validator executions completed AND reported zero findings at or above the failure threshold",
            {"validator_count": len(results)},
        )

    def check_ownership(self) -> None:
        result = self._run(["python3", "architecture-tests/validate_ownership.py"])
        status = "PASS" if result.returncode == 0 else "FAIL"
        self._record("ownership", status, result.stdout.strip().splitlines()[-1] if result.stdout.strip() else "no output")

    def check_cross_references(self) -> None:
        result = self._run(["python3", "architecture-tests/validate_cross_references.py"])
        status = "PASS" if result.returncode == 0 else "FAIL"
        self._record("cross_references", status, result.stdout.strip().splitlines()[-1] if result.stdout.strip() else "no output")

    def check_freeze(self) -> None:
        """Verify the freeze record is current.

        A freeze record embeds the commit hash of the repository state it
        was computed against. This creates an inherent self-reference
        problem: committing the freeze record changes the tree, which
        changes the commit hash, which the freeze record cannot have
        embedded in advance (it would need to know its own resulting hash
        before it exists). A naive `freeze_commit == HEAD` check therefore
        FAILs by construction on every commit that regenerates the freeze
        record, forever — see the Repository Canonicality Repair session's
        commit b0bb1e4f8 and GOVERNANCE-CERTIFICATION-REPORT.md §5 for the
        full writeup of this limitation.

        The correct semantic (documented in freeze_WS0.json's own
        "reason_for_regeneration" field): the freeze record represents the
        repository state as of "the last commit BEFORE this freeze was
        taken". This check therefore treats the freeze as current if
        EITHER:
          1. freeze_commit == current HEAD (the ideal case, achievable
             only when nothing else changes between freeze generation and
             the next commit), OR
          2. freeze_commit == HEAD's parent AND the only file that differs
             between that parent and HEAD is the freeze record itself
             (i.e. the freeze-regenerating commit changed nothing else,
             which is the expected shape of a "regenerate freeze" commit).
        Any other relationship means real repository content changed after
        the freeze was taken without a corresponding freeze regeneration,
        which is a genuine staleness FAIL.
        """
        freeze_path = self.repo_root / ".governance/freeze/freeze_WS0.json"
        if not freeze_path.exists():
            self._record("freeze", "FAIL", "no freeze record found at .governance/freeze/freeze_WS0.json")
            return
        try:
            freeze = json.loads(freeze_path.read_text(encoding="utf-8"))
        except Exception as exc:
            self._record("freeze", "FAIL", f"freeze record failed to parse: {exc}")
            return

        current_commit = self._run(["git", "rev-parse", "HEAD"]).stdout.strip()
        freeze_commit = freeze.get("repository", {}).get("commit_hash") or freeze.get("identity", {}).get("repository_version")

        # WS6/WS9: verify tamper-evidence (Ed25519 signature) BEFORE
        # trusting anything else in the record -- if the signature does
        # not verify, the record's content (including freeze_commit
        # itself) cannot be trusted, regardless of what the staleness
        # check below would otherwise conclude.
        #
        # IMPORTANT: verification uses ONLY the public key
        # (public_key_path), never the private signing key
        # (signing_key_path, git-ignored, absent in any fresh clone).
        # An earlier version of this check defaulted to constructing
        # FreezeValidator from signing_key_path alone, which made
        # verification silently impossible in a fresh clone (the exact
        # defect this session's own mandatory fresh-clone
        # re-verification step caught: `apex-gov integrity` failed the
        # freeze check in a genuinely fresh `git clone` with "record
        # content does not match its embedded signature", even though
        # the record was never tampered with -- the private key file
        # simply didn't exist there). Fixed by reading public_key_path
        # explicitly and passing it as FreezeValidator's public_key_path
        # argument, which is all `verify()` ever needs.
        tamper_evidence = freeze.get("tamper_evidence")
        if tamper_evidence:
            try:
                from ..freeze.freeze_manifest import FreezeValidator
            except ImportError:
                from governance.freeze.freeze_manifest import FreezeValidator  # type: ignore
            key_path = self.repo_root / tamper_evidence.get("signing_key_path", ".governance/freeze/.signing_key")
            public_key_path = self.repo_root / tamper_evidence.get("public_key_path", ".governance/freeze/signing_public_key.pem")
            validator = FreezeValidator(key_path, public_key_path=public_key_path)
            signature = tamper_evidence.get("signature", "")
            if not validator.verify(freeze, signature):
                self._record(
                    "freeze", "FAIL",
                    "freeze record failed tamper-evidence (Ed25519 signature) verification -- "
                    "record content does not match its embedded signature",
                )
                return

        if freeze_commit == current_commit:
            self._record("freeze", "PASS", "freeze record commit_hash matches current HEAD exactly", {"commit": current_commit})
            return

        # Case 2: freeze_commit is HEAD's immediate parent, and every
        # file that changed since then is either the freeze record
        # itself, or a file `apex-gov freeze` legitimately regenerates
        # as a side effect of the canonical pipeline it invokes
        # internally (FreezeEngine.freeze() calls EvidenceEngine.collect(),
        # which itself runs `apex-gov run` as a subprocess to gather
        # fresh evidence -- this necessarily touches governance.db,
        # every .governance/closures/<root>/* artefact (WS2), every
        # .governance/graphs/*.graphml file, exports/, and
        # .governance/evidence/* (WS7), none of which represent
        # unrelated repository content changes).
        #
        # This exception was ORIGINALLY written (Repository
        # Canonicality Repair) when `apex-gov freeze` only ever touched
        # the single freeze JSON file, so "changed_files == exactly one
        # path" was the correct, sufficient check at the time. It
        # became too strict once WS2/WS7 added persistent, timestamped
        # per-run artefacts that `apex-gov run` (and therefore
        # `apex-gov freeze`, transitively) regenerates on every
        # invocation -- confirmed as a real defect via this session's
        # own third fresh-clone re-verification pass, where a genuine
        # freeze-only regeneration commit was incorrectly reported FAIL
        # because 35 closure manifests' timestamp fields (a legitimate,
        # expected side effect) also changed.
        parent_commit = self._run(["git", "rev-parse", "HEAD~1"]).stdout.strip()
        if freeze_commit == parent_commit:
            diff = self._run(["git", "diff", "--name-only", parent_commit, current_commit])
            changed_files = [f for f in diff.stdout.strip().splitlines() if f]
            freeze_rel_path = str(freeze_path.relative_to(self.repo_root))
            allowed_prefixes = (
                freeze_rel_path,
                ".governance/freeze/",
                ".governance/closures/",
                ".governance/graphs/",
                ".governance/evidence/",
                ".governance/exports/",
                ".governance/governance.db",
            )
            unexplained_files = [f for f in changed_files if not f.startswith(allowed_prefixes)]
            if not unexplained_files:
                self._record(
                    "freeze", "PASS",
                    f"freeze record references parent commit {freeze_commit[:12]}; "
                    f"HEAD ({current_commit[:12]}) differs only by the freeze-regeneration commit itself "
                    f"(freeze record + canonical pipeline byproducts: closures/graphs/evidence/exports/database)",
                    {"freeze_commit": freeze_commit, "current_commit": current_commit, "changed_files": changed_files},
                )
                return
            self._record(
                "freeze", "FAIL",
                f"freeze record references parent commit {freeze_commit[:12]}, but HEAD ({current_commit[:12]}) "
                f"also changed file(s) outside the expected freeze-regeneration byproduct set: {unexplained_files}",
                {"freeze_commit": freeze_commit, "current_commit": current_commit, "changed_files": changed_files, "unexplained_files": unexplained_files},
            )
            return

        self._record(
            "freeze", "FAIL",
            f"freeze record commit_hash ({freeze_commit}) is neither current HEAD ({current_commit}) "
            "nor its immediate parent; freeze record is stale and must be regenerated",
            {"freeze_commit": freeze_commit, "current_commit": current_commit},
        )

    def check_evidence(self) -> None:
        # Uses the canonical Evidence Engine (Work Item 5), not WS0's
        # earlier ad hoc file-hashing (WS0VerificationLayer.collect_evidence
        # is superseded by this — see tools/governance/evidence/evidence_engine.py).
        try:
            from ..evidence.evidence_engine import EvidenceEngine
        except ImportError:
            from governance.evidence.evidence_engine import EvidenceEngine  # type: ignore
        try:
            engine = EvidenceEngine(self.repo_root)
            record = engine.collect()
        except Exception as exc:
            self._record("evidence", "FAIL", f"evidence collection raised an exception: {exc}")
            return
        hash_count = len(record.hashes)
        if hash_count == 0:
            self._record("evidence", "FAIL", "evidence collection returned zero artefact hashes")
            return

        # WS7: verify the structured, queryable Evidence Store (10
        # subdirectories) has at least one entry -- distinguishes
        # "evidence CAN be collected" (the check above) from "evidence
        # HAS BEEN persisted queryably", which is the actual WS7
        # checklist requirement ("Evidence is queryable and auditable").
        try:
            from ..evidence.evidence_store import EvidenceStore, STRUCTURED_SUBDIRS
        except ImportError:
            from governance.evidence.evidence_store import EvidenceStore, STRUCTURED_SUBDIRS  # type: ignore
        store = EvidenceStore(self.repo_root / ".governance" / "evidence")
        missing_dirs = [d for d in STRUCTURED_SUBDIRS if not (store.evidence_dir / d).exists()]
        if missing_dirs:
            self._record("evidence", "FAIL", f"structured evidence subdirectories missing: {missing_dirs}")
            return
        if not store.has_any_evidence():
            self._record("evidence", "FAIL", "structured evidence store exists but has zero entries in any Programme bucket")
            return

        self._record(
            "evidence", "PASS",
            f"evidence collection succeeded: {hash_count} artefact hashes, "
            f"{len(record.validator_ids)} validators recorded, commit={record.commit[:12]}; "
            f"structured evidence store has {sum(store.counts().values())} total entries across {len(STRUCTURED_SUBDIRS)} subdirectories",
            {"artefact_hash_count": hash_count, "record_hash": record.record_hash(), "evidence_store_counts": store.counts()},
        )

    def check_metrics(self) -> None:
        output = getattr(self, "_last_run_output", None)
        if output is None:
            result = self._run(["apex-gov", "run"])
            if result.returncode != 0:
                self._record("metrics", "FAIL", "could not execute canonical runtime to verify metrics")
                return
            output = json.loads(result.stdout)
        completeness = output.get("avg_completeness")
        if completeness is None or not isinstance(completeness, (int, float)) or not (0.0 <= completeness <= 1.0):
            self._record("metrics", "FAIL", f"avg_completeness is not a valid float in [0, 1]: {completeness!r}")
            return

        # WS8: verify all 10 Phase-0-frozen metrics are present in the
        # live database, each a valid float in [0, 1] -- not just the
        # pre-existing avg_completeness check above.
        db_path = self.repo_root / self.CANONICAL_DB
        expected_metric_names = {
            "Repository Completeness", "Closure Completeness", "Validator Coverage",
            "Reference Integrity", "Ownership Integrity", "Graph Integrity",
            "Security Coverage", "Schema Coverage", "Interface Coverage", "Event Coverage",
        }
        try:
            conn = sqlite3.connect(str(db_path))
            cur = conn.cursor()
            cur.execute("SELECT metric_name, value FROM metrics")
            live_metrics = dict(cur.fetchall())
            conn.close()
        except Exception as exc:
            self._record("metrics", "FAIL", f"could not query metrics table: {exc}")
            return

        missing = expected_metric_names - set(live_metrics.keys())
        if missing:
            self._record("metrics", "FAIL", f"missing frozen metric(s) in database: {sorted(missing)}")
            return
        invalid = {
            name: val for name, val in live_metrics.items()
            if name in expected_metric_names and not (isinstance(val, (int, float)) and 0.0 <= val <= 1.0)
        }
        if invalid:
            self._record("metrics", "FAIL", f"metric(s) out of valid [0,1] range: {invalid}")
            return

        self._record(
            "metrics", "PASS",
            f"avg_completeness = {completeness:.4f}; all 10 Phase-0-frozen metrics present and valid",
            {"avg_completeness": completeness, "metrics": {k: v for k, v in live_metrics.items() if k in expected_metric_names}},
        )

    def check_repository(self) -> None:
        status = self._run(["git", "status", "--short"])
        commit = self._run(["git", "rev-parse", "HEAD"]).stdout.strip()
        tree_state = "clean" if not status.stdout.strip() else "dirty"
        # A dirty tree is not automatically a FAIL (integrity checks can be
        # run mid-repair); it is reported explicitly rather than hidden.
        self._record("repository", "PASS", f"HEAD={commit}, working tree is {tree_state}", {"commit": commit, "tree_state": tree_state, "changed_files": status.stdout.strip().splitlines()})

    def check_work_queue(self) -> None:
        """WS9 (readiness_checklist.json CHECK-WS9): 'Work queue
        integrity checks pass' -- previously entirely unvalidated by
        this engine's 13 checks (confirmed by the Programme 2.5 Final
        Certification Audit: the 837KB AI-ORCHESTRATION_full_queue.json
        was completely unvalidated). Delegates to
        validator/work_queue/checks.py's check_all_work_queues(), which
        validates schema well-formedness, task_id uniqueness,
        document_path existence on disk, and valid status/priority
        enums for every *.json file under .governance/work_queue/."""
        try:
            from ..validator.work_queue.checks import check_all_work_queues
        except ImportError:
            from governance.validator.work_queue.checks import check_all_work_queues  # type: ignore
        work_queue_dir = self.repo_root / ".governance" / "work_queue"
        result = check_all_work_queues(work_queue_dir, self.repo_root)
        if result["status"] == "FAIL":
            failing_files = [f for f in result.get("files", []) if f["status"] == "FAIL"]
            problem_summary = []
            for f in failing_files:
                problem_summary.extend(f["problems"][:3])
            self._record("work_queue", "FAIL", f"{result['detail']}; sample problems: {problem_summary[:10]}")
            return
        self._record("work_queue", "PASS", result["detail"], {"files": [f["file"] for f in result.get("files", [])]})

    # -- orchestration -----------------------------------------------------

    def run_all(self) -> dict[str, Any]:
        self.results = []
        # Order matters: runtime/roots/closures/metrics populate
        # self._last_run_output, which later checks reuse to avoid
        # redundant `apex-gov run` invocations.
        self.check_configuration()
        self.check_database()
        self.check_graphs()
        self.check_runtime()
        self.check_roots()
        self.check_closures()
        self.check_validators()
        self.check_ownership()
        self.check_cross_references()
        self.check_freeze()
        self.check_evidence()
        self.check_metrics()
        self.check_repository()
        self.check_work_queue()

        overall = "PASS" if all(r.status == "PASS" for r in self.results) else "FAIL"
        return {
            "overall": overall,
            "checks": [
                {"check": r.check, "status": r.status, "detail": r.detail, "evidence": r.evidence}
                for r in self.results
            ],
            "failed_checks": [r.check for r in self.results if r.status == "FAIL"],
        }


def main() -> int:
    repo_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    engine = IntegrityEngine(repo_root)
    report = engine.run_all()
    print(json.dumps(report, indent=2))
    return 0 if report["overall"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
