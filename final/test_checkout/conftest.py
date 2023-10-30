from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker
fake = Faker()
print(fake.password())



@pytest.fixture()
def options():
    options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--window-size=2480,1600')
    return options


@pytest.fixture()
def fake_password():
    password = fake.password()
    return password


@pytest.fixture()
def fake_email():
    email = fake.email()
    return email

@pytest.fixture()
def driver(options):
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, timeout=30)
    return wait


