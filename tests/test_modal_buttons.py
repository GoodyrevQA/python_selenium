'''
Modal buttons tests
'''
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = 'https://goodyrevqa.github.io/'


def test_skills(browser):
    """
    Test modal 'Skills'
    """
    browser.get(URL)
    WebDriverWait(browser, timeout=10, poll_frequency=0.5).until(EC.visibility_of_element_located(
        (By.ID, "button2")))

    open_button_skills = browser.find_element(By.ID, value="button1")
    open_button_skills.click()

    modal_skills = browser.find_element(By.CSS_SELECTOR, value='[class="swal-modal"]')
    close_button_skills = browser.find_element(By.CSS_SELECTOR, value='[class*="--confirm"]')
    assert close_button_skills.text == "NOT BAD"

    close_button_skills.click()
    time.sleep(1)
    assert modal_skills.is_displayed() is False

def test_motto(browser):
    """
    Test modal 'Motto'
    """
    browser.get(URL)
    WebDriverWait(browser, timeout=10, poll_frequency=0.5).until(EC.visibility_of_element_located(
        (By.ID, "button2")))

    open_button_motto = browser.find_element(By.ID, value="button2")
    open_button_motto.click()

    modal_motto = browser.find_element(By.CSS_SELECTOR, value='[class="swal-modal"]')
    close_button_motto = browser.find_element(By.CSS_SELECTOR, value='[class*="--confirm"]')
    assert close_button_motto.text == "OK, let's do it"

    close_button_motto.click()
    time.sleep(1)
    assert modal_motto.is_displayed() is False
