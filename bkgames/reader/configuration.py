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

    def _load(self):
        if self._config:
            return self._config
        
        self._read_json_file()

    def _read_json_file(self):
        with open(self._filename, 'r') as f:
            self._config = json.load(f)
