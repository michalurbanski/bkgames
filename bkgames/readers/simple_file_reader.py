from typing import List


class SimpleFileReader:
    def __init__(self, filename: str):
        self._filename = filename

        if self._filename is None:
            raise ValueError("Filename is None")

    def read(self) -> List[str]:
        """
        First, simple, implementation reads all lines at once to the list.

        Number of lines to be read is small. There's no need to provide
        more sophisticated mechanism. All data can be read into memory.

        Returns:
            list(str): List of lines from the input file.
        """

        lines = []
        with open(self._filename, mode="r") as f:
            for line in f:
                lines.append(line.strip())

        return lines
