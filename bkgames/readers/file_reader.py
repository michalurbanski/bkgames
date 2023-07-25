from bkgames.readers.file_finder import FileFinder
from bkgames.readers.file_finder_factory import FileFinderFactory
from typing import List


class FileReader:
    """
    Responsible for reading lines from input file.
    Input files are expected to be placed in the 'data' folder.
    """

    def __init__(self, 
                 file_finder: FileFinder = None, 
                 data_folder_path: str = "",
                 data_file_name: str = ""):
        """
        Parameters:
            file_finder (FileFinder): One of the finders that specify how
                to search for an input file.
                Note: If not passed as an argument, use FileFinderFactory to create this object.
            
            data_folder_path (str): Path to the folder that has files with games played.

            data_file_name (str): file name in the data_folder_path. If you want to use
                a specific file.
        """
        self._file_finder = file_finder or FileFinderFactory.create_file_finder(
            data_folder_path = data_folder_path,
            filename = data_file_name
        )

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
