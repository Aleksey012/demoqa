import time

from pages.TextBox import TextBox


def test_clear(browser):
    demo_qa = TextBox(browser)
    demo_qa.visit()
    demo_qa.full_name.send_keys('dfsfsdfdf')
    time.sleep(2)
    demo_qa.full_name.clear()
    time.sleep(2)
    assert demo_qa.full_name.get_text() == ''
