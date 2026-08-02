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


# Structural words that carry no distinguishing meaning on their own. Two
# compound terms sharing only one of these are not in conflict: the repository
# deliberately names several components "... Engine", and that consistency is a
# feature of the vocabulary rather than an ambiguity in it.
GENERIC_HEAD_NOUNS = {
    "engine", "manager", "service", "system", "layer", "module",
    "component", "registry", "model", "policy", "contract", "pipeline",
    "matrix", "index", "map", "pool", "gateway", "adapter", "provider",
}


class Validator(BaseValidator):
    VALIDATOR_ID = "VAL-011"
    NAME = "Terminology Validator"
    VERSION = "1.1.0"
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
                    # A shared head noun is ordinary compound vocabulary, not a
                    # collision: "Trading Engine" and "Routing Engine" are
                    # distinct terms that both happen to be engines. Genuine
                    # ambiguity requires one term to be a complete phrase within
                    # the other, so that a reader cannot tell which is meant.
                    shared = (s1 & s2) - GENERIC_HEAD_NOUNS
                    if not shared:
                        continue
                    if not (s1 < s2 or s2 < s1):
                        continue
                    if ti1["domain"] != ti2["domain"]:
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
                # The glossary table defines six columns: Term ID, Term,
                # Canonical Definition, Concept ID, Domain, Related Terms.
                # Only indices 0-5 are read below, so six is the true minimum.
                if len(parts) >= 6:
                    entries[parts[1].lower()] = {
                        "term_id": parts[0], "term": parts[1],
                        "definition": parts[2],
                        "concept_id": parts[3] if parts[3] != "\u2014" else None,
                        "domain": parts[4],
                        "related": parts[5].split(",") if parts[5] else [],
                        "lower": parts[1].lower(),
                    }
        return entries
