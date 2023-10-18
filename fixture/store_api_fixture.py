import pytest
from api.all_store_api.store_api import StoreApi
from data.store_data.store_data import valid_store_data, valid_store_id

"""Конектор к StoreApi """


@pytest.fixture(scope="function")
def store_api() -> StoreApi:
    return StoreApi()


@pytest.fixture(scope="function")
def create_place_order(store_api):
    store_api.place_an_order_for_a_pet(valid_store_data)


@pytest.fixture(scope="function")
def create_delete_place_order(store_api):
    store_api.place_an_order_for_a_pet(valid_store_data)
    yield
    store_api.delete_order_by_id(valid_store_id)


@pytest.fixture(scope="function")
def delete_place_order(store_api):
    yield
    store_api.delete_order_by_id(valid_store_id)