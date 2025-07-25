import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def chrome_driver():
    driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(1)
    yield driver
    driver.quit()