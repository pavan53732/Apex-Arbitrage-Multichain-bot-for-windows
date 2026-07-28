
import pytest
from pathlib import Path
import sys
import json
sys.path.insert(0, str(Path(__file__).parent.parent))
from comparator.golden_comparator import GoldenOutputComparator

def test_compare_pass(tmp_path):
    golden = tmp_path / 'golden'
    actual = tmp_path / 'actual'
    golden.mkdir()
    actual.mkdir()
    data = {'key': 'value'}
    (golden / 'test.json').write_text(json.dumps(data))
    (actual / 'test.json').write_text(json.dumps(data))
    comp = GoldenOutputComparator(golden, actual)
    result = comp.compare('test.json')
    assert result['status'] == 'PASS'
