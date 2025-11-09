import os
import shutil
from .application_paths import ApplicationPaths
from . import constants
import importlib.resources
from bkgames.infrastructure import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)


class Initializer:
    """Initializes application configuration inside the user's home folder.
    Creates required folder if they don't exist.
    Application folder is ~/.bkgames
    Data folder is ~/.bkgames/data

    The config.json file is copied to the application folder.
    You can update it with your own values.
    """

    def __init__(self, custom_paths: ApplicationPaths):
        self._custom_paths = custom_paths

    def initialize(self) -> None:
        self._initialize_config()
        Initializer.create_folder(self._custom_paths.data_folder_path)

    def _initialize_config(self) -> None:
        """Gets a config.json file from the package and copies it to the application folder."""
        config_file_name = constants.CONFIG_FILE_NAME
        config_source_path = (
            importlib.resources.files(constants.MODULE_NAME) / config_file_name
        )

        if not config_source_path:
            raise FileNotFoundError(
                f"Cannot find the configuration file '{config_file_name}' in the package"
            )

        Initializer.create_folder(self._custom_paths.application_folder_path)
        Initializer.copy_file(config_source_path, self._custom_paths.config_path)

    @staticmethod
    def copy_file(source_path: str, target_path: str) -> None:
        if not os.path.exists(target_path):
            shutil.copyfile(source_path, target_path)
            logger.info(f"Configuration file initialized. Location: {target_path}")
        else:
            logger.info(
                f"Configuration file already exists. Skipping creation. Location: {target_path}"
            )

    @staticmethod
    def create_folder(path: str) -> None:
        if os.path.exists(path):
            logger.info(f"Folder exists at {path}")
        else:
            os.makedirs(path)  # Creates folders along the way if they do not exist.
            logger.info(f"Folder created at {path}")
