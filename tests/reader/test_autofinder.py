import unittest
from bkgames.reader import Autofinder
from tests.data_creator import DataCreator


class TestAutofinder(unittest.TestCase):

    # Example:
    # def setUp(self):
    #     self.folder_name = str(uuid.uuid1())
    #     self.file_path = os.path.join(self.folder_name, "input.txt")
    #     os.mkdir(self.folder_name)

    #     with open(self.file_path, mode='w') as f:
    #         f.write("DONE - Nba game 16.10 phi at bos -> bos?\n")
    #         f.write("DONE - Nba game 17.10 dal at phx -> phx\n")

    # def tearDown(self):
    #     try:
    #         os.remove(self.file_path)
    #         os.rmdir(self.folder_name)
    #     except:
    #         pass

    def test_when_folder_path_does_not_exist_reports_error(self):
        finder = Autofinder("dummypath")
        self.assertRaises(ValueError, finder.find_input_file)

    def test_when_valid_folder_path_and_one_file_only_then_it_is_returned(self):
        creator = DataCreator()
        try:
            creator.create_folder().create_file_with_data().execute()
            finder = Autofinder(creator.folder_name)
            file_name = finder.find_input_file()

            self.assertIsNotNone(file_name)
        finally:
            creator.cleanup()

    def test_when_folder_has_no_file_reports_error(self):
        creator = DataCreator()
        try:
            creator.create_folder().execute()  # Only folder, no file

            finder = Autofinder(creator.folder_name)

            self.assertRaises(Exception, finder.find_input_file)
        finally:
            creator.cleanup()
