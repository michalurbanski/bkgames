from .config import Config
from .custom_paths import CustomPaths
import os, re


class DataFinder:
    def __init__(self, config: Config, paths: CustomPaths) -> None:
        self._config = config
        self._paths = paths
        self._data_folder_path = self._paths.data_folder_path

        if not self._check_data_folder_exists(self._data_folder_path):
            raise ValueError(
                f"Data folder does not exist. Path {self._data_folder_path}"
            )

        if not self._config.data_file_regexp:
            raise ValueError(
                f"data_file_regexp is not set in {self._paths.config_path}"
            )

    # TODO: could be extracted to helper class
    @staticmethod
    def _check_data_folder_exists(data_folder_path: str) -> bool:
        return os.path.exists(data_folder_path) and os.path.isdir(data_folder_path)

    def find_data_path(self) -> str:
        regexp = self._config.data_file_regexp

        files = [
            os.path.join(self._data_folder_path, f)
            for f in os.listdir(self._data_folder_path)
            if re.match(regexp, f)
        ]

        if len(files) == 0:
            raise ValueError(
                f"No files found in {self._data_folder_path} for the specified pattern {regexp}"
            )

        # By default, File names are expected to have a year in their name.
        # If we sort the files in reverse order, we will get the file for the latest season,
        # when there's more than one file in the folder.
        files.sort(reverse=True)

        return files[0]
