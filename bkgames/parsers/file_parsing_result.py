from dataclasses import dataclass, field
from .parse_result import ParsedLine, NotParsedLine
from typing import List


@dataclass
class FileParsingResult:
    parsed_lines: List[ParsedLine] = field(default_factory=list)
    not_parsed_lines: List[NotParsedLine] = field(default_factory=list)
