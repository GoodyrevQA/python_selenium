'''
Buttons test
'''
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BTNS = [0, 1]
URL = 'https://goodyrevqa.github.io/'

@pytest.mark.parametrize('case', BTNS)
def test_btns(browser, case):
    """
    Test of buttons
    """
    browser.get(URL)
    WebDriverWait(browser, timeout=10, poll_frequency=0.5).until(EC.visibility_of_element_located(
        (By.ID, "button2")))

    cards = browser.find_elements(By.CSS_SELECTOR, value='[class="btn"]')
    cards[case].click()

    WebDriverWait(browser, timeout=10, poll_frequency=0.5).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".swal-title")))

    modal = browser.find_element(By.CSS_SELECTOR, value='[class="swal-title"]')

    assert modal.text in ["Умею:", "FAC SI FACIS"]
