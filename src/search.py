import copy
class Search:
    def get_filtered_users_by_search_term(self, user_data, search_term, search_value):
        
        print ("values here")
        user_with_search_term =  list(filter(lambda user: search_term in user, user_data))
        filtered_users = list(filter(lambda user: user[search_term]== search_value, user_with_search_term))
        return filtered_users
    def get_filtered_tickets_by_search_term(self, ticket_data, search_term, search_value):
        # if more arrays are added in future, we can add it here
        list_of_arr_types = ["tags"]
        filtered_tickets = []
        tickets_with_search_term = list(filter(lambda ticket: search_term in ticket, ticket_data))
        if search_term in list_of_arr_types:
           filtered_tickets = list(filter(lambda ticket: search_value in ticket[search_term], tickets_with_search_term))
        else:
            filtered_tickets = list(filter(lambda ticket: ticket[search_term]== search_value, tickets_with_search_term))
        return filtered_tickets   
        
    def get_tickets_for_users(self, filtered_users, ticket_data):
        '''
        aid for user search
        '''
        # gets tickets for a group of users filtered in last step
        copy_filtered_users = copy.deepcopy(filtered_users)
        # only gets tickets with assignee key , as we will search through them for assiniee_id
        filter_tickets_with_assignee_key = list (filter ( lambda ticket: "assignee_id" in ticket, ticket_data))
        # if the search term was name, two more users might have same name, so hence a for loop.
        for user in copy_filtered_users:
            
            # gets all the tickets for a particular user with given ids
            filtered_tix_for_users = list (filter (lambda ticket: ticket['assignee_id'] == user['_id'], filter_tickets_with_assignee_key))
            ticket_name = []
            for filtered_tick in filtered_tix_for_users:
                # TODO: what if id doesn't exists
                if filtered_tick['assignee_id'] == user["_id"]:
                    ticket_name.append(filtered_tick['subject'])
                    
            user['tickets'] = ticket_name
        return copy_filtered_users

    def get_owners_for_tickets(self, filtered_tickets, user_data):
        '''
            aid for ticket search
            filtered_tickets: [] contains all tickets that has given search term in it 
        '''
        copy_filtered_tickets = copy.deepcopy(filtered_tickets)
        for ticket in copy_filtered_tickets:
            
            # get users for a given assignie id 
            #ASSUMPTION one ticket can have only one id
            if "assignee_id" in ticket:
                users_with_given_ticket = list (filter (lambda user: user['_id'] == ticket['assignee_id'], user_data))
                # ASSUMPTION:just in case more than one users have same ticket
                for filtered_user in users_with_given_ticket:
                    # TODO: what if id doesn't exists
                    if filtered_user['_id'] == ticket["assignee_id"]:
                        ticket['assignee_name'] = filtered_user['name']
        return copy_filtered_tickets            
    # for a given user get the tickets of that user
        
    def get_search_data(self, type_of_search, search_term, search_value, user_data, ticket_data):
        '''
        Returns user with given tickets with user's name or tickets with user name
        '''
        #contains filtered tickets or filtered users based on the type_of_search 
        filtered_search_data = []
        search_data = []
        if type_of_search =='users':
            
        # gives filtered list of users's array  where searched value and term matches
            filtered_search_data = self.get_filtered_users_by_search_term( user_data, search_term, search_value)
            search_data =  self.get_tickets_for_users( filtered_search_data, ticket_data)
        elif type_of_search == 'tickets':
            filtered_search_data = self.get_filtered_tickets_by_search_term( ticket_data, search_term, search_value)
            search_data =  self.get_owners_for_tickets( filtered_search_data, user_data)

            pass
        if (len(filtered_search_data)==0):
            return []
        else:
            # give all tickets for a given user
           return search_data
           