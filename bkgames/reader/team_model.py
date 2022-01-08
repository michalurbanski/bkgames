from datetime import datetime
from typing import List


class TeamModel:
    """
    Represents team that have dates when it played
    """

    def __init__(self, team_code: str):
        self.team_code = team_code
        self._games_dates = []

    def add_game(self, game_date: datetime):
        self._games_dates.append(game_date)

    @property
    def games(self) -> List[datetime]:
        return self._games_dates

    @property
    def team_code(self) -> str:
        return self._team_code

    @team_code.setter
    def team_code(self, value: str):
        self._team_code = value

    def __repr__(self):
        games = [date.strftime("%Y-%m-%d") for date in self._games_dates]
        return f"Team: {self._team_code}, Games: {games}"
