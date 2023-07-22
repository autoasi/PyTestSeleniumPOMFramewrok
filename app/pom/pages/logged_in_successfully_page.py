from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from app.pom.pages.base_page import BasePage


# Inherit from BasePage
class LoggedInSuccessfullyPage(BasePage):
    _url = "https://practicetestautomation.com/logged-in-successfully/"
    __header_locator = (By.TAG_NAME, "h1")
    __log_out_button_locator = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def current_url(self) -> str:   # Hint - method returns str
        return self._driver.current_url

    @property
    def expected_url(self) -> str:  # Hint - method returns str
        return self._url

    @property
    def header(self) -> str:    # Hint - method returns str
        return super()._get_text(self.__header_locator)

    def is_logout_button_displayed(self) -> bool:    # Hint - method returns bool
        return super().is_displayed(self.__log_out_button_locator)
