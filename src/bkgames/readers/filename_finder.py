from bkgames.readers.file_finder import FileFinder
import os


class FilenameFinder(FileFinder):
    def __init__(self, filename):
        self._filename = filename

        if self._filename is None:
            raise ValueError(
                "This finder requires providing a filename parameter")

    def find_input_file(self) -> str:
        return self._find_filename_path(self._filename)

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

    @staticmethod
    def _get_data_directory() -> str:
        path = FilenameFinder._get_current_directory()
        path = os.path.join(path, "data")
        return path

    @staticmethod
    def _get_current_directory() -> str:
        return os.path.abspath(os.getcwd())
