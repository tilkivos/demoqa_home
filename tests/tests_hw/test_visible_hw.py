import time
from pages.accordion import Accordion

def test_visible_accordion(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()
    assert accordion_page.section1_content.visible()
    accordion_page.section1_heading.click()
    time.sleep(2)
    assert not accordion_page.section1_content.visible()


def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()
    assert not accordion_page.section2_content_1.visible()
    assert not accordion_page.section2_content_2.visible()
    assert not accordion_page.section3_content.visible()