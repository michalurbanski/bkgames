from bkgames.reader import TeamModel
from typing import List, Dict
from datetime import datetime


class GamesHistory:
    def __init__(self):
        self._teams = {}

    def build_teams_history(self, games: List[dict]) -> Dict[str, TeamModel]:
        """
        Converts list of parsed lines to a dictionary with teams.

        Returns:
            Dictionary -> (team_code, TeamModel)
        """
        for game in games:
            # Dictionary item created as a result of parsing input file
            # is unpacked here.
            # Unpacking tries to match passed object properties as function
            # parameters.
            self._add_game(**game)

        return self._teams

    # Note: **kwargs is used here because object that is passed has a 'line' key
    # that is not used by this method, but this key used in a different logic,
    # so it cannot be removed from the passed object.

    def _add_game(
        self, home_team: str, away_team: str, date: datetime, **kwargs
    ):  # pylint: disable=unused-argument
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
