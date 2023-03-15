from page_models.locators.HomePageLocators import HomePageLocators
from page_models.pages.BasePage import BasePage


class HomePage(BasePage):
    @property
    def url(self):
        return super(HomePage, self).url + '/home'

    @property
    def display_name(self):
        return self.driver.find_element(*HomePageLocators.DISPLAY_NAME)

    @property
    def logout_button(self):
        return self.driver.find_element(*HomePageLocators.LOGOUT_BUTTON)
