import json
from bkgames.decorators.singleton import singleton


@singleton
class Configuration:

    def __init__(self, filename):
        self._filename = filename
        self._config = None

    @property
    def season_year(self):
        self._load()
        return self._config["season_year"]

    @property
    def allowed_teams(self):
        self._load()
        return self._config["allowed_teams"]

    @property
    def season_start_month(self):
        self._load()
        return self._config["season_start_month"]

    def _load(self):
        if self._config:
            return
        self._read_json_file()

    def _read_json_file(self):
        with open(self._filename, 'r') as f:
            self._config = json.load(f)
