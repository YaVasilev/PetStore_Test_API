from model.user_model import RequestCreateUserModel

"""Данные для создания пользователя"""
valid_user_name = "TestUser"
create_valid_user_data = RequestCreateUserModel(258, valid_user_name, "Test", "User", "TestEmail", "TestPass", "TestPhone", 333).to_dict()

no_valid_user_name = (111, True)
create_no_valid_user_data = RequestCreateUserModel("258", 111, 222, 333, 444, 555, 666, "333").to_dict()

"""Данные для обновления пользователя"""
update_user_data = RequestCreateUserModel(8, "UpdateUser", "Update", "User", "UpdateEmail", "UpdatePass", "UpdatePhone", 5).to_dict()

response_valid_user_data = 200, "unknown", 258