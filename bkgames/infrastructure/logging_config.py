import logging.config
from importlib.resources import files, as_file
from bkgames.configuration import constants

_logging_configured = False


def setup_logging():
    # 'global' keyword is needed to be able to change the value of the global variable inside the function.
    global _logging_configured
    if not _logging_configured:
        # Locate logging config file that is in the package root.
        source = files(constants.MODULE_NAME).joinpath(
            constants.LOGGING_CONFIG_FILE_NAME
        )
        with as_file(source) as logging_config_file:
            logging.config.fileConfig(logging_config_file)

        _logging_configured = True
