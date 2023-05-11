from pages.form_page import FormPage
import time


def test_login_form(browser):
    form = FormPage(browser)
    form.visit()
    assert not form.modal_dialog.exist()
    time.sleep(2)
    form.first_name.send_keys('tester')
    form.last_name.send_keys('testerovich')
    form.user_email.send_keys('test@ttt.tt')
    form.gender_radio_1.click()
    form.user_number.send_keys('6666666666666')
    time.sleep(2)
    form.btn_submit.click()
    time.sleep(2)

