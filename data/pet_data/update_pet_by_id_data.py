"""Данные для обновления Name и Status по id"""
from model.create_update_pet_model import update_data


update_pet_id = 123
valid_update_data = update_data(update_name="UpdateName", update_status="UpdateStatus")
