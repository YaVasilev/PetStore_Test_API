import pytest
from data.store_data.place_order_for_pet_data import valid_store_data
from schema.store_shemas import STORE_SCHEMA, ERROR_DELETE_STORE_SCHEMA

pytest_plugins = ["fixture.store_api_fixture"]


def test_place_order_for_store_valid(store_api):
    store_api.place_an_order_for_a_pet(valid_store_data)
    store_api.status_code_should_be(200)
    store_api.assert_schema_is_valid(STORE_SCHEMA)


def test_find_order_by_id_valid(store_api):
    store_api.find_order_by_id(3)
    store_api.status_code_should_be(200)
    store_api.assert_schema_is_valid(STORE_SCHEMA)


def test_find_order_by_id_no_exist_id(store_api):
    store_api.find_order_by_id(2)
    store_api.status_code_should_be(404)
    store_api.assert_schema_is_valid(ERROR_DELETE_STORE_SCHEMA)


def test_delete_order_by_id_valid(store_api):
    store_api.delete_order_by_id(3)
    store_api.status_code_should_be(200)
    store_api.assert_schema_is_valid(ERROR_DELETE_STORE_SCHEMA)


def test_delete_order_by_id_no_exist_id(store_api):
    store_api.delete_order_by_id(3)
    store_api.status_code_should_be(404)
    store_api.assert_schema_is_valid(ERROR_DELETE_STORE_SCHEMA)
