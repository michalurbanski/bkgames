from abc import ABC, abstractmethod
from typing import Union
from .parse_result import ParsedLine, NotParsedLine


class LineParserBase(ABC):
    @abstractmethod
    def parse(self, _line: str) -> Union[ParsedLine, NotParsedLine]:
        pass
