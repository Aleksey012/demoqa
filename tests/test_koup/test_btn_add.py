import time

from pages.koup import Koup
from pages.koup_elements import KoupAdd


def test_btn_add(browser):
    koup_page = Koup(browser)
    koup_add = KoupAdd(browser)
    koup_page.visit()

    assert koup_page.link_add.get_text() == 'Add/Remove Elements'
    koup_page.link_add.click()
    assert koup_add.equal_url()

    assert koup_add.btn_add.get_text() =='Add Element'

    assert koup_add.btn_add.get_dom_attribute('onclick') == 'addElement()'

    for i in range(4):
        koup_add.btn_add.click()

    assert koup_add.btns_delete.check_count_elements(4)

    for element in koup_add.btns_delete.find_element():
        assert element.text == 'Delete'



    while koup_add.btns_delete.exist():
        koup_add.btns_delete.click()

    assert not koup_add.btns_delete.exist()






