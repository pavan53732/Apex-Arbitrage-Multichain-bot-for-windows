from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class RepairTask:
    root_path: str
    dimension: str
    document_path: str
    section: str
    finding_category: str
    acceptance_criteria: List[str]
    validator_ids: List[str]
    status: str = "PENDING"


class RepairPlanner:
    """Programme 3 Repair Planner.

    Maps validator findings to deterministic repair tasks for closure dimensions.
    """

    def __init__(self, repo_root: str):
        self.repo_root = repo_root

    def plan_repairs(self, root_path: str, dimension: str, findings: List[dict]) -> List[RepairTask]:
        """Plan repair tasks from validator findings.

        Each finding is mapped to a canonical owner document and section.
        """
        tasks: List[RepairTask] = []
        for f in findings:
            doc_path = f.get("document_path")
            category = f.get("category")
            section = f.get("section") or self._default_section_for_dimension(dimension)
            acceptance = self._acceptance_for_dimension(dimension, category)
            validators = f.get("validators", [])
            tasks.append(
                RepairTask(
                    root_path=root_path,
                    dimension=dimension,
                    document_path=doc_path,
                    section=section,
                    finding_category=category,
                    acceptance_criteria=acceptance,
                    validator_ids=validators,
                )
            )
        return tasks

    def _default_section_for_dimension(self, dimension: str) -> str:
        return {
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
        }[dimension]

    def _acceptance_for_dimension(self, dimension: str, category: str) -> List[str]:
        """Return acceptance criteria checklist for a dimension/category.
        """
        if dimension == "EVENT":
            return [
                "Producer defined",
                "Consumer(s) defined",
                "Payload schema defined",
                "Ordering specified",
                "Delivery semantics defined",
                "Retry policy defined",
                "Dead-letter handling defined",
                "Version compatibility defined",
                "Ownership documented",
            ]
        if dimension == "INTERFACE":
            return [
                "Ownership documented",
                "Responsibilities documented",
                "Inputs defined",
                "Outputs defined",
                "Message format defined",
                "Error behaviour defined",
                "Versioning strategy defined",
                "Compatibility documented",
                "Lifecycle documented",
                "Implementation boundary documented",
            ]
        # Other dimensions can be extended similarly.
        return []
