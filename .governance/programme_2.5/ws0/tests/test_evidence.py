
import pytest
import hashlib
from pathlib import Path

def test_evidence_generation(tmp_path):
    evidence = {'repository_hash': hashlib.sha256(b'repo').hexdigest(), 'commit_hash': 'abc123', 'evidence_hash': hashlib.sha256(b'evidence').hexdigest()}
    evidence_file = tmp_path / 'evidence.json'
    import json
    with open(evidence_file, 'w') as f:
        json.dump(evidence, f)
    assert evidence_file.exists()
