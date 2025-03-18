from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_footer(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    footer = demo_qa_page.get_text_from_footer()
    assert footer == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_page_text(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    elements_page = ElementsPage(browser)
    demo_qa_page.btn_elements.click()
    center_text = elements_page.get_text_from_center()
    assert center_text == 'Please select an item from left to start practice.'