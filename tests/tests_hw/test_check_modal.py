from conftest import browser
from pages.modal_dialogs import ModalDialogs
import time

timeout = 5


def test_check_modal(browser):
    page = ModalDialogs(browser)

    page.visit()

    assert page.small_modal.exist()
    assert page.large_modal.exist()

    page.small_modal.click()
    assert page.small_m_dial.exist()
    page.close_small_modal.click()

    page.large_modal.click()
    assert page.large_modal.exist()
    page.close_large_modal.click()