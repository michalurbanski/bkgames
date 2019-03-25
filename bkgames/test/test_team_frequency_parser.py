import unittest
from datetime import datetime
from bkgames.parsers import *

class TestTeamFrequencyParser(unittest.TestCase):
    
    def test_parse_line_returns_teams_and_date_of_the_game(self):
        input = "DONE - Nba game 16.10 phi at bos -> bos?"
        result = TeamFrequencyParser.Parse(input)
        
        self.assertEqual(result["home_team"], "phi")
        self.assertEqual(result["away_team"], "bos")
        # TODO: to be set somewhere in config for which year application should run
        self.assertEqual(result["date"], datetime(2018, 10, 16))

    def test_parse_line_with_standings_returns_teams_and_date_of_the_game(self):
        input = "DONE - Nba game 12.12 det at cha -> cha (cha 14:13; det 13:13) "
        result = TeamFrequencyParser.Parse(input)

        self.assertEqual(result["home_team"], "det")
        self.assertEqual(result["away_team"], "cha")
        self.assertEqual(result["date"], datetime(2018, 12, 12))

    # TODO: add more examples of lines (like the one with results, and check if it works OK)
