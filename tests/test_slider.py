from pages.slider import Slider
from selenium.webdriver.common.keys import Keys


def test_range_slider(browser):
    r_slider = Slider(browser)
    r_slider.visit()
    assert r_slider.slider.exist()
    assert r_slider.pole.exist()
    assert r_slider.slider.get_dom_attribute('value') == '25'
    while not r_slider.pole.get_dom_attribute('value') == '50':
        r_slider.slider.send_keys(Keys. ARROW_RIGHT)

    assert r_slider.pole.get_dom_attribute('value') == '50'



