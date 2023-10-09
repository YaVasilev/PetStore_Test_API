def generate_store_data(store_id, pet_id, quantity, ship_date, status, complete):
    valid_store_data = ({
        "id": store_id,
        "petID": pet_id,
        "quantity": quantity,
        "shipDate": ship_date,
        "status": status,
        "complete": complete
    })

    return valid_store_data
