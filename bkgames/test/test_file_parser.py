import unittest
from unittest.mock import Mock
import datetime
from bkgames.reader.file_parser import FileParser
from bkgames.parsers.team_frequency_parser import TeamFrequencyParser
from bkgames.games_history.games_history import GamesHistory

class TestFileParser(unittest.TestCase):
    
    def setUp(self):
        self.line_parser = TeamFrequencyParser(2018)
        self.games_history_results = GamesHistory()


    def test_parsed_file_has_results_collection(self):
        lines = [
            'DONE - Nba game 20.10 hou at lal -> hou',
            'DONE - Nba game 22.10 nyk at mil -> mil'
        ]
        
        file_parser = FileParser(lines, self.line_parser, self.games_history_results)
        file_parser.run()
        self.assertEqual(len(file_parser.results), 4) # 4 teams should be identified


    def test_parsed_file_has_not_parsed_lines(self):
        lines = ['1', '2']

        file_parser = FileParser(lines, self.line_parser, self.games_history_results)
        file_parser.run()
        self.assertEqual(len(file_parser.not_parsed_lines), 2)


    def test_parsed_file_has_both_parsed_and_not_parsed_lines(self):
        lines = [
            'DONE - Nba game 20.10 hou at lal -> hou',
            '1'
        ]

        file_parser = FileParser(lines, self.line_parser, self.games_history_results)
        file_parser.run()
        self.assertEqual(len(file_parser.results), 2)
        self.assertEqual(len(file_parser.not_parsed_lines), 1)
        

