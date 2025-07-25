
from pages.authorization_page import AuthorizationPage

def test_correct_authorization(chrome_driver):
    """
    Функция проверяет успешную авторизацию - TestCase ID - 3
    """
    page = AuthorizationPage(chrome_driver)
    page.open()
    page.correct_email()
    page.correct_password()
    page.submit()
    assert page.if_authorization_is_ok() == 'Система тестирования'


def test_incorrect_authorization(chrome_driver):
    """
    Функция проверяет неудачную авторизацию - TestCase ID - 5
    """
    page = AuthorizationPage(chrome_driver)
    page.open()
    page.correct_email()
    page.password_input().send_keys('****')
    page.submit()
    assert page.if_authorization_is_fail() == 'Не удалось выполнить вход'
