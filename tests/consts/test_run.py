import unittest
from unittest.mock import patch

from src.run import RunApplication
from tests.consts import consts_run


class RunApplicationTests(unittest.TestCase):
    def setUp(self):
        self.run_app = RunApplication()

    def test_formatted_user_output(self):
        self.assertEqual(
            self.run_app.formatted_user_output(consts_run.DATA_TO_FORMAT),
            consts_run.EXPECTED_AFTER_FORMATTING_DATA,
        )

    @patch("builtins.input", side_effect=["_id", "1001"])
    def test_get_input_data(self, mock_inputs):

        self.assertEqual(
            self.run_app.get_results_for_input_data(
                "random", consts_run.USER_DATA, consts_run.TICKET_DATA
            ),
            "No results found",
        )

    @patch("builtins.input", side_effect=["_id", "1001"])
    def test_get_input_data2(self, mock_inputs):

        self.assertEqual(
            self.run_app.get_results_for_input_data(
                "users", consts_run.USER_DATA, consts_run.TICKET_DATA
            ),
            consts_run.EXPECTED_GET_RESULTS_FOR_INPUT,
        )

    @patch("builtins.input", side_effect=["tags", "Ohio"])
    def test_get_input_data_ticket_3(self, mock_inputs):

        self.assertEqual(
            self.run_app.get_results_for_input_data(
                "tickets", consts_run.USER_DATA, consts_run.TICKET_DATA
            ),
            consts_run.EXPECTED_GET_RESULTS_FOR_INPUT_TICKET,
        )

    @patch("builtins.input", side_effect=["quit"])
    def test_run_flow(self, mock_inputs):
        self.assertEqual(
            self.run_app.run_flow(
                user_files_path="tests/test_files/users",
                ticket_files_path="tests/test_files/tickets",
            ),
            "initial quit",
        )

    @patch("builtins.input", side_effect=["1", "1", "1", "_id", "1001", "quit"])
    def test_run_flow_option1_users_search(self, mock_inputs):
        self.assertEqual(
            self.run_app.run_flow(
                user_files_path="tests/test_files/users",
                ticket_files_path="tests/test_files/tickets",
            ),
            {"last_value": consts_run.EXPECTED_RUN_FLOW_CHOICE_1},
        )

    @patch(
        "builtins.input",
        side_effect=[
            "1",
            "1",
            "2",
            "_id",
            "25d9edca-7756-4d28-8fdd-f16f1532f6ab",
            "quit",
        ],
    )
    def test_run_flow_option1_tickets_search(self, mock_inputs):
        self.assertEqual(
            self.run_app.run_flow(
                user_files_path="tests/test_files/users",
                ticket_files_path="tests/test_files/tickets",
            ),
            {"last_value": consts_run.EXPECTED_RUN_FLOW_CHOICE_2},
        )

    @patch("builtins.input", side_effect=["1", "2", "quit"])
    def test_run_flow_option_2(self, mock_inputs):
        self.assertEqual(
            self.run_app.run_flow(
                user_files_path="tests/test_files/users",
                ticket_files_path="tests/test_files/tickets",
            ),
            {"last_value": consts_run.EXPECTED_LIST_ALL_FIELDS},
        )


if __name__ == "__main__":
    unittest.main()
