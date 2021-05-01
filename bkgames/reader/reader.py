import os
from os import listdir
from os.path import isfile
from bkgames.reader.autofinder import Autofinder


class Reader:
    """
    Responsible for reading lines from input file.
    Input files are expected to be placed in the 'data' folder.
    """

    def __init__(self, autofind: bool = True, filename: str = None,
                 autofinder: Autofinder = None):
        """
        Parameters:
            autofind (bool): If set to 'true' then automatically searches for
                the latest file in the folder provided to autofinder
                (order determined based on the naming convention used for files).
                If 'false', then filename parameter should be passed instead.
            filename (str): Path to file with data - either absolute path, or if
                relative file name is passed, then it'll be searched for inside
                the 'data' folder.
            autofinder (Autofinder): Autofinder used to automatically search
                for the latest file. If None is passed, then the default
                Autofinder is used, that searches inside the 'data' folder.
        """
        self._autofind = autofind
        self._filename = filename
        self._autofinder = autofinder

        if not self._filename and not self._autofind:
            raise ValueError(
                "You must provide a filename or autofind must be set to 'true'")

        self._set_file_finder()

    def _set_file_finder(self):
        self._run_autofinder = False

        # When filename is provided that we're not using autofinder,
        # even if the user provides it, it doesn't make sense to use it as
        # requested operation is to read from the specific file.
        if self._filename is not None:
            self._autofinder = None
            return

        if self._autofind:
            self._run_autofinder = True
            if self._filename is None and self._autofinder is None:
                # Use the default AutoFinder
                self._autofinder = Autofinder("data")

    def read(self) -> list:
        """
        First simple implementation reads all lines at once to the list.

        Returns:
            list(str): List of lines from the input file.
        """

        # TODO: make filename path finder also a separate finder, so then 'if/else' here can be avoided
        if self._run_autofinder:
            filename = self._autofinder.find_input_file()
        else:
            filename = self._find_filename_path(self._filename)

        lines = []

        with open(filename, mode="r") as f:
            for line in f:
                lines.append(line.strip())

        return lines

    @staticmethod
    def _get_data_directory() -> str:
        path = Reader._get_current_directory()
        path = os.path.join(path, "data")
        return path

    @staticmethod
    def _get_current_directory() -> str:
        return os.path.abspath(os.getcwd())

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
