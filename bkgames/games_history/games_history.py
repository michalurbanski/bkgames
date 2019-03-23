from datetime import datetime
from .games_history_operations import GamesHistoryOperations

class GamesHistory:

    def get_teams_frequency(self):
        results = { 
            "first_team": [datetime(2019, 3, 22), datetime(2019, 5, 5)],
            "second_team": [datetime(2019, 3, 2)],
            "third_team": [datetime(2019, 3, 5)]
        }
        return results

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
