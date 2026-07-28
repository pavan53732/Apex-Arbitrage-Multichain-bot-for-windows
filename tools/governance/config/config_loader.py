from __future__ import annotations
import yaml
from pathlib import Path

def load_config(config_path: str) -> dict:
    p = Path(config_path)
    if not p.is_absolute():
        p = Path(__file__).parent.parent.parent.parent / p
    with p.open(encoding="utf-8") as f:
        return yaml.safe_load(f)
