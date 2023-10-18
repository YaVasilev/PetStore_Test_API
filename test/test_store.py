import pytest
from data.store_data.store_data import (valid_store_data, no_valid_store_data, valid_store_id, no_valid_id,
                                        check_store_data, no_valid_check_data)
from schema.store_shemas import STORE_SCHEMA, ERROR_DELETE_STORE_SCHEMA
from fixture.store_api_fixture import create_place_order, create_delete_place_order, delete_place_order

pytest_plugins = ["fixture.store_api_fixture"]


@pytest.mark.parametrize("store_valid_data", [valid_store_data])
@pytest.mark.parametrize("check_data", check_store_data)
def test_place_order_for_store_valid(store_api, store_valid_data, check_data, delete_place_order):
    store_api.place_an_order_for_a_pet(store_valid_data)
    store_api.status_code_should_be(200)
    store_api.assert_schema_is_valid(STORE_SCHEMA)
    store_api.assert_response_values_is_valid(check_data)


@pytest.mark.parametrize("store_no_valid_data", [no_valid_store_data])
@pytest.mark.parametrize("check_data_no_valid", [no_valid_check_data])
def test_place_order_for_store_no_valid(store_api, store_no_valid_data, check_data_no_valid):
    store_api.place_an_order_for_a_pet(store_no_valid_data)
    store_api.status_code_should_be(500)
    store_api.assert_schema_is_valid(ERROR_DELETE_STORE_SCHEMA)
    store_api.assert_response_values_is_valid(check_data_no_valid)


@pytest.mark.parametrize("valid_id_store", [valid_store_id])
@pytest.mark.parametrize("check_data", check_store_data)
def test_find_order_by_id_valid(store_api, valid_id_store, check_data, create_delete_place_order):
    store_api.find_order_by_id(valid_id_store)
    store_api.status_code_should_be(200)
    store_api.assert_schema_is_valid(STORE_SCHEMA)
    store_api.assert_response_values_is_valid(check_data)


@pytest.mark.parametrize("no_valid_store_id", no_valid_id)
@pytest.mark.parametrize("check_data_no_valid", no_valid_check_data)
def test_find_order_by_id_no_valid_id(store_api, no_valid_store_id, check_data_no_valid):
    store_api.find_order_by_id(no_valid_store_id)
    store_api.status_code_should_be(404)
    store_api.assert_schema_is_valid(ERROR_DELETE_STORE_SCHEMA)
    store_api.assert_response_values_is_valid(check_data_no_valid)


@pytest.mark.parametrize("valid_id_store", [valid_store_id])
def test_delete_order_by_id_valid(store_api, valid_id_store, create_place_order):
    store_api.delete_order_by_id(valid_id_store)
    store_api.status_code_should_be(200)
    store_api.assert_schema_is_valid(ERROR_DELETE_STORE_SCHEMA)


@pytest.mark.parametrize("no_valid_store_id", no_valid_id)
def test_delete_order_by_id_no_exist_id(store_api, no_valid_store_id):
    store_api.delete_order_by_id(no_valid_store_id)
    store_api.status_code_should_be(404)
    store_api.assert_schema_is_valid(ERROR_DELETE_STORE_SCHEMA)

