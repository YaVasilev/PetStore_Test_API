import pytest
from data.add_new_pet_to_store_data import valid_create_data, valid_create_data_test
from schema.post_add_new_pet_schema import POST_RESPONSE_SCHEMA

pytest_plugins = ["fixture.pet_api_fixture"]


def test_add_with_valid_params(pet_api):
    pet_api.add_pet_to_store()
    pet_api.status_code_should_be(200)
    pet_api.assert_schema_is_valid(POST_RESPONSE_SCHEMA)


def test_add_with_no_valid_params():
    pass
