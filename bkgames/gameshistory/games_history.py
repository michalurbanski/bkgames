from bkgames.reader import TeamModel
from bkgames.gameshistory.games_history_operations import GamesHistoryOperations
from typing import List, Tuple, Dict
from datetime import datetime


class GamesHistory:

    def __init__(self):
        self._teams = {}

    def build_games_history(self, games: List[dict]) -> Dict[str, TeamModel]:
        for game in games:
            self._add_game(**game)

        return self._teams

    # Note: **kwargs is used here because object that is passed has a 'line' key
    # that is not used by this method, but this key used in a different logic,
    # so it cannot be removed from the passed object.

    def _add_game(self, home_team, away_team, date, **kwargs):  # pylint: disable=unused-argument
        team = self._add_game_to_team(home_team, date)
        team2 = self._add_game_to_team(away_team, date)

        self._teams[team.team_code] = team
        self._teams[team2.team_code] = team2

    def _add_game_to_team(self, team, date):
        existing_team = self._teams.get(team, None)
        if existing_team is None:
            existing_team = TeamModel(team)
        existing_team.add_game(date)
        return existing_team

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
        for key, team in self._teams.items():
            results[key] = team.games
        self._teams_frequency = results

    # TODO: consider where to move this method, like a new WatchStatistics class or so
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
