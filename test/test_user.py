import pytest
from data.user_data.create_user_data import create_valid_user_data, create_no_valid_user_data
from data.user_data.update_user_data import update_user_data
from schema.user_schemas import CREATE_UPDATE_GET_USER_SCHEMA, DELETE_ERROR_USER_SCHEMA

pytest_plugins = ["fixture.user_api_fixture"]


@pytest.mark.parametrize("valid_create_data", [create_valid_user_data])
def test_create_user_valid(user_api, valid_create_data):
    user_api.create_user(valid_create_data)
    user_api.status_code_should_be(200)
    user_api.assert_schema_is_valid(CREATE_UPDATE_GET_USER_SCHEMA)


@pytest.mark.parametrize("no_valid_create_data", [create_no_valid_user_data])
def test_create_user_no_valid(user_api, no_valid_create_data):
    user_api.create_user(no_valid_create_data)
    user_api.status_code_should_be(405)
    user_api.assert_schema_is_valid(DELETE_ERROR_USER_SCHEMA)


def test_update_user_valid(user_api):
    user_api.update_user(user_name="TestUser", json_body=update_user_data)
    user_api.status_code_should_be(200)
    user_api.assert_schema_is_valid(CREATE_UPDATE_GET_USER_SCHEMA)


def test_get_user_by_name_valid(user_api):
    user_api.get_user("UpdateUser")
    user_api.status_code_should_be(200)
    user_api.assert_schema_is_valid(CREATE_UPDATE_GET_USER_SCHEMA)


def test_delete_user_by_name_valid(user_api):
    user_api.delete_user("UpdateUser")
    user_api.status_code_should_be(200)
    user_api.assert_schema_is_valid(DELETE_ERROR_USER_SCHEMA)
