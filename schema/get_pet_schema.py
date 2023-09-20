GET_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "category": {
            "id": {"type": "integer"},
            "name": {"type": "string"}
        },
        "name": {"type": "string"},
        "photoUrls": {"type": "string"},
        "tags": {
            "id": {"type": "integer"},
            "name": {"type": "string"}
        },
        "status": {"type": "string"}
    }
}
