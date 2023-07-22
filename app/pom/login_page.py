from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from app.pom.base_page import BasePage


# Inherit BasePage
class LoginPage(BasePage):
    # Private variables
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID, "username")
    __password_field = (By.NAME, "password")
    __submit_button = (By.XPATH, "//button[@class='btn']")
    __error_message = (By.ID, "error")

    def __init__(self, driver: WebDriver):  # :WebDriver - Hint to init method about the driver type
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def login(self, username: str, password: str):
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._click(self.__submit_button)

    def get_error_message(self) -> str:
        return super()._get_text(self.__error_message, time=3)