from .config import Config
import json


class ConfigFileReader:
    def __init__(self, file_path: str):
        self._file_path = file_path

    def read(self) -> Config:
        content = self._read_file()
        return Config.from_dict(content)

    def _read_file(self) -> dict:
        with open(self._file_path, "r") as f:
            return json.load(f)
