from bkgames.gameshistory import GamesHistoryOperations
from typing import Dict, List, Tuple
from datetime import datetime
from bkgames.reader import TeamModel


class PastOnlyPlanner:
    """ Finds teams to watch, based only on past games."""

    def __init__(self, teams_history: Dict[str, TeamModel]):
        self._teams_history = teams_history

    def get_teams_to_watch(self) -> List[Tuple[str, int, List[datetime], datetime]]:
        """
        Gets teams to watch, based on historic results.
        Team watched the longest time ago is the last in this collection.

        Returns:
            (list): List of tuples
                (team_code, number of games, list of all dates, latest date)
                # TODO: confirm if this is valid
        """
        self._get_teams_frequency()

        if self._teams_frequency is None:
            raise TypeError("Teams frequency is not defined")

        if not self._teams_frequency:
            raise ValueError("List with teams frequency cannot be empty")

        ordered_by_games_played = GamesHistoryOperations.order_by_games_played(
            self._teams_frequency)
        ordered_by_most_recent = GamesHistoryOperations.order_by_most_recent_games(
            self._teams_frequency)

        oldest_games_dict = {item[0]: item[1]
                             for item in ordered_by_most_recent}
        result = [(item[0], item[1], item[2], oldest_games_dict.get(item[0], None))
                  for item in ordered_by_games_played]

        return sorted(result, key=lambda x: (x[1], x[3]), reverse=True)

    def _get_teams_frequency(self):
        """
        Converts team_model to dictionary that is expected by other logic.

        Returns: dict()

        Example:

        results = {
            "first_team": [datetime(2019, 3, 22), datetime(2019, 5, 5)],
            "second_team": [datetime(2019, 3, 2)],
            "third_team": [datetime(2019, 3, 5)]

        }
        """
        # NOTE: It's possible to use model all the way instead of dictionary - to be considered
        results = {}
        for name, team_data in self._teams_history.items():
            results[name] = team_data.games
        self._teams_frequency = results
