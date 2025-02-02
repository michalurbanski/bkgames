import pytest
from unittest.mock import MagicMock
from bkgames.configuration import ConfigFileReader
from pydantic import ValidationError


class TestConfig:
    def test_config_missing_input_property_throws_validation_exception(self):
        # This is json with missing data.
        json = {"season_start_month": 9}

        reader = ConfigFileReader("config.json")
        reader._read_file = MagicMock(return_value=json)

        with pytest.raises(ValidationError):
            _ = reader.read()

    def test_config_with_all_properties_validated_success(self):
        json = {
                "season_start_month": 9,
                "data_file_regexp": ".*",
                "allowed_teams": [],
                "skipped_teams": [],
                }
        
        reader = ConfigFileReader("config.json")
        reader._read_file = MagicMock(return_value=json)
        _ = reader.read()
    
