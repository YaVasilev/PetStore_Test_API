from api.base_api import BaseApi

PLACE_ORDER_FOR_PET = "/v2/store/order"
FIND_ORDER_BY_ID = "/v2/store/order/"
DELETE_ORDER_BY_ID = "/v2/store/order/"


class StoreApi(BaseApi):
    """Размещение заказа на животное"""

    def place_an_order_for_a_pet(self, json_body):
        return self.post(endpoint=PLACE_ORDER_FOR_PET,
                         headers=self.HEADERS,
                         json=json_body)

    """Поиск заказа по Id"""
    def find_order_by_id(self, get_store_id):
        return self.get(endpoint=FIND_ORDER_BY_ID,
                        id=get_store_id)

    def delete_order_by_id(self, delete_store_id):
        return self.delete(endpoint=DELETE_ORDER_BY_ID,
                           id=delete_store_id)
