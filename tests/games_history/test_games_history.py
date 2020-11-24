import unittest
from bkgames.gameshistory import GamesHistory
from datetime import datetime


class TestGamesHistory(unittest.TestCase):

    def test_add_game_results_in_two_teams_having_the_same_game_date(self):
        games_history = GamesHistory()
        home_team = "bos"
        away_team = "tor"
        date = datetime(2018, 10, 13)

        game_dictionary = self._construct_game_dictionary(
            home_team, away_team, date)
        games_history.add_game(**game_dictionary)
        teams_to_watch = games_history.get_teams_to_watch()

        self.assertEqual(len(teams_to_watch), 2)

        first_team_result = self._find_team_results_in_teams_to_watch(
            teams_to_watch, home_team)
        second_team_result = self._find_team_results_in_teams_to_watch(
            teams_to_watch, away_team)

        first_team_game_date = first_team_result[-1]  # last tuple element
        second_team_game_date = second_team_result[-1]

        self.assertEqual(first_team_game_date, second_team_game_date)

    def test_add_game_to_existing_team_should_have_two_game_dates(self):
        # First game
        games_history = GamesHistory()
        home_team = "bos"
        away_team = "tor"
        date = datetime(2018, 10, 13)
        game_dictionary = self._construct_game_dictionary(
            home_team, away_team, date)
        games_history.add_game(**game_dictionary)

        # Add second game for the same home_team
        away_team = "phx"
        date = datetime(2018, 10, 15)
        game_dictionary = self._construct_game_dictionary(
            home_team, away_team, date)
        games_history.add_game(**game_dictionary)
        teams_to_watch = games_history.get_teams_to_watch()

        self.assertEqual(len(teams_to_watch), 3)  # There are 3 teams overall
        # home team has two game dates
        team_results = self._find_team_results_in_teams_to_watch(
            teams_to_watch, home_team)
        # second to last column are dates for a team
        self.assertEqual(len(team_results[-2]), 2)

    def test_single_team_results_has_expected_information(self):
        games_history = GamesHistory()
        games_history.add_game("bos", "tor", datetime(2018, 10, 13))
        teams_to_watch = games_history.get_teams_to_watch()

        # At least one entry exists
        self.assertGreater(len(teams_to_watch), 0,
                           msg="At least one team must exist")

        # Expected properties:
        # - 1st tuple element - Name of the team
        # - 2nd tuple element - number of games
        # - 3rd tuple element - list of all dates
        # - 4th tuple element - last game date

        # Get first element, but as all should have the same structure it can be really any element
        entry = teams_to_watch[0]
        team_name = entry[0]
        games_number = entry[1]
        dates_list = entry[2]
        last_game_date = entry[3]

        self.assertIsInstance(team_name, str)
        self.assertEqual(games_number, 1)
        self.assertIsInstance(dates_list, list)
        self.assertIsInstance(last_game_date, datetime)

    def test_teams_to_watch_next_returns_next_to_watch_as_last_on_the_list(self):
        games_history = GamesHistory()
        games_history.add_game("bos", "tor", datetime(2018, 10, 13))
        teams_to_watch = games_history.get_teams_to_watch()

        # Expected result is list of ("team", number_of_games_played, games, rank)
        # Order by number_of_games_played descending, and rank descending

        # check if column 2 and 4 are sorted descending
        # Assume that there are items in collection
        self.assertGreater(len(teams_to_watch), 0)

        number_of_games_played_column = [item[1] for item in teams_to_watch]
        self.assertEqual(number_of_games_played_column, sorted(
            number_of_games_played_column, reverse=True))

        rank = [item[3] for item in teams_to_watch]
        self.assertEqual(rank, sorted(rank, reverse=True))

    def test_get_teams_to_watch_getting_games_where_none_added_throws_exception(self):
        games_history = GamesHistory()
        self.assertRaises(ValueError, games_history.get_teams_to_watch)

    @staticmethod
    def _find_team_results_in_teams_to_watch(teams_to_watch, team_name):
        return [result for result in teams_to_watch if result[0] == team_name][0]

    @staticmethod
    def _construct_game_dictionary(home_team, away_team, date):
        return {
            "home_team": home_team,
            "away_team": away_team,
            "date": date
        }
