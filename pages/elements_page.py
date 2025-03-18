from pages.base_page import BasePage
from components.components import WebElement

class ElementsPage(BasePage):


    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)
        self.center_text = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6')

    def get_text_from_center(self):
        return self.center_text.get_text()