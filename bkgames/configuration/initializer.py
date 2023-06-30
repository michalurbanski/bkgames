import os
import pkg_resources
import shutil

class Initializer:
    """
        Copies config.json file from the package to user's profile.
        Users can then easily set their own configuration settings.
    """
    def __init__(self, config_file_name:str = "config.json", user_folder:str = ".bkgames"):
        self._config_file_name = config_file_name
        self._user_folder = user_folder

    def initialize(self) -> None:
        self._copy_config()

    def _copy_config(self) -> None:
        config_source_path = pkg_resources.resource_filename("bkgames", self._config_file_name)
        if not config_source_path:
            raise Exception("Cannot find configuration file in the package")

        profile_path = os.path.expanduser("~")
        profile_config_folder_path = os.path.join(profile_path, self._user_folder)
        if not os.path.exists(profile_config_folder_path):
            os.mkdir(profile_config_folder_path)
            print(
                f"Configuration folder created under {profile_config_folder_path}")

        profile_config_path = os.path.join(
            profile_config_folder_path, self._config_file_name)

        if not os.path.exists(profile_config_path):
            # Note: When the config file contents changes, a new version does not
            #       overwrite copy that the users have in their profile.
            #       This is fine for now.
            shutil.copyfile(config_source_path, profile_config_path)
            print(f"Configuration file initialized. Location: {profile_config_path}")
        else:
            print(f"Configuration file already exists. Skipping creation. Location: {profile_config_path}")
