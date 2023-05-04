from pages.demoqa import DemoQa
from components.components import WebElement


def test_toolsqa(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    if WebElement.get_text == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.':
        return True
    else:
        return False


def test_po_centru(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    if WebElement.get_text == '//*[@id="app"]/div/div/div[2]/div[2]/text()':
        return True
    else:
        return False
