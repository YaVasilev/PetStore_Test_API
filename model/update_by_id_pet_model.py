"""Метод и модель создания тестовых данных, для обновления pet по id"""


def update_data(update_name, update_status):
    up_data = {
        "name": update_name,
        "status": update_status
    }

    return up_data
