import unittest
from bkgames.games_history import GamesHistory
from datetime import datetime

class TestGamesHistory(unittest.TestCase):

    def test_get_games_frequency_by_team_returns_list_of_teams(self):
        games_history = GamesHistory()
        teams_frequency = games_history.get_teams_frequency()
        self.assertGreater(len(teams_frequency), 0)

    def test_single_team_frequency_has_expected_information(self):
        games_history = GamesHistory()
        teams_frequency = games_history.get_teams_frequency()
        
        # Expected properties:
        # - key: Name of the team
        # - value: list of values:
        # -- For each game played by the team, date of a game

        # Get first element, but as all should have the same structure it can be really any element
        entry = next(iter(teams_frequency.items()))
        team_name = entry[0]
        games = entry[1]
        game = next(iter(games))
        
        self.assertIsInstance(team_name, str)
        self.assertIsInstance(game, datetime)
        

    # TODO: probably moved to a different class where operations on collections will be implemented
    # def test_get_longest_time_passed_since_watching_team(self):
    #     pass
