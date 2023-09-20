from api.base_api import BaseApi
from schema.get_pet_schema import GET_SCHEMA
from configurations import BASE_URL, GET_PET_BY_ID_ENDPOINT


def test_with_valid_id():
    BaseApi.status_code_should_be(BaseApi.get(BaseApi, endpoint=GET_PET_BY_ID_ENDPOINT, pet_id=222), 200)

    BaseApi.response_has_keys_in_json(BaseApi, BaseApi.get(BaseApi, endpoint=GET_PET_BY_ID_ENDPOINT, pet_id=222),
                                      ["id", "category", "name", "photoUrls", "tags", "status"])

    BaseApi.response_has_value_in_json(BaseApi, BaseApi.get(BaseApi, endpoint=GET_PET_BY_ID_ENDPOINT,
                                                   pet_id=222), "id", 222, "Wrong value")

    BaseApi.response_has_value_in_json(BaseApi, BaseApi.get(BaseApi, endpoint=GET_PET_BY_ID_ENDPOINT,
                                                   pet_id=222), "name", "TestName","Wrong value")

    BaseApi.response_has_value_in_json(BaseApi, BaseApi.get(BaseApi, endpoint=GET_PET_BY_ID_ENDPOINT,
                                                   pet_id=222), "status", "available","Wrong value")

    BaseApi.response_schema_is_valid(BaseApi.get(BaseApi, endpoint=GET_PET_BY_ID_ENDPOINT, pet_id=222), GET_SCHEMA)


def test_with_no_valid_id():
    BaseApi.status_code_should_be(BaseApi.get(BaseApi, endpoint=GET_PET_BY_ID_ENDPOINT, pet_id="asd"), 404)

    BaseApi.response_has_keys_in_json(BaseApi, BaseApi.get(BaseApi, endpoint=GET_PET_BY_ID_ENDPOINT,
                                                                     pet_id="asd"), ["code", "type", "message"])
