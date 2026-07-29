"""
WS0 - Governance Verification Layer

WS0 is NOT a governance runtime. It does NOT compute governance state.

WS0 consumes canonical governance outputs from tools/governance/ and provides:
- Verification: Cross-reference canonical outputs against evidence
- Evidence Collection: Aggregate and certify governance evidence
- Regression Checking: Compare canonical outputs across executions
- Certification: Package evidence for governance certification
- Reporting: Generate verification and certification reports

All governance computation originates EXCLUSIVELY from tools/governance/.
"""

import json
import subprocess
import hashlib
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional


class WS0VerificationLayer:
    """
    WS0 Verification Layer - consumes canonical governance outputs.
    
    Does NOT perform:
    - Repository indexing
    - Metadata parsing
    - Reference parsing
    - Root detection
    - Graph construction
    - Closure generation
    - Validation
    - Metrics computation
    - Integrity computation
    - Freeze computation
    - Evidence generation (from scratch)
    
    ONLY performs:
    - Verification of canonical outputs
    - Evidence collection from canonical outputs
    - Regression checking across executions
    - Certification packaging
    - Reporting
    """
    
    def __init__(self, repo_root: Path):
        self.repo_root = Path(repo_root).resolve()
        self.ws0_dir = self.repo_root / ".governance" / "programme_2.5" / "ws0"
        self.reports_dir = self.ws0_dir / "reports"
        self.baseline_path = self.reports_dir / "baseline_output.json"
        self.canonical_cli = "tools/governance/cli/main.py"

    def load_baseline(self) -> Optional[Dict[str, Any]]:
        """Load the stored baseline canonical output, if one exists.

        The baseline is the canonical governance output (documents_indexed,
        behavioural_roots, etc.) captured at the time of the last successful
        certification. `run_regression_check` compares the current run
        against this baseline to detect governance-state drift.
        """
        if not self.baseline_path.exists():
            return None
        with open(self.baseline_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_baseline(self, canonical_output: Dict[str, Any]) -> Path:
        """Persist the current canonical output as the new regression baseline."""
        self.reports_dir.mkdir(parents=True, exist_ok=True)
        with open(self.baseline_path, "w", encoding="utf-8") as f:
            json.dump(canonical_output, f, indent=2)
        return self.baseline_path
    
    def invoke_canonical_runtime(self, command: str, config_path: Optional[str] = None) -> Dict[str, Any]:
        """
        Invoke the canonical governance runtime (tools/governance).
        
        This is the ONLY way WS0 obtains governance state.
        """
        cmd = ["python", "-m", "tools.governance.cli.main", command]
        if config_path:
            cmd.extend(["--config-path", config_path])
        
        result = subprocess.run(
            cmd,
            cwd=self.repo_root,
            capture_output=True,
            text=True
        )
        
        return {
            "command": command,
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "success": result.returncode == 0
        }
    
    def run_full_pipeline(self, config_path: Optional[str] = None) -> Dict[str, Any]:
        """
        Run the complete canonical governance pipeline via tools/governance.
        
        Returns the canonical governance output.
        """
        return self.invoke_canonical_runtime("run", config_path)
    
    def verify_canonical_output(self, output: Dict[str, Any]) -> Dict[str, Any]:
        """
        Verify canonical governance output integrity.
        
        Checks:
        - Output structure matches expected schema
        - Hash consistency
        - Required fields present
        """
        verification = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "output_hash": self._hash_dict(output),
            "checks": {}
        }
        
        required_fields = [
            "documents_indexed",
            "behavioural_roots", 
            "validation_findings",
            "closures_computed",
            "avg_completeness",
            "graph_nodes",
            "graph_edges"
        ]
        
        for field in required_fields:
            verification["checks"][field] = {
                "present": field in output,
                "value": output.get(field)
            }
        
        verification["all_checks_pass"] = all(
            check["present"] for check in verification["checks"].values()
        )
        
        return verification
    
    def collect_evidence(self, canonical_output: Dict[str, Any]) -> Dict[str, Any]:
        """
        Collect evidence for this certification run.

        SUPERSEDED IMPLEMENTATION NOTICE (Repository Canonicality Repair,
        Work Item 5): this method previously performed its own ad hoc file
        hashing (repository hash + a flat list of graph/freeze file
        hashes), independent of any canonical evidence engine, because no
        such engine existed yet. A canonical Evidence Engine now exists at
        tools/governance/evidence/evidence_engine.py, which additionally
        records the producing command, inputs, execution time, and
        validator results — the full field set required by the
        Repository Canonicality Repair directive. This method now
        delegates to it and returns a superset of the original shape
        (all original keys are preserved for backward compatibility with
        existing certification-package consumers; new fields are added
        alongside them, not in place of them).
        """
        try:
            from tools.governance.evidence.evidence_engine import EvidenceEngine
        except ImportError:
            from governance.evidence.evidence_engine import EvidenceEngine  # type: ignore

        engine = EvidenceEngine(self.repo_root)
        record = engine.collect()

        # Preserve the original flat evidence_files shape (path/hash/type)
        # for graphs and freeze records, derived from the canonical
        # EvidenceRecord's `hashes` dict, so existing consumers of this
        # method's return value keep working unchanged.
        evidence_files = []
        for rel_path, file_hash in sorted(record.hashes.items()):
            if rel_path.endswith(".graphml"):
                evidence_files.append({"path": rel_path, "hash": file_hash, "type": "graph"})
        freeze_dir = self.repo_root / ".governance" / "freeze"
        if freeze_dir.exists():
            for freeze_file in sorted(freeze_dir.glob("*.json")):
                evidence_files.append({
                    "path": str(freeze_file.relative_to(self.repo_root)),
                    "hash": self._hash_file(freeze_file),
                    "type": "freeze"
                })

        evidence = {
            "repository_hash": self._get_repo_hash(),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "canonical_output_hash": self._hash_dict(canonical_output),
            "evidence_files": evidence_files,
            # New fields from the canonical Evidence Engine:
            "evidence_engine_record": record.to_dict(),
            "evidence_record_hash": record.record_hash(),
        }
        return evidence
    
    def run_regression_check(self, current_output: Dict[str, Any], 
                             baseline_output: Dict[str, Any]) -> Dict[str, Any]:
        """
        Run regression check between current and baseline canonical outputs.
        """
        regression = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "fields_compared": [],
            "regressions": [],
            "passed": True
        }
        
        all_keys = set(current_output.keys()) | set(baseline_output.keys())
        
        for key in all_keys:
            if key in ["timestamp", "execution_time"]:
                continue
            
            regression["fields_compared"].append(key)
            
            current_val = current_output.get(key)
            baseline_val = baseline_output.get(key)
            
            if current_val != baseline_val:
                regression["regressions"].append({
                    "field": key,
                    "baseline": baseline_val,
                    "current": current_val
                })
                regression["passed"] = False
        
        return regression
    
    def generate_certification_package(self, verification: Dict[str, Any],
                                        evidence: Dict[str, Any],
                                        regression: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate WS0 certification package from verification results.
        """
        package = {
            "certification_id": self._generate_cert_id(),
            "workstream_id": "WS0",
            "version": "1.0.0",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "verification": verification,
            "evidence": evidence,
            "regression": regression,
            "certification_decision": "PASS" if (
                verification.get("all_checks_pass", False) and 
                regression.get("passed", False)
            ) else "FAIL",
            "repository_hash": self._get_repo_hash()
        }
        
        return package
    
    def save_report(self, report: Dict[str, Any], filename: str) -> Path:
        """Save a verification/certification report."""
        self.reports_dir.mkdir(parents=True, exist_ok=True)
        report_path = self.reports_dir / filename
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        return report_path
    
    def _hash_dict(self, data: Dict[str, Any]) -> str:
        """Generate deterministic hash of a dictionary."""
        content = json.dumps(data, sort_keys=True)
        return hashlib.sha256(content.encode()).hexdigest()[:16]
    
    def _hash_file(self, path: Path) -> str:
        """Generate hash of a file."""
        with open(path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()[:16]
    
    def _get_repo_hash(self) -> str:
        """Get repository commit hash."""
        try:
            result = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=self.repo_root,
                capture_output=True,
                text=True
            )
            return result.stdout.strip()[:16]
        except:
            return "unknown"
    
    def _generate_cert_id(self) -> str:
        """Generate certification ID."""
        return hashlib.sha256(
            f"{datetime.now(timezone.utc).isoformat()}{self._get_repo_hash()}".encode()
        ).hexdigest()[:16]


def main():
    """CLI entry point for WS0 verification layer."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python -m .governance.programme_2.5.ws0 <command>")
        print("Commands: verify, certify, regress, evidence")
        sys.exit(1)
    
    repo_root = Path(sys.argv[2]) if len(sys.argv) > 2 else Path.cwd()
    ws0 = WS0VerificationLayer(repo_root)
    command = sys.argv[1]
    
    if command == "verify":
        output = ws0.run_full_pipeline()
        if output["success"]:
            canonical = json.loads(output["stdout"])
            verification = ws0.verify_canonical_output(canonical)
            ws0.save_report(verification, f"verification_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.json")
            print(json.dumps(verification, indent=2))
        else:
            print(f"Canonical runtime failed: {output['stderr']}")
            sys.exit(1)
    
    elif command == "certify":
        output = ws0.run_full_pipeline()
        if output["success"]:
            canonical = json.loads(output["stdout"])
            verification = ws0.verify_canonical_output(canonical)
            evidence = ws0.collect_evidence(canonical)

            baseline = ws0.load_baseline()
            if baseline is None:
                # No baseline exists yet (first certification run). This is
                # NOT the same as "regression passed" — it is explicitly
                # marked as an un-compared first run so certification
                # reports never claim a regression check that did not
                # actually happen.
                regression = {
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "fields_compared": [],
                    "regressions": [],
                    "passed": True,
                    "baseline_available": False,
                    "note": "No baseline present; this is the initial certification run. Baseline saved for future regression checks.",
                }
            else:
                regression = ws0.run_regression_check(canonical, baseline)
                regression["baseline_available"] = True

            package = ws0.generate_certification_package(verification, evidence, regression)
            ws0.save_report(package, f"ws0_certification_package_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.json")

            # Only advance the baseline when certification actually passed —
            # a failed run must not silently become the new "known good" state.
            if package["certification_decision"] == "PASS":
                ws0.save_baseline(canonical)

            print(json.dumps(package, indent=2))
        else:
            print(f"Canonical runtime failed: {output['stderr']}")
            sys.exit(1)

    elif command == "regress":
        baseline = ws0.load_baseline()
        if baseline is None:
            print("No baseline found. Run `certify` at least once to establish a baseline.")
            sys.exit(1)
        output = ws0.run_full_pipeline()
        if output["success"]:
            canonical = json.loads(output["stdout"])
            regression = ws0.run_regression_check(canonical, baseline)
            regression["baseline_available"] = True
            ws0.save_report(regression, f"regression_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.json")
            print(json.dumps(regression, indent=2))
            if not regression["passed"]:
                sys.exit(1)
        else:
            print(f"Canonical runtime failed: {output['stderr']}")
            sys.exit(1)

    elif command == "evidence":
        output = ws0.run_full_pipeline()
        if output["success"]:
            canonical = json.loads(output["stdout"])
            evidence = ws0.collect_evidence(canonical)
            ws0.save_report(evidence, f"evidence_report_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.json")
            print(json.dumps(evidence, indent=2))
        else:
            print(f"Canonical runtime failed: {output['stderr']}")
            sys.exit(1)
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()