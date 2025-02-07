import pytest
import datetime
from bkgames.validators import TeamsValidator


class TestTeamsValidator:
    def test_valid_team_maintains_parsing_result(self):
        previous_parsing_result = {
            "home_team": "okc",
            "away_team": "hou",
            "date": datetime.datetime(2018, 12, 1),
            "line": "This is input line, content not relevant here"
        }

        valid_teams = ["okc", "hou"]  # read from file
        valid_team_parser = TeamsValidator(valid_teams)
        result, data = valid_team_parser.validate(previous_parsing_result)

        assert result == True
        assert data == previous_parsing_result

    def test_invalid_team_marks_line_as_not_parsed_even_if_previously_successful(self):
        previous_parsing_result = {
            "home_team": "okc",
            "away_team": "hwo",
            "date": datetime.datetime(2018, 12, 1),
            "line": "This is input line, content not relevant here"
        }
        valid_teams = ["okc", "hou"]
        valid_team_parser = TeamsValidator(valid_teams)
        result, data = valid_team_parser.validate(previous_parsing_result)

        assert result == False
        assert data["not_parsed"] is not None
        assert data["error"] is not None

        # It's validation based on list, so no traceback expected.
        with pytest.raises(KeyError):
            data["traceback"]
