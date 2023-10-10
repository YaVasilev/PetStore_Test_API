from model.create_user_model import generate_user_data

"""Данные для создания пользователя"""
valid_user_name = "TestUser"
create_valid_user_data = generate_user_data(user_id=258, user_name=valid_user_name, first_name="Test", last_name="User", user_email="TestEmail",
                                 user_pass="TestPass", user_phone="TestPhone", user_status=333)

no_valid_user_name = (111, True)
create_no_valid_user_data = generate_user_data(user_id="258", user_name=111, first_name=222, last_name=333, user_email=444,
                                 user_pass=555, user_phone=666, user_status="333")

"""Данные для обновления пользователя"""
update_user_data = generate_user_data(user_id=8, user_name="UpdateUser", first_name="Update", last_name="User",
                                      user_email="UpdateEmail", user_pass="UpdatePass", user_phone="UpdatePhone", user_status=5)