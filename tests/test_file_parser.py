import unittest
from unittest.mock import Mock
import datetime
from bkgames.reader import Configuration
from bkgames.parsers import TeamFrequencyParser, ValidTeamParser, FileParser
from bkgames.gameshistory import GamesHistory

class TestFileParser(unittest.TestCase):
    
    def setUp(self):
        self.line_parser = TeamFrequencyParser(2018)
        self.teams_parser = ValidTeamParser(["hou", "lal", "nyk", "mil"]) # contains list of teams from examples used in this file
        self.games_history_results = GamesHistory()


    def test_parsed_file_has_results_collection(self):
        lines = [
            'DONE - Nba game 20.10 hou at lal -> hou',
            'DONE - Nba game 22.10 nyk at mil -> mil'
        ]
        
        file_parser = FileParser(lines, self.line_parser, self.teams_parser, self.games_history_results)
        file_parser.run()
        self.assertEqual(len(file_parser.results), 4) # 4 teams should be identified


    def test_parsed_file_has_not_parsed_lines(self):
        lines = ['1', '2']

        file_parser = FileParser(lines, self.line_parser, self.teams_parser, self.games_history_results)
        file_parser.run()
        self.assertEqual(len(file_parser.not_parsed_lines), 2)


    def test_parsed_file_has_both_parsed_and_not_parsed_lines(self):
        lines = [
            'DONE - Nba game 20.10 hou at lal -> hou',
            '1'
        ]

        file_parser = FileParser(lines, self.line_parser, self.teams_parser, self.games_history_results)
        file_parser.run()
        self.assertEqual(len(file_parser.results), 2)
        self.assertEqual(len(file_parser.not_parsed_lines), 1)
        

