from notebook.final.all_info.URLS import *
from notebook.final.all_info.selectors import *
from notebook.final.all_info.info import *
from selenium.webdriver.support import expected_conditions as EC



def test_login_good_log_pass(driver,wait):
    # Arrange
    driver.get(PAGE_LOGIN)

    # Act
    driver.find_element(*LOGIN_EMAIL_WIN).send_keys(good_email)
    driver.find_element(*LOGIN_PASS_WIN).send_keys(good_pass)
    driver.find_element(*LOGIN_BUTTON).click()

    # Assert
    assert wait.until(EC.element_to_be_clickable(SUCCESS_LOGIN_TEXT)).text == success_login_msg , 'не получилось войти с коректным лог паролем'


def test_login_bad_pass(driver,wait):
    # Arrange
    driver.get(PAGE_LOGIN)

    # Act
    driver.find_element(*LOGIN_EMAIL_WIN).send_keys(good_email)
    driver.find_element(*LOGIN_PASS_WIN).send_keys(good_pass+'1')
    driver.find_element(*LOGIN_BUTTON).click(   )

    # Assert
    assert wait.until(EC.element_to_be_clickable(ALERT_MSG)).text == alert_msg , 'получилось войти с не коректным лог паролем'
    assert wait.until(EC.element_to_be_clickable(ALERT_MSG_INCORECT_LOGPASS)).text == alert_bad_log_pass , ' получилось войти с не коректным лог паролем'
