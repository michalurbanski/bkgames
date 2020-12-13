import os
from os import listdir
from os.path import isfile


class Reader:
    """
    Responsible for reading input from file.
    Input files should be provided in the 'data' folder.
    """

    def read(self, autofind: bool = True, filename: str = None) -> list:
        """
        First simple implementation reads all lines at once to the list.

        Parameters:
            autofind (bool): If set to 'true' then automatically searches for
                the latest file in the 'data' directory (based on naming convention).
                If 'false', then filename parameter should be passed instead.
            filename (str): Path to file with data - either absolute path, or if
                relative file name is passed, then it'll be searched for inside
                the 'data' folder.

        Returns:
            list(str): List of lines from input file.
        """

        if not filename:
            if not autofind:
                raise ValueError(
                    "You must provide filename or autofind should be set to 'true'")
            else:
                filename = self._auto_find_file()
        else:
            filename = self._find_filename_path(filename)

        lines = []

        with open(filename, mode="r") as f:
            for line in f:
                lines.append(line.strip())

        return lines

    @staticmethod
    def _get_data_directory() -> str:
        path = os.path.abspath(os.getcwd())
        path = os.path.join(path, "data")
        return path

    @staticmethod
    def _get_current_directory() -> str:
        return os.path.abspath(os.getcwd())

    def _auto_find_file(self) -> str:
        path = self._get_data_directory()

        if not os.path.exists(path):
            raise Exception(
                "Directory where input files are expected {} does not exist".format(path))

        only_files: list = [f for f in listdir(
            path) if isfile(os.path.join(path, f))]

        if not only_files:
            raise Exception("No file with input data can be found")

        only_files.sort(reverse=True)

        return os.path.join(path, only_files[0])

    def _find_filename_path(self, filename: str) -> str:
        """ Check if file exists and if not check it in the 'data' directory """

        if os.path.exists(filename):
            return filename
        else:
            path = self._get_data_directory()
            path = os.path.join(path, filename)
            if os.path.exists(path):
                return path
            else:
                raise ValueError(
                    "Provided file {} cannot be found.".format(path))
