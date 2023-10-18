from model.store_model import RequestStoreModel

"""Данные для создания заказа на животное"""

valid_store_id = 3
valid_pet_id = 0
valid_quantity = 12
valid_status = "placed"
valid_complete = "true"
valid_ship_date = "2023-10-09T10:29:56.000+0000"

check_store_data = valid_store_id, valid_pet_id, valid_quantity, valid_status, valid_complete, valid_ship_date

valid_store_data = RequestStoreModel(valid_store_id, valid_pet_id, valid_quantity, valid_ship_date, valid_status,
                                     valid_complete).to_dict()



no_valid_id = ("abc", " ")
no_valid_check_data = ["404"]
no_valid_store_data = RequestStoreModel("abc", "zxc", "rtyr", 123, 4444, False).to_dict()

del_check_data = 404, "unknown", valid_store_id
