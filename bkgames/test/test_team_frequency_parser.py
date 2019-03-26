import unittest
from datetime import datetime
from bkgames.parsers import *

class TestTeamFrequencyParser(unittest.TestCase):
    
    def setUp(self):
        self.parser = TeamFrequencyParser(2018)

    def test_parse_line_returns_teams_and_date_of_the_game(self):
        input = "DONE - Nba game 16.10 phi at bos -> bos?"
        parsing_status, result = self.parser.parse(input)
        
        self.assertTrue(parsing_status)
        self.assertEqual(result["home_team"], "phi")
        self.assertEqual(result["away_team"], "bos")
        self.assertEqual(result["date"], datetime(2018, 10, 16))

    def test_parse_line_with_standings_returns_teams_and_date_of_the_game(self):
        input = "DONE - Nba game 12.12 det at cha -> cha (cha 14:13; det 13:13) "
        parsing_status, result = self.parser.parse(input)

        self.assertTrue(parsing_status)
        self.assertEqual(result["home_team"], "det")
        self.assertEqual(result["away_team"], "cha")
        self.assertEqual(result["date"], datetime(2018, 12, 12))

    def test_parse_incorrect_data_returns_failed_status_and_not_parsed_line(self):
        input = "Line with incorrect data"
        parsing_status, result = self.parser.parse(input)

        self.assertFalse(parsing_status)
        self.assertEqual(result["not_parsed"], input)
