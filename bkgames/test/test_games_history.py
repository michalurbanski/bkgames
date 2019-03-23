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
        
    def test_teams_to_watch_next_lack_of_list_throws_exception(self):
        games_history = GamesHistory()

        self.assertRaises(TypeError, games_history.get_teams_to_watch, None)
        
    def test_teams_to_watch_next_empty_games_list_throws_exception(self):
        games_history = GamesHistory()

        self.assertRaises(ValueError, games_history.get_teams_to_watch, list())
    
    def test_teams_to_watch_next_returns_next_to_watch_as_last_on_the_list(self):
        games_history = GamesHistory()
        teams_frequency = games_history.get_teams_frequency()
        teams_to_watch = games_history.get_teams_to_watch(teams_frequency)

        # Expected result is list of ("team", number_of_games_played, games, rank)
        # Order by number_of_games_played descending, and rank descending
        
        # check if column 2 and 4 are sorted descending
        # Assume that there are items in collection
        self.assertGreater(len(teams_to_watch), 0)

        number_of_games_played_column = [item[1] for item in teams_to_watch]
        self.assertEqual(number_of_games_played_column, sorted(number_of_games_played_column, reverse = True))

        rank = [item[3] for item in teams_to_watch]
        self.assertEqual(rank, sorted(rank, reverse = True))

        


    # TODO: probably moved to a different class where operations on collections will be implemented
    # def test_get_longest_time_passed_since_watching_team(self):
    #     pass
