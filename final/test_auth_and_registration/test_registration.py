from notebook.final.all_info.URLS import *
from notebook.final.all_info.selectors import *
from notebook.final.all_info.info import *
from selenium.webdriver.support import expected_conditions as EC


def test_reg_with_good_email(driver, fake_email, fake_password, wait):
    # Arrange
    driver.get(PAGE_LOGIN)

    # Act
    driver.find_element(*REG_EMAIL_WIN).send_keys(fake_email)
    driver.find_element(*REG_PASS_1_WIN).send_keys(fake_password)
    driver.find_element(*REG_PASS_2_WIN).send_keys(fake_password)
    driver.find_element(*REGISTRATION_BUTTON).click()

    # Assert
    assert wait.until(EC.element_to_be_clickable(
        SUCCESS_REG_TEXT)).text == success_reg_msg, "Не получилось зарегаться с валидными данными"


def test_reg_with_bad_email(driver, wait, fake_password):
    # Arrange
    driver.get(PAGE_LOGIN)

    # Act
    driver.find_element(*REG_EMAIL_WIN).send_keys(bad_email)
    driver.find_element(*REG_PASS_1_WIN).send_keys(fake_password)
    driver.find_element(*REG_PASS_2_WIN).send_keys(fake_password)
    driver.find_element(*REGISTRATION_BUTTON).click()

    # Assert
    assert driver.current_url == PAGE_LOGIN, "Получилось зарегаться с плохим емейлом"


def test_reg_with_short_pass(driver, wait, fake_email):
    # Arrange
    driver.get(PAGE_LOGIN)

    # Act
    driver.find_element(*REG_EMAIL_WIN).send_keys(fake_email)
    driver.find_element(*REG_PASS_1_WIN).send_keys(bad_pass)
    driver.find_element(*REG_PASS_2_WIN).send_keys(bad_pass)
    driver.find_element(*REGISTRATION_BUTTON).click()

    # Assert
    assert wait.until(EC.element_to_be_clickable(ALERT_MSG)).text == alert_msg, 'НЕТ СООБЩЕНИЯ ОБ ОШИБКЕ РЕГИСТРАЦИИ'
    assert wait.until(
        EC.element_to_be_clickable(ALERT_MSG_INFO)).text == alert_short_pass, 'НЕТ СООБЩЕНИЯ О КОРОТКОМ ПАРОЛЕ'


def test_reg_with_bad_second_pass(driver, wait, fake_email, fake_password):
    # Arrange
    driver.get(PAGE_LOGIN)

    # Act
    driver.find_element(*REG_EMAIL_WIN).send_keys(fake_email)
    driver.find_element(*REG_PASS_1_WIN).send_keys(fake_password)
    driver.find_element(*REG_PASS_2_WIN).send_keys(fake_password + '1')
    driver.find_element(*REGISTRATION_BUTTON).click()

    # Assert
    assert wait.until(EC.element_to_be_clickable(ALERT_MSG)).text == alert_msg, 'НЕТ СООБЩЕНИЯ ОБ ОШИБКЕ РЕГИСТРАЦИИ'
    assert wait.until(
        EC.element_to_be_clickable(ALERT_MSG_INFO)).text == alert_second_pass, 'НЕТ СООБЩЕНИЯ О НЕСОВПАДЕНИИ ПАРОЛЕЙ'


def test_reg_with_empty_info(driver,wait):
    # Arrange
    driver.get(PAGE_LOGIN)

    # Act
    driver.find_element(*REGISTRATION_BUTTON).click()

    # Assert
    assert driver.current_url == PAGE_LOGIN, "Получилось зарегаться с плохим емейлом"

def test_try_reg_with_exist_acc(driver ,wait):
    # Arrange
    driver.get(PAGE_LOGIN)

    # Act
    driver.find_element(*REG_EMAIL_WIN).send_keys(good_email)
    driver.find_element(*REG_PASS_1_WIN).send_keys(good_pass)
    driver.find_element(*REG_PASS_2_WIN).send_keys(good_pass)
    driver.find_element(*REGISTRATION_BUTTON).click()

    # Assert
    assert wait.until(EC.element_to_be_clickable(ALERT_MSG)).text == alert_msg, 'НЕТ СООБЩЕНИЯ ОБ ОШИБКЕ РЕГИСТРАЦИИ'
    assert wait.until(
        EC.element_to_be_clickable(ALERT_MSG_INFO)).text == alert_exist_acc, 'НЕТ СООБЩЕНИЯ О НЕСОВПАДЕНИИ ПАРОЛЕЙ'
