import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    service = Service("F:/QA/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()