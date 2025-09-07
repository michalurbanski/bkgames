from dataclasses import dataclass, field
from typing import List


@dataclass
class FileParsingResult:
    parsed_lines: List[dict] = field(default_factory=list)
    not_parsed_lines: List[dict] = field(default_factory=list)
