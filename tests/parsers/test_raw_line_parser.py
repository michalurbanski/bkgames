import pytest
from bkgames.parsers import TeamFrequencyParser, RawLineParser
from bkgames.validators import TeamsValidator


@pytest.fixture
def team_frequency_parser() -> TeamFrequencyParser:
    season_start_month = 9
    return TeamFrequencyParser(season_start_month)


@pytest.fixture
def teams_validator() -> TeamsValidator:
    return TeamsValidator(["hou", "lal", "nyk", "mil"])


@pytest.fixture
def raw_line_parser(
    team_frequency_parser: TeamFrequencyParser,
    teams_validator: TeamsValidator,
) -> RawLineParser:
    return RawLineParser(team_frequency_parser, teams_validator)


# Based on the https://docs.pytest.org/en/stable/example/parametrize.html#different-options-for-test-ids
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


class TestRawLineParser:
    @pytest.mark.parametrize("lines, parsed, not_parsed", testdata)
    def test_parametrized(
        self, raw_line_parser: RawLineParser, lines: str, parsed: int, not_parsed: int
    ):
        results = raw_line_parser.run(lines)

        assert len(results.parsed_lines) == parsed
        assert len(results.not_parsed_lines) == not_parsed
