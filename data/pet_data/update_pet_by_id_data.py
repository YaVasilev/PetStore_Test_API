"""Данные для обновления Name и Status по id"""
from model.uodate_by_id_pet_model import update_data



update_pet_id = 123
valid_update_data = update_data(update_name="UpdateName", update_status="UpdateStatus")
