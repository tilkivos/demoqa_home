import time
from pages.text_box import TextBox


def test_text_box(browser):
    text_box = TextBox(browser)
    text_box.visit()

    full_name = 'Ivanov Ivan'
    current_address = 'Lenina str Moscow'
    text_box.name.send_keys(full_name)
    text_box.address.send_keys(current_address)
    text_box.btn_submit.click_force()
    time.sleep(2)

    assert text_box.text_name.get_text() == 'Name:'+full_name
    assert text_box.text_address.get_text() == 'Current Address :'+current_address