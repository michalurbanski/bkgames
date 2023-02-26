from bkgames.reader.file_finder import FileFinder
from bkgames.reader.file_finder_factory import FileFinderFactory
from typing import List


class Reader:
    """
    Responsible for reading lines from input file.
    Input files are expected to be placed in the 'data' folder.
    """

    def __init__(self, file_finder: FileFinder = None):
        """
        Parameters:
            file_finder (FileFinder): One of the finders that specify how
                to search for an input file.
                Note: Use FileFinderFactory to create this object.
        """
        self._file_finder = file_finder or FileFinderFactory.create_file_finder()

    def read(self) -> List[str]:
        """
        First, simple, implementation reads all lines at once to the list.

        Number of lines to be read is small. There's no need to provide 
        more sophisticated mechanism. All data can be read into memory.

        Returns:
            list(str): List of lines from the input file.
        """

        lines = []
        filename = self._file_finder.find_input_file()

        with open(filename, mode="r") as f:
            for line in f:
                lines.append(line.strip())

        return lines
