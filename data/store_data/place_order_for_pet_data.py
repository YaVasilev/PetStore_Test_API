from model.place_order_for_pet_model import generate_store_data

"""Данные для создания заказа на животное"""
valid_id = 3
valid_store_data = generate_store_data(store_id=valid_id, pet_id=123, quantity=12, ship_date="2023-10-09T10:29:56.485Z",
                                       status="placed", complete=True)

no_valid_id = ("abc", 999, " ")
no_valid_store_data = generate_store_data(store_id="abc", pet_id="zxc", quantity="rtyr", ship_date=123,
                                          status=4444, complete=False)