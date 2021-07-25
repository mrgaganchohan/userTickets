ARRAY_OF_DICTS = [
    {
        "_id": 1001,
        "name": "Test1",
        "created_at": "2016-04-15T05:19:46-10:00",
        "verified": True,
    },
    {"_id": 1002, "name": "Test2", "created_at": "2016-04-15T05:19:46-10:00"},
]

EXPECTED_GET_UNIQ_KEYS = ["_id", "name", "created_at", "verified"]

USER_DATA = [
    {
        "_id": 1001,
        "name": "Test1",
        "created_at": "2016-04-15T05:19:46-10:00",
        "verified": True,
    }
]

TICKET_DATA = [
    {
        "_id": "436bf9b0-1147-4c0a-8439-6f79833bff5b",
        "created_at": "2016-04-28T11:19:34-10:00",
        "type": "incident",
        "subject": "A Catastrophe in Korea (North)",
        "assignee_id": 24,
        "tags": ["Ohio", "Pennsylvania", "American Samoa", "Northern Mariana Islands"],
    }
]
EXPECTED_LIST_ALL_FIELDS = "---------------------------\nSearch Users with:\n_id\nname\ncreated_at\nverified\n---------------------------\nSearch tickets with:\n_id\ncreated_at\ntype\nsubject\nassignee_id\ntags\n---------------------------\n"

EXPECTED_WELCOME_TEXT = (
    "Welcome to Search\nType 'quit' to exit at any time, Press 'Enter' to continue "
)

EXPECTED_SEARCH_OPTIONS_TEXT = "\tSelect Search options:\n\t * Press 1 to search\n\t * Press 2 to view a list of searchable fields\n\t * Type 'quit' to exit\n"
