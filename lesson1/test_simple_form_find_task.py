import pytest
from selenium.webdriver.common.by import By
from time import sleep
import math
import time
from selenium.webdriver.support import expected_conditions as EC
from notebook.lesson1.help_files import *

def test_fast_ins(driver):
    driver.get('http://suninjuly.github.io/simple_form_find_task.html')
    driver.find_element(By.XPATH, "//*[@name = 'first_name']").send_keys('Ivan')
    driver.find_element(By.XPATH, "//*[@name = 'last_name']").send_keys('Petrov')
    driver.find_element(By.XPATH, "//*[@class = 'form-control city']").send_keys('Smolensk')
    driver.find_element(By.XPATH, "//*[@id = 'country']").send_keys('Russia')
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id = 'submit_button']").click()
    sleep(14)

def test_find_by_text_link(driver):
    driver.get("http://suninjuly.github.io/find_link_text")

    driver.find_element(By.LINK_TEXT , "224592").click()
    sleep(1)

    driver.find_element(By.XPATH, "//*[@name = 'first_name']").send_keys('Ivan')
    driver.find_element(By.XPATH, "//*[@name = 'last_name']").send_keys('Petrov')
    driver.find_element(By.XPATH, "//*[@class = 'form-control city']").send_keys('Smolensk')
    driver.find_element(By.XPATH, "//*[@id = 'country']").send_keys('Russia')
    sleep(1)
    driver.find_element(By.XPATH, "//button").click()
    sleep(14)


def test_big_form_insert(driver):
    driver.get("http://suninjuly.github.io/huge_form.html")

    list = driver.find_elements(By.XPATH , "//*[@type='text']")
    for i in list:
        i.send_keys("Bla")

    driver.find_element(By.XPATH , "//*[@type='submit']").click()
    sleep(20)


def test_xpath_selectr(driver):
    driver.get("http://suninjuly.github.io/find_xpath_form")

    driver.find_element(By.XPATH, "//*[@name = 'first_name']").send_keys('Ivan')
    driver.find_element(By.XPATH, "//*[@name = 'last_name']").send_keys('Petrov')
    driver.find_element(By.XPATH, "//*[@class = 'form-control city']").send_keys('Smolensk')
    driver.find_element(By.XPATH, "//*[@id = 'country']").send_keys('Russia')

    driver.find_element(By.XPATH, "//*[text() = 'Submit']").click()
    sleep(10)

def test_auth_page(driver):
    # driver.get("http://suninjuly.github.io/registration1.html")
    driver.get("http://suninjuly.github.io/registration2.html")

    driver.find_element(By.XPATH, "//*[@placeholder='Input your first name']").send_keys('Fahir')
    driver.find_element(By.XPATH, "//*[@placeholder='Input your last name']").send_keys('Abas')
    driver.find_element(By.XPATH, "//*[@placeholder='Input your email']").send_keys('fahir@mail.com')
    sleep(2)
    driver.find_element(By.XPATH, "//*[@type='submit']").click()
    assert driver.find_element(By.XPATH , "//h1[text()='Congratulations! You have successfully registered!']").text =="Congratulations! You have successfully registered!"


def test_robots_checkbox(driver):
    driver.get("http://suninjuly.github.io/get_attribute.html")

    x = driver.find_element(By.XPATH,"//*[@id='treasure']").get_attribute("valuex")
    otvet = math.log(abs(12*math.sin(int(x))))
    print(otvet)
    driver.find_element(By.XPATH , "//*[@id='answer']").send_keys(otvet)
    driver.find_element(By.XPATH, "//*[@id='robotCheckbox']").click()
    driver.find_element(By.XPATH, "//*[@id='robotsRule']").click()
    driver.find_element(By.XPATH, "//*[@type='submit']").click()
    sleep(15)

