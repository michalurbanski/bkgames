import json
from typing import List
from bkgames.decorators.singleton import singleton


@singleton
class Configuration:
    """ Reads configuration values from config file """

    def __init__(self, filename: str):
        self._filename = filename
        self._config = None

    @property
    def season_year(self) -> int:
        self._load()
        return self._config["season_year"]

    @property
    def allowed_teams(self) -> List[str]:
        self._load()
        return self._config["allowed_teams"]

    @property
    def season_start_month(self) -> int:
        self._load()
        return self._config["season_start_month"]

    def _load(self) -> None:
        if self._config:
            return
        self._read_json_file()

    def _read_json_file(self) -> None:
        with open(self._filename, 'r') as f:
            self._config = json.load(f)
