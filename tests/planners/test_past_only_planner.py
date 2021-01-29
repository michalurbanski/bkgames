import unittest
from datetime import datetime
from bkgames.gameshistory import GamesHistory
from bkgames.planners.past_only_planner import PastOnlyPlanner


class TestPastOnlyPlanner(unittest.TestCase):
    def test_most_games_team_at_the_top_least_games_and_oldest_at_the_bottom(self):
        """
            input:
            bos, atl, 2020-01-05
            bos, phx, 2020-01-10

            should give the following outcome:
            bos -> at the top
            atl -> at the bottom
        """
        bos = "bos"
        atl = "atl"
        phx = "phx"
        first_game_date = datetime(2020, 1, 5)
        second_game_date = datetime(2020, 1, 10)

        games = list()
        games.append(self._make_game(atl, bos, first_game_date))
        games.append(self._make_game(phx, bos, second_game_date))

        games_history = GamesHistory()
        teams = games_history.build_teams_history(games)
        games_planner = PastOnlyPlanner(teams)
        teams_to_watch = games_planner.get_teams_to_watch()

        self.assertEqual(teams_to_watch[0][0], bos)
        self.assertEqual(teams_to_watch[-1][0], atl)

    def test_empty_list_of_games_throws_error(self):
        games = list()
        games_history = GamesHistory()
        teams = games_history.build_teams_history(games)

        games_planner = PastOnlyPlanner(teams)

        self.assertRaises(ValueError, games_planner.get_teams_to_watch)

    @staticmethod
    def _make_game(home_team, away_team, date):
        return {
            "home_team": home_team,
            "away_team": away_team,
            "date": date
        }
