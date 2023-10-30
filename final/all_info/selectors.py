from selenium.webdriver.common.by import By

# PEREHODY

GO_TO_LOGIN_PAGE_BUTTON = (By.XPATH, "//*[@id='login_link']")
REGISTRATION_BUTTON = (By.XPATH, "//*[@value='Register']")
LOGIN_BUTTON = (By.XPATH,"//*[@name='login_submit']")


# registration
REG_EMAIL_WIN = (By.XPATH, "//*[@id='id_registration-email']")
REG_PASS_1_WIN = (By.XPATH, "//*[@id='id_registration-password1']")
REG_PASS_2_WIN = (By.XPATH, "//*[@id='id_registration-password2']")
SUCCESS_REG_TEXT = (By.XPATH, "//div[@class='alertinner wicon']")
ALERT_MSG = (By.XPATH, "//*[@class='alert alert-danger']")
ALERT_MSG_INFO = (By.XPATH, "//*[@class='error-block']")


# login

LOGIN_EMAIL_WIN = (By.XPATH, "//*[@id='id_login-username']")
LOGIN_PASS_WIN = (By.XPATH, "//*[@id='id_login-password']")
SUCCESS_LOGIN_TEXT = (By.XPATH, "//div[@class='alertinner wicon']")
ALERT_MSG_INCORECT_LOGPASS = (By.XPATH, "(//div[@class='alert alert-danger'])[2]")


#CATALOG
ALL_ITEMS = (By.XPATH,"(//*[@tabindex='-1'])[1]")
ITEM_FIRST = (By.XPATH,"(//button[@class='btn btn-primary btn-block'])[1]")
ITEM_SECOND = (By.XPATH,"(//button[@class='btn btn-primary btn-block'])[2]")
ITEM_THIRD = (By.XPATH,"(//button[@class='btn btn-primary btn-block'])[3]")
GO_TO_CART = (By.XPATH,"//a[@class='btn btn-default' and @href='/ru/basket/']")
FINAL_PRICE_IN_CART = (By.XPATH,"//*/h3[@class='price_color']")
ITEM_1_PRICE = (By.XPATH,"//p[@class='price_color']")

#CHECKOUT
CHECKOUT_BUTTON = (By.XPATH,"//*[@href='/ru/checkout/']")
ALL_WINDOWS = (By.XPATH,"//input[@type='text']")

FIRST_NAME_WINDOW = (By.XPATH,"//input[@name='first_name']")
LAST_NAME_WINDOW = (By.XPATH,"//input[@name='last_name']")
ADRESS_1_WINDOW = (By.XPATH,"//input[@name='line1']")
ADRESS_2_WINDOW = (By.XPATH,"//input[@name='line2']")
CITY_WINDOW = (By.XPATH,"//input[@name='line4']")
POSTCODE_WINDOW = (By.XPATH,"//input[@name='postcode']")

COUNTRY_BURGER = (By.XPATH,"//*[@name='country']")
COUNTRY_BURGER_RUSSIA = (By.XPATH,"//*[@value='RU']")
CONTINUE_BUTTON_1_STEP = (By.XPATH,"//*[@class='btn btn-lg btn-primary']")
CONTINUE_BUTTON_2_STEP = (By.XPATH,"//*[@id='view_preview']")
PLACE_ORDER_BUTTON = (By.XPATH,"//*[@id='place-order']")


CONFIRM_ORDER_TXT = (By.XPATH,"//h1")
