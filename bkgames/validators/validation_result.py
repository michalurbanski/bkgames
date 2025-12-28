from dataclasses import dataclass


@dataclass
class ValidationResult:
    input: str
    # TODO: message is for errors, so it should be called error_message
    message: str
    is_valid: bool = False


# TODO: change this to normal class, to have initializer, it will be easier to use.
# The same for the ValidResult. And change their order.
@dataclass
class InvalidResult(ValidationResult):
    is_valid: bool = False


@dataclass
class ValidResult(ValidationResult):
    is_valid: bool = True
    message: str = ""
