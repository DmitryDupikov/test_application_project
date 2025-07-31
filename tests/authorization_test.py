import pytest
from conftest import chrome_driver

from pages.authorization_page import AuthorizationPage

def test_correct_authorization(chrome_driver):
    """
    Данная функция выполняет проверку успешной авторизации - TestCase ID - 3
    """
    page = AuthorizationPage(chrome_driver)
    page.open()
    page.correct_email()
    page.correct_password()
    page.submit()
    assert page.if_authorization_is_ok() == 'Система тестирования'

def test_incorrect_authorization(chrome_driver):
    """
    Данная функция выполняет проверку негативной авторизации - TestCase ID - 5
    """
    page = AuthorizationPage(chrome_driver)
    page.open()
    page.correct_email()
    page.password_input().send_keys('****')
    page.submit()
    assert page.if_authorization_is_fail() == 'Не удалось выполнить вход'


@pytest.mark.parametrize("enter_parameters", AuthorizationPage.ENTER_PARAMETERS)
def test_incorrect_authorization_with_multiply_parameters(chrome_driver, enter_parameters):
    """
    Данная функция выполняет проверку негативной авторизации c использованием параметрически 
    заданных значений - TestCase ID - 5
    """
    page = AuthorizationPage(chrome_driver, )
    login, password = enter_parameters
    page.open()
    page.email_input().send_keys(login)
    page.password_input().send_keys(password)
    page.submit()
    assert page.if_authorization_is_fail() == 'Не удалось выполнить вход'
