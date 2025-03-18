from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class SwagLabs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://www.saucedemo.com/'
        super().__init__(driver, self.base_url)


    def exist_icon(self):
        try:
            self.find_element('div.login_logo')
        except NoSuchElementException:
            return False
        return True

