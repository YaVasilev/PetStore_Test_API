import requests
import json
import json.decoder
from requests import Response
from jsonschema import validate
from helper.logger import log


class BaseApi:

    def __init__(self):
        self.response = None

    def get(self, url: str, endpoint: str, pet_id: int):
        self.response = requests.get(url=f"{url}{endpoint}{pet_id}")
        log(self.response)
        return self

    def post(self, url: str, endpoint: str, json: dict = None):
        self.response = requests.post(url=f"{url}{endpoint}",
                                      json=json)
        log(self.response, request_body=json)
        return self

    def status_code_should_be(self, expected_status_code: int):
        actual_status_code = self.response.status_code
        assert actual_status_code == expected_status_code, (f"Actual status code {actual_status_code}, "
                                                            f"Expected status code {expected_status_code}")
        log(self.response)
        return self

    def response_has_keys_in_json(self, response: Response, keys: list):
        try:
            response = self.response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is {response.text}"
        for key in keys:
            assert key in response, f"Response JSON doesn`t have keys {response.text}"

    def response_has_value_in_json(self, response: Response, key, value, error_message):
        try:
            response = self.response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is {self.response.text}"

        assert key in response, f"Response JSON doesn`t have key {self.response.text}"
        assert response[key] == value, error_message

    def response_schema_is_valid(self, schema):
        if isinstance(self.response.json(), list):
            for item in self.response.json():
                validate(item, schema)
            else:
                validate(self.response.json(), schema)
        return self

