class Reader:
    
    def __init__(self, path_to_file):
        self._path_to_file = path_to_file

    def read(self):
        """ 
        First simple implementation reads all lines at once to list.
        """
        lines = []

        with open(self._path_to_file, mode = "r") as f:
            for line in f:
                lines.append(line.strip())

        return lines
