import pytest
from api.all_user_api.user_api import UserApi
from data.user_data.user_data import create_valid_user_data, valid_user_name
pytest_plugins = ["fixture.user_api_fixture"]

"""Конектор к UserApi """


@pytest.fixture(scope="function")
def user_api() -> UserApi:
    return UserApi()


@pytest.fixture(scope="function")
def create_delete_user_valid_fixture(user_api):
    user_api.create_user(create_valid_user_data)
    yield
    user_api.delete_user(valid_user_name)


@pytest.fixture(scope="function")
def delete_user_valid_fixture(user_api):
    yield
    user_api.delete_user(valid_user_name)