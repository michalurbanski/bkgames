import os


class CustomPaths:
    """
    Paths are not configurable because there's no need to.
    They could be taken from .json file though, if ever needed.

    Paths of interest, in this implementation, are stored in the application folder,
    that's inside the user folder.
    """

    def __init__(self):
        self._configuration_root_path = os.path.expanduser("~")  # User's folder.
        self._application_folder_path = os.path.join(
            self._configuration_root_path,
            ".bkgames",
        )
        self._config_file_name = "config.json"

    @property
    def application_folder_path(self):
        return self._application_folder_path

    @property
    def config_file_name(self):
        return self._config_file_name

    @property
    def config_path(self):
        return os.path.join(
            self._application_folder_path,
            self._config_file_name,
        )

    @property
    def data_folder_path(self):
        return os.path.join(
            self._application_folder_path,
            "data",
        )
