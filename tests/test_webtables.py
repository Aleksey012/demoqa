import time

from selenium.webdriver import Keys

from pages.webtables import webtables



def test_webtables(browser):
    tables_page = webtables(browser)
    tables_page.visit()
    assert not tables_page.nrf.exist()


    while tables_page.btn_delete.exist():
        tables_page.btn_delete.click()

    time.sleep(2)
    assert tables_page.nrf.exist()


def test_webtables2(browser):
    table_page = webtables(browser)
    table_page.visit()
    assert table_page.btn_add.get_text() == 'Add'
    table_page.btn_add.click()
    time.sleep(3)
    assert not table_page.btn_submit.click()
    time.sleep(3)
    table_page.first_name.send_keys('Aleksey')
    table_page.last_name.send_keys('Yakovlev')
    table_page.email.send_keys('alelsey1334@mail.ru')
    table_page.age.send_keys('30')
    table_page.salary.send_keys('100000')
    table_page.department.send_keys('ffffffu')
    table_page.btn_submit.click()
    time.sleep(5)
    table_page.pencil.click()
    time.sleep(2)
    table_page.first_name.clear()
    time.sleep(2)
    table_page.first_name.send_keys('Nikolay')
    time.sleep(2)
    table_page.btn_submit.click()
    time.sleep(2)
    table_page.delete.click()
    time.sleep(2)

def test_webtables3(browser):
    table_page = webtables(browser)
    table_page.visit()
    table_page.str.scroll_to_element()
    time.sleep(2)
    table_page.str.click()
    table_page.rows_5.click()
    time.sleep(2)
    assert not table_page.next_button.click()
    assert not table_page.previous_button.click()





