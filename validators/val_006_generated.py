"""
VAL-006: Generated Artifact Guard
Fail-fast validator that detects prohibited temporary/generated files.
"""

from __future__ import annotations
from pathlib import Path
from validator_sdk import (
    BaseValidator,
    ValidationContext,
    ValidationError,
    ErrorCode,
    format_error,
)


class Validator(BaseValidator):
    VALIDATOR_ID = "VAL-006"
    NAME = "Generated Artifact Guard"
    VERSION = "1.0.0"
    DESCRIPTION = "Detects prohibited temporary/generated files that must not be committed"
    CATEGORY = "generated"
    SEVERITY = "ERROR"
    SUPPORTED_METADATA_SCHEMA_VERSIONS = ["1.0"]
    SUPPORTED_REPOSITORY_SPEC_VERSIONS = ["1.0"]

    # Prohibited file patterns (from Validation Specification and AI Workspace Policy)
    PROHIBITED_FILENAMES = {
        "AUDIT.md", "REVIEW.md", "REPORT.md", "SUMMARY.md",
        "ANALYSIS.md", "FINDINGS.md", "NOTES.md", "PLAN.md",
        "TODO.md", "MIGRATION.md", "IMPLEMENTATION-REPORT.md",
        "COMPLETION-REPORT.md", "STATUS.md", "LOG.md", "RESULT.md",
    }

    PROHIBITED_EXTENSIONS = {".tmp", ".bak", ".old", ".temp", ".swp", ".swo"}
    PROHIBITED_PATTERNS = {"*~"}

    # Prohibited CI/CD paths
    PROHIBITED_CICD_PATHS = {
        ".github/workflows",
        ".gitlab-ci.yml",
        ".circleci",
        "jenkins",
        ".travis.yml",
        ".azure-pipelines",
    }

    def validate(self, context: ValidationContext) -> ValidationError:
        self._start_timer()
        errors = []
        checked = 0

        # Get prohibited patterns from config (with defaults)
        prohibited_files = set(self.PROHIBITED_FILENAMES)
        prohibited_exts = set(self.PROHIBITED_EXTENSIONS)
        prohibited_cicd = set(self.PROHIBITED_CICD_PATHS)

        vc = context.config.validator_configs.get("VAL-006", {})
        if "prohibited_patterns" in vc:
            prohibited_files.update(vc["prohibited_patterns"])
        if "prohibited_extensions" in vc:
            prohibited_exts.update(vc["prohibited_extensions"])
        if "prohibited_dirs" in vc:
            prohibited_cicd.update(vc["prohibited_dirs"])

        # Check all markdown files for prohibited names/extensions
        for md_file in context.all_markdown_files:
            checked += 1
            rel_path = md_file.relative_to(context.repository_root)
            rel_str = str(rel_path).replace("\\", "/")

            # Check filename
            if md_file.name in prohibited_files:
                errors.append(ValidationError(
                    code=ErrorCode.PROHIBITED_TEMP_FILE,
                    file=rel_str,
                    line=1,
                    message=format_error(ErrorCode.PROHIBITED_TEMP_FILE, file=rel_str),
                    severity="ERROR",
                    rule="Temporary execution output files are prohibited in repository",
                    suggestion="Delete this file or move to /tmp/ if it's temporary work"
                ))

            # Check extension
            if md_file.suffix in prohibited_exts:
                errors.append(ValidationError(
                    code=ErrorCode.PROHIBITED_TEMP_FILE,
                    file=rel_str,
                    line=1,
                    message=format_error(ErrorCode.PROHIBITED_TEMP_FILE, file=rel_str),
                    severity="ERROR",
                    rule="Temporary file extensions are prohibited",
                    suggestion="Rename or delete this file"
                ))

        # Check for CI/CD files in repository
        for cicd_path in prohibited_cicd:
            full_path = context.repository_root / cicd_path
            if full_path.exists():
                checked += 1
                if full_path.is_dir():
                    for f in full_path.rglob("*"):
                        if f.is_file():
                            rel = f.relative_to(context.repository_root)
                            errors.append(ValidationError(
                                code=ErrorCode.PROHIBITED_CICD_FILE,
                                file=str(rel).replace("\\", "/"),
                                line=1,
                                message=format_error(ErrorCode.PROHIBITED_CICD_FILE, file=str(rel)),
                                severity="ERROR",
                                rule="CI/CD files are prohibited (local-first execution model)",
                                suggestion="Remove CI/CD configuration; this repo uses local validation only"
                            ))
                else:
                    rel = full_path.relative_to(context.repository_root)
                    errors.append(ValidationError(
                        code=ErrorCode.PROHIBITED_CICD_FILE,
                        file=str(rel).replace("\\", "/"),
                        line=1,
                        message=format_error(ErrorCode.PROHIBITED_CICD_FILE, file=str(rel)),
                        severity="ERROR",
                        rule="CI/CD files are prohibited (local-first execution model)",
                        suggestion="Remove CI/CD configuration; this repo uses local validation only"
                    ))

        # Check for generated/ directory files that aren't properly classified
        generated_dir = context.repository_root / "generated"
        if generated_dir.exists():
            for gen_file in generated_dir.rglob("*.md"):
                checked += 1
                rel = gen_file.relative_to(context.repository_root)
                # Check if properly marked as generated in metadata
                from validator_sdk import MetadataParser
                metadata, _ = MetadataParser.parse(gen_file)
                authority = metadata.get("authority", "")
                if authority != "Generated":
                    errors.append(ValidationError(
                        code=ErrorCode.MISCLASSIFIED_GENERATED_DOC,
                        file=str(rel).replace("\\", "/"),
                        line=1,
                        message=format_error(ErrorCode.MISCLASSIFIED_GENERATED_DOC, doc_id=metadata.get("document_id", "unknown")),
                        severity="WARNING",
                        rule="Files in generated/ must have authority: Generated",
                        suggestion="Add authority: Generated to frontmatter or move out of generated/"
                    ))

        if errors:
            return self._result_fail(checked, errors)
        return self._result_pass(checked)