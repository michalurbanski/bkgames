from copy import deepcopy
from typing import List
from .game_date import GameDate
from functools import total_ordering


# Note: one could argue that this class' responsibilities do not fit the name
#       of this class. This class is defined in this way for simplicity.
@total_ordering
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
    
    # Note: It's necessary for the TeamModel type to be used in this way, as it's only defined in this file.
    def __lt__(self, obj: "TeamModel"):
        if self.number_of_games_played < obj.number_of_games_played:
            return True
        
        if self.number_of_games_played > obj.number_of_games_played:
            return False
        
        # The same number of games played. The one that played earlier is less.
        self_games_dates = sorted(self.games_dates)
        length = len(self_games_dates)
        obj_games_dates = sorted(obj.games_dates)

        for i in range(length):
            minus_index = -(i+1)
            if self_games_dates[minus_index] == obj_games_dates[minus_index]:
                continue

            if self_games_dates[minus_index] < obj_games_dates[minus_index]:
                return True
            
            return False


        # When not returned earlier it means that all teams have exactly the same dates.
        # It's arbitrary to say which is less.
        return True

    def __eq__(self, obj: "TeamModel"):
        if self.number_of_games_played != obj.number_of_games_played:
            return False
        
        obj_games_dates = obj.games_dates
        for i, game_date in enumerate(self.games_dates):
            if game_date == obj_games_dates[i]:
                continue

            return False

        return True

