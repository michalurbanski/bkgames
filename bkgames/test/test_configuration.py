import unittest
from unittest.mock import MagicMock
from bkgames.reader.configuration import Configuration

class TestConfiguration(unittest.TestCase):
    
    def test_config_has_year(self):
        configuration = Configuration("config.json")
        self.assertIs(type(configuration.season_year), int)

    def test_config_has_allowed_teams_collection(self):
        configuration = Configuration("config.json")
        self.assertIs(type(configuration.allowed_teams), list)

    def test_config_can_be_called_twice(self):
        configuration = Configuration("config.json")
        season_year = configuration.season_year
        configuration._read_json_file = MagicMock()        
        
        season_year = configuration.season_year

        # Second time configuration is taken from cache
        self.assertFalse(configuration._read_json_file.called)

    def test_config_is_singleton(self):
        configuration = Configuration("config.json")
        conf2 = Configuration("config.json")
        self.assertEqual(configuration, conf2)
        
