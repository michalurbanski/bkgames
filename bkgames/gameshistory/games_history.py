from bkgames.reader import TeamModel
from typing import List, Dict
from datetime import datetime


class GamesHistory:
    def __init__(self):
        self._teams = {}

    def build_teams_history(self, games: List[dict]) -> List[TeamModel]:
        """Adds games from parsed lines to teams.

        Returns:
            List of teams with dates of their games.
        """
        for game in games:
            # Dictionary item created as a result of parsing input file
            # is unpacked here.
            # Unpacking tries to match passed object properties as function
            # parameters.
            self._add_game(**game)

        return list(self._teams.values())

    # Note: **kwargs is used here because object that is passed has a 'line' key
    # that is not used by this method, but this key used in a different logic,
    # so it cannot be removed from the passed object.

    def _add_game(
        self, home_team: str, away_team: str, date: datetime, **kwargs
    ):  # pylint: disable=unused-argument
        """Adds parsed game to TeamModel object.

        Args:
            home_team (str): home team code
            away_team (str): away team code
            date (datetime): date of played game
        """

        team = self._add_game_to_team(home_team, date)
        team2 = self._add_game_to_team(away_team, date)

        self._teams[team.team_code] = team
        self._teams[team2.team_code] = team2

    def _add_game_to_team(self, team_code, date):
        existing_team = self._teams.get(team_code, None)
        if existing_team is None:
            existing_team = TeamModel(team_code)
        existing_team.add_game(date)
        return existing_team
