from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from help_files import *


def test_stepik_next_step(driver,wait):
    driver.get("https://stepik.org/lesson/25969/step/12")
    driver.find_element(By.XPATH , LOGIN).click()
    driver.find_element(By.XPATH , EMAIL).send_keys('')


    wait.until(EC.element_to_be_clickable((By.XPATH , "//*[@id='ember459']"))).click()
    sleep(3)
    driver.find_element(By.XPATH ,"//*[@id='ember459']" ).send_keys('get()')
    sleep(3)