"""
VAL-015: Cross-Domain Consistency Validator
Detects contradictions across specification domains by comparing claims,
verifying cross-reference integrity, and validating authority/dependency consistency.
"""

from __future__ import annotations
import re
from pathlib import Path
from collections import defaultdict
from validator_sdk import (
    BaseValidator,
    ValidationContext,
    ValidationError,
    ValidationWarning,
    ErrorCode,
    format_error,
    MetadataParser,
)


# Domain pairs that must agree on shared concerns
CROSS_DOMAIN_PAIRS = [
    ("Architecture", "Runtime"),
    ("Runtime", "Execution"),
    ("Execution", "Market"),
    ("AI", "Runtime"),
    ("Security", "Interfaces"),
    ("Deployment", "Windows"),
    ("Architecture", "AI"),
    ("Execution", "State Machines"),
    ("Runtime", "State Machines"),
    ("Configuration", "Runtime"),
    ("Data", "Runtime"),
]

# Quantitative claims are the one class of cross-domain statement that can be
# compared mechanically without natural-language understanding. A named metric
# bound to a number and a unit is either the same value everywhere it is
# asserted or it is a contradiction, and a contradiction between two canonical
# documents is a defect regardless of which one is right.
#
# The pattern deliberately requires a unit. Bare numbers ("3 retries", "phase 2")
# carry too little context to compare safely across domains.
QUANTITATIVE_CLAIM = re.compile(
    r"([A-Za-z][A-Za-z0-9 _\-]{4,44}?)\s*"          # metric name
    r"(?:<=|>=|=|:|is|of|to)\s*"                     # binding
    r"([0-9]+(?:\.[0-9]+)?)\s*"                      # value
    r"(ms|s|seconds|minutes|%|bps|USD|MB|GB|gwei)\b",  # unit
    re.IGNORECASE,
)

# Words that make a claim conditional, illustrative, or bounded to one variant.
# "AI inference p95 <= 500ms for small models" and "... <= 2000ms for large
# models" are two scoped facts, not a disagreement, so lines carrying a
# qualifier are not treated as absolute assertions.
CLAIM_QUALIFIERS = re.compile(
    r"\b(for|when|if|per|example|e\.g\.|such as|small|large|default|"
    r"minimum|maximum|min|max|up to|at least|at most|target|budget|"
    r"tier|phase|draft|deprecated|legacy|was|previously)\b",
    re.IGNORECASE,
)

# Metric names too generic to identify a single shared quantity.
GENERIC_METRIC_NAMES = {
    "value", "size", "count", "limit", "threshold", "budget", "total",
    "time", "duration", "interval", "timeout", "delay", "rate", "usage",
    "memory", "cpu", "disk", "latency", "cost", "amount", "number",
}


