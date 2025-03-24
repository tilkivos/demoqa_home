import time
from pages.form_page import FormPage
from selenium.webdriver.common.keys import Keys


def test_login_form(browser):
    form_page = FormPage(browser)
    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('testerovich')
    form_page.user_email.send_keys('test@ttt.tt')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('1111111111')
    form_page.hobbies.click_force()
    form_page.current_address.send_keys('text')
    time.sleep(2)
    form_page.btn_submit.click_force()
    time.sleep(2)

    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()


def test_state(browser):
    form_page = FormPage(browser)
    form_page.visit()
    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    form_page.btn_state.click()
    form_page.btn_NCR.click()
    time.sleep(2)


def test_state_2(browser):
    form_page = FormPage(browser)
    form_page.visit()
    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    time.sleep(2)
    form_page.inp_state.send_keys('NCR')
    form_page.inp_state.send_keys(Keys.ENTER)
    time.sleep(2)

def test_state_3(browser):
    form_page = FormPage(browser)
    form_page.visit()
    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    time.sleep(2)
    form_page.btn_state.click()
    form_page.inp_state.send_keys(Keys.PAGE_DOWN)
    form_page.inp_state.send_keys(Keys.ENTER)
    time.sleep(2)
