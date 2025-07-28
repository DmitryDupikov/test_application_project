from selenium.webdriver.support.ui import WebDriverWait


from pages.card_page import Test_Card_Page

def login_and_navigate(page):
    page.open()
    page.correct_email()
    page.correct_password()
    page.submit()
    page.menu_selection()
    page.test_selection()
    page.plus_icon()


def create_new_test(page):
    page.create_title()
    page.chose_type()
    page.chosing_option()
    page.add_button()
    page.select_test()


def add_question_and_answers_one_answer_is_correct(page):
    page.add_questions_button()
    page.add_new_question_button()
    page.add_question_text()
    page.choose_qustion_type()
    page.click_add_button()
    page.add_answer_text()
    page.add_answer_button()
    page.add_answer_text()
    page.add_answer_button()
    page.add_answer_text()
    page.add_answer_button()
    page.choose_the_correct_answer()


def add_question_and_answers_few_answers_are_correct(page):
    page.add_questions_button()
    page.add_new_question_button()
    page.add_question_text()
    page.few_answers_are_correct()
    page.click_add_button()
    page.add_answer_text()
    page.add_answer_button()
    page.add_answer_text()
    page.add_answer_button()
    page.add_answer_text()
    page.add_answer_button()
    page.first_asnswer_is_correct()
    page.third_asnswer_is_correct()


def test_rename_test(chrome_driver):
    """
    Фуункция проверяет возможность переименования созданного теста. 
    TestCase ID - 17
    """
    page = Test_Card_Page(chrome_driver)
    login_and_navigate(page)
    create_new_test(page)
    page.select_test_menu()
    page.rename_test()
    page.write_new_title()
    page.save_renaming()
    WebDriverWait(chrome_driver, 10).until(
        lambda d: page.renaming_is_correctly() == page.updated_title
    )


def test_delete_test(chrome_driver):
    """
    Фуункция проверяет возможность удаления созданного теста. 
    TestCase ID - 16
    """
    page = Test_Card_Page(chrome_driver)
    login_and_navigate(page)
    test_title = page.create_page.title
    create_new_test(page)
    page.select_test_menu()
    page.delete_test()
    assert not page.is_test_present(test_title)


def test_activation_without_questions_unavailible(chrome_driver):
    """
    Фуункция проверяет что тест без вопросов не активируется. 
    TestCase ID - N/A
    """
    page = Test_Card_Page(chrome_driver)
    login_and_navigate(page)
    create_new_test(page)
    page.select_test_menu()
    page.activate_button()
    assert page.incorrect_activation() == 'В тесте нет вопросов'


def test_question_with_one_answer_can_be_added(chrome_driver):
    """
    Фуункция проверяет возможность создания вопроса с одним вариантом ответа 
    в только что созданном тесте - TestCase ID - 18
    """
    page = Test_Card_Page(chrome_driver)
    login_and_navigate(page)
    create_new_test(page)
    add_question_and_answers_one_answer_is_correct(page)
    page.return_to_test_menu()
    assert page.how_many_questions_in_test() == '1'


def test_question_with_a_few_answers_can_be_added(chrome_driver):
    """
    Фуункция проверяет возможность создания вопроса с несколькими вариантами 
    ответов - TestCase ID - 25
    """
    page = Test_Card_Page(chrome_driver)
    login_and_navigate(page)
    create_new_test(page)
    add_question_and_answers_few_answers_are_correct(page)
    page.return_to_test_menu()
    assert page.how_many_questions_in_test() == '1'


def test_question_with_open_answer_can_be_added(chrome_driver):
    """
    Фуункция проверяет возможность создания вопроса с открытым ответом 
    ответов - TestCase ID - 25
    """
    page = Test_Card_Page(chrome_driver)
    login_and_navigate(page)
    create_new_test(page)
    page.add_questions_button()
    page.add_new_question_button()
    page.add_question_text()
    page.question_type_open_answer()
    page.click_add_button()
    page.add_answer_for_open_question()
    page.put_answer_to_the_field_for_open_question()
    page.confirm_answer_for_open_question()
    page.return_to_test_menu()
    assert page.how_many_questions_in_test() == '1'


