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

EXPECTED1_FILTER_USER_BY_SEARCH_TERM = [
    {
        "_id": 1001,
        "name": "Test1",
        "created_at": "2016-04-15T05:19:46-10:00",
        "verified": True,
    }
]
EXPECTED2_FILTER_USER_BY_SEARCH_TERM = [
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

KEY_ERROR_USER_DATA = [
    {
        "_id2": 1001,
    }
]
EXPECTED1_FILTER_TICKETS_BY_SEARCH_TERM = [
    {
        "_id": "436bf9b0-1147-4c0a-8439-6f79833bff5b",
        "created_at": "2016-04-28T11:19:34-10:00",
        "type": "incident",
        "subject": "A Catastrophe in Korea (North)",
        "assignee_id": 1001,
        "tags": ["Ohio", "Pennsylvania", "American Samoa", "Northern Mariana Islands"],
    }
]

EXPECTED2_FILTER_TICKETS_BY_SEARCH_TERM = [
    {
        "_id": "436bf9b0-1147-4c0a-8439-6f798312315b",
        "created_at": "2016-04-28T11:19:34-10:00",
        "type": "incident",
        "subject": "A Catastrophe in Korea (North)1",
        "assignee_id": 1001,
        "tags": ["Ohio", "Pennsylvania", "American Samoa", "Northern Mariana Islands1"],
    }
]

TICKET_DATA_NO_TAGS = [
    {
        "_id": "436bf9b0-1147-4c0a-8439-6f79833bff5b",
        "created_at": "2016-04-28T11:19:34-10:00",
        "type": "incident",
        "subject": "A Catastrophe in Korea (North)",
        "assignee_id": 1001,
    },
    {
        "_id": "436bf9b0-1147-4c0a-8439-6f798312315b",
        "created_at": "2016-04-28T11:19:34-10:00",
        "type": "incident",
        "subject": "A Catastrophe in Korea (North)1",
        "assignee_id": 1001,
    },
]
FILTERED_USER_DATA = [
    {
        "_id": 1001,
        "name": "Test1",
        "created_at": "2016-04-15T05:19:46-10:00",
        "verified": True,
    }
]
EXPECTED1_GET_TIX_FOR_USER = [
    {
        "_id": 1001,
        "name": "Test1",
        "created_at": "2016-04-15T05:19:46-10:00",
        "verified": True,
        "tickets": [
            "A Catastrophe in Korea (North)",
            "A Catastrophe in Korea (North)1",
        ],
    }
]

EXPECTED_GET_OWNERS_FOR_TIX = [
    {
        "_id": "436bf9b0-1147-4c0a-8439-6f79833bff5b",
        "created_at": "2016-04-28T11:19:34-10:00",
        "type": "incident",
        "subject": "A Catastrophe in Korea (North)",
        "assignee_id": 1001,
        "tags": ["Ohio", "Pennsylvania", "American Samoa", "Northern Mariana Islands"],
        "assignee_name": "Test1",
    },
    {
        "_id": "436bf9b0-1147-4c0a-8439-6f798312315b",
        "created_at": "2016-04-28T11:19:34-10:00",
        "type": "incident",
        "subject": "A Catastrophe in Korea (North)1",
        "assignee_id": 1001,
        "tags": ["Ohio", "Pennsylvania", "American Samoa", "Northern Mariana Islands1"],
        "assignee_name": "Test1",
    },
]

EXPECTED_GET_SEARCH_DATA = [
    {
        "_id": 1001,
        "name": "Test1",
        "created_at": "2016-04-15T05:19:46-10:00",
        "verified": True,
        "tickets": [
            "A Catastrophe in Korea (North)",
            "A Catastrophe in Korea (North)1",
        ],
    }
]

EXPECTED1_GET_SEARCH_DATA = [
    {
        "_id": "436bf9b0-1147-4c0a-8439-6f79833bff5b",
        "created_at": "2016-04-28T11:19:34-10:00",
        "type": "incident",
        "subject": "A Catastrophe in Korea (North)",
        "assignee_id": 1001,
        "tags": ["Ohio", "Pennsylvania", "American Samoa", "Northern Mariana Islands"],
        "assignee_name": "Test1",
    }
]
