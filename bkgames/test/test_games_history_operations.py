import unittest
from bkgames.games_history import GamesHistoryOperations
from datetime import datetime

class TestGamesHistoryOperations(unittest.TestCase):

    def setUp(self):
        self.team_frequency = {
            "first_team" : [datetime(2019, 3, 3), datetime(2019, 3, 4)],
            "second_team": [datetime(2019, 1, 1)]
        }

    def test_order_by_games_played(self):
        
        # list of tuples
        most_played_games = GamesHistoryOperations.order_by_games_played(self.team_frequency)
        
        first_team = most_played_games[0]
        second_team = most_played_games[-1]
        self.assertGreaterEqual(first_team[1], second_team[1])
    
    # TODO: test case for situation when there's only one entry (KeyError handling)
