from typing import List, Union
from bkgames.parsers import ParsedLine, NotParsedLine, LineParserBase, FileParsingResult
from bkgames.validators import TeamsValidator

# TODO: importing TeamsValidator causes import from from this file, which imports TeamValidator
# pytest tests/parsers/test_team_validator.py


class RawLineParser:
    """RawLineParser parses lines using a validator.
    If validator check doesn't pass, then line is added to not parsed lines."""

    def __init__(
        self,
        lines_parser: LineParserBase,
        teams_validator: TeamsValidator,
    ):
        self._lines_parser = lines_parser
        self._teams_validator = teams_validator

    def run(self, lines: List[str]) -> FileParsingResult:
        """Goes through each line and parses it according to specified rules.

        If successful, then adds to the parsed lines list.
        If parsing failed, then adds to the not parsed lines list.
        """

        results = FileParsingResult()

        for line in lines:
            parse_result = self._parse_line(line)
            if isinstance(parse_result, ParsedLine):
                results.parsed_lines.append(parse_result)
            else:
                results.not_parsed_lines.append(parse_result)

        return results

    def _parse_line(self, line: str) -> Union[ParsedLine, NotParsedLine]:
        parse_result = self._lines_parser.parse(line)

        # If line was parsed correctly, it may still have wrong teams in it.
        # Additional validation for team codes in the parsed line is required.
        if isinstance(parse_result, ParsedLine):
            validation_result = self._teams_validator.validate(
                parse_result.raw_line,
                parse_result.home_team,
                parse_result.away_team,
            )
            if not validation_result.is_valid:
                # TODO: this is messy - how this type is constructed does not fit usage here.
                # Maybe it fits in the TeamFrequencyParser, but definitely not here.
                return NotParsedLine(
                    parse_result.raw_line,
                    None,
                    "error occurred during parsing",
                )

        return parse_result
