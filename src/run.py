from src.services.read_service import ReadFilesFromFolder
from src.services.search_service import Search
from src.services.print_service import PrintService
import os


class RunApplication:
    def __init__(self):
        self.PrintService = PrintService()

    def formatted_user_output(self, user_with_tickets):
        formatted_users_with_tickets = ""
        # user_with_tickets contains all the users and their respective tickets
        for user in user_with_tickets:
            single_formatted_user = ""
            for key, value in user.items():
                single_formatted_user = (
                    single_formatted_user + key + "\t" + str(value) + "\n"
                )
            formatted_users_with_tickets = (
                formatted_users_with_tickets + "\n\n" + single_formatted_user
            )
        return formatted_users_with_tickets

    def get_input_data(self, type_of_search, user_data, ticket_data):
        print("Enter search term")
        search_term = input()
        print("Enter search value")
        search_value = ""
        search_value = input()

        search_obj = Search()
        # TODO: more meaningful name here
        user_tickets = search_obj.get_search_data(
            type_of_search, search_term, search_value, user_data, ticket_data
        )
        return_value = ""
        if user_tickets == []:
            return_value = "No results found"
        else:
            return_value = self.formatted_user_output(user_tickets)
        return return_value

    def run_flow(self):

        welcome_text = self.PrintService.get_welcome_text()
        print(welcome_text)
        first_input = input()
        user_directory = os.path.join(os.getcwd(), "json-files/users")
        ticket_directory = os.path.join(os.getcwd(), "json-files/tickets")
        user = ReadFilesFromFolder()
        user_data = user.read_all_files_directory(user_directory)
        ticket_data = user.read_all_files_directory(ticket_directory)
        if first_input == "quit":
            print("GoodBye")
            exit()
        type_of_search = ""
        while True:
            search_options_text = self.PrintService.get_search_options()
            print(search_options_text)
            user_input = input()
            if user_input == "quit":
                break
            elif user_input == "1":
                print(self.PrintService.get_search_selection())
                search_selection = input()
                if search_selection == "1":
                    type_of_search = "users"

                elif search_selection == "2":
                    type_of_search = "tickets"
                user_with_tickets_arr = self.get_input_data(
                    type_of_search, user_data, ticket_data
                )
                print(user_with_tickets_arr)

            elif user_input == "2":

                all_searchable_fields = self.PrintService.list_all_fields(
                    user_data, ticket_data
                )
                print(all_searchable_fields)
