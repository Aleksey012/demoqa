from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_navigation(browser):
    demo_qa_page = DemoQa(browser)
    elem = ElementsPage(browser)


    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    elem.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    assert elem.equal_url()
