from model.store_model import RequestStoreModel

"""Общие данные"""
"""Id для поиска, удаления не валидного заказа"""
no_valid_id = ("abc", " ")

"""Type для создания, поиска, удаления заказа"""
response_expected_type = "unknown"

"""Code для поиска, удаления не валидного заказа"""
response_expected_no_valid_code = 404

"""StoreId для создания, поиска, удаления валидного заказа"""
valid_store_id = 3

"""Данные для создания валидного заказа на животное"""

valid_pet_id = 0
valid_quantity = 12
valid_status = "placed"
valid_complete = "True"
valid_ship_date = "2023-10-09T10:29:56.000+0000"

valid_store_data = RequestStoreModel(valid_store_id, valid_pet_id, valid_quantity, valid_ship_date, valid_status,
                                     valid_complete).to_dict()

"""Данные для проверки создания и поиска валидного заказа на животное"""
response_expected_valid_store_id = valid_store_id
response_expected_valid_pet_id = valid_pet_id
response_expected_valid_valid_quantity = valid_quantity
response_expected_valid_ship_date = valid_ship_date
response_expected_valid_status = valid_status
response_expected_valid_complete = bool(valid_complete)

"""Данные для создания не валидного заказа на животное"""
no_valid_store_id = "abc"
no_valid_pet_id = "zxc"
no_valid_quantity = "rtyr"
no_valid_status = 123
no_valid_complete = 4444
no_valid_ship_date = False

no_valid_store_data = RequestStoreModel(no_valid_store_id, no_valid_pet_id, no_valid_quantity, no_valid_status,
                                        no_valid_complete, no_valid_ship_date).to_dict()

"""Данные для проверки создания не валидного заказа на животное"""
response_post_expected_no_valid_code = 500
response_post_expected_no_valid_message = "something bad happened"

"""Данные для проверки поиска не валидного заказа"""

#response_get_expected_no_valid_message = "java.lang.NumberFormatException: For input string: \"abc\""

"""Данные для проверки удаления валидного заказа"""
response_delete_expected_valid_code = 200
response_delete_expected_valid_message = str(valid_store_id)
