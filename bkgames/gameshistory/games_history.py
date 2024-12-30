from bkgames.models import TeamModel, GameDate
from typing import List


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
        self, home_team: str, away_team: str, game_date: GameDate, **kwargs
    ):  # pylint: disable=unused-argument
        """Adds parsed game to TeamModel object.

        Args:
            home_team (str): home team code
            away_team (str): away team code
            game_date (GameDate): object that contains date of played game

            kwargs is needed because object passed to this method is being unpacked
            when the method is called.
        """

        home = self._add_game_to_team(home_team, game_date)
        away = self._add_game_to_team(away_team, game_date)

        self._teams[home.team_code] = home
        self._teams[away.team_code] = away

    def _add_game_to_team(self, team_code: str, game_date: GameDate):
        existing_team = self._teams.get(team_code, None)
        if existing_team is None:
            existing_team = TeamModel(team_code)

        existing_team.add_game(game_date)
        return existing_team
