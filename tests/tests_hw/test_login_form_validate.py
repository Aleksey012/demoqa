import time

from pages.form_page import FormPage


def test_login_form(browser):
    login_form_page = FormPage(browser)
    login_form_page.visit()
    assert login_form_page.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert login_form_page.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert login_form_page.user_email.get_dom_attribute('pattern') == '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'
    time.sleep(3)
    login_form_page.form.exist()
    time.sleep(3)

def test_login_form_State(browser):
    login_form_page = FormPage(browser)
    login_form_page.visit()