class Validator(BaseValidator):
    VALIDATOR_ID = "VAL-015"
    NAME = "Cross-Domain Consistency Validator"
    VERSION = "1.1.0"
    DESCRIPTION = "Detects contradictions across specification domains and validates cross-domain consistency"
    CATEGORY = "consistency"
    SEVERITY = "WARNING"
    SUPPORTED_METADATA_SCHEMA_VERSIONS = ["1.0"]
    SUPPORTED_REPOSITORY_SPEC_VERSIONS = ["1.0"]

    def validate(self, context: ValidationContext) -> ValidationResult:
        self._start_timer()
        errors = []
        warnings = []
        checked = 0

        # Build domain→documents index
        domain_docs: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
        # domain → [(doc_id, path, authority)]

        for doc_id, entry in context.document_registry.items():
            if entry.status != "Active":
                continue
            domain_docs[entry.domain].append((doc_id, entry.path, entry.authority))

        # 1. Cross-domain contradiction detection.
        #
        #    Quantitative claims are collected per domain and compared across the
        #    domain pairs that must agree. When the same named metric is asserted
        #    with different values in two domains, at least one of the two
        #    documents is wrong, and an implementer reading either in isolation
        #    would build to the wrong number.
        claims = self._collect_quantitative_claims(context, domain_docs)

        reported: set[tuple] = set()
        for dom_a, dom_b in CROSS_DOMAIN_PAIRS:
            if dom_a not in claims or dom_b not in claims:
                continue
            checked += 1

            for metric, unit in set(claims[dom_a]) & set(claims[dom_b]):
                values_a = claims[dom_a][(metric, unit)]
                values_b = claims[dom_b][(metric, unit)]
                distinct = {v for v, _, _ in values_a} | {v for v, _, _ in values_b}
                if len(distinct) < 2:
                    continue

                # Report the pair once, against the document in the first domain.
                key = (metric, unit, dom_a, dom_b)
                if key in reported:
                    continue
                reported.add(key)

                sources = sorted(
                    {f"{v}{unit} in {p} ({d})"
                     for d, vs in ((dom_a, values_a), (dom_b, values_b))
                     for v, p, _ in vs}
                )
                first_path = sorted(values_a)[0][1]
                warnings.append(ValidationWarning(
                    code="CROSS_DOMAIN_VALUE_CONFLICT",
                    file=first_path, line=1,
                    message=(
                        f"Metric '{metric}' is asserted with conflicting values across "
                        f"{dom_a} and {dom_b}: " + "; ".join(sources)
                    ),
                    severity="WARNING",
                    rule="A named quantitative claim must hold the same value in every domain that asserts it.",
                    suggestion=(
                        f"Establish the canonical value for '{metric}' in its owning document "
                        f"and have the other domains reference it instead of restating it."
                    ),
                ))

        # 2. Authority consistency: Derived docs must have canonical_source pointing to
        #    a document in the appropriate domain
        for doc_id, entry in context.document_registry.items():
            if entry.authority == "Derived" and entry.status == "Active":
                checked += 1
                canonical_src = entry.canonical_source

                # Check if canonical_source is a DOC-ID or a path
                if canonical_src.startswith("DOC-"):
                    if canonical_src not in context.document_registry:
                        errors.append(ValidationError(
                            code="DERIVED_CANONICAL_UNRESOLVED",
                            file=entry.path, line=1,
                            message=f"Derived document {doc_id} canonical_source {canonical_src} not registered",
                            severity="ERROR",
                            rule="Derived documents must reference a registered canonical source.",
                            suggestion=f"Register {canonical_src} or update canonical_source.",
                        ))

        # 3. Dependency consistency: verify dependencies cross domains correctly
        for doc_id, entry in context.document_registry.items():
            if not entry.dependencies:
                continue
            checked += 1

            for dep_id in entry.dependencies:
                dep_id = dep_id.strip()
                if not dep_id:
                    continue
                if dep_id not in context.document_registry:
                    errors.append(ValidationError(
                        code="DEPENDENCY_UNRESOLVED",
                        file=entry.path, line=1,
                        message=f"Document {doc_id} depends on {dep_id} which is not registered",
                        severity="ERROR",
                        rule="All dependencies must be registered DOC-IDs.",
                        suggestion=f"Register {dep_id} or remove it from dependencies.",
                    ))
                    continue

                dep_entry = context.document_registry[dep_id]

                # Check dependency not superseded
                if dep_entry.status == "Superseded":
                    warnings.append(ValidationWarning(
                        code="DEPENDENCY_ON_SUPERSEDED",
                        file=entry.path, line=1,
                        message=f"Document {doc_id} depends on superseded document {dep_id}",
                        severity="WARNING",
                        rule="Active documents should not depend on superseded documents.",
                        suggestion=f"Update {doc_id} to depend on {dep_id}'s successor.",
                    ))

                # Check cross-plane dependency validity
                if entry.plane != dep_entry.plane:
                    # ROM docs can depend on PS docs (e.g., documentation-map references)
                    # PS docs generally should not depend on ROM docs
                    if entry.plane == "Product Specification" and dep_entry.plane == "Repository Operating Model":
                        warnings.append(ValidationWarning(
                            code="CROSS_PLANE_DEPENDENCY",
                            file=entry.path, line=1,
                            message=f"Product Specification document {doc_id} depends on "
                                    f"Repository Operating Model document {dep_id}",
                            severity="WARNING",
                            rule="Product Specification documents should minimize dependencies on "
                                  "Repository Operating Model documents.",
                            suggestion="Verify this cross-plane dependency is intentional.",
                        ))

        # 4. Consumer consistency
        for doc_id, entry in context.document_registry.items():
            if not entry.consumers:
                continue
            checked += 1

            for consumer_id in entry.consumers:
                consumer_id = consumer_id.strip()
                if not consumer_id:
                    continue
                if consumer_id not in context.document_registry:
                    errors.append(ValidationError(
                        code="CONSUMER_UNRESOLVED",
                        file=entry.path, line=1,
                        message=f"Document {doc_id} lists consumer {consumer_id} which is not registered",
                        severity="ERROR",
                        rule="All consumers must be registered DOC-IDs.",
                        suggestion=f"Register {consumer_id} or remove it from consumers.",
                    ))

        if errors:
            return self._result_fail(checked, errors)
        return self._result_pass(checked, warnings)

    def _collect_quantitative_claims(
        self,
        context: ValidationContext,
        domain_docs: dict[str, list[tuple[str, str, str]]],
    ) -> dict[str, dict[tuple[str, str], set[tuple[str, str, str]]]]:
        """Index absolute quantitative claims per domain.

        Returns domain -> (metric, unit) -> {(value, path, doc_id)}.

        Only unqualified assertions in canonical documents are collected. A
        qualified line states a scoped fact rather than a global one, and
        comparing scoped facts across domains produces false conflicts.
        """
        claims: dict[str, dict[tuple[str, str], set[tuple[str, str, str]]]] = defaultdict(
            lambda: defaultdict(set)
        )

        for domain, docs in domain_docs.items():
            for doc_id, path, authority in docs:
                if authority != "Canonical":
                    continue
                md_file = context.repository_root / path
                if not md_file.exists():
                    continue
                try:
                    content = md_file.read_text(encoding="utf-8")
                except Exception:
                    continue

                in_frontmatter = False
                in_code = False
                for index, line in enumerate(content.split("\n")):
                    stripped = line.strip()

                    # Frontmatter and fenced code are not prose assertions.
                    if stripped == "---" and index == 0:
                        in_frontmatter = True
                        continue
                    if in_frontmatter:
                        if stripped == "---":
                            in_frontmatter = False
                        continue
                    if stripped.startswith("```"):
                        in_code = not in_code
                        continue
                    if in_code or not stripped:
                        continue
                    if CLAIM_QUALIFIERS.search(stripped):
                        continue

                    for match in QUANTITATIVE_CLAIM.finditer(stripped):
                        metric = " ".join(match.group(1).split()).strip(" -|*#:").lower()
                        metric = re.sub(r"^[^a-z]+", "", metric)
                        if len(metric) < 6 or metric in GENERIC_METRIC_NAMES:
                            continue
                        unit = match.group(3).lower()
                        unit = {"seconds": "s", "minutes": "min"}.get(unit, unit)
                        claims[domain][(metric, unit)].add(
                            (match.group(2), path, doc_id)
                        )

        return claims
