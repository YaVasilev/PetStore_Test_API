GET_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "category": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"}}
        },
        "name": {"type": "string"},
        "photoUrls": {
            "type": "array",
            "properties": {
                "name": {"type": "string"}
            }
        },
        "tags": {
            "type": "array",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"}}
        },
        "status": {"type": "string"}
    }
}

GET_ERROR_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "code": {"type": "integer"},
        "type": {"type": "string"},
        "message": {"type": "string"}
    }
}

GET_EMPTY_SCHEMA = None
