from bkgames.readers.file_finder import FileFinder
from bkgames.readers.autofinder import Autofinder
from bkgames.readers.filename_finder import FilenameFinder
from bkgames.root_path import ROOT_PATH
import os


class FileFinderFactory:
    @classmethod
    def create_file_finder(
        cls, filename: str = None, autofind: bool = True
    ) -> FileFinder:
        """
        Parameters:
            filename (str): Path to file with data - either absolute path, or if
                relative file name is passed, then it'll be searched for inside
                the 'data' folder.
            autofind (bool): If set to 'true' then automatically searches for
                the latest file in the folder provided to autofinder
                (order determined based on the naming convention used for files).
                If 'false', then filename parameter should be passed instead.
        """
        if not autofind and filename is None:
            raise ValueError(
                "You must provide a filename or autofind must be set to 'true'"
            )

        # Filename checked at first - if user provides filename explicitly
        # it means they decided not to use the autofinder.
        if filename:
            return FilenameFinder(filename)

        # TODO: consider if autofinder is actually needed.
        return Autofinder(os.path.join(ROOT_PATH, "data"))
