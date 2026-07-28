from governance.parser.section_parser import SectionParser
from governance.metadata.metadata_parser import MetadataParser

def test_front_matter_extraction():
    text = """---
type: CONTRACT
owner: docs/EXECUTION-ENGINE.md
status: STABLE
version: 1.0.0
---

# Execution Engine
"""
    fm = SectionParser.extract_front_matter(text)
    assert fm["type"] == "CONTRACT"
    assert fm["owner"] == "docs/EXECUTION-ENGINE.md"

def test_metadata_parser():
    text = """---
type: SPECIFICATION
owner: docs/AI-PIPELINE.md
status: DRAFT
version: 0.9.0
---

# AI Pipeline
"""
    parser = MetadataParser()
    meta = parser.parse_document(text, "docs/AI-PIPELINE.md")
    assert meta.type == "SPECIFICATION"
    assert meta.owner == "docs/AI-PIPELINE.md"
