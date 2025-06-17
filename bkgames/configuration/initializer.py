import os
import shutil
from .application_paths import ApplicationPaths
from . import constants
import importlib.resources
from bkgames.infrastructure import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)


# TODO: improve class description
class Initializer:
    """Initializes application configuration, in the application folder,
    inside the users's home folder.

    - Copies config.json file from the package to the user's home folder.
    Users can then easily set their own configuration settings,
    by modifying the config.json content,
    - Creates folder for data.
    """

    def __init__(self, custom_paths: ApplicationPaths):
        self._custom_paths = custom_paths

    # TODO: should this be part of __init__? it would be easier than to remember to call this method.
    def initialize(self) -> None:
        self._copy_config()
        Initializer._create_folder(self._custom_paths.data_folder_path)

    # TODO: could be further split into smaller method
    def _copy_config(self) -> None:
        # Get a config.json file from the package.
        config_source_path = (
            importlib.resources.files(constants.MODULE_NAME)
            / constants.CONFIG_FILE_NAME
        )

        if not config_source_path:
            raise Exception("Cannot find configuration file in the package")

        Initializer._create_folder(self._custom_paths.application_folder_path)

        if not os.path.exists(self._custom_paths.config_path):
            shutil.copyfile(config_source_path, self._custom_paths.config_path)
            logger.info(
                f"Configuration file initialized. Location: {self._custom_paths.config_path}"
            )
        else:
            logger.info(
                f"Configuration file already exists. Skipping creation. Location: {self._custom_paths.config_path}"
            )

    @classmethod
    def _create_folder(cls, path: str) -> None:
        if os.path.exists(path):
            logger.info(f"Folder exists at {path}")
        else:
            os.makedirs(path)  # Creates folders along the way if they do not exist.
            logger.info(f"Folder created at {path}")
