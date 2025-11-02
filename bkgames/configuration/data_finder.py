from .config import Config
from .application_paths import ApplicationPaths
from bkgames.infrastructure.file_utilities import FileUtilities
import os, re


class DataFinder:
    """DataFinder is responsible for finding path to the data file."""

    def __init__(self, config: Config, paths: ApplicationPaths) -> None:
        self._config = config
        self._paths = paths
        self._data_folder_path = self._paths.data_folder_path

        if not FileUtilities.is_folder_exists(self._data_folder_path):
            raise ValueError(
                f"Data folder does not exist. Path {self._data_folder_path}"
            )

        if not self._config.data_file_regexp:
            raise ValueError(
                f"data_file_regexp is not set in {self._paths.config_path}"
            )

    def find_data_path(self) -> str:
        """Finds the exact path to the file with data.

        Files should be in the application folder in the user home directory.
        There can be many files with data. This method selects the latest one, based on its name.
        """
        regexp = self._config.data_file_regexp

        files = [
            os.path.join(self._data_folder_path, f)
            for f in os.listdir(self._data_folder_path)
            if re.match(regexp, f)
        ]

        if len(files) == 0:
            # Below, it's the way to make a multi-line string.
            raise ValueError(
                f"No files found in {self._data_folder_path} for the specified pattern {regexp}. "
                f"This pattern is defined in the config.json file."
            )

        # By default, File names are expected to have a year in their name.
        # If we sort the files in reverse order, we will get the file for the latest season,
        # when there's more than one file in the folder.
        files.sort(reverse=True)

        return files[0]
