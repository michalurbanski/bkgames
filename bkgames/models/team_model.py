from datetime import datetime
from typing import List


class TeamModel:
    """
    Represents team that have dates when it played
    """

    def __init__(self, team_code: str):
        self.team_code = team_code
        self._games_dates = []
        self.skip_from_watching = False

    def add_game(self, game_date: datetime):
        self._games_dates.append(game_date)

    # TODO: name of this property is confusing, it should be indicate that this field is about dates of games, not games
    @property
    def games(self) -> List[datetime]:
        return self._games_dates

    @property
    def number_of_games_played(self) -> int:
        return len(self.games)

    @property
    def team_code(self) -> str:
        return self._team_code

    @property
    def skip_from_watching(self) -> bool:
        return self._skip_from_watching

    @team_code.setter
    def team_code(self, value: str):
        self._team_code = value

    @skip_from_watching.setter
    def skip_from_watching(self, value: bool):
        self._skip_from_watching = value

    def __repr__(self):
        games = [date.strftime("%Y-%m-%d") for date in self._games_dates]
        return f"Team: {self._team_code}, Games: {games}"
