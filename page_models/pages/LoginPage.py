from page_models.locators.LoginPageLocators import LoginPageLocators
from page_models.pages.BasePage import BasePage


class LoginPage(BasePage):
    @property
    def url(self):
        return super(LoginPage, self).url + '/login'

    @property
    def email(self):
        return self.driver.find_element(*LoginPageLocators.EMAIL)

    @property
    def password(self):
        return self.driver.find_element(*LoginPageLocators.PASSWORD)

    @property
    def login_button(self):
        return self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)

    @property
    def remember_me(self):
        return self.driver.find_element(*LoginPageLocators.REMEMBER_ME)

    @property
    def need_help(self):
        return self.driver.find_element(*LoginPageLocators.NEED_HELP)

    @property
    def error_display(self):
        return self.driver.find_element(*LoginPageLocators.ERROR_DISPLAY)
