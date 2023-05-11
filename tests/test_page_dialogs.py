from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa


def test_modal_elements(browser):
    elements_page = ModalDialogs(browser)
    elements_page.visit()
    assert elements_page.el.find_elements()


def test_navigation_modal(browser):
    elements_page = ModalDialogs(browser)
    demoqa_page = DemoQa(browser)
    elements_page.visit()
    elements_page.refresh()
    elements_page.icon.click()
    elements_page.back()
    browser.set_window_size(width=900, height=400)
    elements_page.forward()
    assert demoqa_page.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(width=1000, height=1000)
