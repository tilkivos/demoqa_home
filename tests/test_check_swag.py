from pages.swag_labs import SwagLabs

def test_icon_exist(browser):
    swag_page = SwagLabs(browser)
    swag_page.visit()
    assert swag_page.exist_icon()
    assert swag_page.find_element('input#user-name')
    assert swag_page.find_element('input#password')
