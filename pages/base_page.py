from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException, 
    StaleElementReferenceException, 
    ElementClickInterceptedException
)

class ActionBot:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(
            driver,
            15,
            poll_frequency=5,
            ignored_exceptions=[
                NoSuchElementException,
                StaleElementReferenceException,
                ElementClickInterceptedException
        ])

    def element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))
    
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()


    