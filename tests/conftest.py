'''
Fixture
'''
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    '''
    Main fixture
    '''
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox") # отключаем песочницу
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"

    service = Service(ChromeDriverManager().install()) # устанавливаем драйвер или контролируем,
    #что он уже есть
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver   # если тест упадет, браузер закроется
    driver.quit()
