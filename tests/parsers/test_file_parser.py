import unittest
import datetime
from bkgames.parsers import TeamFrequencyParser, FileParser
from bkgames.validators import TeamsValidator
from bkgames.gameshistory import GamesHistory


class TestFileParser(unittest.TestCase):

    def setUp(self):
        self.line_parser = TeamFrequencyParser(2018, 9)
        # contains list of teams from examples used in this file
        self.teams_validator = TeamsValidator(["hou", "lal", "nyk", "mil"])

    def test_parsed_file_has_parsed_lines_collection(self):
        lines = [
            'DONE - Nba game 20.10 hou at lal -> hou',
            'DONE - Nba game 22.10 nyk at mil -> mil'
        ]

        file_parser = FileParser(lines, self.line_parser, self.teams_validator)
        file_parser.run()
        self.assertEqual(len(file_parser.parsed_lines), 2)

    def test_parsed_file_has_not_parsed_lines(self):
        lines = ['1', '2']

        file_parser = FileParser(lines, self.line_parser, self.teams_validator)
        file_parser.run()
        self.assertEqual(len(file_parser.not_parsed_lines), 2)

    def test_parsed_file_has_both_parsed_and_not_parsed_lines(self):
        lines = [
            'DONE - Nba game 20.10 hou at lal -> hou',
            '1'
        ]

        file_parser = FileParser(lines, self.line_parser, self.teams_validator)
        file_parser.run()
        self.assertEqual(len(file_parser.parsed_lines), 1)
        self.assertEqual(len(file_parser.not_parsed_lines), 1)
