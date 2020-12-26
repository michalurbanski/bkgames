from typing import List, Tuple
from datetime import datetime


class TeamsToWatchPrinter:

    def __init__(self, data: List[Tuple[str, int, List[datetime], datetime]]):
        self._data = data

    def print_teams_to_watch(self):
        for team in self._data:
            print(team[0], team[1])
