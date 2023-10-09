import pytest
from api.all_store_api.store_api import StoreApi

"""Конектор к StoreApi """


@pytest.fixture(scope="function")
def store_api() -> StoreApi:
    return StoreApi()
