import unittest
from unittest.mock import Mock
import os
from bkgames.reader import Reader
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

    def test_read_lines_from_file_returns_correct_number_of_teams(self):
        teams_with_games = Reader(filename=self.creator.file_path).read()
        self.assertEqual(2, len(teams_with_games))

        first_item = teams_with_games[0]
        self.assertTrue("bos" in first_item)

    def test_when_no_filename_is_specified_then_autofind_runs(self):
        reader = Reader()
        reader._autofinder.find_input_file = Mock(
            return_value=self.creator.file_path)

        reader.read()

        self.assertTrue(reader._autofinder.find_input_file.called)

    def test_when_filename_is_specified_then_autofind_does_not_run(self):
        reader = Reader(filename=self.creator.file_path)
        reader._autofinder = Mock()  # can be None, so also has to be mocked
        reader._autofinder.find_input_file = Mock(
            return_value=self.creator.file_path)

        reader.read()

        self.assertFalse(reader._autofinder.find_input_file.called)

    def test_no_autofinder_and_no_input_filename_provided_throws_error(self):
        self.fail("to be implemented to increase the coverage")
