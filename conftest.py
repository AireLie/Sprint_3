import pytest
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Registration:
    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

@pytest.fixture
def get_valid_user_data():
    random_numbers = random.randint(100, 999)
    return Registration(f"alinabakhareva11{random_numbers}@yandex.ru", "736540", "AireLie")

@pytest.fixture
def get_empty_username_data():
    random_numbers = random.randint(100, 999)
    return Registration(f"alinabakhareva11{random_numbers}@yandex.ru", "736540", "  ")

@pytest.fixture
def get_invalid_password_data():
    return Registration("aire@ouch.ru", "12345", "AireLie")

class Credentials:
	def __init__(self, email, password):
		self.email = email
		self.password = password
@pytest.fixture
def get_credentials():
	return Credentials("alinabakhareva11736@yandex.ru", "736540")
