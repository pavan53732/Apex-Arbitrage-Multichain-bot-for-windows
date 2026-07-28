
import pytest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from loader.fixture_loader import RepositoryFixtureLoader

def test_loader_initialization(tmp_path):
    loader = RepositoryFixtureLoader(tmp_path)
    assert loader.fixtures_dir == tmp_path
    assert len(loader.fixtures) == 10

def test_load_fixture_minimal(tmp_path):
    fixture_path = tmp_path / 'minimal_valid'
    fixture_path.mkdir(parents=True)
    (fixture_path / 'test.md').write_text('---\ntype: CONTRACT\n---\n\nBEHAVIOURAL')
    loader = RepositoryFixtureLoader(tmp_path)
    result = loader.load_fixture('minimal_valid')
    assert result.name == 'minimal_valid'
    assert result.actual_docs == 1
    assert result.actual_roots == 1

def test_run_all_fixtures(tmp_path):
    loader = RepositoryFixtureLoader(tmp_path)
    results = loader.run_all_fixtures()
    assert len(results) == 10
