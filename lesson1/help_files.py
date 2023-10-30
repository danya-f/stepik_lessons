from selenium.webdriver.common.by import By
import math
import time
#SELECTORS

LOGIN = "//*[@id='ember27']"
EMAIL = "//*[@id='id_login_email']"
PASSWORD = "//*[@id='id_login_password']"
OTVET_WINDOW= (By.XPATH,"//*[@class='ember-text-area ember-view textarea string-quiz__textarea']")
CONFIRM_OTVET= (By.XPATH,"//*[@class='submit-submission']")
TEXT_ITOG = (By.XPATH,"//*[@class='smart-hints__hint']")
LOGIN_STEPIK = (By.XPATH,"//*[@id='ember33']")
EMAIL_WIND = (By.XPATH,"//*[@id='id_login_email']")
PASS_WIND = (By.XPATH,"//*[@id='id_login_password']")
CONFIRM_LOGPASS = (By.XPATH,"//*[@class='sign-form__btn button_with-loader ']")


my_email = "danyafed6991@gmail.com"
my_pass = "Palevo1996"
#INFO

email = ''
password ='dsfsdfsd'

answer = math.log(int(time.time()))
print(answer)