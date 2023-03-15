from page_models.locators.HudlPageLocators import HudlPageLocators
from page_models.pages.BasePage import BasePage


class HudlPage(BasePage):
    @property
    def login_button(self):
        return self.driver.find_element(*HudlPageLocators.LOGIN_BUTTON)

    @property
    def hudl_login_button(self):
        return self.driver.find_element(*HudlPageLocators.HUDL_LOGIN_BUTTON)
