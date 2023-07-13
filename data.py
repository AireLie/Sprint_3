import random

class Registration:
    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

    def get_valid_user_data():
        random_numbers = random.randint(100, 999)
        return Registration(f"alinabakhareva11{random_numbers}@yandex.ru", "736540", "AireLie")

    def get_empty_username_data():
        random_numbers = random.randint(100, 999)
        return Registration(f"alinabakhareva11{random_numbers}@yandex.ru", "736540", "  ")

    def get_invalid_password_data():
        return Registration("aire@ouch.ru", "12345", "AireLie")

class Credentials:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def get_credentials():
        return Credentials("alinabakhareva11736@yandex.ru", "736540")
