from pages.form_page import FormPage
import time


def test_login_form(browser):
    form = FormPage(browser)
    form.visit()
    assert not form.modal_dialog.exist()
    time.sleep(2)
    form.first_name.send_keys('Aleksey')
    form.last_name.send_keys('Yakovlev')
    form.user_email.send_keys('aleksey1334@mail.ru')
    form.gender_radio_1.click_force()
    form.user_number.send_keys('89213549993')
    form.hobbies.click_force()
    form.Current_Addres.send_keys('sjfhnfnvdjnxsvdkjsdvnb')
    time.sleep(2)
    form.btn_submit.click_force()
    time.sleep(2)
    assert form.modal_dialog.exist()



