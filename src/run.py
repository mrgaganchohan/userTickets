from src.read import ReadFilesFromFolder
from src.search import Search
import os
class RunApplication:
    

    def __init__(self):
        self.INT_SEARCH_TERMS_USERS = [ '_id', ]
        self.INT_SEARCH_TERMS_TICKETS = ['assignee_id']
        self.USER_FIELDS = ['_id', "name", "created_at", "verified"]
        self.TICKETS_FIELDS = ["_id", "created_at", "type", "subject","assignee_id",
        "tags"]
        
    def get_one_dir_up(self):
        # since original obj is from main.py, main.py will 
        return os.getcwd()
    
    def formatted_user_output(self, user_with_tickets):
        formatted_users_with_tickets=''
        # user_with_tickets contains all the users and their respective tickets
        for user in user_with_tickets:
            single_formatted_user = ''
            for key, value in user.items():
                 single_formatted_user = single_formatted_user + key +'\t'+ str(value) +'\n'
            formatted_users_with_tickets = formatted_users_with_tickets + '\n\n'+ single_formatted_user
        return formatted_users_with_tickets
            
    def user_flow(self, type_of_search, user_data, ticket_data):
        print ("Enter search term")
        search_term = input()
        print ("Enter search value")
        search_value = 0
        int_terms = []
        if (type_of_search=='tickets'):
            int_terms = self.INT_SEARCH_TERMS_TICKETS
        elif (type_of_search=='users'):
            int_terms = self.INT_SEARCH_TERMS_USERS
           
        if search_term in int_terms:
            search_value = int (input())
        else:
            search_value = input()
        search_obj = Search()
        if search_term == 'verified' and type_of_search=='users':
            search_value = bool(search_value)
        user_tickets = search_obj.get_search_data(type_of_search, search_term, search_value, user_data, ticket_data)
        return_value = ''
        if user_tickets == []:
            return_value =  'No results found'
        else:
            return_value = self.formatted_user_output(user_tickets)
        return return_value
    
    def run_flow(self):
        print ("Welcome to Search")
        print ("Type 'quit' to exit at any time, Press 'Enter' to continue ")
        first_input = input()
        # user_path = 'json-files/users/users.json'
        # user_abs_file_path = os.path.join(os.getcwd(), user_path)
        user_directory = os.path.join(os.getcwd(), 'json-files/users')
        ticket_directory = os.path.join(os.getcwd(), 'json-files/tickets')
        # ticket_path = 'json-files/tickets/tickets.json' 
        user = ReadFilesFromFolder()
        user_data = user.read_all_files_directory(user_directory)
        ticket_data = user.read_all_files_directory(ticket_directory)
        # user_data  = user.read(user_abs_file_path)
        # ticket_data = user.read(ticket_abs_file_path)
        if (first_input=="quit"):
            print ("GoodBye")
            exit()
        while True:
            print("\tSelect Search options:")
            print ("\t * Press 1 to search ")
            print ("\t * Press 2 to view a list of searchable fields")
            print ("\t * Type 'quit' to exit")
            user_input = input()
            if user_input=="quit":
                break
            elif user_input=="1":
                print ("Select 1) Users 2) Tickets")
                search_selection = input()
                if search_selection == "1":
                    type_of_search = 'users'
                    
                elif search_selection == "2":
                    type_of_search='tickets'
                    
                user_with_tickets_arr = self.user_flow(type_of_search, user_data, ticket_data)
                print (user_with_tickets_arr)
                    # user_search_flow = UserSearchFlow()
                    # user_search_flow.user_search_flow(user_data, ticket_data)
                # present user with options, search by users or tickets
            elif (user_input=="2"):
                print ("---------------------------")
                print ("Search Users with:")
                for user_field in self.USER_FIELDS:
                    print (user_field)
                print ("---------------------------")
                print ("Search tickets with:")
                for ticket_field in self.TICKETS_FIELDS:
                    print (ticket_field)
                print ("----------------------------")
                # call
                
            


            
            
       
