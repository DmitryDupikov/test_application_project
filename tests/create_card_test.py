
import pytest
from pages.create_card_page import Create_Card_Page


def login_and_navigate(page):
    """
    Функция описывает действия по регистрации и переходу к созданию теста 
    для исключения дублирования
    """
    page.open()
    page.correct_email()
    page.correct_password()
    page.submit()
    page.menu_selection()
    page.test_selection()
    page.plus_icon()


def test_creation_menu_is_exist(chrome_driver):
    """
    Фуункция проверяет наличие меню созданния теста при клике на "+".
    TestCase ID - 21
    """
    page = Create_Card_Page(chrome_driver)
    login_and_navigate(page)
    assert page.creation_menu_is_exist() == ''


def test_commmon_new_test_creation(chrome_driver):
    """
    Функция проверяет создания нового теста с типом "Общий".
    по умолчанию - TestCase ID - 13
    """
    page = Create_Card_Page(chrome_driver)
    login_and_navigate(page)
    page.create_title()
    page.add_button()
    assert page.new_test_created_correctly() == f'{Create_Card_Page.title}'


def test_hr_new_test_creation(chrome_driver):
    """
    Функция проверяет создания нового теста с выбранным типом - TestCase ID - 6
    проверяет Номер(натуральное число), Название, Тип и Статус
    """
    page = Create_Card_Page(chrome_driver)
    login_and_navigate(page)
    page.create_title()
    page.chose_type()
    page.chosing_option()
    page.add_button()
    assert page.new_test_created_correctly() == f'{Create_Card_Page.title}'
    assert page.new_test_type_is_correct() == 'HR'
    assert page.test_appears_in_the_first_row() == page.title
    assert page.created_test_has_correct_status() == 'Не активен'
    number = page.test_has_sequential_number()
    assert isinstance(number, int)
    assert number > 0


def test_cancel_test_creation(chrome_driver):
    """
    Функция проверяет успешную отмену создания теста - TestCase ID - 14
    проверяем отсутствие тайтла, использованного при создании в таблице с тестами на странице
    """
    page = Create_Card_Page(chrome_driver)
    login_and_navigate(page)
    page.create_title()
    page.chose_type()
    page.chosing_option()
    page.cancel_button()
    all_tests = page.get_test_titles()
    assert Create_Card_Page.title not in all_tests


def test_test_is_not_created_with_empty_title(chrome_driver):
    """
    Функция проверяет что при нажатии кнопки "Добавить" при пустом тайтле
    тест не создается - TestCase ID - 15
    (функция реализует проверку длинн списков тестов до и после, это может быть 
    не корректно, так как равенство объемов не гарантирует равенство составов)
    """
    page = Create_Card_Page(chrome_driver)
    login_and_navigate(page)
    initial_test_count = len(page.get_test_titles())
    page.add_button()
    current_test_count = len(page.get_test_titles())
    assert initial_test_count == current_test_count


def test_test_is_not_created_with_empty_title_by_class(chrome_driver):
    """
    Функция проверяет что при нажатии кнопки "Добавить" при пустом тайтле
    тест не создается - TestCase ID - 15
    (функция реализует проверку наличия класса "ng-invalid", до и после нажатия на кнопку 
    "Добавить", данынй класс меняется на "ng-valid", когда в добавляется тайтл. В нашем же 
    случае човпадение значений до и после подтверждает что тест не создался)
    """
    page = Create_Card_Page(chrome_driver)
    login_and_navigate(page)
    name_field = page.title_input_field()
    assert "ng-invalid" in name_field.get_attribute('class')
    page.add_button()
    assert "ng-invalid" in name_field.get_attribute('class')


def test_two_symbol_title_input(chrome_driver):
    """
    Функция проверяет что при нажатии кнопки "Добавить" после ввода в тайтл 
    двух символов тест не создается - TestCase ID - 24
    """
    page = Create_Card_Page(chrome_driver)
    login_and_navigate(page)
    name_field = page.title_input_field()
    assert "ng-invalid" in name_field.get_attribute('class')
    page.wrong_title_input()
    page.add_button()
    assert "ng-invalid" in name_field.get_attribute('class')


@pytest.mark.parametrize("title_parameters", Create_Card_Page.TITLE_PARAMETERS)
def test_two_symbol_title_input_with_parameters(chrome_driver, title_parameters):
    """
    Функция проверяет что при нажатии кнопки "Добавить" после ввода в тайтл 
    двух символов тест не создается - TestCase ID - 24
    """
    page = Create_Card_Page(chrome_driver)
    login_and_navigate(page)
    input = title_parameters
    name_field = page.title_input_field()
    assert "ng-invalid" in name_field.get_attribute('class')
    page.title_input_field().send_keys(input)
    page.add_button()
    assert "ng-invalid" in name_field.get_attribute('class')


def test_default_test_type_is_common(chrome_driver):
    """
    Функция проверяет что значение "Общий" установлено как значение по умолчанию 
    для типа теста в стартовом состоянии меню создания теста - TestCase ID - 23
    """
    page = Create_Card_Page(chrome_driver)
    login_and_navigate(page)
    assert page.default_type_field() == 'Общий'


def test_type_selection_options__are_availible(chrome_driver):
    """
    Функция проверяет что создание теста содержит выпадающий список с видами тестов - TestCase ID - 22
    """
    page = Create_Card_Page(chrome_driver)
    login_and_navigate(page)
    page.chose_type()
    options = page.get_all_dropdown_options_value()
    expected_values = ["COMMON", "HR", "AT", "FT", "ISTQB", "TEST", "POLL"]
    assert set(options) == set(expected_values)

