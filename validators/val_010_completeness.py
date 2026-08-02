"""
VAL-010: Specification Completeness Validator
Checks that specification-class documents have required sections.

Completeness is evaluated against two distinct tiers:

* Core sections apply to every specification regardless of subject matter.
  A specification that does not state its purpose, scope, dependencies, and
  consumers cannot be reviewed or traced, so these are enforced as errors.
* Domain sections apply only where the subject matter makes them meaningful.
  Requiring a "Security" heading on a dashboard layout document, or a
  "Performance" heading on a governance policy, produces noise rather than
  signal, so domain sections are scoped to the domains that own them.

Structured frontmatter satisfies a requirement on equal terms with a prose
heading. The repository records `purpose`, `scope`, `dependencies`, and
`consumers` as canonical metadata fields, and VAL-002 already validates them
there. Demanding that the same information be restated as a heading would
duplicate canonical metadata into prose and split its authority.
"""

from __future__ import annotations
import re
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


# Sections required of every document of a given class, irrespective of domain.
CORE_SECTIONS = {
    "Specification": ["Purpose", "Scope", "Dependencies", "Consumers"],
    "Guide": ["Purpose", "Scope", "Prerequisites", "Steps"],
    "ADR": ["Context", "Decision", "Consequences", "Status"],
    "Policy": ["Purpose", "Scope", "Rules"],
    "Reference": ["Purpose", "Scope", "Description"],
}

# Sections required only of specifications whose domain owns the concern.
# A domain absent from this mapping requires the core sections alone.
DOMAIN_SECTIONS = {
    "Execution": ["Failure Handling"],
    "Runtime": ["Failure Handling"],
    "Market": ["Failure Handling"],
    "Operations": ["Failure Handling"],
    "State Machines": ["State Machine"],
}

# Sections that improve a document without being mandatory. Absence is
# reported as a warning so that quality remains visible without blocking.
RECOMMENDED_SECTIONS = {
    "Specification": [
        "Architecture", "Interfaces", "Failure Handling",
        "Security", "Performance", "Testing", "State Machine",
    ],
    "Guide": ["Examples"],
    "ADR": ["Affected Components"],
    "Policy": ["Enforcement", "Exceptions"],
    "Reference": ["Examples", "Related Documents"],
}

# Heading synonyms. Documents in this repository express the same concern under
# a variety of established headings; recognising them prevents the validator
# from demanding a specific wording where the substance is already present.
SECTION_SYNONYMS = {
    "Purpose": ["purpose", "overview", "summary", "intent"],
    "Scope": ["scope", "applies to", "boundaries", "authority boundary"],
    "Dependencies": ["dependencies", "depends on", "requires", "upstream"],
    "Consumers": ["consumers", "consumed by", "downstream", "used by"],
    "Architecture": ["architecture", "design", "structure", "components", "responsibilities"],
    "State Machine": [
        "state machine", "state diagram", "states and transitions",
        "lifecycle", "state model", "transitions",
    ],
    "Failure Handling": [
        "failure handling", "failure modes", "failure", "error handling",
        "errors", "recovery", "fault", "fallback", "retry", "degradation",
        "resilience", "exception",
    ],
    "Security": ["security", "threat model", "permissions", "trust boundary", "access control"],
    "Performance": ["performance", "latency", "throughput", "budget", "slo", "timing"],
    "Interfaces": ["interfaces", "interface contract", "api", "contract", "protocol", "schema"],
    "Testing": ["testing", "tests", "validation", "verification", "test strategy"],
    "Prerequisites": ["prerequisites", "requirements", "before you begin"],
    "Steps": ["steps", "procedure", "instructions", "walkthrough"],
    "Examples": ["examples", "example", "usage", "sample"],
    "Context": ["context", "background", "problem"],
    "Decision": ["decision", "resolution"],
    "Consequences": ["consequences", "implications", "trade-offs", "tradeoffs"],
    "Affected Components": ["affected components", "impact", "affected"],
    "Status": ["status"],
    "Rules": ["rules", "policy", "requirements", "constraints"],
    "Enforcement": ["enforcement", "compliance", "validation"],
    "Exceptions": ["exceptions", "waivers", "exemptions"],
    "Description": ["description", "details", "reference"],
    "Related Documents": ["related documents", "cross-references", "cross references", "see also"],
}

# Frontmatter keys that satisfy a section requirement when populated.
METADATA_EQUIVALENTS = {
    "Purpose": ["purpose"],
    "Scope": ["scope"],
    "Dependencies": ["dependencies"],
    "Consumers": ["consumers"],
}


