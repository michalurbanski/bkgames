import logging.config
import importlib.resources
from bkgames.configuration import constants

_logging_configured = False


def setup_logging():
    # 'global' keyword is needed to be able to change the value of the global variable inside the function.
    global _logging_configured
    if not _logging_configured:
        # Locate logging config file that is in the package root.
        with importlib.resources.path(
            constants.MODULE_NAME, constants.LOGGING_CONFIG_FILE_NAME
        ) as logging_config_path:
            logging.config.fileConfig(logging_config_path)

        _logging_configured = True