def test_question_can_be_deleted_from_test(chrome_driver):
    """
    Фуункция проверяет возможность удаления вопроса из теста - TestCase ID - 19
    """
    page = Test_Card_Page(chrome_driver)
    login_and_navigate(page)
    create_new_test(page)
    page.add_questions_button()
    page.add_new_question_button()
    page.add_question_text()
    page.choose_qustion_type()
    page.click_add_button()
    page.return_to_test_menu()
    assert page.how_many_questions_in_test() == '1'
    page.add_questions_button()
    page.delete_question_button()
    page.return_to_test_menu()
    assert page.how_many_questions_in_test() == '0'


def test_question_can_be_added_into_the_existing_test(chrome_driver):
    """
    Фуункция проверяет возможность добавления вопроса в ранее созданный тест
    после logout`a и повторного login`a - TestCase ID - 20
    """
    page = Test_Card_Page(chrome_driver)
    login_and_navigate(page)
    create_new_test(page)
    add_question_and_answers_one_answer_is_correct(page)
    add_question_and_answers_one_answer_is_correct(page)
    page.return_to_test_menu()
    assert page.how_many_questions_in_test() == '2'
    page.profile_button()
    page.exit_button()
    page.correct_email()
    page.correct_password()
    page.submit()
    page.select_test()
    add_question_and_answers_one_answer_is_correct(page)
    page.return_to_test_menu()
    assert page.how_many_questions_in_test() == '3'


def test_question_can_be_edit_into_the_existing_test(chrome_driver):
    """
    Фуункция проверяет возможность редактирования вопроса в тесте.
    TestCase ID - 28
    """
    page = Test_Card_Page(chrome_driver)
    login_and_navigate(page)
    create_new_test(page)
    add_question_and_answers_one_answer_is_correct(page)
    page.menu_selection()
    page.test_selection()
    page.select_test()
    page.add_questions_button()
    page.edit_question_button()
    page.update_answer_text()
    page.save_new_question_text()
    assert page.updated_answer() == page.updated_question_test


def test_answers_can_be_added_into_the_test_with_a_few_answers(chrome_driver):
    """
    Фуункция проверяет возможность добавления ответа в ранее созданный вопрос
    c несколькими вариантами ответов - TestCase ID - 27
    """
    page = Test_Card_Page(chrome_driver)
    login_and_navigate(page)
    create_new_test(page)
    add_question_and_answers_few_answers_are_correct(page)
    initial_count = page.get_checboxes_count()
    assert initial_count == 3
    page.menu_selection()
    page.test_selection()
    page.select_test()
    page.add_questions_button()
    page.add_answer_text()
    page.add_answer_button()
    assert page.get_checboxes_count() == initial_count + 1


def test_answers_can_be_added_into_the_current_test(chrome_driver):
    """
    Фуункция проверяет возможность добавления ответа в ранее созданный вопрос
    c одним вариантом ответа - TestCase ID - N/A
    """
    page = Test_Card_Page(chrome_driver)
    login_and_navigate(page)
    create_new_test(page)
    add_question_and_answers_one_answer_is_correct(page)
    initial_count = page.get_answers_count()
    assert initial_count == 3
    page.menu_selection()
    page.test_selection()
    page.select_test()
    page.add_questions_button()
    page.add_answer_text()
    page.add_answer_button()
    assert page.get_answers_count() == initial_count + 1


def test_test_can_be_deactivted_if_active(chrome_driver):
    """
    Фуункция проверяет возможность деактивации ранее созданного и 
    активированного теста - TestCase ID - 64
    """
    page = Test_Card_Page(chrome_driver)
    page.open()
    page.correct_email()
    page.correct_password()
    page.submit()
    page.menu_selection()
    page.test_selection()
    page.choose_last_test()
    assert page.is_test_active() == 'Деактивировать'
    page.deactivate_confirmation()
    page.select_test_menu()
    assert page.is_test_deactivated() == 'Активировать'





