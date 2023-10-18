"""Данные для создания pet"""
from model.pet_model import RequestUpdatePetModel, RequestPetModel

"""Общие данные"""
"""Id для создания, поиска, изменения, удаления"""
valid_main_id = 123

"""Code для не валидных поиска, удаления"""
response_exp_no_valid_code = 404

"""Code для валидных изменения, удаления"""
response_exp_valid_code = 200

"""Type для добавления, поиска, изменения, удаления"""
response_expected_type = "unknown"

"""Валидные данные для добавления животного"""
valid_category_id = 123
valid_category_name = "CategoryName1"
valid_name = "Name1"
valid_photoUrls = "Test string1"
valid_tags_id = 321
valid_tags_name = "TagsName1"
valid_status = "available"

valid_post_data = RequestPetModel(valid_main_id, valid_category_id, valid_category_name, valid_name, valid_photoUrls,
                                  valid_tags_id, valid_tags_name, valid_status).generate_data()

"""Проверка валидных данных добавления животного"""
response_expected_valid_main_id = valid_main_id
response_expected_valid_category_id_name = {'id': valid_category_id, 'name': valid_category_name}
response_expected_valid_name = valid_name
response_expected_valid_photoUrls = [valid_photoUrls]
response_expected_valid_tags_id_name = [{"id": valid_tags_id, "name": valid_tags_name}]
response_expected_valid_valid_status = valid_status

"""Не валидные данные для добавления животного"""
no_valid_main_id = "Test"
no_valid_category_id = "TestCatID"
no_valid_category_name = 1
no_valid_name = 2
no_valid_photoUrls = 3
no_valid_tags_id = "TestTagsID"
no_valid_tags_name = 4
no_valid_status = False

no_valid_post_data = RequestPetModel(no_valid_main_id, no_valid_category_id, no_valid_category_name, no_valid_name,
                                     no_valid_photoUrls, no_valid_tags_id, no_valid_tags_name, no_valid_status).generate_data()

"""Проверка не валидных данных добавления животного"""
response_expected_no_valid_code = 500

response_expected_no_valid_message = "something bad happened"

"""Не валидные данные для поиска животного"""
not_valid_pet_id = "abs"

"""Проверка не валидных данных для поиска животного"""

response_get_expected_no_valid_message = "java.lang.NumberFormatException: For input string: \"abs\""

"""Валидные данные для изменения животного"""
valid_update_name = "UpdateName"
valid_update_status = "UpdateStatus"

valid_update_data = RequestUpdatePetModel(valid_update_name, valid_update_status).update_data()

"""Проверка валидных данных для изменения животного"""
response_upd_expected_valid_message = str(valid_main_id)

"""Проверка валидных данных для удаления животного"""
response_del_expected_valid_message = str(valid_main_id)

"""Не валидные данные для удаления животного"""
no_valid_main_id = "cvb"

"""Проверка не валидных данных для удаления животного"""
response_del_expected_no_valid_message = "java.lang.NumberFormatException: For input string: \"cvb\""