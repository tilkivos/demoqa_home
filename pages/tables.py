from pages.base_page import BasePage
from components.components import WebElement


class Tables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://Demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.block = WebElement(driver, 'div.rt-noData')
        self.btn_delete_row = WebElement(driver, "[title = 'Delete']")
        self.add_btn = WebElement(driver, '#addNewRecordButton')
        self.firstName = WebElement(driver, '#firstName')
        self.LastName = WebElement(driver, '#lastName')
        self.userEmail = WebElement(driver, "#userEmail")
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.submit_btn = WebElement(driver, '#submit')
        self.pencil = WebElement(driver, '#edit-record-4')
        self.tableFirstName = WebElement(driver, "div:nth-child(4) > div > div:nth-child(1)")
        self.previous_btn = WebElement(driver, 'div.pagination-bottom> div .-previous > button')
        self.next_button = WebElement(driver, 'div.pagination-bottom > div> .-next > button')
        self.select_area = WebElement(driver, 'div > span.select-wrap.-pageSizeOptions > select')
        self.select_5 = WebElement(driver, 'span.select-wrap.-pageSizeOptions> select > option:nth-child(1)')
        self.page2 = WebElement(driver, 'div > div.-center > span.-pageInfo > span')
        self.jump_to_page = WebElement(driver, ' div > input[type=number]')
        self.table_1_Column = WebElement(driver, 'div.rt-table > div.rt-thead.-header > div > div:nth-child(1)')
        self.tableElement = WebElement(driver, 'div.rt-table > div.rt-tbody > div:nth-child(1) > div > div:nth-child(1)')