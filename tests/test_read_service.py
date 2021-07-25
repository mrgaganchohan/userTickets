import unittest
import os
from src.services.read_service import ReadFilesFromFolder
from tests.consts import consts_read_serv


class ReadTests(unittest.TestCase):
    def setUp(self):
        self.read_service = ReadFilesFromFolder()

    def test_read_all_files_directory(self):
        directory = os.path.join(os.getcwd(), "tests/test_files")
        self.assertListEqual(
            self.read_service.read_all_files_directory(directory),
            consts_read_serv.EXPECTED_READ_ALL_FILES_DIRECTORY,
        )

    def test_read(self):
        directory = os.path.join(os.getcwd(), "tests/test_files/users.json")
        self.assertEqual(
            self.read_service.read(directory),
            consts_read_serv.EXPECTED_SINGLE_READ,
        )


if __name__ == "__main__":
    unittest.main()
