class PrintService:
    def get_unique_keys(self, array_of_dicts):
        uniqur_keys = []
        for dictionary in array_of_dicts:
            for key in dictionary:
                if not key in uniqur_keys:
                    uniqur_keys.append(key)
        return uniqur_keys

    def list_all_fields(self, user_data, ticket_data):
        print_string = ''
        user_data = [
            {
                "_id": 1001,
                "name": "Test1",
                        "created_at": "2016-04-15T05:19:46-10:00",
                        "verified": True
            },
            {
                "_id": 1002,
                "name": "Test2",
                        "created_at": "2016-04-15T05:19:46-10:00"
            }
        ]

        print_string = "---------------------------"
        print_string = print_string + "\nSearch Users with:"
        unique_user_searchable_terms = self.get_unique_keys(user_data)
        for user_searchable_term in unique_user_searchable_terms:
            print_string = print_string + "\n" + user_searchable_term
        print_string = print_string + "\n---------------------------\n"
        print_string = print_string + "Search tickets with:"
        unique_ticket_searchable_terms = self.get_unique_keys(ticket_data)
        for ticket_searchable_term in unique_ticket_searchable_terms:
            print_string = print_string + "\n" + ticket_searchable_term
        print_string = print_string + "\n---------------------------\n"

        return print_string

    def get_welcome_text(self):
        welcome_text = "Welcome to Search\n"
        welcome_text = welcome_text + \
            "Type 'quit' to exit at any time, Press 'Enter' to continue "
        return welcome_text

    def get_search_options(self):
        search_options_text = '\tSelect Search options:\n'
        search_options_text = search_options_text + '\t * Press 1 to search\n'
        search_options_text = search_options_text + \
            "\t * Press 2 to view a list of searchable fields\n"
        search_options_text = search_options_text + "\t * Type 'quit' to exit\n"
        return search_options_text

    def get_search_selection(self):
        return "Select 1) Users 2) Tickets\n"
