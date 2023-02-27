import unittest
from unittest.mock import Mock
import os
from bkgames.readers import FileReader
from bkgames.readers import FileFinderFactory
from tests.data_creator import DataCreator


class TestReader(unittest.TestCase):

    # A way to create and remove files for tests (for each test case)
    # def setUp(self):
    #     self.filename = "input.txt"
    #     with open(self.filename, mode='w') as f:
    #         f.write("DONE - Nba game 16.10 phi at bos -> bos?\n")
    #         f.write("DONE - Nba game 17.10 dal at phx -> phx\n")

    # def tearDown(self):
    #     try:
    #         os.remove(self.filename)
    #     except:
    #         pass

    def setUp(self):
        self.creator = DataCreator().create_folder().create_file_with_data()
        self.creator.execute()

    def tearDown(self):
        self.creator.cleanup()

    def test_read_lines_from_file_returns_the_correct_number_of_teams(self):
        finder = FileFinderFactory().create_file_finder(filename=self.creator.file_path)
        teams_with_games = FileReader(finder).read()
        self.assertEqual(2, len(teams_with_games))

        first_item = teams_with_games[0]
        self.assertTrue("bos" in first_item)

    def test_when_finder_is_not_provided_then_autofinder_is_used(self):
        reader = FileReader()
        self.assertIsNotNone(reader._file_finder)  # Not the best way to check.
