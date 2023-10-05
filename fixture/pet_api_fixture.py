from api.all_pet_api.pet_api import PetApi
import pytest


"""Конектор к PetApi """
@pytest.fixture(scope="function")
def pet_api() -> PetApi:
    return PetApi()
