import os
import pkg_resources
import shutil


class Initializer:
    """Initializes application configuration.

    - Copies config.json file from the package to user's profile.
    Users can then easily set their own configuration settings,
    by modifying config.json content,
    - Creates folder for data.
    """

    def __init__(
        self,
        application_folder_path: str,
        config_file_name: str,
        config_file_path: str,
        data_folder_path: str,
    ):
        self._application_folder_path = application_folder_path
        self._config_file_name = config_file_name
        self._config_file_path = config_file_path
        self._data_folder_path = data_folder_path

    def execute(self) -> None:
        self._copy_config()
        self._create_data_folder()

    # TODO: could be further split into smaller methods
    def _copy_config(self) -> None:
        config_source_path = pkg_resources.resource_filename(
            "bkgames",
            self._config_file_name,
        )
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
