from components.components import WebElement
from pages.base_page import BasePage


class Accordion(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        self.text_accord = WebElement(driver, '#section1Content > p')
        self.head = WebElement(driver, '#section1Heading')
        self.cont1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.cont2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.cont3 = WebElement(driver, '#section3Content > p')
        super().__init__(driver, self.base_url)
