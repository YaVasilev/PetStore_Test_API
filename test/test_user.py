import pytest
from data.user_data.user_data import (create_valid_user_data, create_no_valid_user_data, update_user_data,
                                      no_valid_user_name, valid_user_name, response_valid_user_data)
from schema.user_schemas import CREATE_UPDATE_GET_USER_SCHEMA, DELETE_ERROR_USER_SCHEMA
from fixture.user_api_fixture import create_delete_user_valid_fixture, delete_user_valid_fixture

pytest_plugins = ["fixture.user_api_fixture"]


@pytest.mark.parametrize("valid_create_data", [create_valid_user_data])
@pytest.mark.parametrize("response_data_values", response_valid_user_data)
def test_create_user_valid(user_api, valid_create_data, delete_user_valid_fixture, response_data_values):
    user_api.create_user(valid_create_data)
    user_api.status_code_should_be(200)
    user_api.assert_schema_is_valid(CREATE_UPDATE_GET_USER_SCHEMA)
    user_api.assert_response_values_is_valid(response_data_values)


@pytest.mark.parametrize("no_valid_create_data", [create_no_valid_user_data])
def test_create_user_no_valid(user_api, no_valid_create_data):
    user_api.create_user(no_valid_create_data)
    user_api.status_code_should_be(200)
    user_api.assert_schema_is_valid(DELETE_ERROR_USER_SCHEMA)


@pytest.mark.parametrize("user_name_valid", [valid_user_name])
def test_update_user_valid(user_api, user_name_valid):
    user_api.update_user(user_name=user_name_valid, json_body=update_user_data)
    user_api.status_code_should_be(200)
    user_api.assert_schema_is_valid(CREATE_UPDATE_GET_USER_SCHEMA)


@pytest.mark.parametrize("user_name_no_valid", no_valid_user_name)
def test_update_user_no_valid(user_api, user_name_no_valid):
    user_api.update_user(user_name=user_name_no_valid, json_body=update_user_data)
    user_api.status_code_should_be(200)
    user_api.assert_schema_is_valid(CREATE_UPDATE_GET_USER_SCHEMA)


@pytest.mark.parametrize("user_name_valid", [valid_user_name])
@pytest.mark.parametrize("data_values", create_valid_user_data)
def test_get_user_by_name_valid(user_api, user_name_valid, data_values, create_delete_user_valid_fixture):
    user_api.get_user(user_name_valid)
    user_api.status_code_should_be(200)
    user_api.assert_schema_is_valid(CREATE_UPDATE_GET_USER_SCHEMA)
    user_api.assert_response_values_is_valid(data_values)


@pytest.mark.parametrize("user_name_no_valid", no_valid_user_name)
def test_get_user_by_name_no_valid(user_api, user_name_no_valid):
    user_api.get_user(user_name_no_valid)
    user_api.status_code_should_be(404)
    user_api.assert_schema_is_valid(CREATE_UPDATE_GET_USER_SCHEMA)


@pytest.mark.parametrize("user_name_valid", [valid_user_name])
def test_delete_user_by_name_valid(user_api, user_name_valid):
    user_api.delete_user(user_name_valid)
    user_api.status_code_should_be(200)
    user_api.assert_schema_is_valid(DELETE_ERROR_USER_SCHEMA)


@pytest.mark.parametrize("user_name_no_valid", no_valid_user_name)
def test_delete_user_by_name_no_valid(user_api, user_name_no_valid):
    user_api.delete_user(user_name_no_valid)
    user_api.status_code_should_be(404)
