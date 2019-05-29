import unittest
from bkgames.helpers import game_helper

class TestGameHelper(unittest.TestCase):

    def test_month_later_than_start_month_should_return_season_start_year(self):
        month = 8
        season_start_month = 7
        season_start_year = 2018

        calculated_year = game_helper.calculate_game_year(
            season_start_year,
            season_start_month,
            month
        )

        self.assertEqual(calculated_year, season_start_year)

    def test_month_earlier_than_start_month_should_return_year_after_start_year(self):
        month = 3
        season_start_month = 7
        season_start_year = 2018

        calculated_year = game_helper.calculate_game_year(
            season_start_year,
            season_start_month,
            month
        )

        self.assertEqual(calculated_year, season_start_year + 1)
        

        
