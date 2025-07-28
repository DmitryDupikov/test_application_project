import os
from random import randint
from dotenv import load_dotenv

from selenium.webdriver.common.by import By

from pages.base_page import ActionBot

load_dotenv()

class Create_Card_Page(ActionBot):
    title =f'My_First_TEST_25 {randint(1, 100)}'
    EMAIL = (By.XPATH, "//div/input[@data-placeholder='Введите почту']")
    PASSWORD = (By.XPATH, "//div/input[@data-placeholder='Введите пароль']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    MENU_SELECTION = (By.XPATH, "//mat-toolbar/button[position()=1]")
    TESTS_SELECTION = (By.CSS_SELECTOR, ".mat-list-item:nth-of-type(2)")
    PLUS_ICON = (By.XPATH, '//div/button[@mattooltip="Добавить тест"]')
    TEST_NAME = (By.XPATH, "//div/input[@data-placeholder='Укажите название теста']")
    ADD_BUTTON = (By.XPATH, "//span[text()='Добавить ']")
    CHOOSE_TYPE = (By.XPATH, '//app-test-create-dialog//mat-select[@formcontrolname="type"]')
    CHOSING_OPTION = (By.XPATH, '//mat-option//span[contains(text(), "HR")]')
    TEST_TYPE = (By.XPATH, "//table//*[1][name()='tr']//td[text()='HR']")
    FIRST_ROW_TITLE = (By.XPATH, "//table/tbody/tr[1]/td[3]")
    CREATED_TEST_TITLE = (By.XPATH, f"//a[text()='{title}']")
    CREATED_TEST_STATUS = (By.XPATH, "//table/tbody/tr[1]/td[5]")
    CREATED_TEST_NUMBER = (By.XPATH, "//table/tbody/tr[1]/td[1]")
    CANCEL_CREATION_BUTTON = (By.XPATH, "//span[text()='Отмена ']")
    FIND_ALL_ROWS = (By.CSS_SELECTOR, "app-tests-table tr.mat-row")
    FIND_ALL_TITLES_IN_ROWS = (By.CSS_SELECTOR, "td.mat-column-name a")
    TITLE_INPUT_FIELD = (By.CSS_SELECTOR, "input[formcontrolname='name']")
    TEST_CHOOSING_OPTION = (By.CSS_SELECTOR, "mat-option")

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

    def menu_selection(self):
        return self.element(self.MENU_SELECTION).click()
    
    def test_selection(self):
        return self.element(self.TESTS_SELECTION).click()
    
    def plus_icon(self):
        return self.element(self.PLUS_ICON).click()
    
    def creation_menu_is_exist(self):
        return self.element(self.TEST_NAME).text
    
    def create_title(self):
        return self.element(self.TEST_NAME).send_keys(self.title)
    
    def chose_type(self):
        return self.element(self.CHOOSE_TYPE).click()
    
    def chosing_option(self):
        return self.element(self.CHOSING_OPTION).click()
    
    def add_button(self): 
        return self.element(self.ADD_BUTTON).click()
    
    def new_test_created_correctly(self):
        return self.element(self.CREATED_TEST_TITLE).text
    
    def new_test_type_is_correct(self):
        return self.element(self.TEST_TYPE).text
    
    def test_appears_in_the_first_row(self):
        return self.element(self.FIRST_ROW_TITLE).text
    
    def created_test_has_correct_status(self):
        return self.element(self.CREATED_TEST_STATUS).text
    
    def test_has_sequential_number(self):
        number_text = self.element(self.CREATED_TEST_NUMBER).text
        return int(number_text.lstrip('#'))
    
    def cancel_button(self):
        return self.element(self.CANCEL_CREATION_BUTTON).click()
        
    def get_test_titles(self):
        rows = self.elements(self.FIND_ALL_ROWS)
        return [row.find_element(*self.FIND_ALL_TITLES_IN_ROWS).text for row in rows]
        
    def title_input_field(self):
        return self.element(self.TITLE_INPUT_FIELD)

    def is_name_valid(self):
        classes = self.title_input_field().get_attribute("class")
        return "ng-valid" in classes and "ng-invalid" not in classes
    
    def default_type_field(self):
        return self.element(self.CHOOSE_TYPE).text
    
    def wrong_title_input(self):
        return self.element(self.TEST_NAME).send_keys('**')
    
    def get_all_dropdown_options_value(self):
        """
        Функция получает список всех текстовых значений из выпадающего меню 
        выбора типа теста
        """
        return [
            option.get_dom_attribute('value') 
            for option in self.elements(self.TEST_CHOOSING_OPTION)
        ]
