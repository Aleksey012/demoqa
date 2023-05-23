from pages.progress_bar import Bar
import time


def test_progress_bar(browser):
    bar = Bar(browser)
    bar.visit()
    time.sleep(2)
    bar.start_button.click()
    time.sleep(2)
    while True:
        if bar.progress.get_dom_attribute('aria-valuenow') == '51':
            bar.start_button.click()
            break
    time.sleep(2)