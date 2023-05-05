from pages.base_page import BasePage
from components.components import WebElement

class ElementsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)
        self.centr = WebElement(driver, 'div.pattern-backgound.playgound-header')
        self.icon_head = WebElement(driver, '#app > header > a > img')
        self.first_side_bar = WebElement(driver, ' div:nth-child(1) > span > div')
        self.btn_sidebar_first_textbox = WebElement(driver, '#item-0')
        self.toolsqa = WebElement(driver, '#app > footer > span')
        self.centrqa = WebElement(driver, '//*[@id="app"]/div/div/div[2]/div[2]')
        self.po_centru = WebElement(driver, 'div.row > div.col-12.mt-4.col-md-6')