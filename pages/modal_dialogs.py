from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.buttons = WebElement(driver, 'div:nth-child(3) > div > ul > li')
        self.icon = WebElement(driver, '#app > header > a > img')
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div')