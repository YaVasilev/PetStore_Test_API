from api.all_pet_api.pet_api import PetApi
from data.pet_data.pet_data import valid_post_data, valid_main_id
import pytest

"""Конектор к PetApi """


@pytest.fixture(scope="function")
def pet_api() -> PetApi:
    return PetApi()


@pytest.fixture(scope="function")
def create_pet_valid_fixture(pet_api):
    pet_api.add_pet_to_store(valid_post_data)


@pytest.fixture(scope="function")
def create_delete_pet_valid_fixture(pet_api):
    pet_api.add_pet_to_store(valid_post_data)
    yield
    pet_api.delete_pet(valid_main_id)


@pytest.fixture(scope="function")
def delete_pet_valid_fixture(pet_api):
    yield
    pet_api.delete_pet(valid_main_id)
