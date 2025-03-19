import time
from pages.modal_dialogs import ModalDialogs


def test_modal_elements(browser):
    modal_dialogs_page = ModalDialogs(browser)
    modal_dialogs_page.visit()

    assert modal_dialogs_page.buttons.check_count_elements(count=5)


def test_navigation_modal(browser):
    modal_dialogs_page = ModalDialogs(browser)
    modal_dialogs_page.visit()
    browser.refresh()
    modal_dialogs_page.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()

    assert modal_dialogs_page.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)