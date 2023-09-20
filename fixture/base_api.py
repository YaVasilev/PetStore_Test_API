import pytest
from api.base_api import BaseApi


@pytest.fixture(scope="function")
def base_api() -> BaseApi:
    return BaseApi()
