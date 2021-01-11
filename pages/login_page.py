from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD_CONFIRM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON_CONFIRM).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Current URL is not have word login in URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login from is not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register from is not found"
