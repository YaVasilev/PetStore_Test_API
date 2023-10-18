import pytest
from data.user_data.user_data import (create_valid_user_data, create_no_valid_user_data, update_user_data,
                                      no_valid_user_name, valid_user_name, response_expected_code,
                                      response_expected_type, response_expected_message,
                                      response_expected_no_valid_code,
                                      response_expected_no_valid_message,
                                      response_update_expected_message,
                                      response_update_expected_no_valid_message,
                                      response_get_id, response_get_username, response_get_firstName,
                                      response_get_lastName,
                                      response_get_email, response_get_password, response_get_phone,
                                      response_get_userStatus,
                                      response_get_expected_no_valid_code, response_get_expected_no_valid_type,
                                      response_get_expected_no_valid_message,
                                      response_delete_expected_no_valid_message)
from fixture.user_api_fixture import create_user_valid_fixture, create_delete_user_valid_fixture, \
    delete_user_valid_fixture
from schema.user_schemas import CREATE_UPDATE_GET_USER_SCHEMA, DELETE_ERROR_USER_SCHEMA

pytest_plugins = ["fixture.user_api_fixture"]


@pytest.mark.parametrize("valid_create_data", [create_valid_user_data])
def test_create_user_valid(user_api, valid_create_data, delete_user_valid_fixture):
    user_api.create_user(valid_create_data)
    user_api.status_code_should_be(200)
    user_api.assert_schema_is_valid(CREATE_UPDATE_GET_USER_SCHEMA)
    user_api.assert_equal_value_in_response_parameter(["code"], response_expected_code, True)
    user_api.assert_equal_value_in_response_parameter(["type"], response_expected_type, True)
    user_api.assert_equal_value_in_response_parameter(["message"], response_expected_message, True)


@pytest.mark.parametrize("no_valid_create_data", [create_no_valid_user_data])
def test_create_user_no_valid(user_api, no_valid_create_data):
    user_api.create_user(no_valid_create_data)
    user_api.status_code_should_be(500)
    user_api.assert_schema_is_valid(DELETE_ERROR_USER_SCHEMA)
    user_api.assert_equal_value_in_response_parameter(["code"], response_expected_no_valid_code, True)
    user_api.assert_equal_value_in_response_parameter(["type"], response_expected_type, True)
    user_api.assert_equal_value_in_response_parameter(["message"], response_expected_no_valid_message, True)


@pytest.mark.parametrize("user_name_valid", [valid_user_name])
def test_update_user_valid(user_api, user_name_valid, create_delete_user_valid_fixture):
    user_api.update_user(user_name=user_name_valid, json_body=update_user_data)
    user_api.status_code_should_be(200)
    user_api.assert_schema_is_valid(CREATE_UPDATE_GET_USER_SCHEMA)
    user_api.assert_equal_value_in_response_parameter(["code"], response_expected_code, True)
    user_api.assert_equal_value_in_response_parameter(["type"], response_expected_type, True)
    user_api.assert_equal_value_in_response_parameter(["message"], response_update_expected_message, True)


@pytest.mark.parametrize("user_name_no_valid", no_valid_user_name)
def test_update_user_no_valid(user_api, user_name_no_valid):
    user_api.update_user(user_name=user_name_no_valid, json_body=update_user_data)
    user_api.status_code_should_be(200)
    user_api.assert_schema_is_valid(CREATE_UPDATE_GET_USER_SCHEMA)
    user_api.assert_equal_value_in_response_parameter(["code"], response_expected_code, True)
    user_api.assert_equal_value_in_response_parameter(["type"], response_expected_type, True)
    user_api.assert_equal_value_in_response_parameter(["message"], response_update_expected_no_valid_message, True)


@pytest.mark.parametrize("user_name_valid", [valid_user_name])
def test_get_user_by_name_valid(user_api, user_name_valid, create_delete_user_valid_fixture):
    user_api.get_user(user_name_valid)
    user_api.status_code_should_be(200)
    user_api.assert_schema_is_valid(CREATE_UPDATE_GET_USER_SCHEMA)
    user_api.assert_equal_value_in_response_parameter(["id"], response_get_id, True)
    user_api.assert_equal_value_in_response_parameter(["username"], response_get_username, True)
    user_api.assert_equal_value_in_response_parameter(["firstName"], response_get_firstName, True)
    user_api.assert_equal_value_in_response_parameter(["lastName"], response_get_lastName, True)
    user_api.assert_equal_value_in_response_parameter(["email"], response_get_email, True)
    user_api.assert_equal_value_in_response_parameter(["password"], response_get_password, True)
    user_api.assert_equal_value_in_response_parameter(["phone"], response_get_phone, True)
    user_api.assert_equal_value_in_response_parameter(["userStatus"], response_get_userStatus, True)


@pytest.mark.parametrize("user_name_no_valid", no_valid_user_name)
def test_get_user_by_name_no_valid(user_api, user_name_no_valid):
    user_api.get_user(user_name_no_valid)
    user_api.status_code_should_be(404)
    user_api.assert_schema_is_valid(CREATE_UPDATE_GET_USER_SCHEMA)
    user_api.assert_equal_value_in_response_parameter(["code"], response_get_expected_no_valid_code, True)
    user_api.assert_equal_value_in_response_parameter(["type"], response_get_expected_no_valid_type, True)
    user_api.assert_equal_value_in_response_parameter(["message"], response_get_expected_no_valid_message, True)


@pytest.mark.parametrize("user_name_valid", [valid_user_name])
def test_delete_user_by_name_valid(user_api, user_name_valid, create_user_valid_fixture):
    user_api.delete_user(user_name_valid)
    user_api.status_code_should_be(200)
    user_api.assert_schema_is_valid(DELETE_ERROR_USER_SCHEMA)
    user_api.assert_equal_value_in_response_parameter(["code"], response_expected_code, True)
    user_api.assert_equal_value_in_response_parameter(["type"], response_expected_type, True)
    user_api.assert_equal_value_in_response_parameter(["message"], response_delete_expected_no_valid_message, True)


@pytest.mark.parametrize("user_name_no_valid", no_valid_user_name)
def test_delete_user_by_name_no_valid(user_api, user_name_no_valid):
    user_api.delete_user(user_name_no_valid)
    user_api.status_code_should_be(404)
