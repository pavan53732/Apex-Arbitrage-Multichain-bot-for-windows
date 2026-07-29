"""
Programme 2.5 Governance Reconciliation Tool.

Regenerates WS1-WS9 manifest.json files from LIVE evidence produced by
verify_workstreams.py, replacing the stale hand-written "PENDING" manifests
that were never updated since programme inception (2026-07-28T22:18:54Z).

This tool does NOT declare any workstream COMPLETE. It reports the
factual state -- NOT_STARTED / PARTIALLY_IMPLEMENTED / IMPLEMENTED --
computed strictly from the pass/fail checklist evidence, so the
manifests can never again silently drift from reality.

Usage: run from repo root with `governance` package installed:
    python .governance/programme_2.5/_reconciliation/generate_manifests.py
"""
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "tools" / "governance"))

VERIFY_SCRIPT = Path(__file__).resolve().parent / "verify_workstreams.py"

WS_NAMES = {
    "WS1": "Root Detection Engine",
    "WS2": "Closure Engine",
    "WS3": "Validator Framework",
    "WS4": "Knowledge Graph",
    "WS5": "Database Consolidation",
    "WS6": "Freeze Framework",
    "WS7": "Evidence System",
    "WS8": "Metrics Engine",
    "WS9": "Integrity Engine",
}


def get_commit_hash() -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=REPO, capture_output=True, text=True
    )
    return result.stdout.strip()


def classify(items: list[dict]) -> str:
    statuses = [i["status"] for i in items if i["status"] in ("PASS", "FAIL")]
    passed = sum(1 for s in statuses if s == "PASS")
    total = len(statuses)
    if total == 0:
        return "NOT_STARTED"
    if passed == 0:
        return "NOT_STARTED"
    if passed == total:
        return "IMPLEMENTED"
    return "PARTIALLY_IMPLEMENTED"


def main():
    proc = subprocess.run(
        [sys.executable, str(VERIFY_SCRIPT), str(REPO)],
        capture_output=True, text=True,
    )
    if proc.returncode != 0:
        print("verify_workstreams.py failed:", proc.stderr, file=sys.stderr)
        sys.exit(1)
    results = json.loads(proc.stdout)

    commit = get_commit_hash()
    now = datetime.now(timezone.utc).isoformat()

    for ws_id, items in results.items():
        status = classify(items)
        passed = sum(1 for i in items if i["status"] == "PASS")
        total = len([i for i in items if i["status"] in ("PASS", "FAIL")])
        manifest = {
            "workstream_id": ws_id,
            "name": WS_NAMES[ws_id],
            "status": status,
            "checklist_items_passing": f"{passed}/{total}",
            "checklist_evidence": items,
            "created_at": "2026-07-28T22:18:54.000000+00:00",
            "last_verified_at": now,
            "last_verified_commit": commit,
            "verification_method": "governance/programme_2.5/_reconciliation/verify_workstreams.py (live execution against installed `governance` package + direct source inspection; no field is asserted without a corresponding executed check)",
            "notes": [
                "This manifest replaces a stale hand-authored manifest that reported "
                "status=PENDING unconditionally from programme inception through "
                "commit 3b1240164, regardless of actual implementation progress made "
                "in prior remediation rounds. That was a governance self-description "
                "defect (repository's own governance metadata did not reflect actual "
                "implementation state) -- flagged as CRITICAL in the Programme 2.5 "
                "Final Certification Audit.",
                "PARTIALLY_IMPLEMENTED is not a passing grade. It means some checklist "
                "items are genuinely satisfied by live, executable code and some are "
                "not. See checklist_evidence for the itemized breakdown.",
                "This manifest is derived data. Re-run verify_workstreams.py + this "
                "script after any future change to tools/governance/ to keep it "
                "truthful; do not hand-edit the status field.",
            ],
        }
        out_path = REPO / ".governance" / "programme_2.5" / ws_id.lower() / "manifest.json"
        out_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        print(f"{ws_id}: {status} ({passed}/{total}) -> {out_path.relative_to(REPO)}")

    # Also emit a single rollup for convenience / evidence.
    ws_statuses = {ws_id: classify(items) for ws_id, items in results.items()}
    fully_implemented = [ws for ws, s in ws_statuses.items() if s == "IMPLEMENTED"]
    partial = [ws for ws, s in ws_statuses.items() if s == "PARTIALLY_IMPLEMENTED"]
    not_started = [ws for ws, s in ws_statuses.items() if s == "NOT_STARTED"]
    if not partial and not not_started:
        overall_status_message = f"ALL {len(ws_statuses)} WORKSTREAMS IMPLEMENTED -- every checkable readiness-checklist item passes as of this run"
    else:
        overall_status_message = (
            f"NOT_COMPLETE -- {len(fully_implemented)}/{len(ws_statuses)} workstreams fully IMPLEMENTED "
            f"({', '.join(sorted(fully_implemented)) if fully_implemented else 'none'}); "
            f"remaining gaps in {', '.join(sorted(partial + not_started))} -- see each workstream's "
            f"manifest.json checklist_evidence for the itemized, disclosed reasons"
        )
    rollup = {
        "programme": "PROGRAMME_2.5",
        "generated_at": now,
        "generated_at_commit": commit,
        "workstreams": {
            ws_id: {
                "status": classify(items),
                "passing": sum(1 for i in items if i["status"] == "PASS"),
                "total": len([i for i in items if i["status"] in ("PASS", "FAIL")]),
            }
            for ws_id, items in results.items()
        },
        "overall_programme_status": overall_status_message,
    }
    rollup_path = REPO / ".governance" / "programme_2.5" / "WORKSTREAM-STATUS-ROLLUP.json"
    rollup_path.write_text(json.dumps(rollup, indent=2) + "\n", encoding="utf-8")
    print(f"Rollup -> {rollup_path.relative_to(REPO)}")


if __name__ == "__main__":
    main()
