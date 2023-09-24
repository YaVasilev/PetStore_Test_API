from api.all_pet_api.pet_api import PetApi
import pytest


@pytest.fixture(scope="function")
def pet_api() -> PetApi:
    return PetApi()
