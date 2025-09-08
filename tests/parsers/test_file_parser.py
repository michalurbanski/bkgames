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


testdata = [
    pytest.param(
        [
            "DONE - Nba game 20.10 hou at lal -> hou",
            "DONE - Nba game 22.10 nyk at mil -> mil",
        ],
        2,
        0,
        id="_validLines_parsedCorrectly",
    ),
    pytest.param(
        ["1", "2"],
        0,
        2,
        id="_invalidLines_notParsed",
    ),
    pytest.param(
        ["DONE - Nba game 20.10 hou at lal -> hou", "1"],
        1,
        1,
        id="_mixedLines_oneParsedOneNotParsed",
    ),
    pytest.param(
        ["DONE - Nba game 20.10 hwu at lal -> hwu"],
        0,
        1,
        id="_invalidTeam_isNotParsed",
    ),
]


class TestFileParser:
    @pytest.mark.parametrize("lines, parsed, not_parsed", testdata)
    def test_parametrized(
        self, file_parser: FileParser, lines: str, parsed: int, not_parsed: int
    ):
        results = file_parser.run(lines)

        assert len(results.parsed_lines) == parsed
        assert len(results.not_parsed_lines) == not_parsed
