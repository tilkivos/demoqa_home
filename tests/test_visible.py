import time

from pages.elements_page import ElementsPage


def test_visible_brn_sidebar(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    # elements_page.btn_sidebar_first.click()
    # time.sleep(3)
    # assert elements_page.btn_sidebar_first_textbox.exist()
    assert elements_page.btn_sidebar_first_textbox.visible()


def test_not_visible_brn_sidebar(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.btn_sidebar_first_checkbox.visible()
    elements_page.btn_sidebar_first.click()
    time.sleep(2)
    assert not elements_page.btn_sidebar_first_checkbox.visible()
