import pytest
from data.find_pet_by_id_data import valid_pet_id, not_valid_pet_id, empty_pet_id
from schema.get_pet_schema import GET_SCHEMA, GET_ERROR_SCHEMA, GET_EMPTY_SCHEMA

pytest_plugins = ["fixture.pet_api_fixture"]


@pytest.mark.parametrize("pet_id", valid_pet_id)
def test_with_valid_id(pet_api, pet_id):
    pet_api.get_pet(pet_id)
    pet_api.status_code_should_be(200)
    pet_api.assert_schema_is_valid(GET_SCHEMA)


@pytest.mark.parametrize("pet_id", not_valid_pet_id)
def test_with_no_valid_id(pet_api, pet_id):
    pet_api.get_pet(pet_id)
    pet_api.status_code_should_be(404)
    pet_api.assert_schema_is_valid(GET_ERROR_SCHEMA)


@pytest.mark.parametrize("pet_id", empty_pet_id)
def test_with_empty_id(pet_api, pet_id):
    pet_api.get_pet(pet_id)
    pet_api.status_code_should_be(405)
    pet_api.assert_schema_is_valid(GET_EMPTY_SCHEMA)