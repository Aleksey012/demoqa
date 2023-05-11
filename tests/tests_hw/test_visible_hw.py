import time

from pages.accordion import Accordion


def test_visible_accordion(browser):
    accord_page = Accordion(browser)
    accord_page.visit()
    accord_page.text_accord.click()
    assert accord_page.text_accord.visible()
    accord_page.head.click()
    time.sleep(2)
    assert not accord_page.text_accord.visible()


def test_visible_accordion_default(browser):
    accord_page = Accordion(browser)
    accord_page.visit()
    assert not accord_page.cont1.visible()
    assert not accord_page.cont2.visible()
    assert not accord_page.cont3.visible()



