import time

from pages.webtables import webtables


def test_webtables(browser):
    tables_page = webtables(browser)
    tables_page.visit()
    assert not tables_page.nrf.exist()


    while tables_page.btn_delete.exist():
        tables_page.btn_delete.click()

    time.sleep(2)
    assert tables_page.nrf.exist()

