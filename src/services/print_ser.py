class PrintService:
    def get_unique_keys(self, array_of_dicts):
        uniqur_keys= []
        for dictionary in array_of_dicts:
            for key in dictionary:
                if not key in uniqur_keys:
                    uniqur_keys.append(key)
        return uniqur_keys
    def list_all_fields(self, user_data, ticket_data):
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
                    
        print("---------------------------")
        print("Search Users with:")
        unique_user_searchable_terms = self.get_unique_keys(user_data)
        for user_searchable_term in unique_user_searchable_terms:
            print (user_searchable_term)
        print("---------------------------")
        print("Search tickets with:")
        unique_ticket_searchable_terms = self.get_unique_keys(ticket_data)
        for ticket_searchable_term in unique_ticket_searchable_terms:
            print (ticket_searchable_term)
        print("----------------------------")
        return "Print Success"