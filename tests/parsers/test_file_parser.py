import pytest
from bkgames.parsers import TeamFrequencyParser, FileParser
from bkgames.validators import TeamsValidator

SEASON_START_MONTH = 9


@pytest.fixture
def team_frequency_parser() -> TeamFrequencyParser:
    return TeamFrequencyParser(SEASON_START_MONTH)


# TODO: shouldn't the class be now called TeamValidator (singular)?
@pytest.fixture
def teams_validator() -> TeamsValidator:
    return TeamsValidator(["hou", "lal", "nyk", "mil"])


@pytest.fixture
def file_parser(
    team_frequency_parser: TeamFrequencyParser,
    teams_validator: TeamsValidator,
) -> FileParser:
    return FileParser(team_frequency_parser, teams_validator)


# TODO: this could be now array tests
class TestFileParser:
    def test_parsed_file_has_parsed_lines_collection(self, file_parser: FileParser):
        lines = [
            "DONE - Nba game 20.10 hou at lal -> hou",
            "DONE - Nba game 22.10 nyk at mil -> mil",
        ]

        results = file_parser.run(lines)

        assert len(results.parsed_lines) == 2

    def test_parsed_file_has_not_parsed_lines(self, file_parser: FileParser):
        lines = ["1", "2"]

        results = file_parser.run(lines)

        assert len(results.not_parsed_lines) == 2

    def test_parsed_file_has_both_parsed_and_not_parsed_lines(
        self, file_parser: FileParser
    ):
        lines = ["DONE - Nba game 20.10 hou at lal -> hou", "1"]

        results = file_parser.run(lines)

        assert len(results.parsed_lines) == 1
        assert len(results.not_parsed_lines) == 1

    def test_line_correctly_parsed_but_with_invalid_team_is_treated_as_not_parsed(
        self, file_parser: FileParser
    ):
        lines = ["DONE - Nba game 20.10 hwu at lal -> hwu"]

        results = file_parser.run(lines)

        assert len(results.not_parsed_lines) == 1