class Validator(BaseValidator):
    VALIDATOR_ID = "VAL-010"
    NAME = "Specification Completeness Validator"
    VERSION = "2.0.0"
    DESCRIPTION = "Checks specification-class documents for required sections"
    CATEGORY = "completeness"
    SEVERITY = "WARNING"
    SUPPORTED_METADATA_SCHEMA_VERSIONS = ["1.0"]
    SUPPORTED_REPOSITORY_SPEC_VERSIONS = ["1.0"]

    def validate(self, context: ValidationContext) -> ValidationResult:
        self._start_timer()
        errors = []
        warnings = []
        infos = []
        checked = 0

        for md_file in context.all_markdown_files:
            checked += 1
            rel_path = md_file.relative_to(context.repository_root)
            rel_str = str(rel_path).replace("\\", "/")

            metadata, body = MetadataParser.parse(md_file)
            if not metadata:
                continue

            doc_id = metadata.get("document_id", "unknown")
            doc_class = metadata.get("class", "")
            authority = metadata.get("authority", "")
            domain = metadata.get("domain", "")

            core = list(CORE_SECTIONS.get(doc_class, []))
            if not core:
                continue

            if doc_class == "Specification":
                core.extend(
                    section for section in DOMAIN_SECTIONS.get(domain, [])
                    if section not in core
                )

            recommended = [
                section for section in RECOMMENDED_SECTIONS.get(doc_class, [])
                if section not in core
            ]

            headings = self._extract_headings(body)

            missing_core = [
                s for s in core if not self._has_section(s, headings, metadata)
            ]
            missing_recommended = [
                s for s in recommended if not self._has_section(s, headings, metadata)
            ]

            present_count = len(core) - len(missing_core)
            completeness_pct = (present_count / len(core)) * 100 if core else 100

            enforce = authority == "Canonical" and doc_class == "Specification"

            for section in missing_core:
                if enforce:
                    errors.append(ValidationError(
                        code="MISSING_REQUIRED_SECTION",
                        file=rel_str,
                        line=1,
                        message=(
                            f"Canonical {doc_class} document {doc_id} "
                            f"({doc_class}, {domain}) is missing required section: '{section}'"
                        ),
                        severity="ERROR",
                        rule=f"All Canonical Specification documents must have a '{section}' section.",
                        suggestion=(
                            f"Add a '{section}' section to {rel_str}, or populate the "
                            f"equivalent frontmatter field."
                        ),
                    ))
                else:
                    warnings.append(ValidationWarning(
                        code="MISSING_RECOMMENDED_SECTION",
                        file=rel_str,
                        line=1,
                        message=f"{doc_class} document {doc_id} is missing recommended section: '{section}'",
                        severity="WARNING",
                        rule=f"Documents of class {doc_class} should have a '{section}' section.",
                        suggestion=f"Consider adding a '{section}' section to {rel_str}.",
                    ))

            for section in missing_recommended:
                warnings.append(ValidationWarning(
                    code="MISSING_RECOMMENDED_SECTION",
                    file=rel_str,
                    line=1,
                    message=f"{doc_class} document {doc_id} is missing recommended section: '{section}'",
                    severity="WARNING",
                    rule=f"Documents of class {doc_class} benefit from a '{section}' section.",
                    suggestion=f"Consider adding a '{section}' section to {rel_str}.",
                ))

            infos.append(ValidationWarning(
                code="COMPLETENESS_SCORE",
                file=rel_str,
                line=1,
                message=(
                    f"Document {doc_id}: {completeness_pct:.0f}% complete "
                    f"({present_count}/{len(core)} required sections present)"
                ),
                severity="INFO",
                rule="Completeness measured against required sections for document class and domain.",
                suggestion="",
            ))

        if errors:
            return self._result_fail(checked, errors)
        return self._result_pass(checked, warnings + infos)

    def _extract_headings(self, body: str) -> list[tuple[int, str]]:
        headings = []
        for line in body.split("\n"):
            stripped = line.strip()
            if stripped.startswith("#"):
                level = len(stripped) - len(stripped.lstrip("#"))
                text = stripped.lstrip("#").strip().lower()
                # Numbered headings such as "## 5. Failure Modes" carry the same
                # meaning as their unnumbered equivalents.
                text = re.sub(r"^\d+(\.\d+)*\.?\s*", "", text)
                headings.append((level, text))
        return headings

    def _has_section(
        self,
        section: str,
        headings: list[tuple[int, str]],
        metadata: dict,
    ) -> bool:
        """Report whether a required section is satisfied.

        A section counts as present when a populated frontmatter field records
        it, or when any heading matches the section name or one of its
        recognised synonyms.
        """
        for key in METADATA_EQUIVALENTS.get(section, []):
            if self._metadata_field_populated(metadata, key):
                return True

        candidates = SECTION_SYNONYMS.get(section, [section.lower()])
        for _, text in headings:
            for candidate in candidates:
                if candidate in text:
                    return True
        return False

    @staticmethod
    def _metadata_field_populated(metadata: dict, key: str) -> bool:
        """Report whether a frontmatter field is present and carries content.

        List-valued fields such as `dependencies` and `consumers` are
        meaningful when declared even if empty: an explicit empty list is a
        deliberate statement that the document has none, which is exactly the
        information the section would have conveyed.
        """
        if key not in metadata:
            return False

        value = metadata[key]
        if value is None:
            return False
        if isinstance(value, (list, tuple)):
            return True
        return bool(str(value).strip())
