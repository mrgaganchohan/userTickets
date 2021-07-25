import copy


class Search:
    def __init__(self):
        self.INT_SEARCH_KEYS_USERS = [
            "_id",
        ]
        self.INT_TYPES_KEYS_TICKETS = ["assignee_id"]

    def convert_search_value_to_req_type(
        self, type_of_search, search_term, search_value
    ):
        """based on the search_term, it converts search_value
        to either bool or int or keep it as string.

        Args:
            type_of_search (str): type of search 'users'  or 'tickets'
            search_term (str): search term selected, eg.  '_id' or 'name'
            search_value (str): comes as string but will be converted to int/bool/string

        Returns:
            bool/int/str: parsed to required type based on search_term
        """
        int_type_keys = []

        if type_of_search == "tickets":
            int_type_keys = self.INT_TYPES_KEYS_TICKETS

        elif type_of_search == "users":
            int_type_keys = self.INT_SEARCH_KEYS_USERS

        if search_term in int_type_keys:
            try:
                search_value = int(search_value)
            except ValueError:
                print("\nPlease enter a valid integer\n")

        if search_term == "verified" and type_of_search == "users":
            if search_value in ["true", "false"]:
                search_value = True if search_value == "true" else False
            else:
                print("Please enter either true or false")
        return search_value

    def get_filtered_users_by_search_term(
        self, user_data, search_term, search_value, type_of_search
    ):
        """for type of search =>'users', it filters from the list of users
           based on search term. e.g.: if name: Gagan is the search term,
           it will get all users with name Gagan.
        Args:
            user_data ([]): array of users {}
            search_term (str): search term entered, e.g.: 'name' or '_id'
            search_value (str): search value entered by user
            type_of_search (str): 'users' or 'tickets', but in this case
                                it will always get type as users

        Returns:
            []: returns an array of user dictionaries
        """
        filtered_users = []

        search_value_with_correct_type = self.convert_search_value_to_req_type(
            type_of_search, search_term, search_value
        )
        # gets all users where search_term is present.
        users_with_search_term = list(
            filter(lambda user: search_term in user, user_data)
        )

        filtered_users = list(
            filter(
                lambda user: user[search_term] == search_value_with_correct_type,
                users_with_search_term,
            )
        )

        return filtered_users

    def get_filtered_tickets_by_search_term(
        self, ticket_data, search_term, search_value, type_of_search
    ):
        filtered_tickets = []

        # if more array type fields are added in future, we can add it here
        list_of_arr_types = ["tags"]
        filtered_tickets = []
        # assignie_id
        tickets_with_search_term = list(
            filter(lambda ticket: search_term in ticket, ticket_data)
        )
        if search_term in list_of_arr_types:
            # if tags is search_term, then filter where input value exists in tickt['tags']
            filtered_tickets = list(
                filter(
                    lambda ticket: search_value in ticket[search_term],
                    tickets_with_search_term,
                )
            )
        else:
            search_value_with_correct_type = self.convert_search_value_to_req_type(
                type_of_search, search_term, search_value
            )

            filtered_tickets = list(
                filter(
                    lambda ticket: ticket[search_term]
                    == search_value_with_correct_type,
                    tickets_with_search_term,
                )
            )

        return filtered_tickets

    def get_tickets_for_users(self, filtered_users, ticket_data):
        """
        aid for user search
        All filtered users with particular search term
        """

        copy_filtered_users = copy.deepcopy(filtered_users)
        # only gets tickets with assignee key , as we will search through them for assiniee_id
        # and assign them to users
        filter_tickets_with_assignee_key = list(
            filter(lambda ticket: "assignee_id" in ticket, ticket_data)
        )
        for user in copy_filtered_users:

            try:
                filtered_tix_for_users = list(
                    filter(
                        lambda ticket: ticket["assignee_id"] == user["_id"],
                        filter_tickets_with_assignee_key,
                    )
                )
                ticket_name = []
                for filtered_tick in filtered_tix_for_users:
                    if filtered_tick["assignee_id"] == user["_id"]:
                        ticket_name.append(filtered_tick["subject"])

                user["tickets"] = ticket_name
            except KeyError:
                print("Error while finding tickets for user " + str(user))
        return copy_filtered_users

    def get_owners_for_tickets(self, filtered_tickets, user_data):
        """
        aid for ticket search
        filtered_tickets: [] contains all tickets that has given search term in it
        """
        copy_filtered_tickets = copy.deepcopy(filtered_tickets)
        for ticket in copy_filtered_tickets:

            # get users for a given assignie id
            try:
                if "assignee_id" in ticket:
                    users_with_given_ticket = list(
                        filter(
                            lambda user: user["_id"] == ticket["assignee_id"], user_data
                        )
                    )
                    # ASSUMPTION:just in case more than one users have same ticket due to some data
                    # corruption
                    for filtered_user in users_with_given_ticket:
                        if filtered_user["_id"] == ticket["assignee_id"]:
                            ticket["assignee_name"] = filtered_user["name"]
            except KeyError:
                print("Error finding user for given ticket ", str(ticket))
        return copy_filtered_tickets

    # for a given user get the tickets of that user

    def get_search_data(
        self, type_of_search, search_term, search_value, user_data, ticket_data
    ):
        """
        Returns user with given tickets with user's name or tickets with user name
        """
        filtered_search_data = []
        search_data = []
        if type_of_search == "users":

            filtered_search_data = self.get_filtered_users_by_search_term(
                user_data, search_term, search_value, type_of_search
            )
            search_data = self.get_tickets_for_users(filtered_search_data, ticket_data)

        elif type_of_search == "tickets":
            filtered_search_data = self.get_filtered_tickets_by_search_term(
                ticket_data, search_term, search_value, type_of_search
            )
            search_data = self.get_owners_for_tickets(filtered_search_data, user_data)

        if len(filtered_search_data) == 0:
            return []
        else:
            return search_data
