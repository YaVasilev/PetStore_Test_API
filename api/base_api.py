import requests
from jsonschema import validate
from helper.logger import log

BASE_URL = "https://petstore.swagger.io"
HEADERS = {
    "accept": "application/json",
    "Content-Type": "application/json"
}


class BaseApi:

    def __init__(self):
        self.response = None

    def get(self, endpoint: str, pet_id: int):
        url = BASE_URL
        self.response = requests.get(url=f"{url}{endpoint}{pet_id}")
        log(response=self.response)
        return self

    def post(self, endpoint: str, headers: dict = None, json: dict = None):
        url = BASE_URL
        self.response = requests.post(url=f"{url}{endpoint}",
                                      headers=headers,
                                      json=json)
        log(self.response, request_body=json)
        return self

    def status_code_should_be(self, expected_status_code: int):
        actual_status_code = self.response.status_code
        assert actual_status_code == expected_status_code, (f"Actual status code {actual_status_code}, "
                                                            f"Expected status code {expected_status_code}")
        return self

    def assert_schema_is_valid(self, expected_schema):
        validate(self.response.json(), expected_schema)
        return self
