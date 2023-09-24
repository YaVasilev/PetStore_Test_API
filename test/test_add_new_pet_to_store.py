import pytest
from data.add_new_pet_to_store_data import generate_valid_data
from schema.post_add_new_pet_schema import POST_RESPONSE_SCHEMA

pytest_plugins = ["fixture.pet_api_fixture"]


@pytest.mark.parametrize("json_body", [generate_valid_data()])
def test_add_with_valid_params(pet_api, json_body):
    pet_api.add_pet_to_store(json_body)
    pet_api.status_code_should_be(200)
    pet_api.assert_schema_is_valid(POST_RESPONSE_SCHEMA)


def test_add_with_no_valid_params():
    pass
