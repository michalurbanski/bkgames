from typing import List
from dataclasses import dataclass
from bkgames.parsers import LineParserBase


# TODO: extract to a separate file
@dataclass
class FileParsingResult:
    parsed_lines: List[dict]
    not_parsed_lines: List[dict]


# TODO: continue with changing this class below, lines should not be passed in the constructor.
# TODO: instead they should be passed to the run method. and then both parsed and not parsed returned in an object of class defined above.


# TODO: change name of this class (?)
class FileParser:
    """Goes through each line of input file and performs operation on it"""

    # TODO: last parameter should also have a type
    def __init__(self, lines: List[str], lines_parser: LineParserBase, teams_validator):
        self._lines = lines
        self._lines_parser = lines_parser
        self._teams_validator = teams_validator
        self._not_parsed_lines = []
        self._parsed_lines = []

    def run(self) -> None:
        """Goes through each line and parses it according to specified rules,
        or adds to not parsed lines.
        """
        for line in self._lines:
            parsing_status, data = self._lines_parser.parse(line)
            if parsing_status:
                validation_status, data = self._teams_validator.validate(data)
                if validation_status:
                    self._parsed_lines.append(data)
                else:
                    self._not_parsed_lines.append(data)
            else:
                self._not_parsed_lines.append(data)

    @property
    def parsed_lines(self) -> List[dict]:
        """Each dictionary entry has the following keys:

        Returns:
            List of the following dictionaries (home_team, away_team, data, line)
        """
        return self._parsed_lines

    @property
    def not_parsed_lines(self) -> List[dict]:
        return self._not_parsed_lines
