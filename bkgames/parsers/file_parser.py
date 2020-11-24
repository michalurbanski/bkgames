class FileParser:
    """ Goes through each line of input file and performs operation on it """

    def __init__(self, lines, lines_parser, teams_parser, games_history):
        self._lines = lines
        self._lines_parser = lines_parser
        self._teams_parser = teams_parser
        self._games_history = games_history
        self._not_parsed_lines = []

    def run(self):
        """ Goes through each line and parses it according to specified rules,
        or adds to not parsed lines """

        # TODO: fix this method
        for line in self._lines:
            parsing_status, data = self._lines_parser.parse(line)
            if parsing_status:
                parsing_status, data = self._teams_parser.parse(data)
                if parsing_status:
                    self._games_history.add_game(**data)
                else:
                    self._not_parsed_lines.append(data)
            else:
                self._not_parsed_lines.append(data)

    # TODO: Does this method fit here? It's pretty nasty dependency
    @property
    def results(self):
        return self._games_history.get_teams_to_watch()

    @property
    def not_parsed_lines(self):
        return self._not_parsed_lines
