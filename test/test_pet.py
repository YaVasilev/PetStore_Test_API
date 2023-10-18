import pytest
from data.pet_data.pet_data import (valid_post_data, no_valid_post_data, valid_update_data, valid_main_id,
                                    response_expected_valid_main_id, response_expected_valid_category_id_name,
                                    response_expected_valid_name, response_expected_valid_photoUrls,
                                    response_expected_valid_tags_id_name, response_expected_valid_valid_status,
                                    response_expected_no_valid_code, response_expected_type,
                                    response_expected_no_valid_message, not_valid_pet_id,
                                    response_get_expected_no_valid_message,
                                    response_upd_expected_valid_message, response_exp_valid_code,
                                    response_del_expected_valid_message, no_valid_main_id,
                                    response_exp_no_valid_code, response_del_expected_no_valid_message)
from schema.pet_schemas import GET_POST_SCHEMA, GET_UPD_DEL_ERROR_SCHEMA
from fixture.pet_api_fixture import create_delete_pet_valid_fixture, delete_pet_valid_fixture, create_pet_valid_fixture

pytest_plugins = ["fixture.pet_api_fixture"]

"""Валидный тест по pet endpoint, создание, просмотр, изменение, удаление"""


@pytest.mark.parametrize("valid_post_body", [valid_post_data])
def test_add_pet_with_valid_params(pet_api, valid_post_body, delete_pet_valid_fixture):
    pet_api.add_pet_to_store(valid_post_body)
    pet_api.status_code_should_be(200)
    pet_api.assert_schema_is_valid(GET_POST_SCHEMA)
    pet_api.assert_equal_value_in_response_parameter(["id"], response_expected_valid_main_id, True)
    pet_api.assert_equal_value_in_response_parameter(["category"], response_expected_valid_category_id_name, True)
    pet_api.assert_equal_value_in_response_parameter(["name"], response_expected_valid_name, True)
    pet_api.assert_equal_value_in_response_parameter(["photoUrls"], response_expected_valid_photoUrls, True)
    pet_api.assert_equal_value_in_response_parameter(["tags"], response_expected_valid_tags_id_name, True)
    pet_api.assert_equal_value_in_response_parameter(["status"], response_expected_valid_valid_status, True)


@pytest.mark.parametrize("no_valid_post_body", [no_valid_post_data])
def test_add_pet_with_no_valid_params(pet_api, no_valid_post_body):
    pet_api.add_pet_to_store(no_valid_post_body)
    pet_api.status_code_should_be(500)
    pet_api.assert_schema_is_valid(GET_UPD_DEL_ERROR_SCHEMA)
    pet_api.assert_equal_value_in_response_parameter(["code"], response_expected_no_valid_code, True)
    pet_api.assert_equal_value_in_response_parameter(["type"], response_expected_type, True)
    pet_api.assert_equal_value_in_response_parameter(["message"], response_expected_no_valid_message, True)


@pytest.mark.parametrize("get_valid_pet_id", [valid_main_id])
def test_get_pet_with_valid_id(pet_api, get_valid_pet_id, create_delete_pet_valid_fixture):
    pet_api.get_pet(get_valid_pet_id)
    pet_api.status_code_should_be(200)
    pet_api.assert_schema_is_valid(GET_POST_SCHEMA)
    pet_api.assert_equal_value_in_response_parameter(["id"], response_expected_valid_main_id, True)
    pet_api.assert_equal_value_in_response_parameter(["category"], response_expected_valid_category_id_name, True)
    pet_api.assert_equal_value_in_response_parameter(["name"], response_expected_valid_name, True)
    pet_api.assert_equal_value_in_response_parameter(["photoUrls"], response_expected_valid_photoUrls, True)
    pet_api.assert_equal_value_in_response_parameter(["tags"], response_expected_valid_tags_id_name, True)
    pet_api.assert_equal_value_in_response_parameter(["status"], response_expected_valid_valid_status, True)


@pytest.mark.parametrize("no_valid_pet_id", [not_valid_pet_id])
def test_get_pet_with_no_valid_id(pet_api, no_valid_pet_id):
    pet_api.get_pet(no_valid_pet_id)
    pet_api.status_code_should_be(404)
    pet_api.assert_schema_is_valid(GET_UPD_DEL_ERROR_SCHEMA)
    pet_api.assert_equal_value_in_response_parameter(["code"], response_exp_no_valid_code, True)
    pet_api.assert_equal_value_in_response_parameter(["type"], response_expected_type, True)
    pet_api.assert_equal_value_in_response_parameter(["message"], response_get_expected_no_valid_message, True)


@pytest.mark.parametrize("update_json_body", [valid_update_data])
@pytest.mark.parametrize("upd_pet_id", [valid_main_id])
def test_update_pet_with_valid_id_and_params(pet_api, upd_pet_id, update_json_body, create_delete_pet_valid_fixture):
    pet_api.update_pet_by_id(pet_id=upd_pet_id, json_body=update_json_body)
    pet_api.status_code_should_be(200)
    pet_api.assert_schema_is_valid(GET_UPD_DEL_ERROR_SCHEMA)
    pet_api.assert_equal_value_in_response_parameter(["code"], response_exp_valid_code, True)
    pet_api.assert_equal_value_in_response_parameter(["type"], response_expected_type, True)
    pet_api.assert_equal_value_in_response_parameter(["message"], response_upd_expected_valid_message, True)


@pytest.mark.parametrize("del_pet_id", [valid_main_id])
def test_delete_pet_with_valid_id(pet_api, del_pet_id, create_pet_valid_fixture):
    pet_api.delete_pet(del_pet_id)
    pet_api.status_code_should_be(200)
    pet_api.assert_schema_is_valid(GET_UPD_DEL_ERROR_SCHEMA)
    pet_api.assert_equal_value_in_response_parameter(["code"], response_exp_valid_code, True)
    pet_api.assert_equal_value_in_response_parameter(["type"], response_expected_type, True)
    pet_api.assert_equal_value_in_response_parameter(["message"], response_del_expected_valid_message, True)


@pytest.mark.parametrize("no_del_pet_id", [no_valid_main_id])
def test_delete_pet_with_no_valid_id(pet_api, no_del_pet_id):
    pet_api.delete_pet(no_del_pet_id)
    pet_api.status_code_should_be(404)
    pet_api.assert_schema_is_valid(GET_UPD_DEL_ERROR_SCHEMA)
    pet_api.assert_equal_value_in_response_parameter(["code"], response_exp_no_valid_code, True)
    pet_api.assert_equal_value_in_response_parameter(["type"], response_expected_type, True)
    pet_api.assert_equal_value_in_response_parameter(["message"], response_del_expected_no_valid_message, True)
