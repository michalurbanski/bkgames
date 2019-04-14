import unittest
import datetime
from bkgames.parsers import ValidTeamParser

class TestValidTeamParser(unittest.TestCase):

    def test_valid_team_maintains_parsing_result(self):
        previous_parsing_result = {
            "home_team": "okc",
            "away_team": "hou",
            "date": datetime.datetime(2018, 12, 1),
            "line": "This is input line, content not relevant here"
        }

        valid_teams = ["okc", "hou"] # read from file
        valid_team_parser = ValidTeamParser(valid_teams)
        result, data = valid_team_parser.parse(previous_parsing_result)
        
        self.assertTrue(result)
        self.assertEqual(data, previous_parsing_result)

    def test_invalid_team_marks_line_as_not_parsed_even_if_previously_successful(self):
        previous_parsing_result = {
            "home_team": "okc",
            "away_team": "hwo",
            "date": datetime.datetime(2018, 12, 1),
            "line": "This is input line, content not relevant here"
        }
        valid_teams = ["okc", "hou"]
        valid_team_parser = ValidTeamParser(valid_teams)
        result, data = valid_team_parser.parse(previous_parsing_result)
        
        self.assertFalse(result)
        self.assertIsNotNone(data["not_parsed"]) 
        self.assertIsNotNone(data["error"])
        self.assertRaises(KeyError, lambda: data["traceback"]) # It's validation based on list, so no traceback expected
