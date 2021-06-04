from typing import List

# TODO: change name of this class


class FileParser:
    """ Goes through each line of input file and performs operation on it """

    def __init__(self, lines: List[str], lines_parser, teams_validator):
        self._lines = lines
        self._lines_parser = lines_parser
        self._teams_validator = teams_validator
        self._not_parsed_lines = []
        self._parsed_lines = []

    def run(self) -> None:
        """ Goes through each line and parses it according to specified rules,
        or adds to not parsed lines """

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
        return self._parsed_lines

    @ property
    def not_parsed_lines(self) -> List[dict]:
        return self._not_parsed_lines
