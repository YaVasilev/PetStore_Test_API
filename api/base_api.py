"""Класс с Базовыми методами и asserts"""
import requests
from jsonschema import validate
from helper.logger import log

BASE_URL = "https://petstore.swagger.io"


class BaseApi:
    HEADERS = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    _HEADERS_UPDATE = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    def __init__(self):
        self.response = None

    def get(self, endpoint: str, id: int):
        url = BASE_URL
        self.response = requests.get(url=f"{url}{endpoint}{id}",
                                     headers=self.HEADERS)
        log(response=self.response)
        return self

    def post(self, endpoint: str, headers: dict = None, json: dict = None, data: dict = None):
        url = BASE_URL
        self.response = requests.post(url=f"{url}{endpoint}",
                                      headers=headers,
                                      json=json,
                                      data=data)
        log(self.response, request_body=json)
        return self

    def delete(self, endpoint: str, id: str):
        url = BASE_URL
        self.response = requests.delete(url=f"{url}{endpoint}{id}",
                                        headers=self.HEADERS)
        log(response=self.response)
        return self

    def status_code_should_be(self, expected_status_code: int):
        actual_status_code = self.response.status_code
        assert actual_status_code == expected_status_code, (f"Actual status code {actual_status_code}, "
                                                            f"Expected status code {expected_status_code}")
        return self

    def assert_schema_is_valid(self, expected_schema):
        validate(self.response.json(), expected_schema)
        return self

    def assert_response_values_is_valid(self):
        pass