def test_robots_2(driver):
    driver.get("https://suninjuly.github.io/selects1.html")

    suma = int(driver.find_element(By.XPATH , "//*[@id='num1']").text)+int(driver.find_element(By.XPATH , "//*[@id='num2']").text)
    driver.find_element(By.XPATH,"//*[@id='dropdown']").click()
    driver.find_element(By.XPATH,f"//*[@value='{suma}']").click()
    driver.find_element(By.XPATH, "//*[@type='submit']").click()
    sleep(15)


def test_robots_checkbox_3(driver):
    driver.get("https://suninjuly.github.io/execute_script.html")

    x = int(driver.find_element(By.XPATH,"//*[@id='input_value']").text)
    otvet = math.log(abs(12*math.sin(int(x))))
    driver.find_element(By.XPATH , "//*[@id='answer']").send_keys(otvet)
    driver.find_element(By.XPATH, "//*[@id='robotCheckbox']").click()
    driver.execute_script("window.scrollBy(0, 150);")
    driver.find_element(By.XPATH, "//*[@id='robotsRule']").click()
    driver.find_element(By.XPATH, "//*[@type='submit']").click()


def test_alert(driver):
    driver.get("https://suninjuly.github.io/alert_accept.html")

    driver.find_element(By.XPATH,"//*[@type='submit']").click()
    alert = driver.switch_to.alert
    alert.accept()
    sleep(3)
    x = int(driver.find_element(By.XPATH, "//*[@id='input_value']").text)
    otvet = math.log(abs(12 * math.sin(int(x))))
    driver.find_element(By.XPATH, "//*[@id='answer']").send_keys(otvet)
    driver.find_element(By.XPATH, "//*[@type='submit']").click()
    sleep(15)



def test_window_switch(driver,wait):
    driver.get("http://suninjuly.github.io/redirect_accept.html")

    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@type='submit']"))).click()
    wkladki = driver.window_handles
    print(wkladki)
    driver.switch_to.window(wkladki[1])
    x = driver.find_element(By.XPATH, "//*[@id='input_value']").text
    otvet = math.log(abs(12 * math.sin(int(x))))
    driver.find_element(By.XPATH, "//*[@id='answer']").send_keys(otvet)
    driver.find_element(By.XPATH, "//*[@type='submit']").click()
    sleep(1)


def test_ec(driver,wait):
    driver.get("https://suninjuly.github.io/explicit_wait2.html")

    wait.until(EC.text_to_be_present_in_element((By.XPATH,"//*[@id='price']"),'100'))
    driver.find_element(By.XPATH,"//*[@id='book']").click()
    x = driver.find_element(By.XPATH, "//*[@id='input_value']").text
    otvet = math.log(abs(12 * math.sin(int(x))))
    driver.find_element(By.XPATH, "//*[@id='answer']").send_keys(otvet)
    driver.find_element(By.XPATH, "//*[@type='submit']").click()
    sleep(30)


@pytest.mark.parametrize('stepik',[236895,236896,236897,236898,236899,236903,236904,236905])
def test_stepik(driver,stepik,wait):
    # url = f"https://stepik.org/lesson/{stepik}/step/1"
    driver.get(f"https://stepik.org/lesson/{stepik}/step/1")
    wait.until(EC.element_to_be_clickable(LOGIN_STEPIK)).click()
    wait.until(EC.element_to_be_clickable(EMAIL_WIND)).send_keys(my_email)
    wait.until(EC.element_to_be_clickable(PASS_WIND)).send_keys(my_pass)
    driver.find_element(*CONFIRM_LOGPASS).click()

    answer = math.log(int(time.time()))

    wait.until(EC.element_to_be_clickable(OTVET_WINDOW)).send_keys(answer)
    wait.until(EC.element_to_be_clickable(OTVET_WINDOW)).click()
    wait.until(EC.element_to_be_clickable(TEXT_ITOG))
    assert driver.find_element(*TEXT_ITOG).text == 'Correct!', driver.find_element(*TEXT_ITOG).text
    sleep(2)




