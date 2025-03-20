import os
import shutil
from .custom_paths import CustomPaths
from . import constants
import importlib.resources


# TODO: improve class description
class Initializer:
    """Initializes application configuration, in the application folder,
    inside the users's home folder.

    - Copies config.json file from the package to the user's home folder.
    Users can then easily set their own configuration settings,
    by modifying the config.json content,
    - Creates folder for data.
    """

    def __init__(self, custom_paths: CustomPaths):
        self._custom_paths = custom_paths

    def initialize(self) -> None:
        self._copy_config()
        self._create_data_folder()

    # TODO: could be further split into smaller method
    def _copy_config(self) -> None:
        # Get a config.json file from the package.
        config_source_path = importlib.resources.files(constants.MODULE_NAME) / constants.CONFIG_FILE_NAME

        if not config_source_path:
            raise Exception("Cannot find configuration file in the package")

        if not os.path.exists(self._custom_paths.application_folder_path):
            os.mkdir(self._custom_paths.application_folder_path)
            print(f"Configuration folder created at {self._custom_paths.application_folder_path}")

        if not os.path.exists(self._custom_paths.config_path):
            shutil.copyfile(config_source_path, self._custom_paths.config_path)
            print(f"Configuration file initialized. Location: {self._custom_paths.config_path}")
        else:
            print(
                f"Configuration file already exists. Skipping creation. Location: {self._custom_paths.config_path}"
            )

    def _create_data_folder(self) -> None:
        if os.path.exists(self._custom_paths.data_folder_path):
            print(f"Data folder exists at {self._custom_paths.data_folder_path}")
        else:
            os.mkdir(self._custom_paths.data_folder_path)
            print(f"Data folder created at {self._custom_paths.data_folder_path}")
