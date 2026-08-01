"""
VAL-007: Document Class Validator
Verifies documents are assigned correct class and plane separation is maintained.
"""

from __future__ import annotations
from pathlib import Path
from validator_sdk import (
    BaseValidator,
    ValidationContext,
    ValidationError,
    ValidationWarning,
    ErrorCode,
    format_error,
    MetadataParser,
)


class Validator(BaseValidator):
    VALIDATOR_ID = "VAL-007"
    NAME = "Document Class Validator"
    VERSION = "1.0.0"
    DESCRIPTION = "Verifies documents are assigned correct class and plane separation is maintained"
    CATEGORY = "class"
    SEVERITY = "ERROR"
    SUPPORTED_METADATA_SCHEMA_VERSIONS = ["1.0"]
    SUPPORTED_REPOSITORY_SPEC_VERSIONS = ["1.0"]

    # Valid class per plane/domain rules
    ROM_DOMAINS = {
        "Agent System", "Governance", "Registries", "Standards",
        "Documentation Lifecycle", "Contribution", "Traceability",
        "Validation", "Workflows"
    }

    PS_DOMAINS = {
        "AI", "Architecture", "Runtime", "Execution", "Market",
        "Operations", "Interfaces", "Data", "Configuration",
        "Dashboard", "Deployment", "Security", "Testing",
        "Plugins", "Windows"
    }

    # Classes that are only valid in specific folders
    REGISTRY_CLASSES = {"Registry"}
    HISTORICAL_CLASSES = {"Historical"}
    ADR_CLASS = {"ADR"}
    GENERATED_CLASS = {"Generated"}

    def validate(self, context: ValidationContext) -> ValidationError:
        self._start_timer()
        errors = []
        warnings = []
        checked = 0

        for md_file in context.all_markdown_files:
            checked += 1
            rel_path = md_file.relative_to(context.repository_root)
            rel_str = str(rel_path).replace("\\", "/")

            metadata, body = MetadataParser.parse(md_file)
            if not metadata:
                continue  # Already caught by VAL-002

            # Metadata is optional at this layer because VAL-002 owns metadata
            # validity. Use a stable fallback so class checks can report malformed
            # but parseable documents without raising formatting errors.
            doc_id = metadata.get("document_id", "unknown")
            plane = metadata.get("plane", "")
            domain = metadata.get("domain", "")
            doc_class = metadata.get("class", "")
            authority = metadata.get("authority", "")
            status = metadata.get("status", "")

            # 1. Plane separation: ROM docs must not contain PS content, PS must not contain ROM
            if plane == "Repository Operating Model" and domain in self.PS_DOMAINS:
                errors.append(ValidationError(
                    code=ErrorCode.PLANE_BOUNDARY_VIOLATION,
                    file=rel_str,
                    line=1,
                    message=format_error(ErrorCode.PLANE_BOUNDARY_VIOLATION, doc_id=doc_id, plane=plane, domain=domain),
                    severity="ERROR",
                    rule="Repository Operating Model documents cannot have Product Specification domains",
                    suggestion=f"Change plane to 'Product Specification' or domain to ROM domain"
                ))

            if plane == "Product Specification" and domain in self.ROM_DOMAINS:
                errors.append(ValidationError(
                    code=ErrorCode.PLANE_BOUNDARY_VIOLATION,
                    file=rel_str,
                    line=1,
                    message=format_error(ErrorCode.PLANE_BOUNDARY_VIOLATION, doc_id=doc_id, plane=plane, domain=domain),
                    severity="ERROR",
                    rule="Product Specification documents cannot have Repository Operating Model domains",
                    suggestion=f"Change plane to 'Repository Operating Model' or domain to PS domain"
                ))

            # 2. Registry documents only in registry folders
            if doc_class == "Registry":
                checked += 1
                if "registries" not in rel_str:
                    errors.append(ValidationError(
                        code=ErrorCode.FOLDER_CLASS_MISMATCH,
                        file=rel_str,
                        line=1,
                        message=format_error(ErrorCode.FOLDER_CLASS_MISMATCH, path=rel_str),
                        severity="ERROR",
                        rule="Registry documents must be in registries/ folder",
                        suggestion="Move to docs/repository-operating-model/registries/ or change class"
                    ))

            # 3. Historical documents only in historical folders
            if doc_class == "Historical" or authority == "Historical" or status == "Historical":
                checked += 1
                if "archive" not in rel_str:
                    errors.append(ValidationError(
                        code=ErrorCode.FOLDER_CLASS_MISMATCH,
                        file=rel_str,
                        line=1,
                        message=format_error(ErrorCode.FOLDER_CLASS_MISMATCH, path=rel_str),
                        severity="ERROR",
                        rule="Historical documents must be in historical/ folder",
                        suggestion="Move to historical/ folder or change class/authority/status"
                    ))

            # 4. ADR documents only in adr/ folder
            if doc_class == "ADR":
                checked += 1
                if not rel_str.startswith("docs/apex-app-docs/architecture/decisions/"):
                    errors.append(ValidationError(
                        code=ErrorCode.FOLDER_CLASS_MISMATCH,
                        file=rel_str,
                        line=1,
                        message=format_error(ErrorCode.FOLDER_CLASS_MISMATCH, path=rel_str),
                        severity="ERROR",
                        rule="ADR documents must be in docs/adr/ folder",
                        suggestion="Move to docs/adr/ or change class"
                    ))

            # 5. Generated documents only in generated/ folder
            if doc_class == "Generated" or authority == "Generated":
                checked += 1
                if not rel_str.startswith("generated/"):
                    errors.append(ValidationError(
                        code=ErrorCode.MISCLASSIFIED_GENERATED_DOC,
                        file=rel_str,
                        line=1,
                        message=format_error(ErrorCode.MISCLASSIFIED_GENERATED_DOC, doc_id=metadata.get("document_id", "unknown")),
                        severity="WARNING",
                        rule="Generated documents must be in generated/ folder",
                        suggestion="Move to generated/ folder or change authority/class"
                    ))

            # 6. Class matches document function (heuristic checks)
            # Specifications should have substantive content
            if doc_class == "Specification":
                checked += 1
                if len(body.strip()) < 100:
                    warnings.append(ValidationWarning(
                        code=ErrorCode.CLASS_MISMATCH,
                        file=rel_str,
                        line=1,
                        message=f"Specification document {metadata.get('document_id')} has minimal content",
                        severity="WARNING",
                        rule="Specifications should have substantive content",
                        suggestion="Add specification content or change class to Reference"
                    ))

            # Index documents should have navigation/lists
            if doc_class == "Index":
                checked += 1
                has_navigation = (
                    any(line.strip().startswith(("- ", "* ", "|")) for line in body.split("\n"))
                    or "](" in body
                    or "cross-reference" in body.lower()
                    or "navigation" in body.lower()
                )
                if not has_navigation:
                    warnings.append(ValidationWarning(
                        code=ErrorCode.INDEX_LAYOUT_HEURISTIC_WARN,
                        file=rel_str,
                        line=1,
                        message=format_error(ErrorCode.INDEX_LAYOUT_HEURISTIC_WARN, doc_id=doc_id),
                        severity="WARNING",
                        rule="Index documents should contain navigation lists",
                        suggestion="Add document lists or change class"
                    ))

            # 7. README files should be Index class
            if rel_path.name == "README.md":
                checked += 1
                if doc_class != "Index":
                    warnings.append(ValidationWarning(
                        code=ErrorCode.CLASS_MISMATCH,
                        file=rel_str,
                        line=1,
                        message=f"README.md should have class: Index, got {doc_class}",
                        severity="WARNING",
                        rule="README files should be class Index",
                        suggestion="Change class to Index"
                    ))

        if errors:
            return self._result_fail(checked, errors)
        return self._result_pass(checked, warnings)