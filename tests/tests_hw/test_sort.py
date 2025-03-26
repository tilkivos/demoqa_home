import time
from pages.tables import Tables

def test_sort(browser):
    page_tables = Tables(browser)
    page_tables.visit()


    page_tables.first_name_column.click()
    assert page_tables.first_name_column.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    time.sleep(2)


    page_tables.last_name_column.click()
    time.sleep(2)
    assert page_tables.last_name_column.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    time.sleep(2)

    page_tables.age_column.click()
    time.sleep(2)
    assert page_tables.age_column.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    time.sleep(2)


    page_tables.email_column.click()
    time.sleep(2)
    assert page_tables.email_column.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    time.sleep(2)

    page_tables.salary_column.click()
    time.sleep(2)
    assert page_tables.salary_column.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    time.sleep(2)


    page_tables.department_column.click()
    time.sleep(2)
    assert page_tables.department_column.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    time.sleep(2)
