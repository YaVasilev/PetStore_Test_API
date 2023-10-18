import pytest
from data.store_data.store_data import (valid_store_data, no_valid_store_data, valid_store_id, no_valid_id,
                                        response_expected_valid_store_id, response_expected_valid_pet_id,
                                        response_expected_valid_valid_quantity, response_expected_valid_status,
                                        response_expected_valid_complete, response_expected_valid_ship_date,
                                        response_post_expected_no_valid_code, response_expected_type,
                                        response_post_expected_no_valid_message, response_expected_no_valid_code,
                                        response_delete_expected_valid_code, response_delete_expected_valid_message)
from schema.store_shemas import STORE_SCHEMA, ERROR_DELETE_STORE_SCHEMA
from fixture.store_api_fixture import create_place_order, create_delete_place_order, delete_place_order

pytest_plugins = ["fixture.store_api_fixture"]


@pytest.mark.parametrize("store_valid_data", [valid_store_data])
def test_place_order_for_store_valid(store_api, store_valid_data, delete_place_order):
    store_api.place_an_order_for_a_pet(store_valid_data)
    store_api.status_code_should_be(200)
    store_api.assert_schema_is_valid(STORE_SCHEMA)
    store_api.assert_equal_value_in_response_parameter(["id"], response_expected_valid_store_id, True)
    store_api.assert_equal_value_in_response_parameter(["petId"], response_expected_valid_pet_id, True)
    store_api.assert_equal_value_in_response_parameter(["quantity"], response_expected_valid_valid_quantity, True)
    store_api.assert_equal_value_in_response_parameter(["shipDate"], response_expected_valid_ship_date, True)
    store_api.assert_equal_value_in_response_parameter(["status"], response_expected_valid_status, True)
    store_api.assert_equal_value_in_response_parameter(["complete"], response_expected_valid_complete, True)


@pytest.mark.parametrize("store_no_valid_data", [no_valid_store_data])
def test_place_order_for_store_no_valid(store_api, store_no_valid_data):
    store_api.place_an_order_for_a_pet(store_no_valid_data)
    store_api.status_code_should_be(500)
    store_api.assert_schema_is_valid(ERROR_DELETE_STORE_SCHEMA)
    store_api.assert_equal_value_in_response_parameter(["code"], response_post_expected_no_valid_code, True)
    store_api.assert_equal_value_in_response_parameter(["type"], response_expected_type, True)
    store_api.assert_equal_value_in_response_parameter(["message"], response_post_expected_no_valid_message, True)


@pytest.mark.parametrize("valid_id_store", [valid_store_id])
def test_find_order_by_id_valid(store_api, valid_id_store, create_delete_place_order):
    store_api.find_order_by_id(valid_id_store)
    store_api.status_code_should_be(200)
    store_api.assert_schema_is_valid(STORE_SCHEMA)
    store_api.assert_equal_value_in_response_parameter(["id"], response_expected_valid_store_id, True)
    store_api.assert_equal_value_in_response_parameter(["petId"], response_expected_valid_pet_id, True)
    store_api.assert_equal_value_in_response_parameter(["quantity"], response_expected_valid_valid_quantity, True)
    store_api.assert_equal_value_in_response_parameter(["shipDate"], response_expected_valid_ship_date, True)
    store_api.assert_equal_value_in_response_parameter(["status"], response_expected_valid_status, True)
    store_api.assert_equal_value_in_response_parameter(["complete"], response_expected_valid_complete, True)


@pytest.mark.parametrize("no_valid_store_id", no_valid_id)
def test_find_order_by_id_no_valid_id(store_api, no_valid_store_id):
    store_api.find_order_by_id(no_valid_store_id)
    store_api.status_code_should_be(404)
    store_api.assert_schema_is_valid(ERROR_DELETE_STORE_SCHEMA)
    store_api.assert_equal_value_in_response_parameter(["code"], response_expected_no_valid_code, True)
    store_api.assert_equal_value_in_response_parameter(["type"], response_expected_type, True)


@pytest.mark.parametrize("valid_id_store", [valid_store_id])
def test_delete_order_by_id_valid(store_api, valid_id_store, create_place_order):
    store_api.delete_order_by_id(valid_id_store)
    store_api.status_code_should_be(200)
    store_api.assert_schema_is_valid(ERROR_DELETE_STORE_SCHEMA)
    store_api.assert_equal_value_in_response_parameter(["code"], response_delete_expected_valid_code, True)
    store_api.assert_equal_value_in_response_parameter(["type"], response_expected_type, True)
    store_api.assert_equal_value_in_response_parameter(["message"], response_delete_expected_valid_message, True)


@pytest.mark.parametrize("no_valid_store_id", no_valid_id)
def test_delete_order_by_id_no_exist_id(store_api, no_valid_store_id):
    store_api.delete_order_by_id(no_valid_store_id)
    store_api.status_code_should_be(404)
    store_api.assert_schema_is_valid(ERROR_DELETE_STORE_SCHEMA)
    store_api.assert_equal_value_in_response_parameter(["code"], response_expected_no_valid_code, True)
    store_api.assert_equal_value_in_response_parameter(["type"], response_expected_type, True)
