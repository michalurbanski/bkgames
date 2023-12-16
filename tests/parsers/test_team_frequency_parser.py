import pytest
from bkgames.parsers import TeamFrequencyParser
from bkgames.models import GameDate

SEASON_START_MONTH = 9


# Fixture has to be outside of the class definition.
@pytest.fixture
def team_frequency_parser():
    return TeamFrequencyParser(SEASON_START_MONTH)


# To easier fetch values from the result object as it is not strongly typed
class ParsedResult:
    def __init__(self, result: dict):
        self._home_team = result.get("home_team")
        self._away_team = result.get("away_team")
        self._date = result.get("date")
        self._line = result.get("line")
        self._not_parsed = result.get("not_parsed")
        self._error = result.get("error")

    @property
    def home_team(self) -> str:
        return self._home_team

    @property
    def away_team(self) -> str:
        return self._away_team

    @property
    def date(self) -> GameDate:
        return self._date

    @property
    def line(self) -> str:
        return self._line

    @property
    def not_parsed(self) -> str:
        return self._not_parsed

    @property
    def error(self):
        return self._error


class TestTeamFrequenceParsers:
    def test_parse_line_returns_teams_and_date_of_the_game(self, team_frequency_parser):
        input = "DONE - Nba game 16.10 phi at bos -> bos?"
        parsing_status, result = team_frequency_parser.parse(input)
        parsed_result = ParsedResult(result)

        assert parsing_status == True
        assert parsed_result.home_team == "phi"
        assert parsed_result.away_team == "bos"
        assert parsed_result.date == GameDate(
            month=10, day=16, season_start_month=SEASON_START_MONTH
        )
        assert parsed_result.line == input

    def test_parse_line_with_single_digit_date_returns_team_and_date_of_the_game(
        self, team_frequency_parser
    ):
        input = "DONE - Nba game 1.11 sac at atl -> atl"
        parsing_status, result = team_frequency_parser.parse(input)
        parsed_result = ParsedResult(result)

        assert parsing_status == True
        assert parsed_result.home_team == "sac"
        assert parsed_result.away_team == "atl"
        assert parsed_result.date == GameDate(
            month=11, day=1, season_start_month=SEASON_START_MONTH
        )
        assert parsed_result.line == input

    def test_parse_line_with_additional_date_returns_teams_and_date_correctly(
        self, team_frequency_parser
    ):
        input = "DONE - Nba game 12.12 det at cha -> cha (cha 14:13; det 13:13) "
        parsing_status, result = team_frequency_parser.parse(input)
        parsed_result = ParsedResult(result)
        assert parsing_status == True
        assert parsed_result.home_team == "det"
        assert parsed_result.away_team == "cha"
        assert parsed_result.date == GameDate(
            month=12, day=12, season_start_month=SEASON_START_MONTH
        )
        assert parsed_result.line == input

    def test_parse_lack_of_date_in_line_returns_failed_status_and_not_parsed_line(
        self, team_frequency_parser
    ):
        input = "Line with incorrect data"
        parsing_status, result = team_frequency_parser.parse(input)
        parsed_result = ParsedResult(result)
        assert parsing_status == False
        assert parsed_result.not_parsed == input
        assert type(parsed_result.error) == ValueError
