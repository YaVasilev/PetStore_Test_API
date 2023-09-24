import random
import json

valid_create_data = ({
    "id": 222,
    "category": {
        "id": 222,
        "name": "TestName"
    },
    "name": "TestName",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 222,
            "name": "TestName"
        }
    ],
    "status": "available"
})

empty_data = {}


def generate_valid_data():
    letters = "abcdefghijklmnopqrstuvwxyz"
    length = 5

    id = random.randint(100, 300)
    category_id = random.randint(100, 300)
    category_name = "".join([random.choice(letters) for _ in range(length)])
    name = "".join([random.choice(letters) for _ in range(length)])
    photoUrls = "".join([random.choice(letters) for _ in range(length)])
    tags_id = random.randint(100, 300)
    tags_name = "".join([random.choice(letters) for _ in range(length)])
    status = "available"

    valid_create_data_test = ({
        "id": id,
        "category": {
            "id": category_id,
            "name": category_name
        },
        "name": name,
        "photoUrls": [
            photoUrls
        ],
        "tags": [
            {
                "id": tags_id,
                "name": tags_name
            }
        ],
        "status": status
    })

    return valid_create_data_test
