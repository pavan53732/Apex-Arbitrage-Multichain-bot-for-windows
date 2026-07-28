from __future__ import annotations
from ..metadata.models import DocumentMetadata

class CompletenessEngine:
    SECTIONS = ["purpose", "scope", "responsibilities", "owns", "does_not_own", "inputs", "outputs", "interfaces", "events_produced", "events_consumed", "configuration", "schemas", "state_machines", "security", "recovery", "failure_behaviour", "performance", "validation", "testing", "cross_references", "version_history", "canonical_source"]

    def score_document(self, meta: DocumentMetadata) -> float:
        present = 0
        total = len(self.SECTIONS)
        for s in self.SECTIONS:
            val = getattr(meta, s, None)
            if val is None:
                continue
            if isinstance(val, str) and val.strip():
                present += 1
            elif isinstance(val, list) and val:
                present += 1
        return present / total if total else 0.0
