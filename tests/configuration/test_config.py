import unittest
from unittest.mock import MagicMock
from bkgames.configuration import Config, ConfigFileReader


class TestConfig(unittest.TestCase):

    def test_config_can_have_empty_properties(self):
        config = Config()
        json = {
            "season_year": 2018
        }
        reader = ConfigFileReader("config.json")
        reader._read_file = MagicMock(return_value=json)
        reader.read(config)

        # has season_year property
        # and if others are missing then object creation doesn't fail
        self.assertEqual(2018, config.season_year)
