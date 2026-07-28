from __future__ import annotations
from pathlib import Path
from ..metadata.models import DocumentMetadata
from ..parser.section_parser import SectionParser
import yaml

TIER_A_PATTERNS = ["*-ENGINE.md", "*-PIPELINE.md", "ORCHESTRATOR.md", "APEX-KERNEL.md", "EVENT-BUS.md", "SECURITY.md", "CONFIGURATION.md", "STATE-MANAGEMENT.md", "IPC-PROTOCOL.md", "RUNTIME-OPERATIONS.md", "TRADING-ENGINE.md", "EXECUTION-ENGINE.md", "RISK-ENGINE.md", "SIMULATION-ENGINE.md", "DECISION-ENGINE.md", "POLICY-ENGINE.md", "SERVICE-REGISTRY.md", "BOOTSTRAP-SEQUENCE.md"]

class Standardiser:
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root)

    def standardise_document(self, meta: DocumentMetadata) -> str:
        text = meta.raw_text
        front = SectionParser.extract_front_matter(text) or {}
        meta_dict = meta.model_dump()
        header_fields = ["type", "owner", "status", "version", "purpose", "scope"]
        fm = {k: meta_dict.get(k) for k in header_fields if meta_dict.get(k) not in (None, "")}
        fm["responsibilities"] = meta.responsibilities or []
        fm["owns"] = meta.owns or []
        fm["does_not_own"] = meta.does_not_own or []
        fm["depends_on"] = meta.depends_on or []
        fm["required_by"] = meta.required_by or []
        fm["interfaces"] = meta.interfaces or []
        fm["events_produced"] = meta.events_produced or []
        fm["events_consumed"] = meta.events_consumed or []
        fm["configuration"] = meta.configuration or []
        fm["schemas"] = meta.schemas or []
        fm["state_machines"] = meta.state_machines or []
        fm["security"] = meta.security or []
        fm["recovery"] = meta.recovery or []
        fm["failure_behaviour"] = meta.failure_behaviour or []
        fm["performance"] = meta.performance or []
        fm["validation"] = meta.validation or []
        fm["testing"] = meta.testing or []
        fm["cross_references"] = meta.cross_references or []
        fm["version_history"] = meta.version_history or []
        fm["canonical_source"] = meta.canonical_source

        header = "---\n" + yaml.dump(fm, sort_keys=False, allow_unicode=True) + "---\n\n"
        body = text
        if SectionParser.extract_front_matter(text):
            import re
            body = re.sub(r"^---\s*\n.*?\n---\s*\n", "", text, flags=re.DOTALL)
        return header + body
