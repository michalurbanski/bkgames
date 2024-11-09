import os
from pathlib import Path


class CustomPaths:
    """
    Paths are not configurable because there's no need to.
    They could be taken from .json file though, if ever needed.

    Data for the application is / should be stored in the .bkgames/data folder inside
    user's folder.
    Inside the .bkgames folder, there should be config.json file.

    If there's no config.json file, then it's initialized with the default data
    when the application runs for the first time.
    """

    def __init__(self):
        self._configuration_root_path = Path.home() # User's folder
        self._application_folder_path = os.path.join(
            self._configuration_root_path,
            ".bkgames",
        )
        self._config_file_name = "config.json"

    @property
    def application_folder_path(self) -> str:
        return self._application_folder_path

    @property
    def config_file_name(self) -> str:
        return self._config_file_name

    @property
    def config_path(self) -> str:
        return os.path.join(
            self._application_folder_path,
            self._config_file_name,
        )

    @property
    def data_folder_path(self) -> str:
        return os.path.join(
            self._application_folder_path,
            "data",
        )
