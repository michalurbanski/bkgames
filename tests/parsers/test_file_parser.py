import pytest
from bkgames.parsers import TeamFrequencyParser, FileParser
from bkgames.validators import TeamsValidator

SEASON_START_MONTH = 9


@pytest.fixture
def team_frequency_parser():
    return TeamFrequencyParser(SEASON_START_MONTH)


@pytest.fixture
def teams_validator():
    return TeamsValidator(["hou", "lal", "nyk", "mil"])


class TestFileParser:
    def test_parsed_file_has_parsed_lines_collection(
        self, team_frequency_parser, teams_validator
    ):
        lines = [
            "DONE - Nba game 20.10 hou at lal -> hou",
            "DONE - Nba game 22.10 nyk at mil -> mil",
        ]

        file_parser = FileParser(lines, team_frequency_parser, teams_validator)
        file_parser.run()
        assert len(file_parser.parsed_lines) == 2

    def test_parsed_file_has_not_parsed_lines(
        self, team_frequency_parser, teams_validator
    ):
        lines = ["1", "2"]

        file_parser = FileParser(lines, team_frequency_parser, teams_validator)
        file_parser.run()
        assert len(file_parser.not_parsed_lines) == 2

    def test_parsed_file_has_both_parsed_and_not_parsed_lines(
        self, team_frequency_parser, teams_validator
    ):
        lines = ["DONE - Nba game 20.10 hou at lal -> hou", "1"]

        file_parser = FileParser(lines, team_frequency_parser, teams_validator)
        file_parser.run()
        assert len(file_parser.parsed_lines) == 1
        assert len(file_parser.not_parsed_lines) == 1

    def test_line_correctly_parsed_but_with_invalid_team_is_treated_as_not_parsed(
        self, team_frequency_parser, teams_validator
    ):
        lines = ["DONE - Nba game 20.10 hwu at lal -> hwu"]
        file_parser = FileParser(lines, team_frequency_parser, teams_validator)
        file_parser.run()
        assert len(file_parser.not_parsed_lines) == 1
