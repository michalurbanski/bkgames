from bkgames.reader import TeamModel
from bkgames.gameshistory.games_history_operations import GamesHistoryOperations
from typing import List, Tuple, Dict
from datetime import datetime


class GamesHistory:

    def __init__(self):
        self._teams = {}

    def build_games_history(self, games: List[dict]) -> Dict[str, TeamModel]:
        """
        Converts list of games to dictionary with teams.
        """
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
