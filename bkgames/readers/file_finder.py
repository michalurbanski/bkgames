from abc import ABC, abstractmethod


class FileFinder(ABC):
    """ Base class for file finders"""

    @abstractmethod
    def find_input_file(self) -> str:
        pass
