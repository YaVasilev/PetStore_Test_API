import pytest
from api.all_user_api.user_api import UserApi

"""Конектор к StoreApi """


@pytest.fixture(scope="function")
def user_api() -> UserApi:
    return UserApi()