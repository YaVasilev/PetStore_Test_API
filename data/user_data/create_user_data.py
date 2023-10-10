from model.create_user_model import generate_user_data

create_valid_user_data = generate_user_data(user_id=258, user_name="TestUser", first_name="Test", last_name="User", user_email="TestEmail",
                                 user_pass="TestPass", user_phone="TestPhone", user_status=333)

create_no_valid_user_data = None