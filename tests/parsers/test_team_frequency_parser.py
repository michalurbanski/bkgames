import pytest
from bkgames.parsers import TeamFrequencyParser, ParsedLine, NotParsedLine
from bkgames.models import GameDate

SEASON_START_MONTH = 9


# Fixture has to be outside of the class under test definition.
@pytest.fixture
def team_frequency_parser():
    return TeamFrequencyParser(SEASON_START_MONTH)


valid_test_data = [
    pytest.param(
        "DONE - Nba game 16.10 phi at bos -> bos?",
        "phi",
        "bos",
        GameDate(month=10, day=16, season_start_month=SEASON_START_MONTH),
        id="valid_line_full_date",
    ),
    pytest.param(
        "DONE - Nba game 1.11 sac at atl -> atl",
        "sac",
        "atl",
        GameDate(month=11, day=1, season_start_month=SEASON_START_MONTH),
        id="valid_line_short_date",
    ),
    pytest.param(
        "DONE - Nba game 12.12 det at cha -> cha (cha 14:13; det 13:13) ",
        "det",
        "cha",
        GameDate(month=12, day=12, season_start_month=SEASON_START_MONTH),
        id="valid_line_with_additional_data",
    ),
]


class TestTeamFrequenceParsers:
    @pytest.mark.parametrize("input, away_team, home_team, game_date", valid_test_data)
    def test_parse_line_correct(
        self,
        team_frequency_parser: TeamFrequencyParser,
        input: str,
        away_team: str,
        home_team: str,
        game_date: GameDate,
    ):
        result = team_frequency_parser.parse(input)

        assert isinstance(result, ParsedLine)
        assert result.away_team == away_team
        assert result.home_team == home_team
        assert result.game_date == game_date
        assert result.raw_line == input

    def test_parse_line_no_date_not_parsed(
        self, team_frequency_parser: TeamFrequencyParser
    ):
        input = "Line with incorrect data"

        result = team_frequency_parser.parse(input)

        assert isinstance(result, NotParsedLine)
        assert result.raw_line == input
        assert type(result.error) == ValueError
        assert result.traceback is not None
