class TeamModel:
    """
    Represents team that have dates when it played
    """

    def __init__(self, team_code: str):
        self.team_code = team_code
        self._games_dates = []

    def add_game(self, game_date):
        self._games_dates.append(game_date)

    @property
    def games(self):
        return self._games_dates

    @property
    def team_code(self):
        return self._team_code

    @team_code.setter
    def team_code(self, value):
        self._team_code = value
