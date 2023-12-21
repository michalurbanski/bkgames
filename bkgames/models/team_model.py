from copy import deepcopy
from typing import List
from .game_date import GameDate


# Note: one could argue that this class' responsibilities do not fit the name
#       of this class. This class is defined in this way for simplicity.
class TeamModel:
    """
    Represents team that have dates when it played
    """

    def __init__(self, team_code: str):
        self.team_code = team_code
        self._games_dates = []
        self.skip_from_watching = False

    def add_game(self, game_date: GameDate):
        self._games_dates.append(game_date)

    @property
    def games_dates(self) -> List[GameDate]:
        # Probably even if it wasn't a deepcopy nothing bad would happen.
        return deepcopy(self._games_dates)

    @property
    def number_of_games_played(self) -> int:
        return len(self.games_dates)

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
        return f"Team: {self.team_code}, Games: {self.games_dates}"
