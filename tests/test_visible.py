import time
from pages.elements_page import ElementsPage

def test_visible_btn_sidebar(browser):
    demo_qa_page = ElementsPage(browser)
    demo_qa_page.visit()
    demo_qa_page.btn_sidebar_first1.click()
    time.sleep(3)
    assert demo_qa_page.btn_sidebar_first_textbox.visible()

def test_not_visible_btn_sidebar(browser):
    demo_qa_page = ElementsPage(browser)
    demo_qa_page.visit()
    demo_qa_page.btn_sidebar_first.click()
    time.sleep(2)
    assert not demo_qa_page.btn_sidebar_first1.visible()
