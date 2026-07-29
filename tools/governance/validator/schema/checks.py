"""SCHEMA-001, SCHEMA-002: schema-contract validators.

SCHEMA-001: every JSON schema file under `schemas/` (per
`config.schemas_glob`) must be syntactically valid JSON and must itself
be a JSON Schema object (has a `$schema` or `type` key) -- catches a
corrupted or placeholder-only schema file before it's relied on
elsewhere.

SCHEMA-002: every `schemas` reference a document declares (its
`## Schemas` section) should name a schema file that actually exists
under `schemas/`, cross-checked by filename stem (case-insensitive,
`.schema.json` suffix optional in the document's reference text) so
documents can refer to schemas either as `event` or
`event.schema.json` without a false-positive mismatch.
"""
from __future__ import annotations

import json
from pathlib import Path

import networkx as nx

from ...metadata.models import DocumentMetadata
from ..base import CategoryFinding

CATEGORY = "schema"


def _normalise_schema_name(name: str) -> str:
    n = name.strip().strip("`").lower()
    for suffix in (".schema.json", ".json"):
        if n.endswith(suffix):
            n = n[: -len(suffix)]
    return n


def run(
    docs: list[DocumentMetadata],
    graph: nx.DiGraph,
    schemas_dir: Path | None = None,
) -> list[CategoryFinding]:
    findings: list[CategoryFinding] = []
    schema_files: list[Path] = []
    if schemas_dir is not None and schemas_dir.exists():
        schema_files = sorted(schemas_dir.glob("*.json"))

    known_schema_stems = {_normalise_schema_name(p.name) for p in schema_files}

    # SCHEMA-001: every schema file is valid JSON and looks like a schema.
    for p in schema_files:
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as exc:
            findings.append(CategoryFinding(
                validator_id="SCHEMA-001",
                path=str(p),
                severity="HIGH",
                message=f"Schema file is not valid JSON: {exc}",
                rule="SCHEMA_VALID_JSON",
            ))
            continue
        if not isinstance(data, dict) or ("$schema" not in data and "type" not in data):
            findings.append(CategoryFinding(
                validator_id="SCHEMA-001",
                path=str(p),
                severity="MEDIUM",
                message="Schema file does not look like a JSON Schema object (missing $schema/type key)",
                rule="SCHEMA_WELL_FORMED",
            ))

    # SCHEMA-002: every document-declared schema reference resolves to
    # a real schema file, IF any schema files exist at all. If no
    # schemas_dir was supplied, this check is skipped rather than
    # flagging every reference as broken (there is nothing to resolve
    # against).
    if schemas_dir is not None:
        for d in docs:
            for sc in d.schemas:
                if _normalise_schema_name(sc) not in known_schema_stems:
                    findings.append(CategoryFinding(
                        validator_id="SCHEMA-002",
                        path=d.path,
                        severity="MEDIUM",
                        message=f"References schema '{sc}' which does not match any file under schemas/",
                        rule="SCHEMA_REFERENCE_RESOLVES",
                    ))
    return findings
