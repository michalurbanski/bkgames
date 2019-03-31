from datetime import datetime
from bkgames.reader.team_model import TeamModel
from .games_history_operations import GamesHistoryOperations

class GamesHistory:

    def __init__(self):
        self._teams = {}

    def add_game(self, home_team, away_team, date):
        team = TeamModel(home_team)
        team.add_game(date)

        team2 = TeamModel(away_team)
        team2.add_game(date)
        self._teams[team.team_code] = team
        self._teams[team2.team_code] = team2

    def get_teams_frequency(self):
        """
        Converts team_model to dictionary that is expected by other logic.
        """
        # NOTE: It's possible to use model all the way instead of dictionary - to be considered
        results = {}
        
        for key, team in self._teams.items():
            results[key] = team.games
        
        return results


        # results = { 
        #     "first_team": [datetime(2019, 3, 22), datetime(2019, 5, 5)],
        #     "second_team": [datetime(2019, 3, 2)],
        #     "third_team": [datetime(2019, 3, 5)]
        # }
        # return results

    # TODO: consider where to move this method, like a new WatchStatistics class or so
    def get_teams_to_watch(self, teams_frequency):
        if teams_frequency is None:
            raise TypeError

        if len(teams_frequency) == 0:
            raise ValueError("List cannot be empty")

        ordered_by_games_played = GamesHistoryOperations.order_by_games_played(teams_frequency)
        ordered_by_most_recent_games = GamesHistoryOperations.order_by_most_recent_games(teams_frequency)

        oldest_games_dict = {item[0]: item[1] for item in ordered_by_most_recent_games}
        result = [(item[0], item[1], item[2], oldest_games_dict.get(item[0], None)) for item in ordered_by_games_played]

        return sorted(result, key = lambda x: (x[1], x[3]), reverse = True)
