import unittest
from bkgames.games_history import GamesHistory

class TestGamesHistory(unittest.TestCase):

    def test_get_games_frequency_by_team_returns_list_of_teams(self):
        games_history = GamesHistory()
        teams_frequency = games_history.get_teams_frequency()
        self.assertGreater(len(teams_frequency), 0)

    # TODO: probably moved to a different class where operations on collections will be implemented
    # def test_get_longest_time_passed_since_watching_team(self):
    #     pass
