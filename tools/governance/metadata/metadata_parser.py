from __future__ import annotations
from .models import DocumentMetadata
from ..parser.section_parser import SectionParser

class MetadataParser:
    REQUIRED_FIELDS = ["type", "owner", "status", "version"]

    def parse_document(self, text: str, path: str) -> DocumentMetadata:
        front = SectionParser.extract_front_matter(text) or {}
        meta = DocumentMetadata(path=path, raw_text=text, **front)
        return meta

    def validate_required(self, meta: DocumentMetadata) -> list[str]:
        missing = []
        for f in self.REQUIRED_FIELDS:
            if getattr(meta, f, None) in (None, ""):
                missing.append(f)
        return missing
