import pytest
from data.store_data.place_order_for_pet_data import valid_store_data, no_valid_store_data, valid_id, no_valid_id
from schema.store_shemas import STORE_SCHEMA, ERROR_DELETE_STORE_SCHEMA

pytest_plugins = ["fixture.store_api_fixture"]


@pytest.mark.parametrize("store_valid_data", [valid_store_data])
def test_place_order_for_store_valid(store_api, store_valid_data):
    store_api.place_an_order_for_a_pet(store_valid_data)
    store_api.status_code_should_be(200)
    store_api.assert_schema_is_valid(STORE_SCHEMA)


@pytest.mark.parametrize("store_no_valid_data", [no_valid_store_data])
def test_place_order_for_store_no_valid(store_api, store_no_valid_data):
    store_api.place_an_order_for_a_pet(store_no_valid_data)
    store_api.status_code_should_be(500)
    store_api.assert_schema_is_valid(ERROR_DELETE_STORE_SCHEMA)


@pytest.mark.parametrize("valid_store_id", [valid_id])
def test_find_order_by_id_valid(store_api, valid_store_id):
    store_api.find_order_by_id(valid_store_id)
    store_api.status_code_should_be(200)
    store_api.assert_schema_is_valid(STORE_SCHEMA)


@pytest.mark.parametrize("no_valid_store_id", no_valid_id)
def test_find_order_by_id_no_valid_id(store_api, no_valid_store_id):
    store_api.find_order_by_id(no_valid_store_id)
    store_api.status_code_should_be(404)
    store_api.assert_schema_is_valid(ERROR_DELETE_STORE_SCHEMA)


@pytest.mark.parametrize("valid_store_id", [valid_id])
def test_delete_order_by_id_valid(store_api, valid_store_id):
    store_api.delete_order_by_id(valid_store_id)
    store_api.status_code_should_be(200)
    store_api.assert_schema_is_valid(ERROR_DELETE_STORE_SCHEMA)


@pytest.mark.parametrize("no_valid_store_id", no_valid_id)
def test_delete_order_by_id_no_exist_id(store_api, no_valid_store_id):
    store_api.delete_order_by_id(no_valid_store_id)
    store_api.status_code_should_be(404)
    store_api.assert_schema_is_valid(ERROR_DELETE_STORE_SCHEMA)
