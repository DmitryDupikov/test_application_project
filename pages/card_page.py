from random import randint
from dotenv import load_dotenv

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import ActionBot
from pages.create_card_page import Create_Card_Page

load_dotenv()


class Test_Card_Page(ActionBot):
    QUESTION_AND_ANSWERS = randint(100, 99999)
    CHOSING_OPTION = (By.XPATH, '//mat-option//span[contains(text(), "Общий")]')
    TEST_MENU = (By.XPATH, '//app-bar-more-button/button')
    RENAME_OPTION = (By.XPATH, "//span[text()='Переименовать']")
    DELETE_OPTION = (By.XPATH, "//*[starts-with(text(), 'Удал')]")
    DELETE_CONFIRMATION = (By.XPATH, "//button/span[text()='Удалить ']")
    SAVE_RENAMING = (By.XPATH, "//span[text()='Сохранить ']")
    UPDATED_TITLE = (By.XPATH, "//app-bar-title")
    ACTIVATE_BUTTON = (By.XPATH, ".//span[text()='Активировать']")
    ACTIVATION_UNAVAILIBLE = (By.XPATH, "//li[text()='В тесте нет вопросов']")
    ADD_QUESTIONS = (By.XPATH, "//*[text()='Вопросы']")
    ADD_NEW_QUESTION = (By.XPATH, "//app-questions-editor//button[contains(@class,'add-button')]")
    ADD_QUESTIONS_FIELD = (By.XPATH, '//textarea[@data-placeholder="Введите вопрос"]')
    QUESTION_TYPE_ONE_ANSWER = (By.CSS_SELECTOR, 'mat-radio-button:first-child')
    QUESTION_TYPE_FEW_ANSWERS = (By.CSS_SELECTOR, 'mat-radio-button:nth-child(2)')
    QUESTION_TYPE_NO_ANSWERS = (By.CSS_SELECTOR, 'mat-radio-button:last-child')
    THE_FIRST_ANSWER_IS_CORRECT = (By.XPATH, "//section//div[position()=1]//mat-checkbox[position()=1]")
    THE_THIRD_ANSWER_IS_CORRECT = (By.XPATH, "//section//div[position()=3]//mat-checkbox[position()=1]")
    CLICK_ADD_QUESTION = (By.XPATH, "//button/span[text()='Добавить ']")
    ADD_ANSWER_TEXT = (By.XPATH, '//textarea[@data-placeholder="Введите ответ"]')
    ADD_ANSWER_BUTTON = (By.XPATH, '//button[@mattooltip="Добавить ответ"]')
    CHOSING_THE_CORRECT_ANSWER = (By.XPATH, '//mat-radio-group//div[position()=2]//mat-radio-button[position()=1]')
    RETURN_TO_TEST_MENU = (By.TAG_NAME, 'app-bar-back-button')
    QUANTITY_OF_QUESTIONS = (By.XPATH, "//a[2]//*[@class='number']")
    AREA_WITH_DELETE_BUTTON = (By.XPATH, "//app-question-edit-form//div[@class='text-container ng-star-inserted']")
    DELETE_QUESTION_BUTTON = (By.XPATH, "//div//button[@mattooltip='Удалить вопрос']")
    DELETE_QUESTION_CONFIRMATION = (By.XPATH, "//span[text()='Удалить ']")
    EDIT_QUESTION_BUTTON = (By.XPATH, "//app-question-edit-form//div[@class='question']//button[@mattooltip='Редактировать']")
    PROFILE_BUTTON = (By.XPATH, "//button[@mattooltip='Профиль']")
    EXTT_BUTTON = (By.XPATH, "//span[text()='Выйти']")
    UPDATED_ANSWER_TEXT = (By.XPATH, "//app-question-edit-form//div[@class='text']")
    SAVE_CHANGES = (By.XPATH, "//button[@mattooltip='Сохранить']")
    UPDATED_QUESTION_AREA = (By.XPATH, '//textarea[@data-placeholder="Введите вопрос"]')
    ANSWER_GROUP = (By.CSS_SELECTOR, "mat-radio-group.mat-radio-group")
    ANSWER_RADIO_BUTTONS = (By.XPATH, ".//mat-radio-button[contains(@class, 'mat-radio-button')]")
    MULTIPLY_ANSWERS_GROUP = (By.CSS_SELECTOR, "section.cdk-drop-list")
    ANSWER_CHECKBOXES = (By.XPATH, ".//mat-checkbox[contains(@class, 'mat-checkbox')]")
    ANSWER_INPUT_FIELD = (By.CSS_SELECTOR, "app-answer-text-edit-form div:nth-of-type(2)")
    ANSWER_PENCIL_BUTTON = (By.XPATH, '//app-answer-text-edit-form//button')
    ANSWER_INPUT_FOR_OPEN_QUESTION = (By.XPATH, '//textarea[@formcontrolname="text"]')
    CONFIRM_OPEN_QUESTION_ANSWER = (By.XPATH, '//button[@mattooltip="Сохранить"]')
    DEACTIVATE_BUTTON = (By.XPATH, "//span[text()='Деактивировать ']")
    DEACTIVATE_CONFIRMATION = (By.XPATH, "//app-test-deactivate-dialog//button[@color='warn']")
    LAST_TEST_CREATED = (By.XPATH, "//table//tr[1][contains(@class, 'mat-row')]//td/a")

    def __init__(self, driver):
        super().__init__(driver)
        self.create_page = Create_Card_Page(driver)
        self.updated_title = f'UPDATED_TEST_25 {randint(1, 100)}'
        self.updated_question_test = f'Новый вопрос {randint(1, 100)}'


    def select_test(self):
        return self.create_page.element(self.create_page.CREATED_TEST_TITLE).click()
    
    def select_test_menu(self):
        return self.element(self.TEST_MENU).click()
    
    def rename_test(self):
        return self.element(self.RENAME_OPTION).click()
    
    def write_new_title(self):
        self.create_page.element(self.create_page.TITLE_INPUT_FIELD).clear()
        return self.create_page.element(self.create_page.TITLE_INPUT_FIELD).send_keys(self.updated_title)
    
    def save_renaming(self):
        return self.element(self.SAVE_RENAMING).click()
    
    def delete_test(self):
        self.element(self.DELETE_OPTION).click()
        return self.element(self.DELETE_CONFIRMATION).click()
    
    def renaming_is_correctly(self):
        return self.element(self.UPDATED_TITLE).text

    def open(self):
        return self.create_page.open()
    
    def correct_email(self):
        return self.create_page.correct_email()
    
    def correct_password(self):
        return self.create_page.correct_password()
    
    def submit(self):
        return self.create_page.submit()
    
    def menu_selection(self):
        return self.create_page.menu_selection()
    
    def test_selection(self):
        return self.create_page.test_selection()
    
    def plus_icon(self):
        return self.create_page.plus_icon()
    
    def create_title(self):
        return self.create_page.element(self.create_page.TEST_NAME).send_keys(self.create_page.title)
    
    def chose_type(self):
        return self.create_page.element(self.create_page.CHOOSE_TYPE).click()
    
    def chosing_option(self):
        return self.element(self.CHOSING_OPTION).click()
    
    def add_button(self):
        return self.create_page.element(self.create_page.ADD_BUTTON).click()
    
    def get_test_titles(self):
        return self.create_page.get_test_titles()
    
    def is_test_present(self, title):
        return title in self.get_test_titles()
    
    def activate_button(self):
        return self.element(self.ACTIVATE_BUTTON).click()

    def incorrect_activation(self):
        return self.element(self.ACTIVATION_UNAVAILIBLE).text
    
    def add_questions_button(self):
        return self.element(self.ADD_QUESTIONS).click()
    
    def add_new_question_button(self):
        return self.element(self.ADD_NEW_QUESTION).click()
    
    def add_question_text(self):
        return self.element(self.ADD_QUESTIONS_FIELD).send_keys(self.QUESTION_AND_ANSWERS)
    
    def choose_qustion_type(self):
        return self.element(self.QUESTION_TYPE_ONE_ANSWER).click()
    
    def click_add_button(self):
        return self.element(self.CLICK_ADD_QUESTION).click()
    
    def add_answer_text(self):
        return self.element(self.ADD_ANSWER_TEXT).send_keys(self.QUESTION_AND_ANSWERS)
    
    def add_answer_button(self):
        return self.element(self.ADD_ANSWER_BUTTON).click()
    
    def choose_the_correct_answer(self):
        return self.element(self.CHOSING_THE_CORRECT_ANSWER).click()

    def return_to_test_menu(self):
        return self.element(self.RETURN_TO_TEST_MENU).click()
    
    def how_many_questions_in_test(self):
        return self.element(self.QUANTITY_OF_QUESTIONS).text
    
    def delete_question_button(self):
        """
        Значок удаления явно не виден на странице, поэтому сначала навожу на область 
        с текстом вопроса чтоб его подстветить, далее уже обнаруживаю кнопку и нажимаю на нее 
        """
        question_text = self.element(self.AREA_WITH_DELETE_BUTTON)
        ActionChains(self.driver).move_to_element(question_text).perform()
        delete_btn = question_text.find_element(*self.DELETE_QUESTION_BUTTON)
        delete_btn.click()
        return self.element(self.DELETE_QUESTION_CONFIRMATION).click()
    
    def edit_question_button(self):
        """
        Тут тоже самое для кнопки edit
        """
        question_text = self.element(self.AREA_WITH_DELETE_BUTTON)
        ActionChains(self.driver).move_to_element(question_text).perform()
        return question_text.find_element(*self.EDIT_QUESTION_BUTTON).click()
    
    def add_answer_for_open_question(self):
        answer_text = self.element(self.ANSWER_INPUT_FIELD)
        ActionChains(self.driver).move_to_element(answer_text).perform()
        return answer_text.find_element(*self.ANSWER_PENCIL_BUTTON).click()

    def profile_button(self):
        return self.element(self.PROFILE_BUTTON).click()
    
    def exit_button(self):
        return self.element(self.EXTT_BUTTON).click()
    
    def update_answer_text(self):
        text_area = self.element(self.UPDATED_QUESTION_AREA)
        text_area.clear()  
        return text_area.send_keys(self.updated_question_test)
    
    def updated_answer(self):
        return self.element(self.UPDATED_ANSWER_TEXT).text
    
    def save_new_question_text(self):
        return self.element(self.SAVE_CHANGES).click()
    
    def get_answers_count(self):
        """
        Функция считает количество ответов по радио-баттонам
        """
        answer_group = self.element(self.ANSWER_GROUP)
        answers = answer_group.find_elements(*self.ANSWER_RADIO_BUTTONS)
        return len(answers)
    
    def get_checboxes_count(self):
        """
        То же самое только для чекбоксов
        """
        answer_group = self.element(self.MULTIPLY_ANSWERS_GROUP)
        answers = answer_group.find_elements(*self.ANSWER_CHECKBOXES)
        return len(answers)
    
    def few_answers_are_correct(self):
        return self.element(self.QUESTION_TYPE_FEW_ANSWERS).click()
    
    def first_asnswer_is_correct(self):
        return self.element(self.THE_FIRST_ANSWER_IS_CORRECT).click()
    
    def third_asnswer_is_correct(self):
        return self.element(self.THE_THIRD_ANSWER_IS_CORRECT).click()
    
    def question_type_open_answer(self):
        return self.element(self.QUESTION_TYPE_NO_ANSWERS).click()
    
    def put_answer_to_the_field_for_open_question(self):
        return self.element(self.ANSWER_INPUT_FOR_OPEN_QUESTION).send_keys(self.QUESTION_AND_ANSWERS)
    
    def confirm_answer_for_open_question(self):
        return self.element(self.CONFIRM_OPEN_QUESTION_ANSWER).click()
    
    def is_test_active(self):
        return self.element(self.DEACTIVATE_BUTTON).text
    
    def deactivate_confirmation(self):
        self.element(self.DEACTIVATE_BUTTON).click()
        return self.element(self.DEACTIVATE_CONFIRMATION).click()
    
    def is_test_deactivated(self):
        return self.element(self.ACTIVATE_BUTTON).text
   
    def choose_last_test(self):
        return self.element(self.LAST_TEST_CREATED).click()