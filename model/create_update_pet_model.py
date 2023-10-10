"""Метод и модель создания тестовых данных, для создания нового pet"""


def generate_data(main_id, category_id, category_name, name, photoUrls, tags_id, tags_name, status):
    valid_create_data_test = ({
        "id": main_id,
        "category": {
            "id": category_id,
            "name": category_name
        },
        "name": name,
        "photoUrls": [
            photoUrls
        ],
        "tags": [
            {
                "id": tags_id,
                "name": tags_name
            }
        ],
        "status": status
    })

    return valid_create_data_test


"""Метод и модель создания тестовых данных, для обновления pet по id"""


def update_data(update_name, update_status):
    up_data = {
        "name": update_name,
        "status": update_status
    }

    return up_data
