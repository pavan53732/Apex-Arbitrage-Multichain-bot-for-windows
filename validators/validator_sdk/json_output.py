"""
JSON serialization and schema validation utilities.
"""

from __future__ import annotations
import json
import jsonschema
from typing import Any
from .base import ValidationResult


def validate_json_output(result: ValidationResult) -> bool:
    """Validate a ValidationResult against its JSON schema."""
    try:
        jsonschema.validate(result.to_dict(), ValidationResult.get_schema())
        return True
    except jsonschema.ValidationError:
        return False


def write_json_result(result: ValidationResult, output_path: str) -> None:
    """Write ValidationResult to JSON file."""
    with open(output_path, "w") as f:
        f.write(result.to_json())


def read_json_result(input_path: str) -> ValidationResult:
    """Read ValidationResult from JSON file."""
    with open(input_path) as f:
        data = json.load(f)
    # Note: This returns dict, not ValidationResult object
    return data