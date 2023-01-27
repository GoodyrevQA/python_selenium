'''
Info test
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://goodyrevqa.github.io/'

def test_is_that_me(browser):
    """
    SMK-1 Ava and name
    """
    browser.get(URL)

    WebDriverWait(browser, timeout=10, poll_frequency=0.5).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "img.box-img")))
    ava = browser.find_element(By.CSS_SELECTOR, value="img.box-img")
    fio = browser.find_element(By.CSS_SELECTOR, value="h2.subtitle")

    assert ava.tag_name == "img", "No tag img"
    assert ava.text == ''
    assert fio.text == 'Иван Гудырев'
    