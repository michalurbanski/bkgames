import os
import shutil
from .custom_paths import CustomPaths
import importlib.resources


class Initializer:
    """Initializes application configuration.

    - Copies config.json file from the package to user's profile.
    Users can then easily set their own configuration settings,
    by modifying config.json content,
    - Creates folder for data.
    """

    def __init__(self, custom_paths: CustomPaths):
        self._application_folder_path = custom_paths.application_folder_path
        self._config_file_name = custom_paths.config_file_name
        self._config_file_path = custom_paths.config_path
        self._data_folder_path = custom_paths.data_folder_path

    def initialize(self) -> None:
        self._copy_config()
        self._create_data_folder()

    # TODO: could be further split into smaller methods
    def _copy_config(self) -> None:
        # Get a config.json file from the package.
        config_source_path = importlib.resources.files("bkgames") / "config.json"

        if not config_source_path:
            raise Exception("Cannot find configuration file in the package")

        if not os.path.exists(self._application_folder_path):
            os.mkdir(self._application_folder_path)
            print(f"Configuration folder created at {self._application_folder_path}")

        if not os.path.exists(self._config_file_path):
            shutil.copyfile(config_source_path, self._config_file_path)
            print(f"Configuration file initialized. Location: {self._config_file_path}")
        else:
            print(
                f"Configuration file already exists. Skipping creation. Location: {self._config_file_path}"
            )

    def _create_data_folder(self) -> None:
        if os.path.exists(self._data_folder_path):
            print(f"Data folder exists at {self._data_folder_path}")
        else:
            os.mkdir(self._data_folder_path)
            print(f"Data folder created at {self._data_folder_path}")
