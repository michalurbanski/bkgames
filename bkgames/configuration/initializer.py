import os
import pkg_resources
import shutil


class Initializer:
    """
    Copies config.json file from the package to user's profile.
    Users can then easily set their own configuration settings,
    by modifying config.json content.
    """

    def __init__(
        self, application_folder_path: str, config_file_name: str, config_file_path: str
    ):
        self._application_folder_path = application_folder_path
        self._config_file_name = config_file_name
        self._config_file_path = config_file_path

    # def __init__(
    #     self, config_file_name: str = "config.json", user_folder: str = ".bkgames"
    # ):
    #     self._config_file_name = config_file_name
    #     self._user_folder = user_folder
    #     self._config_file_path = ""

    def execute(self) -> None:
        self._copy_config()

    # @property
    # def config_file_path(self) -> str:
    #     return self._config_file_path

    def _copy_config(self) -> None:
        config_source_path = pkg_resources.resource_filename(
            "bkgames",
            self._config_file_name,
        )
        if not config_source_path:
            raise Exception("Cannot find configuration file in the package")

        if not os.path.exists(self._application_folder_path):
            os.mkdir(self._application_folder_path)
            print(f"Configuration folder created under {self._application_folder_path}")

        # profile_path = os.path.expanduser("~")
        # profile_config_folder_path = os.path.join(profile_path, self._user_folder)
        # if not os.path.exists(profile_config_folder_path):
        #     os.mkdir(profile_config_folder_path)
        #     print(f"Configuration folder created under {profile_config_folder_path}")

        # profile_config_path = os.path.join(
        #     profile_config_folder_path, self._config_file_name
        # )
        # self._config_file_path = profile_config_path

        if not os.path.exists(self._config_file_path):
            shutil.copyfile(config_source_path, self._config_file_path)
            print(f"Configuration file initialized. Location: {self._config_file_path}")
        else:
            print(
                f"Configuration file already exists. Skipping creation. Location: {self._config_file_path}"
            )

        # if not os.path.exists(profile_config_path):
        #     # Note: When the config file content changes, a new version does not
        #     #       overwrite copy that the users have in their profile.
        #     #       This is fine for now.
        #     shutil.copyfile(config_source_path, profile_config_path)
        #     print(f"Configuration file initialized. Location: {profile_config_path}")
        # else:
        #     print(
        #         f"Configuration file already exists. Skipping creation. Location: {profile_config_path}"
        #     )
