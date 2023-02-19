class NotParsedLinesPrinter:

    def __init__(self, not_parsed_lines):
        self._not_parsed_lines = not_parsed_lines

    def print_not_parsed_lines(self):
        self._print_summary()
        self._print_not_parsed_lines()

    def _print_summary(self):
        print("There are {} not parsed lines".format(len(self._not_parsed_lines)))
    
    def _print_not_parsed_lines(self):
        if self._not_parsed_lines:
            print(self._not_parsed_lines)
