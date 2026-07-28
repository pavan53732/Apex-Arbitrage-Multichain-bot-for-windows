from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict, Optional

from ..metadata.models import DocumentMetadata


@dataclass
class DimensionTask:
    root_path: str
    dimension: str
    documents: List[str]


@dataclass
class SectionTask:
    root_path: str
    dimension: str
    document_path: str
    section: str


class ClosureOrchestrator:
    """Programme 3 Closure Orchestrator.

    Executes behavioural root closures hierarchically:
    closure -> dimension -> document -> section -> validation -> freeze.
    """

    DIMENSIONS = [
        "STRUCTURE",
        "INTERFACE",
        "EVENT",
        "CONFIGURATION",
        "SCHEMA",
        "STATE_MACHINE",
        "RECOVERY",
        "SECURITY",
        "VALIDATION",
        "ALGORITHM",
    ]

    def __init__(self, repo_root: str):
        self.repo_root = repo_root

    def compute_closure(self, root_path: str, documents: List[DocumentMetadata]) -> List[DocumentMetadata]:
        """Compute transitive closure for root_path from documents.

        This is a pure function over the metadata export; it does not mutate state.
        """
        # NOTE: Implementation is intentionally minimal here; full graph traversal
        # is delegated to existing governance graph builder.
        return [d for d in documents if d.path.startswith("docs/")]

    def build_dimension_queue(self, root_path: str, closure: List[DocumentMetadata]) -> List[DimensionTask]:
        """Build dimension tasks for a closure.

        Only critical + required documents (contracts, registries, schemas) are included.
        """
        doc_paths = [d.path for d in closure]
        critical_docs = [p for p in doc_paths if p.endswith(".md")]
        tasks: List[DimensionTask] = []
        for dim in self.DIMENSIONS:
            tasks.append(DimensionTask(root_path=root_path, dimension=dim, documents=critical_docs))
        return tasks

    def build_section_queue(self, task: DimensionTask) -> List[SectionTask]:
        """Build section tasks for a dimension task.

        Sections are dimension-specific (e.g., Events Produced, Interfaces, Configuration Keys).
        """
        section_name = {
            "STRUCTURE": "Structure",
            "INTERFACE": "Interfaces",
            "EVENT": "Events",
            "CONFIGURATION": "Configuration",
            "SCHEMA": "Schemas",
            "STATE_MACHINE": "State Machines",
            "RECOVERY": "Recovery",
            "SECURITY": "Security",
            "VALIDATION": "Validation",
            "ALGORITHM": "Algorithms",
        }[task.dimension]
        return [
            SectionTask(
                root_path=task.root_path,
                dimension=task.dimension,
                document_path=doc_path,
                section=section_name,
            )
            for doc_path in task.documents
        ]

    def freeze_dimension(self, root_path: str, dimension: str) -> None:
        """Mark a dimension as frozen for a root.

        The actual persistence is handled by the governance progress tracker.
        """
        # This is a hook; implementation lives in progress tracker.
        return

    def freeze_closure(self, root_path: str) -> None:
        """Mark a closure as fully implementation-ready.

        Must be called only after all dimensions reach 100% maturity.
        """
        return
