from notebook.final.all_info.URLS import *
from notebook.final.all_info.selectors import *
from notebook.final.all_info.func import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def test_prokruti(driver):
    driver.get("https://the-internet.herokuapp.com/floating_menu")

    actions = ActionChains(driver)
    actions.move_to_element((driver.find_element(By.XPATH,"//*[@target]"))).perform()
    sleep(5)