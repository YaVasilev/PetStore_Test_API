"""Данные для создания pet"""
from model.create_update_pet_model import generate_data


"""Валидные данные"""
valid_post_data = generate_data(main_id=123, category_id=123, category_name="CategoryName1", name="Name1", photoUrls="Test string1",
    tags_id=321, tags_name="TagsName1", status="available")

"""Не валидные данные"""
no_valid_post_data = (generate_data(main_id="Test", category_id=123, category_name="CategoryName1", name="Name1", photoUrls="Test string1",
    tags_id=321, tags_name="TagsName1", status="available"),
                      generate_data(main_id=123, category_id="TestCatID", category_name="CategoryName1", name="Name1", photoUrls="Test string1",
    tags_id=321, tags_name="TagsName1", status="available"),
                      generate_data(main_id=123, category_id=123, category_name=123, name="Name1", photoUrls="Test string1",
    tags_id=321, tags_name="TagsName1", status="available"),
                      generate_data(main_id=123, category_id=123, category_name="CategoryName1", name=456, photoUrls="Test string1",
    tags_id=321, tags_name="TagsName1", status="available"),
                      generate_data(main_id=123, category_id=123, category_name="CategoryName1", name="Name1", photoUrls=123,
    tags_id=321, tags_name="TagsName1", status="available"),
                      generate_data(main_id=123, category_id=123, category_name="CategoryName1", name="Name1", photoUrls="Test string1",
    tags_id="TestTagsID", tags_name="TagsName1", status="available"),
                      generate_data(main_id=123, category_id=123, category_name="CategoryName1", name="Name1", photoUrls="Test string1",
    tags_id=321, tags_name=789, status="available"),
                      generate_data(main_id=123, category_id=123, category_name="CategoryName1", name="Name1", photoUrls="Test string1",
    tags_id=321, tags_name="TagsName1", status=000))

"""Пустое тело запрос"""
empty_data = {}
