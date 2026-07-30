"""Schema reference scanner (Programme 2.5 Phase-0, WS4 Knowledge Graph
-- closing the schema_graph data-completeness gap).

`schema_graph` was confirmed genuinely empty (0 nodes / 0 edges)
because no document populates the `schemas` metadata field via the
`## Schemas` section pattern MetadataParser looks for. However, several
documents DO reference real schema files by literal path in their
PROSE TEXT (not in a structured metadata section) -- e.g.
`docs/PLUGIN-LIFECYCLE.md`: "Validate manifest schema against
schemas/plugin.schema.json."

This module extracts ONLY exact, literal `<name>.schema.json`
references that match a REAL file under `schemas/` byte-for-byte on
filename. It is deliberately conservative, per explicit instruction:
no fuzzy matching, no inferred aliases, no guessing at an intended
schema from a differently-named mention. A document that writes
"config.schema.json" (which does NOT exist -- only
`configuration.schema.json` does, confirmed in `docs/TESTING.md`) does
NOT match anything; it is recorded as an unresolved mention for
traceability/audit purposes, never silently coerced to the
similarly-named real file.

Every extracted reference retains full traceability back to its
source: the document path, the exact matched text, and the 1-indexed
line number it was found on -- so `apex-gov run`'s schema_graph output
can always be traced back to the specific document sentence that
justifies each edge.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

# Matches "<name>.schema.json", optionally preceded by a `schemas/` or
# `SCHEMAS/` directory prefix (either case, since the corpus uses both
# -- see docs/CONFIGURATION-REFERENCE.md's "SCHEMAS/configuration.schema.json"
# vs docs/PLUGIN-LIFECYCLE.md's lowercase "schemas/plugin.schema.json").
# The captured group is the bare filename only (directory prefix is not
# part of the identity match against real files, but no other path
# components are permitted, deliberately narrow).
_SCHEMA_REFERENCE_PATTERN = re.compile(
    r"(?:[Ss][Cc][Hh][Ee][Mm][Aa][Ss]/)?([A-Za-z0-9_-]+\.schema\.json)"
)


@dataclass(frozen=True)
class SchemaReference:
    document_path: str
    line_number: int
    matched_text: str
    schema_filename: str
    resolved: bool


def scan_document_for_schema_references(
    document_path: str, raw_text: str, known_schema_filenames: set[str]
) -> list[SchemaReference]:
    """Scan one document's raw text for literal schema file mentions.

    Args:
        document_path: the document's canonical path (for traceability).
        raw_text: the document's full raw markdown text.
        known_schema_filenames: the exact set of real filenames present
            under `schemas/` (e.g. {"plugin.schema.json", ...}) -- a
            reference resolves ONLY if its filename is byte-for-byte
            present in this set.

    Returns one `SchemaReference` per regex match found (including
    unresolved ones, so callers can audit near-misses like
    "config.schema.json" without silently dropping them), each carrying
    the exact matched text and line number for traceability.
    """
    results: list[SchemaReference] = []
    for line_number, line in enumerate(raw_text.splitlines(), start=1):
        for match in _SCHEMA_REFERENCE_PATTERN.finditer(line):
            filename = match.group(1)
            results.append(
                SchemaReference(
                    document_path=document_path,
                    line_number=line_number,
                    matched_text=match.group(0),
                    schema_filename=filename,
                    resolved=filename in known_schema_filenames,
                )
            )
    return results


def scan_corpus_for_schema_references(
    docs: list, schemas_dir: Path
) -> dict[str, list[SchemaReference]]:
    """Scan every document's raw_text for schema references.

    Args:
        docs: list of DocumentMetadata (must have .path and .raw_text).
        schemas_dir: path to the schemas/ directory.

    Returns a dict of document_path -> list[SchemaReference], including
    only documents that had at least one match (resolved or not).
    """
    known_filenames = (
        {p.name for p in schemas_dir.glob("*.schema.json")} if schemas_dir.exists() else set()
    )
    results: dict[str, list[SchemaReference]] = {}
    for doc in docs:
        refs = scan_document_for_schema_references(doc.path, getattr(doc, "raw_text", "") or "", known_filenames)
        if refs:
            results[doc.path] = refs
    return results


def build_schema_reference_report(scan_results: dict[str, list[SchemaReference]]) -> dict:
    """Build a full audit report: every reference found, resolved or
    not, with full source traceability -- for the
    schema_reference_report.json export."""
    all_refs = [ref for refs in scan_results.values() for ref in refs]
    resolved = [r for r in all_refs if r.resolved]
    unresolved = [r for r in all_refs if not r.resolved]
    return {
        "total_references_found": len(all_refs),
        "resolved_count": len(resolved),
        "unresolved_count": len(unresolved),
        "resolved_references": [
            {
                "document_path": r.document_path,
                "line_number": r.line_number,
                "matched_text": r.matched_text,
                "schema_filename": r.schema_filename,
            }
            for r in sorted(resolved, key=lambda r: (r.document_path, r.line_number))
        ],
        "unresolved_references": [
            {
                "document_path": r.document_path,
                "line_number": r.line_number,
                "matched_text": r.matched_text,
                "schema_filename": r.schema_filename,
                "reason": f"'{r.schema_filename}' does not exactly match any real file under schemas/",
            }
            for r in sorted(unresolved, key=lambda r: (r.document_path, r.line_number))
        ],
    }
