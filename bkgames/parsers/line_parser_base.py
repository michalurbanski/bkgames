from abc import ABC, abstractmethod
from typing import Tuple


class LineParserBase(ABC):
    @abstractmethod
    def parse(self, _line: str) -> Tuple[bool, dict]:
        pass
