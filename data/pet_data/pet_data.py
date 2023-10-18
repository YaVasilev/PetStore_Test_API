"""Данные для создания pet"""
from model.pet_model import RequestUpdatePetModel, RequestPetModel


"""Валидные данные"""
valid_main_id = 123
valid_category_id = 123
valid_category_name = "CategoryName1"
valid_name = "Name1"
valid_photoUrls = "Test string1"
valid_tags_id = 321
valid_tags_name = "TagsName1"
valid_status = "available"

check_data = valid_main_id, valid_category_id, valid_category_name, valid_name, valid_photoUrls, valid_tags_id, valid_tags_name, valid_status

valid_post_data = RequestPetModel(valid_main_id, valid_category_id, valid_category_name, valid_name, valid_photoUrls,
                                  valid_tags_id, valid_tags_name, valid_status).generate_data()

"""Не валидные данные"""
no_valid_post_data = (RequestPetModel("Test", 123, "CategoryName1", "Name1", "Test string1", 321, "TagsName1",
                                      "available").generate_data(),
                      RequestPetModel(123, "TestCatID", "CategoryName1", "Name1", "Test string1", 321, "TagsName1",
                                      "available").generate_data(),
                      RequestPetModel(123, 123, "CategoryName1", "Name1", "Test string1", "TestTagsID", "TagsName1",
                                      "available").generate_data())

check_no_valid_data = 500, "unknown", "something bad happened"

"""Не валидные id"""
not_valid_pet_id = (("abs"), ("2222"), (9999999), (" "))

"""Пустое поле id"""
empty_pet_id = ("")

"""Update data"""
valid_update_data = RequestUpdatePetModel("UpdateName", "UpdateStatus").update_data()

upd_check_data = 200, "unknown", "123"
