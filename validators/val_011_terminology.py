"""
VAL-011: Terminology Validator
Detects inconsistent term usage using the repository glossary.
"""

from __future__ import annotations
from pathlib import Path
from collections import defaultdict
from validator_sdk import (
    BaseValidator, ValidationContext, ValidationWarning,
    ErrorCode, format_error, MetadataParser,
)


class Validator(BaseValidator):
    VALIDATOR_ID = "VAL-011"
    NAME = "Terminology Validator"
    VERSION = "1.0.0"
    DESCRIPTION = "Detects inconsistent term usage across documents using the glossary"
    CATEGORY = "terminology"
    SEVERITY = "WARNING"
    SUPPORTED_METADATA_SCHEMA_VERSIONS = ["1.0"]
    SUPPORTED_REPOSITORY_SPEC_VERSIONS = ["1.0"]

    def validate(self, context: ValidationContext) -> ValidationResult:
        self._start_timer()
        warnings = []
        checked = 0

        glossary = self._load_glossary(context.repository_root)
        if not glossary:
            warnings.append(ValidationWarning(
                code="GLOSSARY_MISSING",
                file="docs/apex-repository-docs/registries/GLOSSARY.md", line=1,
                message="Glossary not found. Terminology validation limited.",
                severity="WARNING",
                rule="Glossary required for term validation.",
                suggestion="Create GLOSSARY.md.",
            ))
            return self._result_pass(0, warnings)

        for md_file in context.all_markdown_files:
            checked += 1
            rel_path = md_file.relative_to(context.repository_root)
            rel_str = str(rel_path).replace("\\", "/")

            metadata, body = MetadataParser.parse(md_file)
            if not metadata:
                continue

            doc_id = metadata.get("document_id", "unknown")
            body_lower = body.lower()
            found = [t for t, info in glossary.items() if t in body_lower]

            for i, t1 in enumerate(found):
                ti1 = glossary[t1]
                for t2 in found[i+1:]:
                    ti2 = glossary[t2]
                    s1 = set(ti1["lower"].split())
                    s2 = set(ti2["lower"].split())
                    shared = s1 & s2
                    if shared and ti1["domain"] != ti2["domain"]:
                        warnings.append(ValidationWarning(
                            code="POTENTIAL_TERM_CONFLICT",
                            file=rel_str, line=1,
                            message=f"Doc {doc_id}: '{ti1['term']}' ({ti1['domain']}) and '{ti2['term']}' ({ti2['domain']}) share words: {', '.join(sorted(shared))}",
                            severity="WARNING",
                            rule="Shared root words between different glossary terms in one doc may indicate inconsistency.",
                            suggestion=f"Verify usage of '{ti1['term']}' and '{ti2['term']}' per glossary.",
                        ))

        return self._result_pass(checked, warnings)

    def _load_glossary(self, repo_root: Path) -> dict:
        gp = repo_root / "docs" / "apex-repository-docs" / "registries" / "GLOSSARY.md"
        if not gp.exists():
            return {}
        content = gp.read_text(encoding="utf-8")
        entries = {}
        for line in content.split("\n"):
            if line.startswith("| TERM-"):
                parts = [p.strip() for p in line.split("|")[1:-1]]
                if len(parts) >= 7:
                    entries[parts[1].lower()] = {
                        "term_id": parts[0], "term": parts[1],
                        "definition": parts[2],
                        "concept_id": parts[3] if parts[3] != "\u2014" else None,
                        "domain": parts[4],
                        "related": parts[5].split(",") if parts[5] else [],
                        "lower": parts[1].lower(),
                    }
        return entries
