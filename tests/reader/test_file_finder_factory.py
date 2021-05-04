import unittest
from bkgames.reader import FileFinderFactory
from bkgames.reader.autofinder import Autofinder
from bkgames.reader.filename_finder import FilenameFinder


class TestFileFinderFactory(unittest.TestCase):
    def test_when_not_autofind_and_no_filename_provided_raises_error(self):
        self.assertRaises(ValueError,
                          lambda: FileFinderFactory.create_file_finder(filename=None, autofind=False))

    def test_when_no_filename_provided_then_autofind_is_created(self):
        finder = FileFinderFactory.create_file_finder()
        self.assertTrue(isinstance(finder, Autofinder))

    def test_when_filename_provided_then_autofinder_is_not_created(self):
        finder = FileFinderFactory.create_file_finder(filename="test")
        self.assertTrue(isinstance(finder, FilenameFinder))
        self.assertFalse(isinstance(finder, Autofinder))
