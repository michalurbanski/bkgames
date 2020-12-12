class FileParser:
    """ Goes through each line of input file and performs operation on it """

    def __init__(self, lines, lines_parser, teams_validator):
        # There's not a lot of lines to be processed, so we can just read
        # them all into memory.
        self._lines = lines
        self._lines_parser = lines_parser
        self._teams_validator = teams_validator
        self._not_parsed_lines = []
        self._parsed_lines = []

    def run(self):
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
    def parsed_lines(self):
        return self._parsed_lines

    @property
    def not_parsed_lines(self):
        return self._not_parsed_lines
