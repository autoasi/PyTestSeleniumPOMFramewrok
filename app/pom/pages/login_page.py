from selenium.webdriver.remote.webdriver import WebDriver

from app.pom.locators.login_page_locators import *
from app.pom.pages.base_page import BasePage
from app.pom.locators import login_page_locators as locators


# Inherit BasePage
class LoginPage(BasePage):
    # Private variables
    __url = "https://practicetestautomation.com/practice-test-login/"

    def __init__(self, driver: WebDriver):  # :WebDriver - Hint to init method about the driver type
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def login(self, username: str, password: str):
        super()._type(username_field, username)
        super()._type(password_field, password)
        super()._click(submit_button)

    def get_error_message(self) -> str:
        return super()._get_text(error_message, time=3)
