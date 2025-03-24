from pages.tables import Tables
import time

def test_tables(browser):
    tables = Tables(browser)

    tables.visit()
    assert not tables.block.exist()

    while tables.btn_delete_row.exist():
        tables.btn_delete_row.click()

    time.sleep(2)
    assert tables.block.exist()

def test_add_btn(browser):
    tables = Tables(browser)
    tables.visit()

    tables.add_btn.click()

    tables.firstName.send_keys('Erik')
    tables.LastName.send_keys('Hansen')
    tables.userEmail.send_keys('E.hansen@test.com')
    tables.age.send_keys('31')
    tables.salary.send_keys('300')
    tables.department.send_keys('SABA')
    time.sleep(2)
    tables.submit_btn.click()
    time.sleep(2)

    tables.pencil.click_force()
    tables.firstName.clear()

    tables.firstName.send_keys('Ben')
    tables.submit_btn.click_force()
    assert tables.tableFirstName.get_text() == 'Ben'
    time.sleep(2)

    tables.btn_delete_row.click()
    time.sleep(2)


def test_next_prev(browser):
    tables = Tables(browser)
    tables.visit()

    tables.select_area.scroll_to_element()
    tables.select_area.click()
    tables.select_5.click()

    assert tables.previous_btn.get_dom_attribute('disabled')
    assert tables.next_button.get_dom_attribute('disabled')

    for i in range(3):
        tables.add_btn.click()

        tables.firstName.send_keys('Erik')
        tables.LastName.send_keys('Hansen')
        tables.userEmail.send_keys('E.hansen@test.com')
        tables.age.send_keys('31')
        tables.salary.send_keys('300')
        tables.department.send_keys('SABA')
        tables.submit_btn.click()
    time.sleep(2)

    assert tables.page2.exist()
    assert not tables.next_button.get_dom_attribute('disabled')

    tables.next_button.click()
    assert tables.jump_to_page.get_dom_attribute('value') == '2'
    time.sleep(3)
    tables.previous_btn.click()
    assert tables.jump_to_page.get_dom_attribute('value') == '1'