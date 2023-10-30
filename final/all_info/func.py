from notebook.final.all_info.URLS import *
from notebook.final.all_info.selectors import *
from notebook.final.all_info.info import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


def login(driver):
    driver.get(PAGE_LOGIN)

    # Act
    driver.find_element(*LOGIN_EMAIL_WIN).send_keys(good_email)
    driver.find_element(*LOGIN_PASS_WIN).send_keys(good_pass)
    driver.find_element(*LOGIN_BUTTON).click()

    return driver

def login_and_add_2_items(driver):
    driver.get(PAGE_LOGIN)
    sleep(2)
    driver.find_element(*LOGIN_EMAIL_WIN).send_keys(good_email)
    sleep(2)
    driver.find_element(*LOGIN_PASS_WIN).send_keys(good_pass)
    sleep(2)
    driver.find_element(*LOGIN_BUTTON).click()
    sleep(2)
    driver.find_element(*ALL_ITEMS).click()
    sleep(2)

    driver.find_element(*ITEM_FIRST).click()
    sleep(2)
    driver.find_element(*ITEM_SECOND).click()
    sleep(2)
    driver.find_element(*GO_TO_CART).click()
    sleep(2)

    return driver



def insert_checkout_info(driver):
    driver.find_element(*FIRST_NAME_WINDOW).send_keys(first_name)
    sleep(2)
    driver.find_element(*LAST_NAME_WINDOW).send_keys(last_name)
    sleep(2)
    driver.find_element(*POSTCODE_WINDOW).send_keys(postcode)
    sleep(2)
    driver.find_element(*CITY_WINDOW).send_keys(city)
    sleep(2)
    driver.find_element(*ADRESS_1_WINDOW).send_keys(street)
    sleep(2)

    driver.find_element(*COUNTRY_BURGER).click()
    sleep(3)
    # actions = ActionChains(driver)
    # actions.move_to_element(COUNTRY_BURGER_RUSSIA).click()
    driver.find_element(*COUNTRY_BURGER_RUSSIA).click()
    sleep(2)
    driver.find_element(*COUNTRY_BURGER).click()
    sleep(2)