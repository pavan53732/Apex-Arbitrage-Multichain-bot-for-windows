from __future__ import annotations
import json
from pathlib import Path
from typing import Iterable
from ..metadata.models import DocumentMetadata

def export_documents_json(docs: Iterable[DocumentMetadata], export_path: str):
    p = Path(export_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    data = [d.model_dump() for d in docs]
    p.write_text(json.dumps(data, indent=2), encoding="utf-8")
