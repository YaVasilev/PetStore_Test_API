def generate_user_data(user_id, user_name, first_name, last_name, user_email, user_pass, user_phone, user_status):
    user_data = ({
        "id": user_id,
        "username": user_name,
        "firstName": first_name,
        "lastName": last_name,
        "email": user_email,
        "password": user_pass,
        "phone": user_phone,
        "userStatus": user_status
    })

    return user_data
