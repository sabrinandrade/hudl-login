from selenium.webdriver.common.by import By


class HomePageLocators:
    DISPLAY_NAME = By.XPATH, "/html/body/div[2]/div/div[1]/nav[1]/div[4]/div[2]/div[1]/div[2]/span"
    LOGOUT_BUTTON = By.CSS_SELECTOR, ".hui-globaladditionalitems--not-phone > a:nth-child(2)"
