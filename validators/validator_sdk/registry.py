"""
Registry loading utilities for Concept, Document, and Traceability registries.
"""

from __future__ import annotations
import re
from pathlib import Path
from typing import Any
from dataclasses import dataclass, field


@dataclass
class ConceptEntry:
    concept_id: str
    status: str
    canonical_concept_id: str | None
    canonical_document: str | None
    description: str
    domain: str
    plane: str
    superseded_by: list[str] = field(default_factory=list)
    supersedes: list[str] = field(default_factory=list)


@dataclass
class DocumentEntry:
    doc_id: str
    path: str
    title: str
    plane: str
    domain: str
    class_: str
    authority: str
    status: str
    owner: str
    version: str
    concept_role: str
    canonical_source: str
    related_concepts: list[str]
    dependencies: list[str]
    consumers: list[str]
    supersedes: list[str]
    superseded_by: list[str]


@dataclass
class TraceabilityEntry:
    trace_id: str
    source_id: str
    relationship: str
    target_id: str
    status: str
    notes: str


class RegistryLoader:
    """Single source for loading all three registries."""

    @staticmethod
    def load_concept_registry(repo_root: Path) -> dict[str, ConceptEntry]:
        """Load Concept Registry and return dict keyed by concept_id."""
        registry_path = repo_root / "docs" / "repository-operating-model" / "registries" / "CONCEPT-REGISTRY.md"
        if not registry_path.exists():
            return {}

        content = registry_path.read_text(encoding="utf-8")
        return RegistryLoader._parse_concept_registry(content)

    @staticmethod
    def _parse_concept_registry(content: str) -> dict[str, ConceptEntry]:
        """Parse the markdown table in Concept Registry."""
        entries = {}

        # Find the table section
        lines = content.split("\n")
        in_table = False
        headers = []

        for line in lines:
            if line.startswith("| Concept ID |"):
                in_table = True
                headers = [h.strip() for h in line.split("|")[1:-1]]
                continue

            if in_table and line.startswith("|") and set(line.replace("|", "").replace(":", "").strip()) <= {"-", " "}:
                # Markdown table separator rows may contain whitespace around dashes.
                continue

            if in_table and line.startswith("|"):
                if not line.strip().startswith("| Concept ID"):
                    parts = [p.strip() for p in line.split("|")[1:-1]]
                    if len(parts) >= 12:
                        try:
                            # Registry schema v1.1 stores the concept name at column
                            # 3 and the canonical owner at columns 4–6.
                            entry = ConceptEntry(
                                concept_id=parts[0],
                                status=parts[9],
                                canonical_concept_id=parts[4] or None,
                                canonical_document=parts[5] or None,
                                description=parts[3],
                                domain=parts[8],
                                plane=parts[7],
                            )
                            entries[entry.concept_id] = entry
                        except (IndexError, ValueError):
                            continue
                continue

            if in_table and not line.startswith("|"):
                break

        return entries

    @staticmethod
    def load_document_registry(repo_root: Path) -> dict[str, DocumentEntry]:
        """Load Document Registry and return dict keyed by doc_id."""
        registry_path = repo_root / "docs" / "repository-operating-model" / "registries" / "DOCUMENT-REGISTRY.md"
        if not registry_path.exists():
            return {}

        content = registry_path.read_text(encoding="utf-8")
        return RegistryLoader._parse_document_registry(content)

    @staticmethod
    def _parse_document_registry(content: str) -> dict[str, DocumentEntry]:
        """Parse the markdown table in Document Registry."""
        entries = {}

        lines = content.split("\n")
        in_table = False

        for line in lines:
            if line.startswith("| Document ID |"):
                in_table = True
                continue

            if in_table and line.startswith("|") and set(line.replace("|", "").replace(":", "").strip()) <= {"-", " "}:
                # Markdown table separator rows may contain whitespace around dashes.
                continue

            if in_table and line.startswith("|"):
                if not line.strip().startswith("| Document ID"):
                    parts = [p.strip() for p in line.split("|")[1:-1]]
                    if len(parts) >= 17:
                        try:
                            entry = DocumentEntry(
                                doc_id=parts[0],
                                path=parts[1],
                                title=parts[2],
                                plane=parts[3],
                                domain=parts[4],
                                class_=parts[5],
                                authority=parts[6],
                                status=parts[7],
                                owner=parts[8],
                                version=parts[9],
                                concept_role=parts[10],
                                canonical_source=parts[11],
                                related_concepts=parts[12].split(",") if parts[12] else [],
                                dependencies=parts[13].split(",") if parts[13] else [],
                                consumers=parts[14].split(",") if parts[14] else [],
                                supersedes=parts[15].split(",") if parts[15] else [],
                                superseded_by=parts[16].split(",") if parts[16] else [],
                            )
                            entries[entry.doc_id] = entry
                        except Exception:
                            pass
                continue

            if in_table and not line.startswith("|"):
                break

        return entries

    @staticmethod
    def load_traceability_registry(repo_root: Path) -> dict[str, TraceabilityEntry]:
        """Load Traceability Registry and return dict keyed by trace_id."""
        registry_path = repo_root / "docs" / "repository-operating-model" / "registries" / "TRACEABILITY-REGISTRY.md"
        if not registry_path.exists():
            return {}

        content = registry_path.read_text(encoding="utf-8")
        return RegistryLoader._parse_traceability_registry(content)

    @staticmethod
    def _parse_traceability_registry(content: str) -> dict[str, TraceabilityEntry]:
        """Parse the markdown table in Traceability Registry."""
        entries = {}

        lines = content.split("\n")
        in_table = False

        for line in lines:
            if line.startswith("| Traceability ID |"):
                in_table = True
                continue

            if in_table and line.startswith("|") and set(line.replace("|", "").replace(":", "").strip()) <= {"-", " "}:
                # Markdown table separator rows may contain whitespace around dashes.
                continue

            if in_table and line.startswith("|"):
                if not line.strip().startswith("| Traceability ID"):
                    parts = [p.strip() for p in line.split("|")[1:-1]]
                    if len(parts) >= 6:
                        try:
                            entry = TraceabilityEntry(
                                trace_id=parts[0],
                                source_id=parts[1],
                                relationship=parts[2],
                                target_id=parts[3],
                                status=parts[4],
                                notes=parts[5],
                            )
                            entries[entry.trace_id] = entry
                        except Exception:
                            pass
                continue

            if in_table and not line.startswith("|"):
                break

        return entries

    @staticmethod
    def load_all(repo_root: Path) -> tuple[dict, dict, dict]:
        """Load all three registries at once."""
        concept = RegistryLoader.load_concept_registry(repo_root)
        document = RegistryLoader.load_document_registry(repo_root)
        traceability = RegistryLoader.load_traceability_registry(repo_root)
        return concept, document, traceability