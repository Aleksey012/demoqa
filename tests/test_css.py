from pages.TextBox import TextBox

def test_test_box(browser):
    ttboxcss = TextBox(browser)
    ttboxcss.visit()

    assert ttboxcss.btn_submit.check_css('color', 'rgba(255, 255, 255, 1)')
    assert ttboxcss.btn_submit.check_css('backgroundColor', 'rgba(0, 123, 255, 1)')
    assert ttboxcss.btn_submit.check_css('borderColor', 'rgb(0, 123, 255)')

