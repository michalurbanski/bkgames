class FileParser:
    """ Goes through each line of input file and performs operation on it """

    def __init__(self, lines, lines_parser, teams_parser):
        # There's not a lot of lines to be processed, so we can just read
        # them into memory.
        self._lines = lines
        self._lines_parser = lines_parser
        self._teams_parser = teams_parser
        self._not_parsed_lines = []
        self._parsed_lines = []

    def run(self):
        """ Goes through each line and parses it according to specified rules,
        or adds to not parsed lines """

        # TODO: fix this method - remove nested ifs
        for line in self._lines:
            parsing_status, data = self._lines_parser.parse(line)
            if parsing_status:
                parsing_status, data = self._teams_parser.parse(data)
                if parsing_status:
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
