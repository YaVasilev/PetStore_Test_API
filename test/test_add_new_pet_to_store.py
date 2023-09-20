from api.base_api import BaseApi
from data.add_new_pet_to_store_data import create_data
from configurations import BASE_URL, GET_PET_BY_ID_ENDPOINT, POST_ADD_PET_TO_STORE


def test_add_with_valid_params():
    BaseApi.post(BaseApi, url=BASE_URL, endpoint=POST_ADD_PET_TO_STORE,
                 json=create_data).status_code_should_be(BaseApi, 200).response_has_keys_in_json(BaseApi,
                                                                                                 BaseApi.post(BaseApi,
                                                                                                              url=BASE_URL,
                                                                                                              endpoint=POST_ADD_PET_TO_STORE,
                                                                                                              json=create_data),
                                                                                                 ["id", "category",
                                                                                                  "name", "photoUrls",
                                                                                                  "tags", "status"])
    BaseApi.post(BaseApi, url=BASE_URL, endpoint=POST_ADD_PET_TO_STORE,
                 json=create_data).status_code_should_be(BaseApi, 200).response_has_value_in_json(BaseApi,
                                                                                                  BaseApi.get(BaseApi,
                                                                                                              url=BASE_URL,
                                                                                                              endpoint=GET_PET_BY_ID_ENDPOINT,
                                                                                                              pet_id=222),
                                                                                                  "id", 222,
                                                                                                  "Wrong value")
    BaseApi.post(BaseApi, url=BASE_URL, endpoint=POST_ADD_PET_TO_STORE,
                 json=create_data).status_code_should_be(BaseApi, 200).response_has_value_in_json(BaseApi,
                                                                                                  BaseApi.get(BaseApi,
                                                                                                              url=BASE_URL,
                                                                                                              endpoint=GET_PET_BY_ID_ENDPOINT,
                                                                                                              pet_id=222),
                                                                                                  "name", "TestName",
                                                                                                  "Wrong value")
    BaseApi.post(BaseApi, url=BASE_URL, endpoint=POST_ADD_PET_TO_STORE,
                 json=create_data).status_code_should_be(BaseApi, 200).response_has_value_in_json(BaseApi,
                                                                                                  BaseApi.get(BaseApi,
                                                                                                              url=BASE_URL,
                                                                                                              endpoint=GET_PET_BY_ID_ENDPOINT,
                                                                                                              pet_id=222),
                                                                                                  "status", "available",
                                                                                                  "Wrong value")


def test_add_with_no_valid_params():
    pass



