import pytest
from data.pet_data.update_pet_by_id_data import valid_update_data
from data.pet_data.add_new_pet_to_store_data import valid_post_data, no_valid_post_data, empty_data
from data.pet_data.find_pet_by_id_data import get_pet_id
from data.pet_data.update_pet_by_id_data import update_pet_id
from data.pet_data.delete_pet_data import delete_pet_id
from schema.pet_schemas import GET_POST_SCHEMA, UPDATE_POST_SCHEMA, DELETE_RESP_PET_SCHEMA, GET_ERROR_SCHEMA

pytest_plugins = ["fixture.pet_api_fixture"]

"""Валидный тест по pet endpoint, создание, просмотр, изменение, удаление"""


@pytest.mark.parametrize("post_json_body", [valid_post_data])
def test_add_pet_with_valid_params(pet_api, post_json_body):
    pet_api.add_pet_to_store(post_json_body)
    pet_api.status_code_should_be(200)
    pet_api.assert_schema_is_valid(GET_POST_SCHEMA)


@pytest.mark.parametrize("get_valid_pet_id", [get_pet_id])
def test_get_pet_with_valid_id(pet_api, get_valid_pet_id):
    pet_api.get_pet(get_valid_pet_id)
    pet_api.status_code_should_be(200)
    pet_api.assert_schema_is_valid(GET_POST_SCHEMA)


@pytest.mark.parametrize("update_json_body", [valid_update_data])
@pytest.mark.parametrize("upd_pet_id", [update_pet_id])
def test_update_pet_with_valid_id_and_params(pet_api, upd_pet_id, update_json_body):
    pet_api.update_pet_by_id(pet_id=upd_pet_id, json_body=update_json_body)
    pet_api.status_code_should_be(200)
    pet_api.assert_schema_is_valid(UPDATE_POST_SCHEMA)


@pytest.mark.parametrize("del_pet_id", [delete_pet_id])
def test_delete_pet_with_valid_id(pet_api, del_pet_id):
    pet_api.delete_pet(delete_pet_id)
    pet_api.status_code_should_be(200)
    pet_api.assert_schema_is_valid(DELETE_RESP_PET_SCHEMA)


@pytest.mark.parametrize("no_val_post_data", no_valid_post_data)
def test_add_pet_with_no_valid_params(pet_api, no_val_post_data):
    pet_api.add_pet_to_store(no_val_post_data)
    pet_api.status_code_should_be(500)
    pet_api.assert_schema_is_valid(GET_ERROR_SCHEMA)


@pytest.mark.parametrize("no_json_data", [empty_data])
def test_add_pet_with_empty_json_body(pet_api, no_json_data):
    pet_api.add_pet_to_store(no_json_data)
    pet_api.pet_api.status_code_should_be(200)
    pet_api.assert_schema_is_valid(GET_POST_SCHEMA)
