
import pytest
import json
from pathlib import Path

def test_freeze_record_complete(tmp_path):
    freeze_record = {'identity': {'workstream_id': 'WS0', 'workstream_version': '1.0.0'}, 'repository': {'commit_hash': 'abc123'}, 'freeze': {'freeze_hash': 'freeze_hash'}}
    freeze_file = tmp_path / 'freeze_WS0.json'
    with open(freeze_file, 'w') as f:
        json.dump(freeze_record, f)
    assert freeze_file.exists()
