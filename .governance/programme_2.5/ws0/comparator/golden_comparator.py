
from pathlib import Path
import json
import hashlib

class GoldenOutputComparator:
    def __init__(self, golden_dir: Path, actual_dir: Path):
        self.golden_dir = golden_dir
        self.actual_dir = actual_dir

    def compare(self, filename: str) -> dict:
        golden_path = self.golden_dir / filename
        actual_path = self.actual_dir / filename

        if not golden_path.exists():
            return {"file": filename, "status": "MISSING_GOLDEN", "diff": None}
        if not actual_path.exists():
            return {"file": filename, "status": "MISSING_ACTUAL", "diff": None}

        with open(golden_path, "r", encoding="utf-8") as f:
            golden = json.load(f)
        with open(actual_path, "r", encoding="utf-8") as f:
            actual = json.load(f)

        # Compare (excluding timestamps, hashes, execution duration)
        diff = self._diff(golden, actual)
        status = "PASS" if not diff else "FAIL"

        return {"file": filename, "status": status, "diff": diff}

    def _diff(self, golden: dict, actual: dict, path: str = "") -> list:
        diffs = []
        for key in set(golden.keys()) | set(actual.keys()):
            if key in ["timestamp", "execution_time", "hash", "salt"]:
                continue  # Ignore non-deterministic fields
            if key not in golden:
                diffs.append(f"{path}.{key}: MISSING_IN_GOLDEN")
            elif key not in actual:
                diffs.append(f"{path}.{key}: MISSING_IN_ACTUAL")
            elif golden[key] != actual[key]:
                diffs.append(f"{path}.{key}: {golden[key]} != {actual[key]}")
        return diffs
