import pytest
from time import sleep





def test_drive(driver):
    driver.get('http://selenium1py.pythonanywhere.com/')
    sleep(10)