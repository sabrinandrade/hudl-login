class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return "https://www.hudl.com"
