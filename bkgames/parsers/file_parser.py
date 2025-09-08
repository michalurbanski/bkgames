from typing import List
from bkgames.parsers import LineParserBase, FileParsingResult
from bkgames.validators import TeamsValidator


# TODO: change name of this class (?) -> it parses input lines, not file ?
class FileParser:
    """FileParser parses lines using a validator.
    If validator check doesn't pass, then lines is added to not parsed lines."""

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
            # TODO: data is passed twice below? + if/else could be simplified?
            parsing_status, data = self._lines_parser.parse(line)
            if parsing_status:
                validation_status, data = self._teams_validator.validate(data)
                if validation_status:
                    results.parsed_lines.append(data)
                else:
                    results.not_parsed_lines.append(data)
            else:
                results.not_parsed_lines.append(data)

        return results

    # @property
    # def parsed_lines(self) -> List[dict]:
    #     """Each dictionary entry has the following keys:

    #     Returns:
    #         List of the following dictionaries (home_team, away_team, data, line)
    #     """
    #     return self._parsed_lines

    # @property
    # def not_parsed_lines(self) -> List[dict]:
    #     return self._not_parsed_lines
