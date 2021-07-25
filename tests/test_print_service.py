import unittest

from src.services.print_service import PrintService
from tests.consts import consts_print_serv


class PrintTests(unittest.TestCase):
    def setUp(self):
        self.print_service = PrintService()

    def test_get_unique_keys(self):
        self.assertListEqual(
            self.print_service.get_unique_keys(consts_print_serv.ARRAY_OF_DICTS),
            consts_print_serv.EXPECTED_GET_UNIQ_KEYS,
        )

    def test_list_all_fields(self):
        self.assertEqual(
            self.print_service.list_all_fields(
                consts_print_serv.USER_DATA, consts_print_serv.TICKET_DATA
            ),
            consts_print_serv.EXPECTED_LIST_ALL_FIELDS,
        )

    def test_get_welcome_text(self):
        self.assertEqual(
            self.print_service.get_welcome_text(),
            consts_print_serv.EXPECTED_WELCOME_TEXT,
        )

    def test_get_search_options(self):
        self.assertEqual(
            self.print_service.get_search_options(),
            consts_print_serv.EXPECTED_SEARCH_OPTIONS_TEXT,
        )

    def test_get_search_selection(self):
        self.assertEqual(
            self.print_service.get_search_selection(), "Select 1) Users 2) Tickets\n"
        )


if __name__ == "__main__":
    unittest.main()
