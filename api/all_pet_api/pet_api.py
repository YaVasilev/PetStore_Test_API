from api.base_api import BaseApi
from data.add_new_pet_to_store_data import generate_valid_data


GET_PET_BY_ID_ENDPOINT = "/v2/pet/"
POST_ADD_PET_TO_STORE = "/v2/pet"
HEADERS = {
    "accept": "application/json",
    "Content-Type": "application/json"
}


class PetApi(BaseApi):
    def get_pet(self, pet_id):
        return self.get(endpoint=GET_PET_BY_ID_ENDPOINT,
                        pet_id=pet_id)

    def add_pet_to_store(self, json_body):
        return self.post(endpoint=POST_ADD_PET_TO_STORE,
                         headers=HEADERS,
                         json=json_body)