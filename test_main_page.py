from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import allure


@pytest.mark.login_guest
class TestLoginFromMainPage():
    @allure.description("Guest can go to Login Page")
    @allure.severity(severity_level="CRITICAL")
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    @allure.severity(severity_level="CRITICAL")
    @allure.description("Guest should see Login link")
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


@allure.description("Should be Login URL")
@allure.severity(severity_level="NORMAL")
def test_should_be_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


@allure.description("Should be Login from")
@allure.severity(severity_level="NORMAL")
def test_should_be_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


@allure.description("Should be Sign-Up from")
@allure.severity(severity_level="NORMAL")
def test_should_be_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()


@allure.description("Guest can't see product in basket opened from Main Page")
@allure.severity(severity_level="NORMAL")
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()
