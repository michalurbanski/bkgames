from .config import Config
import json


class ConfigFileReader:
    def __init__(self, file_path: str):
        self._file_path = file_path

    def read(self) -> Config:
        content = self._read_file()
        return ConfigFileReader._populate_config(content)

    def _read_file(self):
        with open(self._file_path, "r") as f:
            return json.load(f)

    @classmethod
    def _populate_config(cls, content: dict) -> Config:
        config = Config()
        config.data_file_regexp = content.get("data_file_regexp", "")
        config.season_year = content.get("season_year", 0)
        config.allowed_teams = content.get("allowed_teams", [])
        config.season_start_month = content.get("season_start_month", 0)
        config.skipped_teams = content.get("skipped_teams", [])
        return config
