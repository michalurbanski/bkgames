import unittest
from unittest.mock import MagicMock
from bkgames.configuration import ConfigFileReader


class TestConfig(unittest.TestCase):
    def test_config_can_have_empty_properties(self):
        default_season_start_month = 9

        # Mocked json that is normally read from file.
        json = {"season_start_month": default_season_start_month}
        reader = ConfigFileReader("config.json")
        reader._read_file = MagicMock(return_value=json)
        config = reader.read()

        # Has only season_start_month property filled in json,
        # although other properties are available in the object.
        #
        # And if other properties' values are missing in the json,
        # then object creation doesn't fail.
        self.assertEqual(default_season_start_month, config.season_start_month)
