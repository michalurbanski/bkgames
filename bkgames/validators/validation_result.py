from dataclasses import dataclass


@dataclass
class ValidationResult:
    input: str
    message: str
    is_valid: bool = False


@dataclass
class InvalidResult(ValidationResult):
    is_valid: bool = False


@dataclass
class ValidResult(ValidationResult):
    is_valid: bool = True
