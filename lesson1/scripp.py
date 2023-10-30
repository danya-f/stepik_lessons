from selenium.webdriver.common.by import By
from time import sleep
import os



def test_script(driver):
    driver.get("https://suninjuly.github.io/file_input.html")

    driver.find_element(By.XPATH, "//*[@placeholder='Enter first name']").send_keys('Fahir')
    driver.find_element(By.XPATH, "//*[@placeholder='Enter last name']").send_keys('Abas')
    driver.find_element(By.XPATH, "//*[@placeholder='Enter email']").send_keys('fahir@mail.com')
    sleep(2)
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file_with_text.txt')
    driver.find_element(By.XPATH , "//*[@id='file']").send_keys(file_path)
    driver.find_element(By.XPATH , "//*[@type='submit']").click()
    sleep(15)




