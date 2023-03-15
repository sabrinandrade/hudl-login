from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL = By.CSS_SELECTOR, "input[data-qa-id='email-input']"
    PASSWORD = By.CSS_SELECTOR, "input[data-qa-id='password-input']"
    LOGIN_BUTTON = By.CSS_SELECTOR, "button[data-qa-id='login-btn']"
    REMEMBER_ME = By.CSS_SELECTOR, ".uni-form__label--check"
    NEED_HELP = By.CSS_SELECTOR, "a[data-qa-id='need-help-link']"
    ERROR_DISPLAY = By.CSS_SELECTOR, "p[data-qa-id='error-display']"
