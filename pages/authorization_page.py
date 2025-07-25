import os
from dotenv import load_dotenv

from selenium.webdriver.common.by import By

from pages.base_page import ActionBot

load_dotenv()


class AuthorizationPage(ActionBot):
    EMAIL = (By.ID, "mat-input-0")
    PASSWORD = (By.ID, "mat-input-1")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    IF_ERROR = (By.XPATH, '//div[@class="error ng-star-inserted"]')
    IF_CORRECT = (By.XPATH, "//span[text()='Система тестирования']")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(os.getenv('LOGIN_PAGE_URL'))
    
    def correct_email(self):
        return self.element(self.EMAIL).send_keys(os.getenv('LOGIN'))
    
    def correct_password(self):
        return self.element(self.PASSWORD).send_keys(os.getenv('PASSWORD'))
    
    def submit(self):
        return self.element(self.SUBMIT_BUTTON).click()

    def email_input(self):
        return self.element(self.EMAIL) 

    def password_input(self):
        return self.element(self.PASSWORD)

    def if_authorization_is_ok(self):
        return self.element(self.IF_CORRECT).text
    
    def if_authorization_is_fail(self):
        return self.element(self.IF_ERROR).text
       


