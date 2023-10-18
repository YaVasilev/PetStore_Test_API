import pytest
from data.pet_data.pet_data import (valid_post_data, no_valid_post_data, check_data, check_no_valid_data,
                                    valid_update_data, upd_check_data, valid_main_id)
from schema.pet_schemas import GET_POST_SCHEMA, GET_UPD_DEL_ERROR_SCHEMA
from fixture.pet_api_fixture import create_delete_pet_valid_fixture, delete_pet_valid_fixture, create_pet_valid_fixture

pytest_plugins = ["fixture.pet_api_fixture"]

"""Валидный тест по pet endpoint, создание, просмотр, изменение, удаление"""


@pytest.mark.parametrize("post_json_body", [valid_post_data])
@pytest.mark.parametrize("data_check", check_data)
def test_add_pet_with_valid_params(pet_api, post_json_body, data_check, delete_pet_valid_fixture):
    pet_api.add_pet_to_store(post_json_body)
    pet_api.status_code_should_be(200)
    pet_api.assert_schema_is_valid(GET_POST_SCHEMA)
    pet_api.assert_response_values_is_valid(data_check)


@pytest.mark.parametrize("get_valid_pet_id", [valid_main_id])
@pytest.mark.parametrize("data_check", check_data)
def test_get_pet_with_valid_id(pet_api, get_valid_pet_id, data_check, create_delete_pet_valid_fixture):
    pet_api.get_pet(get_valid_pet_id)
    pet_api.status_code_should_be(200)
    pet_api.assert_schema_is_valid(GET_POST_SCHEMA)
    pet_api.assert_response_values_is_valid(data_check)


@pytest.mark.parametrize("update_json_body", [valid_update_data])
@pytest.mark.parametrize("upd_pet_id", [valid_main_id])
@pytest.mark.parametrize("upd_check", upd_check_data)
def test_update_pet_with_valid_id_and_params(pet_api, upd_pet_id, update_json_body, upd_check, create_delete_pet_valid_fixture):
    pet_api.update_pet_by_id(pet_id=upd_pet_id, json_body=update_json_body)
    pet_api.status_code_should_be(200)
    pet_api.assert_schema_is_valid(GET_UPD_DEL_ERROR_SCHEMA)
    pet_api.assert_response_values_is_valid(upd_check)


@pytest.mark.parametrize("del_pet_id", [valid_main_id])
def test_delete_pet_with_valid_id(pet_api, del_pet_id, create_pet_valid_fixture):
    pet_api.delete_pet(del_pet_id)
    pet_api.status_code_should_be(200)
    pet_api.assert_schema_is_valid(GET_UPD_DEL_ERROR_SCHEMA)


@pytest.mark.parametrize("no_val_post_data", no_valid_post_data)
@pytest.mark.parametrize("no_valid_check", check_no_valid_data)
def test_add_pet_with_no_valid_params(pet_api, no_val_post_data, no_valid_check):
    pet_api.add_pet_to_store(no_val_post_data)
    pet_api.status_code_should_be(500)
    pet_api.assert_schema_is_valid(GET_UPD_DEL_ERROR_SCHEMA)
    pet_api.assert_response_values_is_valid(no_valid_check)
