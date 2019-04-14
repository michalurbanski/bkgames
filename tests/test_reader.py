import unittest
import os
from bkgames.reader import Reader

class TestReader(unittest.TestCase):

    def setUp(self):
        self.filename = "input.txt"
        with open(self.filename, mode = 'w') as f:
            f.write("DONE - Nba game 16.10 phi at bos -> bos?\n")
            f.write("DONE - Nba game 17.10 dal at phx -> phx\n")

    def tearDown(self):
        try:
            os.remove(self.filename)
        except:
            pass

    def test_read_lines_from_file_returns_correct_number_of_teams(self):
        reader = Reader("input.txt")
        teams_with_games = reader.read()
        self.assertEqual(2, len(teams_with_games))
        
        first_item = teams_with_games[0]
        self.assertTrue("bos" in first_item)
