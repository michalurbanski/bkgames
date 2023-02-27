import unittest
from bkgames.readers import TeamModel
import datetime


class TestTeamModel(unittest.TestCase):

    def test_add_game_for_a_team_results_in_added_game(self):
        team_model = TeamModel("bos")
        date = datetime.datetime(2018, 3, 13)
        team_model.add_game(date)

        self.assertEqual(len(team_model.games), 1)
        self.assertEqual(team_model.team_code, "bos")

    def test_add_two_games_assigns_games_to_proper_teams(self):
        team_model = TeamModel("tor")
        team_model.add_game(datetime.datetime(2018, 3, 13))
        team_model.add_game(datetime.datetime(2018, 3, 15))

        self.assertEqual(len(team_model.games), 2)
        # Games are sorted by date ascending
        self.assertGreater(team_model.games[-1], team_model.games[0])
