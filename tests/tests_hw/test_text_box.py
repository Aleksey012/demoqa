import time

from pages.TextBox import TextBox


def test_text_box(browser):
    text_box_page = TextBox(browser)
    text_box_page.visit()
    text_box_page.full_name.send_keys('aaa')
    text_box_page.current_address.send_keys('bbb')
    text_box_page.btn_submit.click_force()
    time.sleep(3)
    assert text_box_page.name2.exist()
    assert text_box_page.current_address2.exist()



