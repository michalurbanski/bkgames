import unittest
from bkgames.gameshistory import GamesHistoryOperations
from datetime import datetime

class TestGamesHistoryOperations(unittest.TestCase):

    def setUp(self):
        self.team_frequency = {
            "first_team" : [datetime(2019, 3, 3), datetime(2019, 3, 4)],
            "second_team": [datetime(2019, 1, 1)]
        }

    def test_order_by_games_played_returns_teams_with_most_played_games_on_top(self):
        
        # list of tuples
        most_played_games = GamesHistoryOperations.order_by_games_played(self.team_frequency)
        
        first_team = most_played_games[0]
        second_team = most_played_games[-1]
        self.assertGreaterEqual(first_team[1], second_team[1])
    
    def test_order_by_most_recent_games_returns_most_recent_games_on_top(self):
        oldest_played_games = GamesHistoryOperations.order_by_most_recent_games(self.team_frequency)

        first_team = oldest_played_games[0]
        second_team = oldest_played_games[1]

        self.assertEqual(first_team[0], "first_team")
        self.assertEqual(second_team[0], "second_team")

    # TODO: test case for situation when there's only one entry (KeyError handling)
