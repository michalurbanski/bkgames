import logging.config
import os

_logging_configured = False

def setup_logging():
    global _logging_configured
    if not _logging_configured:
        # Location relative to the file. Ensures that the path to the config file
        # is correct even after the app installation.
        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.dirname(current_dir)
        logging_config_path = os.path.join(parent_dir, "logging.ini")
        logging.config.fileConfig(logging_config_path)
        _logging_configured = True
