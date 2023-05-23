
from pages.demoqa import DemoQa
import pytest


@pytest.mark.skip
def test_decor(browser):
    p_decor = DemoQa(browser)
    p_decor.visit()
    assert p_decor.h5.check_count_elements(6)
    for element in p_decor.h5.find_elements():
        assert not element.text != ''

#@pytest.mark.skipif(True, reason='просто пропуск')
def test_radio_button(browser):
    p_decor = DemoQa(browser)

    if not p_decor.code_status():
        pytest.skip(reason=f'Стрница {p_decor.base_url} недоступна')

    p_decor.visit()
    p_decor.yes.click_force()
    assert p_decor.yes.exist()
    assert p_decor.txt.get_text() == 'Yes'
    p_decor.impressive.click_force()
    assert p_decor.impressive.exist()
    assert p_decor.txt.get_text() == 'Impressive'
    assert 'disabled' in p_decor.no.get_dom_attribute('class')
