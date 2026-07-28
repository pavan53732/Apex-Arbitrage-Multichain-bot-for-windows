
import pytest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from dashboard.test_dashboard import TestDashboard

def test_dashboard_initialization(tmp_path):
    dashboard_file = tmp_path / 'dashboard.json'
    dash = TestDashboard(dashboard_file)
    assert dash.dashboard_file == dashboard_file
    assert dash.data['last_run'] is None
