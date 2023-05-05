from pages.demoqa import DemoQa
from components.components import WebElement
from pages.elements_page import ElementsPage


def test_toolsqa(browser):
    demo_qa_page = ElementsPage(browser)
    demo_qa_page.visit()
    assert demo_qa_page.centrqa.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_po_centru(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    demo_qa_element_page = ElementsPage(browser)
    assert demo_qa_element_page.po_centru.get_text() == 'Please select an item from left to start practice.'




def test_page_elements(browser):
   demo_qa_page = ElementsPage(browser)
   demo_qa_page .visit()
   assert demo_qa_page.centr.get_text() =='Elements'
   assert demo_qa_page.icon_head.exist()
   assert demo_qa_page.first_side_bar.exist()
   assert demo_qa_page.btn_sidebar_first_textbox.exist()
