from .config import Config
import json


class ConfigFileReader:
    def __init__(self, filename: str):
        self._filename = filename

    def _read_file(self):
        with open(self._filename, "r") as f:
            return json.load(f)

    @classmethod
    def _populate_config(cls, content: dict, config: Config):
        config.season_year = content.get("season_year", 0)
        config.allowed_teams = content.get("allowed_teams", [])
        config.season_start_month = content.get("season_start_month", 0)
        config.skipped_teams = content.get("skipped_teams", [])

    def read(self, config: Config) -> None:
        content = self._read_file()
        ConfigFileReader._populate_config(content, config)
