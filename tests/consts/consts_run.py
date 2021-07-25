DATA_TO_FORMAT = [
    {
        "_id": 33,
        "name": "Jaime Dickerson",
        "created_at": "2016-04-30T11:41:42-10:00",
        "verified": True,
        "tickets": [
            "A Problem in Zaire",
            "A Catastrophe in Moldova",
            "A Catastrophe in Sao Tome and Principe",
            "A Catastrophe in Thailand",
        ],
    }
]

USER_DATA = [
    {
        "_id": 1001,
        "name": "Test1",
        "created_at": "2016-04-15T05:19:46-10:00",
        "verified": True,
    },
    {
        "_id": 2,
        "name": "Test2",
        "created_at": "2016-04-15T05:19:46-10:00",
        "verified": False,
    },
    {
        "_id": 3,
        "name": "Test2",
        "created_at": "2016-04-15T05:19:46-10:00",
        "verified": False,
    },
]

TICKET_DATA = [
    {
        "_id": "436bf9b0-1147-4c0a-8439-6f79833bff5b",
        "created_at": "2016-04-28T11:19:34-10:00",
        "type": "incident",
        "subject": "A Catastrophe in Korea (North)",
        "assignee_id": 1001,
        "tags": ["Ohio", "Pennsylvania", "American Samoa", "Northern Mariana Islands"],
    },
    {
        "_id": "436bf9b0-1147-4c0a-8439-6f798312315b",
        "created_at": "2016-04-28T11:19:34-10:00",
        "type": "incident",
        "subject": "A Catastrophe in Korea (North)1",
        "assignee_id": 1001,
        "tags": ["Ohio", "Pennsylvania", "American Samoa", "Northern Mariana Islands1"],
    },
]

EXPECTED_AFTER_FORMATTING_DATA = "\n\n_id\t33\nname\tJaime Dickerson\ncreated_at\t2016-04-30T11:41:42-10:00\nverified\tTrue\ntickets\t['A Problem in Zaire', 'A Catastrophe in Moldova', 'A Catastrophe in Sao Tome and Principe', 'A Catastrophe in Thailand']\n"

EXPECTED_GET_RESULTS_FOR_INPUT = "\n\n_id\t1001\nname\tTest1\ncreated_at\t2016-04-15T05:19:46-10:00\nverified\tTrue\ntickets\t['A Catastrophe in Korea (North)', 'A Catastrophe in Korea (North)1']\n"

EXPECTED_GET_RESULTS_FOR_INPUT_TICKET = "\n\n_id\t436bf9b0-1147-4c0a-8439-6f79833bff5b\ncreated_at\t2016-04-28T11:19:34-10:00\ntype\tincident\nsubject\tA Catastrophe in Korea (North)\nassignee_id\t1001\ntags\t['Ohio', 'Pennsylvania', 'American Samoa', 'Northern Mariana Islands']\nassignee_name\tTest1\n\n\n_id\t436bf9b0-1147-4c0a-8439-6f798312315b\ncreated_at\t2016-04-28T11:19:34-10:00\ntype\tincident\nsubject\tA Catastrophe in Korea (North)1\nassignee_id\t1001\ntags\t['Ohio', 'Pennsylvania', 'American Samoa', 'Northern Mariana Islands1']\nassignee_name\tTest1\n"

EXPECTED_RUN_FLOW_CHOICE_1 = "\n\n_id\t1001\nname\tTest1\ncreated_at\t2016-04-15T05:19:46-10:00\nverified\tTrue\ntickets\t[]\n"

EXPECTED_LIST_ALL_FIELDS = "---------------------------\nSearch Users with:\n_id\nname\ncreated_at\nverified\n---------------------------\nSearch tickets with:\n_id\ncreated_at\ntype\nsubject\nassignee_id\ntags\n---------------------------\n"

EXPECTED_RUN_FLOW_CHOICE_2 = "\n\n_id\t25d9edca-7756-4d28-8fdd-f16f1532f6ab\ncreated_at\t2016-03-01T05:58:09-11:00\ntype\ttask\nsubject\tA Problem in Cyprus\nassignee_id\t75\ntags\t['Puerto Rico', 'Idaho', 'Oklahoma', 'Louisiana']\nassignee_name\tCatalina Simpson\n"
