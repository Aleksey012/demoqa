from pages.base_page import BasePage
from components.components import WebElement


class Bar(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/progress-bar'
        super().__init__(driver, self.base_url)
        self.start_button = WebElement(driver, '#startStopButton')
        self.progress = WebElement(driver, '#progressBar > div')
