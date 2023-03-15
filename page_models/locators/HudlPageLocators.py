from selenium.webdriver.common.by import By


class HudlPageLocators:
    LOGIN_BUTTON = By.CSS_SELECTOR, "a[data-qa-id='login-select']"
    HUDL_LOGIN_BUTTON = By.CSS_SELECTOR, "a[data-qa-id='login-hudl']"
