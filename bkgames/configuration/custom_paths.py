import os
from pathlib import Path
from . import constants


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
        self._application_folder_path = os.path.join(
            Path.home(),
            f".{constants.MODULE_NAME}",
        )

    @property
    def application_folder_path(self) -> str:
        return self._application_folder_path

    @property
    def config_path(self) -> str:
        return os.path.join(
            self._application_folder_path,
            constants.CONFIG_FILE_NAME,
        )

    @property
    def data_folder_path(self) -> str:
        return os.path.join(
            self._application_folder_path,
            constants.DATA_FOLDER_NAME,
        )
