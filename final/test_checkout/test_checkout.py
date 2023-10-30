from notebook.final.all_info.URLS import *
from notebook.final.all_info.selectors import *
from notebook.final.all_info.func import *
from selenium.webdriver.support import expected_conditions as EC


def test_add_item_on_cart(driver,wait):
    # Arrange
    login(driver)

    # Act
    driver.find_element(*ALL_ITEMS).click()

    driver.find_element(*ITEM_FIRST).click()
    # driver.find_element(*ITEM_SECOND).click()
    # driver.find_element(*GO_TO_CART).click()
    price_1_item = driver.find_element(*ITEM_1_PRICE).text
    driver.find_element(*GO_TO_CART).click()
    final_price = driver.find_element(*FINAL_PRICE_IN_CART).text

    # Asserts
    assert price_1_item == final_price

def test_checkout(driver,wait):
    # Arrange
    login_and_add_2_items(driver)

    # Act
    driver.execute_script("window.scrollBy(0, 150);")
    sleep(2)
    driver.find_element(*CHECKOUT_BUTTON).click()
    sleep(2)
    driver.execute_script("window.scrollBy(0, 250);")
    insert_checkout_info(driver)
    sleep(2)
    driver.execute_script("window.scrollBy(0, 150);")
    driver.find_element(*CONTINUE_BUTTON_1_STEP).click()
    sleep(2)
    driver.find_element(*CONTINUE_BUTTON_2_STEP).click()
    sleep(2)
    driver.execute_script("window.scrollBy(0, 150);")

    driver.find_element(*PLACE_ORDER_BUTTON).click()
    sleep(2)

    confirm_msg = (((driver.find_element(*CONFIRM_ORDER_TXT).text).split())[0])+' '+(((driver.find_element(*CONFIRM_ORDER_TXT).text).split())[1])





    # Asserts
    assert confirm_msg == 'Подтверждение заказа'





