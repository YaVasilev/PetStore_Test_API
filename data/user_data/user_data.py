from model.user_model import RequestCreateUserModel

"""Общие данные"""
"""Code в теле ответа для создания, обновления, удаления пользователя"""
response_expected_code = 200
"""Type в теле ответа для создания, обновления, удаления пользователя"""
response_expected_type = "unknown"

"""Данные для создания валидного пользователя"""
valid_user_id = 258
valid_user_name = "TestUser"
create_valid_user_data = RequestCreateUserModel(valid_user_id, valid_user_name, "Test", "User", "TestEmail", "TestPass",
                                                "TestPhone", 333).to_dict()

"""Данные для проверки ответа созданного валидного пользователя"""

response_expected_message = str(valid_user_id)

"""Данные для создания не валидного пользователя"""
create_no_valid_user_data = RequestCreateUserModel(True, True, True, True, True, True, True, True).to_dict()

"""Данные для проверки ответа созданного не валидного пользователя"""
response_expected_no_valid_code = 500
response_expected_no_valid_message = "something bad happened"

"""Данные для обновления валидного пользователя"""
valid_update_user_id = 8
update_user_data = RequestCreateUserModel(valid_update_user_id, "UpdateUser", "Update", "User", "UpdateEmail", "UpdatePass", "UpdatePhone", 5).to_dict()

"""Данные для проверки ответа обновленного, валидного пользователя"""
response_update_expected_message = str(valid_update_user_id)

"""Данные для обновления не валидного пользователя"""
no_valid_user_name = ("@", False)

"""Данные для проверки обновления не валидного пользователя"""
response_update_expected_no_valid_message = str(valid_update_user_id)

"""Данные для поиска валидного пользователя"""
valid_user_name = "TestUser"

"""Данные для проверки поиска валидного пользователя"""
response_get_id = valid_user_id
response_get_username = valid_user_name
response_get_firstName = "Test"
response_get_lastName = "User"
response_get_email = "TestEmail"
response_get_password = "TestPass"
response_get_phone = "TestPhone"
response_get_userStatus = 333

"""Данные для поиска не валидного пользователя"""
no_valid_user_name = ("@", False)

"""Данные для проверки поиска не валидного пользователя"""
response_get_expected_no_valid_code = 1
response_get_expected_no_valid_type = "error"
response_get_expected_no_valid_message = "User not found"

"""Данные для удаления валидного пользователя"""
valid_user_name = "TestUser"

"""Данные для проверки удаления валидного пользователя"""
response_delete_expected_no_valid_message = valid_user_name
