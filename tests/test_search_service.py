import unittest

from src.services.search_service import Search
from tests import consts
from tests.consts import consts_test_search


class PrintTests(unittest.TestCase):
    def setUp(self):
        self.search_service = Search()

    def test_convert_search_value_to_req_type(self):
        self.assertEqual(
            self.search_service.convert_search_value_to_req_type("users", "_id", "33"),
            33,
        )
        self.assertEqual(
            self.search_service.convert_search_value_to_req_type(
                "tickets", "_id", "436bf9b0-1147-4c0a-8439-6f79833bff5b"
            ),
            "436bf9b0-1147-4c0a-8439-6f79833bff5b",
        )
        self.assertEqual(
            self.search_service.convert_search_value_to_req_type(
                "users", "_id", "Test"
            ),
            "Test",
        )

    def test_convert_search_val_to_bool_type(self):
        self.assertEqual(
            self.search_service.convert_search_value_to_req_type(
                "users", "verified", "Test"
            ),
            "Test",
        )
        self.assertEqual(
            self.search_service.convert_search_value_to_req_type(
                "users", "verified", "true"
            ),
            True,
        )
        self.assertEqual(
            self.search_service.convert_search_value_to_req_type(
                "users", "verified", "false"
            ),
            False,
        )

    def test_get_filtered_users_by_search_term(self):
        self.assertListEqual(
            self.search_service.get_filtered_users_by_search_term(
                consts_test_search.USER_DATA, "_id", "1001", "users"
            ),
            consts_test_search.EXPECTED1_FILTER_USER_BY_SEARCH_TERM,
        )
        self.assertListEqual(
            self.search_service.get_filtered_users_by_search_term(
                consts_test_search.USER_DATA, "verified", "false", "users"
            ),
            consts_test_search.EXPECTED2_FILTER_USER_BY_SEARCH_TERM,
        )
        self.assertListEqual(
            self.search_service.get_filtered_users_by_search_term(
                consts_test_search.USER_DATA, "name", "Test1", "users"
            ),
            consts_test_search.EXPECTED1_FILTER_USER_BY_SEARCH_TERM,
        )
        self.assertListEqual(
            self.search_service.get_filtered_users_by_search_term(
                consts_test_search.KEY_ERROR_USER_DATA, "name", "Test1", "users"
            ),
            [],
        )

    def test_get_filtered_tickets_by_search_term(self):
        self.assertListEqual(
            self.search_service.get_filtered_tickets_by_search_term(
                consts_test_search.TICKET_DATA,
                "_id",
                "436bf9b0-1147-4c0a-8439-6f79833bff5b",
                "tickets",
            ),
            consts_test_search.EXPECTED1_FILTER_TICKETS_BY_SEARCH_TERM,
        )

        self.assertListEqual(
            self.search_service.get_filtered_tickets_by_search_term(
                consts_test_search.TICKET_DATA,
                "tags",
                "Northern Mariana Islands1",
                "tickets",
            ),
            consts_test_search.EXPECTED2_FILTER_TICKETS_BY_SEARCH_TERM,
        )
        self.assertListEqual(
            self.search_service.get_filtered_tickets_by_search_term(
                consts_test_search.TICKET_DATA_NO_TAGS,
                "tags",
                "Northern Mariana Islands1",
                "tickets",
            ),
            [],
        )

    def test_get_tickets_for_users(self):

        self.assertListEqual(
            self.search_service.get_tickets_for_users(
                consts_test_search.FILTERED_USER_DATA, consts_test_search.TICKET_DATA
            ),
            consts_test_search.EXPECTED1_GET_TIX_FOR_USER,
        )

    def test_get_tickets_for_users_error(self):

        self.assertListEqual(
            self.search_service.get_tickets_for_users(
                consts_test_search.KEY_ERROR_USER_DATA, consts_test_search.TICKET_DATA
            ),
            consts_test_search.KEY_ERROR_USER_DATA,
        )

    def test_get_owners_for_tickets(self):
        self.assertListEqual(
            self.search_service.get_owners_for_tickets(
                consts_test_search.TICKET_DATA, consts_test_search.USER_DATA
            ),
            consts_test_search.EXPECTED_GET_OWNERS_FOR_TIX,
        )

    def test_get_owners_for_tickets_error(self):
        self.assertListEqual(
            self.search_service.get_owners_for_tickets(
                consts_test_search.TICKET_DATA, consts_test_search.KEY_ERROR_USER_DATA
            ),
            consts_test_search.TICKET_DATA,
        )

    def test_get_search_data(self):

        self.assertListEqual(
            self.search_service.get_search_data(
                "users",
                "_id",
                "1001",
                consts_test_search.USER_DATA,
                consts_test_search.TICKET_DATA,
            ),
            consts_test_search.EXPECTED_GET_SEARCH_DATA,
        )

        self.assertListEqual(
            self.search_service.get_search_data(
                "users",
                "_id",
                "Test",
                consts_test_search.USER_DATA,
                consts_test_search.TICKET_DATA,
            ),
            [],
        )
        self.assertListEqual(
            self.search_service.get_search_data(
                "tickets",
                "_id",
                "436bf9b0-1147-4c0a-8439-6f79833bff5b",
                consts_test_search.USER_DATA,
                consts_test_search.TICKET_DATA,
            ),
            consts_test_search.EXPECTED1_GET_SEARCH_DATA,
        )


if __name__ == "__main__":
    unittest.main()
