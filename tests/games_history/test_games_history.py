import unittest
from bkgames.gameshistory import GamesHistory
from datetime import datetime


class TestGamesHistory(unittest.TestCase):
    def test_add_game_results_in_two_teams_having_the_same_game_date(self):
        games_history = GamesHistory()
        home_team = "bos"
        away_team = "tor"
        date = datetime(2018, 10, 13)

        game_dictionary = self._make_game(home_team, away_team, date)
        games = list()
        games.append(game_dictionary)

        teams = games_history.build_teams_history(games)
        self.assertEqual(len(teams), 2)
        self.assertEqual(teams[0].games[0], teams[0].games[0])

    def test_add_game_to_existing_team_should_have_two_game_dates(self):
        # First game
        games_history = GamesHistory()
        home_team = "bos"
        away_team = "tor"
        date = datetime(2018, 10, 13)
        game_dictionary = self._make_game(home_team, away_team, date)
        games = list()
        games.append(game_dictionary)

        # Add second game for the same home_team
        away_team = "phx"
        date = datetime(2018, 10, 15)
        game_dictionary = self._make_game(home_team, away_team, date)
        games.append(game_dictionary)

        teams = games_history.build_teams_history(games)
        self.assertEqual(len(teams), 3)

        # 'next' finds first occurrence
        selected_team = next(team for team in teams if team.team_code == home_team)

        self.assertEqual(
            len(selected_team.games), 2, "Home team should have 2 game dates"
        )

    @staticmethod
    def _make_game(home_team, away_team, date):
        return {"home_team": home_team, "away_team": away_team, "date": date}
