import os
from pathlib import Path
from . import constants


class ApplicationPaths:
    """
    Paths are not configurable because there's no need to in this simple app.
    They could be taken from .json file, if ever needed.

    Data for the application and configuration files are stored in the user's home folder,
    in the .bkgames subfolder.
    The structure in the .bkgames folder is:
    - config.json
    - data/

    This structure is created when the application runs for the first time.
    - You can change values in config.json file.
    - You should fill in the data in the data folder with your own data files.
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
