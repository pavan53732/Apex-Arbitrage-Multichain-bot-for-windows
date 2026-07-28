
import pytest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from generator.golden_generator import GoldenOutputGenerator

def test_generator_initialization(tmp_path):
    gen = GoldenOutputGenerator(tmp_path)
    assert gen.output_dir == tmp_path

def test_generate_root_registry(tmp_path):
    gen = GoldenOutputGenerator(tmp_path)
    hash_val = gen.generate_root_registry(['root1', 'root2'])
    assert len(hash_val) == 16
    assert (tmp_path / 'golden_root_registry.json').exists()
