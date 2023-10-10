from api.base_api import BaseApi

CREATE_USER_ENDPOINT = "/v2/user"
UPDATE_GET_DELETE_USER_ENDPOINT = "/v2/user/"


class UserApi(BaseApi):

    def create_user(self, json_body):
        return self.post(endpoint=CREATE_USER_ENDPOINT,
                         headers=self.HEADERS,
                         json=json_body)

    def update_user(self, user_name, json_body):
        return self.put(endpoint=f"{UPDATE_GET_DELETE_USER_ENDPOINT}{user_name}",
                        headers=self.HEADERS,
                        json=json_body)

    def get_user(self, user_name):
        return self.get(endpoint=UPDATE_GET_DELETE_USER_ENDPOINT,
                        id=user_name)

    def delete_user(self, user_name):
        return self.delete(endpoint=UPDATE_GET_DELETE_USER_ENDPOINT,
                           id=user_name)