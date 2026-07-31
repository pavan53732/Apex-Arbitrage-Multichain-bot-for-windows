"""
VAL-008: Traceability Validator
Verifies traceability relationships form valid chains.
"""

from __future__ import annotations
from pathlib import Path
from collections import defaultdict
from validator_sdk import (
    BaseValidator,
    ValidationContext,
    ValidationError,
    ValidationWarning,
    ErrorCode,
    format_error,
)


class Validator(BaseValidator):
    VALIDATOR_ID = "VAL-008"
    NAME = "Traceability Validator"
    VERSION = "1.0.0"
    DESCRIPTION = "Verifies traceability relationships form valid chains"
    CATEGORY = "traceability"
    SEVERITY = "ERROR"
    SUPPORTED_METADATA_SCHEMA_VERSIONS = ["1.0"]
    SUPPORTED_REPOSITORY_SPEC_VERSIONS = ["1.0"]

    # Valid relationship types from Validation Specification
    VALID_RELATIONSHIPS = {
        "Defines", "Consumes", "Produces", "Related",
        "ValidatedBy", "TestedBy", "DependsOn",
        "Supersedes", "DerivedFrom", "Indexes", "References"
    }

    def validate(self, context: ValidationContext) -> ValidationError:
        self._start_timer()
        errors = []
        warnings = []
        checked = 0

        traceability_registry = context.traceability_registry
        document_registry = context.document_registry
        concept_registry = context.concept_registry

        # Build adjacency for DependsOn cycle detection
        depends_on_graph = defaultdict(set)
        all_ids = set(document_registry.keys()) | set(concept_registry.keys())

        # 1. Validate each traceability relationship
        for trace_id, trace in traceability_registry.items():
            checked += 1

            # Check source and target IDs resolve
            source_ok = trace.source_id in all_ids
            target_ok = trace.target_id in all_ids

            if not source_ok:
                errors.append(ValidationError(
                    code=ErrorCode.TRACEABILITY_ID_UNRESOLVED,
                    file="",
                    line=1,
                    message=format_error(ErrorCode.TRACEABILITY_ID_UNRESOLVED, trace_id=trace_id, source_id=trace.source_id, target_id=trace.target_id),
                    severity="ERROR",
                    rule="Traceability source must be valid DOC-ID or CONCEPT-ID",
                    suggestion=f"Fix source ID in {trace_id}"
                ))

            if not target_ok:
                errors.append(ValidationError(
                    code=ErrorCode.TRACEABILITY_ID_UNRESOLVED,
                    file="",
                    line=1,
                    message=format_error(ErrorCode.TRACEABILITY_ID_UNRESOLVED, trace_id=trace_id, source_id=trace.source_id, target_id=trace.target_id),
                    severity="ERROR",
                    rule="Traceability target must be valid DOC-ID or CONCEPT-ID",
                    suggestion=f"Fix target ID in {trace_id}"
                ))

            # Check relationship type
            if trace.relationship not in self.VALID_RELATIONSHIPS:
                errors.append(ValidationError(
                    code=ErrorCode.INVALID_RELATIONSHIP_TYPE,
                    file="",
                    line=1,
                    message=format_error(ErrorCode.INVALID_RELATIONSHIP_TYPE, trace_id=trace_id, type=trace.relationship),
                    severity="ERROR",
                    rule=f"Relationship must be one of: {', '.join(sorted(self.VALID_RELATIONSHIPS))}",
                    suggestion=f"Change relationship to valid type"
                ))

            # Build DependsOn graph for cycle detection
            if trace.relationship == "DependsOn" and source_ok and target_ok:
                depends_on_graph[trace.source_id].add(trace.target_id)

        # 2. Check for circular DependsOn chains
        cycles = self._find_cycles(depends_on_graph)
        for cycle in cycles:
            checked += 1
            errors.append(ValidationError(
                code=ErrorCode.CIRCULAR_DEPENDS_ON,
                file="",
                line=1,
                message=format_error(ErrorCode.CIRCULAR_DEPENDS_ON, concepts=" -> ".join(cycle)),
                severity="ERROR",
                rule="DependsOn relationships must not form cycles",
                suggestion="Break the cycle by removing or reversing a DependsOn relationship"
            ))

        # 3. Check untraced requirements (Concepts with no incoming traceability)
        # Requirements = concepts that should have implementations
        # This is a warning per spec
        traced_targets = set()
        for trace in traceability_registry.values():
            if trace.target_id in concept_registry:
                traced_targets.add(trace.target_id)

        # Concepts that are "requirement-like" (Specifications, Policies) should be traced
        for concept_id, concept in concept_registry.items():
            if concept.status == "Active" and concept.domain != "Registries":
                # Check if any document with concept_role: Owner traces to this
                has_trace = concept_id in traced_targets
                if not has_trace:
                    checked += 1
                    warnings.append(ValidationWarning(
                        code=ErrorCode.UNTRACED_REQUIREMENT,
                        file="",
                        line=1,
                        message=f"Active concept {concept_id} has no incoming traceability relationships",
                        severity="WARNING",
                        rule="Requirements should be traced to implementations",
                        suggestion=f"Add traceability from implementation to {concept_id}"
                    ))

        # 4. Check validators are traced to documents (from previous_results)
        # This is informational - validators should trace to what they validate

        if errors:
            return self._result_fail(checked, errors)
        return self._result_pass(checked, warnings)

    def _find_cycles(self, graph: dict[str, set[str]]) -> list[list[str]]:
        """Find all cycles in directed graph using DFS."""
        visited = set()
        rec_stack = set()
        cycles = []
        path = []

        def dfs(node: str):
            visited.add(node)
            rec_stack.add(node)
            path.append(node)

            for neighbor in graph.get(node, set()):
                if neighbor not in visited:
                    dfs(neighbor)
                elif neighbor in rec_stack:
                    # Found cycle
                    cycle_start = path.index(neighbor)
                    cycles.append(path[cycle_start:] + [neighbor])

            rec_stack.remove(node)
            path.pop()

        for node in graph:
            if node not in visited:
                dfs(node)

        return cycles